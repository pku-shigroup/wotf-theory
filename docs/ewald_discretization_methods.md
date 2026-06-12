# Ewald 球壳直接离散化：方案评估

## 你当前的方案

```python
# 核心逻辑（temp_ewald_cap_test_fast.py 第 82–95 行）
@jax.jit
def build_cap_spectrum(inside_det, i_idx, j_idx, sx, sy):
    spec = jnp.zeros((nz, ny, nx), dtype=jnp.complex64)
    def body(a, s):
        k_indices = jnp.round((kz_ideal - f_vecs[a,2] - fz[0]) / dfz).astype(int)
        k_indices = jnp.clip(k_indices, 0, nz - 1)
        s = s.at[
            k_indices, j_idx - sy[a], i_idx - sx[a]
        ].set(inside_det_cplx, mode='promise_in_bounds')
        return s
    return jax.lax.fori_loop(0, num_angles, body, spec)
```

**步骤分解**：
1. 对每个 $(k_x, k_y)$ 网格点，计算 $k_z^{\text{ideal}} = \sqrt{f_m^2 - k_x^2 - k_y^2}$
2. 对每个照明角度 $\mathbf{f} = (f_x, f_y, f_z)$：
   - `snap2grid` 将 $f_x, f_y$ 量化为最近的网格索引 → `sx, sy`
   - 平移后的 $k_z$：$k_z^{\text{ideal}} - f_z$，取最近网格索引
   - 将值写入 `spec[kz_idx, ky_idx - sy, kx_idx - sx]`

### 这个方案的优点

1. **直观**：直接对应理论——Ewald 球面点映射到 Cartesian 网格
2. **快**：`fori_loop` + `@jit` 下每个角度只需一次 $O(N_\perp)$ 的索引操作
3. **无频谱泄露**：不像 FFT 方法有有限 $z$ 范围的截断效应
4. **$(k_x, k_y)$ 天然落在网格上**（你指出的）：因为 `kz_ideal` 是在已有 $(k_x, k_y)$ 网格上计算的

### 问题

#### 问题 1：`.set()` 覆写而非累加 ⚠️ （最严重）

当多个照明角度的 Ewald 球冠在 3D 频率空间中重叠时（这在实际中是**必然的**——不同角度的球冠在低频区域有交集），`.set()` 只保留最后一个角度的值，之前的被覆盖。

```python
# 修复：改为累加
s = s.at[...].add(weights)  # 而非 .set()
```

#### 问题 2：kz 最近邻分配产生台阶伪影

$$\delta(k_z - \kappa) \;\xrightarrow{\text{最近邻}}\; \begin{cases} 1 & \text{if } k_z = \text{round}(\kappa/\Delta k_z) \cdot \Delta k_z \\ 0 & \text{otherwise} \end{cases}$$

效果是把光滑的球面近似为**分段平坦的台阶**。$k_z$ 方向的分辨率直接等于 $\Delta k_z$，
而物理上传递函数在 $k_z$ 方向的"厚度"由数据的 $z$ 范围 $Z$ 决定：$\delta k_z \sim 1/Z$。

如果 $\Delta k_z \ll 1/Z$（$k_z$ 网格很密），最近邻分配的球面**比物理上可分辨的更薄**，
这会造成前向模型与数据之间的不匹配。

#### 问题 3：缺少 $1/(2i\kappa)$ 倾斜因子

传递函数的系数中包含 $1/(2i\kappa_+)$ 和 $1/(2i\kappa_-)$。当前所有点赋值均为 $1.0$，
缺少这个权重。（均匀权重在 $\kappa \to 0$ 的赤道附近不会发散，这是唯一的好处。）

#### 问题 4：缺少 pupil 权重

当前 `inside_det` 是二值的（0 或 1）。实际 pupil 可以有 apodization（如 Gaussian）。
对传递函数精度要求高的场景应当支持非二值 pupil。

---

## 替代方案

### 方案 A：修复当前方案（最小改动）

```
.set() → .add()
uniform 权重 → oblique_factor * pupil_weight
```

**代价**：几乎为零。**收益**：消除最严重的 bug，加上正确的物理权重。

### 方案 B：kz 线性插值（2 点分配）

替代最近邻：将每个球面点的权重分配到相邻**两个** $k_z$ 平面上。

```python
kz_continuous = (kz_ideal - f_vecs[a, 2] - fz[0]) / dfz
kz_lo = jnp.floor(kz_continuous).astype(int)
kz_hi = kz_lo + 1
w_lo = 1.0 - (kz_continuous - kz_lo)    # 线性插值权重
w_hi = kz_continuous - kz_lo

s = s.at[kz_lo, ...].add(weights * w_lo)
s = s.at[kz_hi, ...].add(weights * w_hi)
```

**优势**：
- 将 kz 量化误差从 $O(\Delta k_z)$ 降至 $O(\Delta k_z^2)$
- 球面在 kz 方向的"宽度"从 1 个 voxel 变为 2 个 voxel，更平滑
- 计算量仅增加约 2×

**劣势**：
- 仍然是 ad hoc 的插值，没有物理依据
- 传递函数的"厚度"仍由 $\Delta k_z$ 而非 $1/Z$ 决定

### 方案 C：有限 $z$ 范围一致的壳近似

