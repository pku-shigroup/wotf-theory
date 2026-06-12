# 求解器架构分析与 4090 性能评估

## 1. 代码库全景

```
pgt/src/
├── phase_gradient_tomography_solver.py       # CPU 版本 (JAX, 默认 CPU backend)
├── phase_gradient_tomography_solver_gpu.py   # GPU 优化版本 (JAX + XLA fusion)
├── pgt_solver_merged.py                      # (待确认)

experiments/tf-debug/
├── gpu_padded_wotf.py                        # z 方向过采样 WOTF + 降采样，缓解频谱泄露
└── gpu_padded_wotf_offset.py                 # 变体

ic/
├── ewald_cap_test.py                         # 直接离散化 Ewald cap 原型
├── temp_ewald_cap_test_fast.py               # 加速版 (fori_loop + jit)
├── operate_ewald_cap.py                      # Ewald cap ↔ 图像 映射 (骨架)
└── temp_cap_calculator.py                    # 采样需求计算

temp_cap_calculator.py                        # Ewald cap Nyquist 采样率估算
```

## 2. 三个求解器的架构对比

### 2.1 CPU 版本 (`phase_gradient_tomography_solver.py`)

```
__init__:
  ├── _generate_wotf()          ← 预计算 H_real, H_imag (nz, ny, nx, nchan)
  │   └── 存为 self.H_real, self.H_imag (各 ~4 GB × 2 for 512³×4)
  └── 完成

solve():
  ├── _normalize_born/rytov()
  ├── _deconv_with_tikhonov()
  │   ├── dpc_fft = fft3(dpc_imgs)                  ← 3D FFT of data
  │   ├── A1 = sum(H_real*·H_real) + α                ← 通道规约
  │   ├── B1 = sum(H_real*·H_imag)
  │   ├── C1 = sum(H_real*·dpc_fft)
  │   ├── ...                                          ← 解 2×2 系统
  │   ├── V_real = ifft3(V_real_fft).real
  │   └── V_imag = ifft3(V_imag_fft).real
  └── _scattering_potential_to_ri()
```

**瓶颈**：H 矩阵占大量内存（512³×4 complex64 ≈ 8 GB），CPU FFT 带宽受限。

### 2.2 GPU 版本 (`phase_gradient_tomography_solver_gpu.py`)

```
__init__:
  ├── fsp_det_conj = fft2(prop_kernel · oblique)*   ← 与通道无关，预计算一次
  ├── _build_system_matrices()
  │   └── _build_wotf_system()                       ← jit 编译
  │       └── for each channel:                       ← 计算 H → 累加到 A1,B1,B2 → 丢弃 H
  │           ├── h_real, h_imag = WOTF(channel)
  │           ├── A1 += Hr_r² + Hr_i²
  │           ├── B1 += Hr* · Hi
  │           └── B2 += Hi_r² + Hi_i²
  └── 只保留 A1, B1_r, B1_i, B2 (各 nz×ny×nx float32 ≈ 4×256 MB)

solve():
  ├── _normalize_born/rytov()
  ├── _deconv_with_tikhonov()
  │   ├── Phase 1: _deconv_phase1()
  │   │   └── for each channel:                       ← 重新计算 WOTF + 3D FFT of data + 累加
  │   │       ├── fft = fft3(dpc[channel])
  │   │       ├── h_real, h_imag = WOTF(channel)     ← 与 _build_wotf_system 相同的计算！
  │   │       ├── c1 += H* · fft
  │   │       └── c2 += ...
  │   ├── del dpc_imgs                               ← 释放原始数据
  │   └── Phase 2: _deconv_phase2()
  │       └── 解 2×2 系统 + 2× ifft3
  └── _scattering_potential_to_ri()
```

**关键设计决策**：WOTF 被计算了**两次**——一次在 `__init__` 中（规约到 A1, B1, B2），
一次在 `_deconv_phase1` 中（计算 C1, C2）。这是因为存储完整的 H 矩阵「太费显存」。
代码注释说这避免了 9.6 GB → 3.7 GB 的显存占用。

### 2.3 Padded WOTF 版本 (`gpu_padded_wotf.py`)

```
generate_all_tfs_gpu():
  └── for each channel:
      └── generate_padded_wotf_gpu():
          ├── 在 z_padded (nz=128) 上逐 batch 计算 h_real, h_imag
          │   └── _compute_batch():
          │       ├── pk = pupil_det · exp(i·2π·Fz·z)    ← 传播核 (在更密的 z 网格上)
          │       ├── fsp_cross = fft2(src·pk) · conj(fft2(pk·oblique))
          │       └── h_real/h_imag = ifft2(fsp_cross.imag/real)
          └── z-FFT → 加窗 → 降采样到 nz_orig=41

deconvolve_tikhonov():
  ├── _deconv_phase1_from_tfs(dpc, H_real, H_imag)    ← 与 GPU 版相同，但 H 已预存
  ├── _build_system_from_tfs(H_real, H_imag)           ← 由预存的 H 规约
  └── _deconv_phase2(A1, B1, ..., C1, C2)
```