物理上，有限 $z$ 范围 $[-Z/2, Z/2]$ 意味着 $\delta(k_z - \kappa)$ 应被替换为
其与矩形窗 Fourier 变换的卷积：

$$\delta(k_z - \kappa) \;\longrightarrow\; Z \cdot \text{sinc}\left(\frac{(k_z - \kappa) Z}{2\pi}\right)$$

对于 $(k_x, k_y)$ 网格上的每个点，在 kz 方向不放置单点，而是放置一个 sinc 轮廓：

```python
for each (kx, ky):
    kz_center = kz_ideal - fz_shift
    # 在 kz_center 周围的 kz 网格点上计算 sinc 权重
    for kz_idx in range(nz):
        weight = Z * jnp.sinc((fz[kz_idx] - kz_center) * Z / (2*pi))
        spec[kz_idx, ky_idx, kx_idx] += oblique_factor * weight
```

**优势**：
- 有明确的物理依据——直接来自有限 $z$ 范围
- 传递函数厚度与数据一致（$\sim 1/Z$）
- 可以用 Hamming 窗代替矩形窗以抑制旁瓣

**劣势**：
- 计算量增大：对每个 $(k_x, k_y)$ 需要沿整个 $k_z$ 维度计算权重
  （实际只需在中心附近 $\pm 3/Z$ 范围内计算，其余可截断）
- 如果 $Z$ 很大（$k_z$ 分辨率很高），sinc 非常窄，退化为方案 A/B

### 方案 D：体素相交积分

对每个 Cartesian 体素 $V_{ijk} = [k_x^i, k_x^{i+1}] \times [k_y^j, k_y^{j+1}] \times [k_z^k, k_z^{k+1}]$，
计算 Ewald 球面与该体素的交集面积：

$$H_{ijk} = \int_{V_{ijk}} \delta(k_z - \kappa(k_x, k_y)) \cdot \frac{P(k_x, k_y)}{2i\kappa(k_x, k_y)} \, d^3\mathbf{k}$$

对于球面，体素相交面积可以解析计算（球面与长方体的交集），不需要超采样。

**优势**：
- 数学上最严谨
- 自动处理所有几何效应（球面曲率、体素形状）

**劣势**：
- 实现复杂（3D 几何求交）
- 对每个非零体素需要计算球面-长方体相交面积
- 每个角度需要重新计算

### 方案 E：傅里叶变换法（等价于现有 WOTF）

用 $(z, k_x, k_y)$ 域的传播相位 $e^{i 2\pi \kappa z}$ 配 FFT 来隐式构造球壳——
即现有 solver 的方法。这不是"直接离散化"，但它是当前最成熟的方案。

---

## 各方案对比

| 方案 | 精度 | 计算量 | 实现难度 | 物理一致性 |
|------|------|--------|---------|----------|
| A：修复 .set→.add + 权重 | 低 | $O(N_\perp N_{\text{angles}})$ | 极低 | 低 |
| B：+ kz 线性插值 | 中 | $O(2N_\perp N_{\text{angles}})$ | 低 | 中 |
| C：sinc 壳近似 | **高** | $O(N_\perp N_{\text{angles}} W)$ (W≈10) | 中 | **高** |
| D：体素相交 | **最高** | $O(N_\perp N_{\text{angles}})$ | **高** | **最高** |
| E：FFT 传播-相关 | 中 | $O(N_\perp N_z \log N_\perp N_{\text{angles}})$ | 已有 | 中（受限于截断） |

> $W$ 是 sinc 在 $k_z$ 方向的非零宽度（以 voxel 计），通常 $\approx Z \cdot \Delta k_z$。

---

## 建议路线

1. **立即**：修复方案 A（`.set()` → `.add()` + oblique factor）。这可以在不改动架构的情况下消除最大 bug。

2. **下一步**：实现方案 C（sinc 壳近似）。这是性价比最高的方案——有明确物理依据，与数据
   的有限 $z$ 范围一致，计算量可控（sinc 在 $\pm 3/Z$ 以外截断）。

3. **长期**：如果方案 C 的结果在定量精度上仍不满足需求（例如在与 FFT 方案对比时发现
   显著差异），考虑方案 D（体素相交）。但方案 C 和 FFT 方案（在 padded z 条件下）的结果
   应当非常接近——因为它们本质上建模了相同的物理过程。

### 方案 C 的快速实现思路

```python
# 预计算：对每个 (kx, ky)，在 kz_center 周围 ±3*dfz_sinc 范围内分配权重
kz_center = kz_ideal - fz_shift           # shape (nx, ny)
sinc_width = 3.0 / (z_range)              # ±3 个主瓣宽度
kz_half_window = int(sinc_width / dfz)    # voxel 数

for dk in range(-kz_half_window, kz_half_window + 1):
    kz_idx = kz_center_idx + dk
    weight = oblique_factor * jnp.sinc((dk * dfz) * z_range / (2 * jnp.pi))
    spec = spec.at[kz_idx, ...].add(weight * pupil)
```

其中 `z_range = nz * dz` 是数据的总 $z$ 范围。sinc 宽度由 $1/\text{z\_range}$ 自然决定，
与 FFT 方案的 $k_z$ 分辨率一致。