**优势**：nz=128 的细 z 网格 → z 范围更大 → sinc 主瓣更窄 → 频谱泄露显著减小。
代价是 WOTF 计算量增大约 128/41 ≈ 3×，但这是一次性成本。

## 3. RTX 4090 上的性能评估

### 3.1 硬件规格

| 参数 | RTX 4090 | 高端 CPU (e.g. 7950X) |
|------|----------|---------------------|
| FP32 算力 | ~82 TFLOPS | ~2 TFLOPS |
| 显存/内存带宽 | ~1 TB/s | ~50-100 GB/s |
| 显存/内存容量 | 24 GB | 64-128 GB |
| FFT 优化 | cuFFT (tensor core 加速) | FFTW / MKL |

### 3.2 典型数据规模下的预估

以 `(nz=256, ny=1024, nx=1024, nchan=4)` 为例：

| 操作 | GPU (4090) | CPU | 加速比 |
|------|-----------|-----|--------|
| 2D FFT × 256 slices × 4 ch | ~0.05s | ~0.5s | ~10× |
| 3D FFT (1024³) | ~0.1s | ~2s | ~20× |
| WOTF per channel | ~0.3s | ~3s | ~10× |
| Total WOTF (4 ch) | ~1.2s | ~12s | ~10× |
| Deconv (solve + 2× IFFT3) | ~0.3s | ~4s | ~13× |
| **Total solve** | **~2s** | **~20s** | **~10×** |

> 实际时间取决于 JAX 的 XLA 编译缓存。首次运行需要编译（约 30s-2min），后续运行直接执行。

### 3.3 显存占用分析

**GPU 版本 (on-the-fly)**：

| 数据 | 大小 (512³×4) | 大小 (256×1024²×4) |
|------|-------------|-----------------|
| dpc_imgs (float32) | 2 GB | 1 GB |
| prop_kernel (complex64) | 1 GB | 512 MB |
| fsp_det_conj (complex64) | 1 GB | 512 MB |
| A1, B1_r, B1_i, B2 (float32) | 2 GB | 1 GB |
| Phase 1 intermediates | ~4 GB | ~2 GB |
| **总计 (峰值)** | **~10 GB** | **~5 GB** |

✅ 24 GB 显存绰绰有余。

**如果改为预存 H 矩阵**（GPU padded 方案）：

| 数据 | 512³×4 | 256×1024²×4 |
|------|--------|-------------|
| H_real + H_imag (complex64) | **8 GB** | **4 GB** |
| + 其他 (同上) | ~6 GB | ~3 GB |
| **总计** | **~14 GB** | **~7 GB** |

✅ 仍然在 24 GB 以内。

### 3.4 结论：4090 上哪个方案更快？

**对于少量重建（≤ 10 次）**：GPU on-the-fly 版本 ≈ GPU padded 版本。
两者总时间相近（WOTF 计算 + 反演都在秒级），差异在噪声水平。

**对于大量重建（时间序列、参数扫描）**：GPU padded / 预计算方案更快。
因为 WOTF 只算一次，后续每次反演只需 ~0.3s（Phase 1 I/O + Phase 2 solve），
而 on-the-fly 每次反演都要重复 WOTF 计算 (~1.2s)。

```
            首次    第2次   第10次   第100次
on-the-fly:  ~3s     ~3s     ~3s      ~3s  (每次都重算 WOTF)
预计算+H:    ~3s    ~0.5s   ~0.5s    ~0.5s (WOTF 只算一次)
```

## 4. 预计算传递函数并加载到显存的可行性

### 4.1 完全可行，且已有先例

`gpu_padded_wotf.py` 就是这个模式：
1. `generate_all_tfs_gpu()` → 计算 H_real, H_imag
2. `deconvolve_tikhonov()` → 使用预存的 H 做反演

这两步可以完全分离——计算 H 一次，保存为 `.npy`，之后加载使用：

```python
# 步骤 1：预计算（离线，可运行在任意机器上）
H_real, H_imag = generate_all_tfs_gpu(config, ...)
np.save("H_real.npy", np.array(H_real))
np.save("H_imag.npy", np.array(H_imag))

# 步骤 2：使用时加载（在线）
H_real = jnp.array(np.load("H_real.npy"))
H_imag = jnp.array(np.load("H_imag.npy"))
ri = solve(dpc_images, H_real, H_imag)
```

### 4.2 传递函数文件大小

| 规模 | nz | ny | nx | nchan | 文件大小 (2 × complex64) |
|------|----|----|----|----|--------------------------|
| 小 | 64 | 512 | 512 | 4 | 2 × 64×512²×4 × 8B = **1 GB** |
| 中 | 128 | 1024 | 1024 | 4 | 2 × 128×1024²×4 × 8B = **8 GB** |
| 大 | 256 | 1024 | 1024 | 4 | 2 × 256×1024²×4 × 8B = **16 GB** |
| 超大 | 256 | 2048 | 2048 | 4 | **64 GB** (需分块或降采样) |

对于中小规模（≤ 8 GB），单文件 `.npy` 可直接 `mmap` 模式加载，无需完整读入内存。
对于大规模，可用 `zarr` 分块存储，按需加载到显存。

### 4.3 直接离散化 Ewald 球壳 + 预计算的场景

这是预计算策略最有价值的应用场景：

| 方案 | WOTF 计算时间 (单角度) | 存储大小 | 反演速度 |
|------|---------------------|---------|---------|
| FFT 传播-相关 (GPU on-the-fly) | ~0.3s | 0 (不存) | 快 |
| FFT 传播-相关 (GPU padded) | ~1s | 大 | 最快 |
| Ewald cap 直接离散化 (最近邻) | ~10s | 大 | 最快 |
| Ewald cap 直接离散化 (体素相交) | ~10min | 大 | 最快 |

直接离散化方案的 TF 计算可能是 FFT 方案的 10-1000× 慢，但一旦预计算完成，**反演阶段的速度完全相同**（都是把 H 矩阵代入 Tikhonov 求解器）。

### 4.4 推荐工作流

```
┌─────────────────────────────────────────────────────┐
│  离线预计算 (一次性)                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────────────┐ │
│  │ 光学参数  │ → │ TF 计算   │ → │ H_real/imag.npy  │ │
│  │ (NA, λ)  │   │ (任意方法) │   │ (磁盘, 1-16 GB)  │ │
│  └──────────┘   └──────────┘   └──────────────────┘ │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│  在线反演 (每次实验)                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────────────┐ │
│  │ 实验数据  │   │ 加载 H   │   │ JAX GPU solver   │ │
│  │ (DPC)    │ → │ → GPU    │ → │ → RI 重建 (~1s)  │ │
│  └──────────┘   └──────────┘   └──────────────────┘ │
└─────────────────────────────────────────────────────┘
```

这与 `gpu_padded_wotf.py` 的架构一致，只需将 `generate_all_tfs_gpu()` 替换为直接离散化版本的
TF 生成函数即可。

## 5. 对你现有 Ewald cap 代码的观察

`ewald_cap_test.py` / `temp_ewald_cap_test_fast.py` 已经实现了直接离散化的核心：

```python
# 核心逻辑（temp_ewald_cap_test_fast.py 第 82-95 行）
@jax.jit
def build_cap_spectrum(inside_det, i_idx, j_idx, sx, sy):
    spec = jnp.zeros((nz, ny, nx), dtype=jnp.complex64)
    def body(a, s):
        k_indices = jnp.round((kz_ideal - f_vecs[a, 2] - fz[0]) / dfz).astype(int)
        k_indices = jnp.clip(k_indices, 0, nz - 1)
        s = s.at[k_indices, j_idx - sy[a], i_idx - sx[a]].set(
            inside_det_cplx, mode='promise_in_bounds')
        return s
    return jax.lax.fori_loop(0, num_angles, body, spec)
```

**当前状态**：
- ✅ 正确地计算了 Ewald cap 的 $(k_x, k_y, k_z)$ 坐标
- ✅ 使用了最近邻 (`jnp.round`) 分配到 Cartesian 网格
- ✅ 用 `fori_loop` + `@jit` 避免显存爆炸
- ❌ 缺少 pupil 截断（`inside_det` 只检查了检测 NA，未检查照明 NA）
- ❌ 缺少 $1/(2i\kappa)$ 权重因子
- ❌ 缺少 $F_{\text{re}}$ / $F_{\text{im}}$ 的分离（只设置了 uniform 复数值）
- ❌ 尚未集成到 Tikhonov 求解器

**下一步建议**：
1. 在 `build_cap_spectrum` 中加入 `oblique_factor` 权重（即 $1/(4\pi F_z)$）
2. 对每个 cap 分别计算 `H_real` 和 `H_imag`（利用 cap 的纯虚/纯实系数）
3. 输出与 `gpu_padded_wotf.py` 兼容的 `(nz, ny, nx, nchan)` 格式
4. 与 FFT 方案的 TF 做逐体素对比，验证正确性