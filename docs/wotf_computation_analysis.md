# 传递函数计算：传播-相关方法与直接 Ewald 球壳离散化

---

## 第一部分：传播-相关方法的数学原理

使用 `pgt_theory.tex` 的符号体系。

### 1.1 出发公式

由修正后的推导，交叉项为：

$$\begin{aligned}
T_1(\mathbf{k}) &= P^*(\mathbf{k}_{\text{inc},\perp}) P(\mathbf{k}_{\perp} + \mathbf{k}_{\text{inc},\perp}) \,
                  \frac{\delta\bigl(k_z + k_{\text{inc},z} - \kappa_+\bigr)}{2i(k_z + k_{\text{inc},z})} \,
                  \widetilde{F}(\mathbf{k}) \\[4pt]
T_2(\mathbf{k}) &= P(\mathbf{k}_{\text{inc},\perp}) P^*(-\mathbf{k}_{\perp} + \mathbf{k}_{\text{inc},\perp}) \,
                  \frac{\delta\bigl(-k_z + k_{\text{inc},z} - \kappa_-\bigr)}{2i(k_z - k_{\text{inc},z})} \,
                  \widetilde{F}^*(-\mathbf{k})
\end{aligned}$$

其中 $\kappa_\pm = \sqrt{k_m^2 - |\mathbf{k}_{\perp} \pm \mathbf{k}_{\text{inc},\perp}|^2}$。

$T_1$ 与 $T_2$ 在 $\mathbf{k}$ 空间中是分布在 **Ewald 球面**上的 $\delta$ 函数。

### 1.2 核心恒等式：$\delta$ 函数与传播相位的对偶

$$\delta(k_z - \kappa) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-i(k_z - \kappa)z} \, dz,
\qquad
\int e^{-i k_z z} \, e^{i \kappa z} \, dz = 2\pi \, \delta(k_z - \kappa)$$

在 3D 频率空间中位于 Ewald 球面 $k_z = \kappa$ 上的 $\delta$ 分布，等价于在 $(z, \mathbf{k}_{\perp})$
混合域中用传播相位 $e^{i \kappa z}$ 表示该球面约束，然后对 $z$ 做 Fourier 变换。

### 1.3 将 $T_1$ 变换到 $(z, \mathbf{k}_{\perp})$ 混合域

对 $T_1$ 做关于 $k_z$ 的逆 Fourier 变换。$\delta$ 函数取 $k_z = \kappa_+ - k_{\text{inc},z}$，
分母替换为 $2i\kappa_+$；再将 3D 散射势 $\widetilde{F}(\mathbf{k}_{\perp}, k_z)$ 用 2D 切片展开
$\widetilde{F}(\mathbf{k}_{\perp}, k_z) = \int \widetilde{F}_{2D}(\mathbf{k}_{\perp}, z') \, e^{-i k_z z'} \, dz'$：

$$\boxed{
\widetilde{T}_1(\mathbf{k}_{\perp}, z) = \frac{1}{2\pi} \, P^* P \, \frac{e^{i(\kappa_+ - k_{\text{inc},z})z}}{2i\kappa_+}
\int \widetilde{F}_{2D}(\mathbf{k}_{\perp}, z') \, e^{-i(\kappa_+ - k_{\text{inc},z})z'} \, dz'
}$$

同理对 $T_2$（$\delta$ 函数取 $k_z = k_{\text{inc},z} - \kappa_-$，分母 $-2i\kappa_-$）：

$$\boxed{
\widetilde{T}_2(\mathbf{k}_{\perp}, z) = \frac{1}{2\pi} \, P P^* \, \frac{e^{i(k_{\text{inc},z} - \kappa_-)z}}{2i(-\kappa_-)}
\int \widetilde{F}_{2D}^*(-\mathbf{k}_{\perp}, z') \, e^{-i(k_{\text{inc},z} - \kappa_-)z'} \, dz'
}$$

### 1.4 强度谱的 $(z, \mathbf{k}_{\perp})$ 域表示

探测器平面 $(z=0)$ 的 2D 强度谱是各深度贡献之和。将 $\widetilde{F}_{2D} = F_{\text{re}} + iF_{\text{im}}$
和 $\widetilde{F}_{2D}^*(-\mathbf{k}_{\perp}) = F_{\text{re}}(-\mathbf{k}_{\perp}) - iF_{\text{im}}(-\mathbf{k}_{\perp})$
代入并整理：

$$\begin{aligned}
\widetilde{I}(\mathbf{k}_{\perp}, 0) &= \int dz \Bigg[
   \underbrace{\frac{1}{2\pi} \left[ \frac{P^*P}{2i\kappa_+} F_{\text{re}}(\mathbf{k}_{\perp}, z) +
          \frac{P P^*}{-2i\kappa_-} F_{\text{re}}(-\mathbf{k}_{\perp}, z) \right]}_{\text{纯虚系数 → 代码中从 .imag 提取}} \\
   &+ \underbrace{\frac{1}{2\pi} \left[ \frac{P^*P}{2\kappa_+} F_{\text{im}}(\mathbf{k}_{\perp}, z) +
          \frac{P P^*}{-2\kappa_-} \bigl(-F_{\text{im}}(-\mathbf{k}_{\perp}, z)\bigr) \right]}_{\text{纯实系数 → 代码中从 .real 提取}}
   \Bigg]
\end{aligned}$$

### 1.5 与代码的映射

| 理论符号 | 代码变量 |
|---------|---------|
| $(\mathbf{k}_{\perp}, z) \leftrightarrow (F_x, F_y, z)$ | `prop_kernel` 的 axes |
| $P(\mathbf{k}_{\perp})$ | `pupil_det` |
| $e^{i \kappa z}$（传播相位） | `jnp.exp(1j * 2 * jnp.pi * Fz * z)` |
| $1/(2i\kappa)$（Weyl 因子） | `oblique_factor = pupil_det / (4*pi*Fz)` |
| $S(\mathbf{k}_{\perp})$（照明图案） | `source_pattern` |

代码的计算流程：

```
(1) A[z, Fy, Fx] = source × P_det × exp(i·2π·Fz·z)     ← 照明场在混合域
(2) B[z, Fy, Fx] = P_det × 1/(4πFz) × exp(i·2π·Fz·z)   ← 探测核在混合域
(3) FFT2d(A) → u_ill(x,y,z)                               ← 照明场在实空间
(4) FFT2d(B) → h_det(x,y,z)                               ← 探测 PSF 在实空间
(5) u_ill × conj(h_det)                                   ← 每个深度的强度响应（correlation）
(6) IFFT2d → 回到 (Fy, Fx)                                ← 2D 传递函数 @ depth z
(7) FFT along z → (Fz, Fy, Fx)                            ← 3D 传递函数
```

步骤 (3)–(5) 等价于在横向频率域计算 $\widetilde{\psi}^*(-\mathbf{k}) \ast \widetilde{\psi}(\mathbf{k})$
的横向分量；步骤 (7) 的 $z$ 方向 FFT 将传播相位转化为轴向频率分量，还原出 3D Ewald 球。

---

## 第二部分：传播-相关方法的频谱泄露

### 2.1 泄露的数学来源

连续理论中，$(z, \mathbf{k}_{\perp})$ 域的传播相位 $e^{i \kappa z}$ 在 $z \in (-\infty, \infty)$
上的 Fourier 变换给出理想的 $\delta(k_z - \kappa)$。实际 $z$ 范围 $[-Z/2, Z/2]$ 等效于加了矩形窗：

$$\int_{-Z/2}^{Z/2} e^{i \kappa z} \, e^{-i k_z z} \, dz = Z \cdot \text{sinc}\bigl((k_z - \kappa) Z / 2\pi\bigr)$$

### 2.2 泄露的表现

1. **主瓣展宽**：Ewald 球面厚度 $\approx 1/Z$
2. **旁瓣振荡**：sinc 旁瓣产生振铃，Hamming 窗可抑制但进一步展宽主瓣
3. **DC 泄露**：低频分量的展宽污染 $k_z \approx 0$ 区域
4. **周期延拓假象**：FFT 隐含周期性，$z$ 堆栈两端的不连续产生额外频率分量

### 2.3 缓解措施

| 措施 | 效果 | 代价 |
|------|------|------|
| Hamming 窗（代码已使用） | 旁瓣抑制 ≈ −43 dB | 主瓣展宽约 2× |
| $z$ 方向过采样（padded WOTF） | 增大 $Z$，缩窄 sinc 主瓣 | 一次性的 TF 计算量增大 |
| 多角度合成孔径 | 不同角度球冠互补 | 不能修复单角度的泄露 |

---

## 第三部分：直接离散化 Ewald 球壳

传播-相关方法的频谱泄露来自有限 $z$ 范围的 FFT。一个自然的替代思路是：**不通过 $(z, \mathbf{k}_{\perp})$ 域**，
直接在 3D Cartesian 频率网格上构造传递函数。

### 3.1 核心原则：$H$ 与数据的角色分离

有限 $z$ 范围导致数据 $g$ 中丢失了高频 $k_z$ 信息。这个不完整性应该由**反演的正则化**来处理，
而不应该被手动烧进前向算子 $H$ 里。把 sinc 展宽写进 $H$ 等于主动放弃了可能从 Tikhonov
或其他正则化中部分恢复的分辨率信息。

**正确的做法**：$H$ 尽可能精确地表示理论的理想 $\delta$ 球壳。数据的不完整性是反演要解决的问题，
不是前向模型要妥协的问题。

因此问题归结为：**在 Cartesian 网格上，如何最精确地离散化一个 $\delta(k_z - \kappa)$？**

### 3.2 问题简化：1D $\delta$ 离散化

观察你的方案：
- $(k_x, k_y)$ **已经天然落在网格上**（你在已有网格上计算 `kz_ideal = sqrt(fm² - kx² - ky²)`）
- 平移后的 $k_z^* = k_z^{\text{ideal}} - f_z$ 一般**不在** $k_z$ 网格点上

所以这不是 3D 几何问题，而是**1D $\delta$ 函数在均匀网格上的离散化**：对每个 $(k_x, k_y)$ 柱，
把一个 $\delta(k_z - k_z^*)$ 分配到周围的 $k_z$ 网格点上。

### 3.3 离散化方案（按精度递进）

#### 方案 A：最近邻（你当前的方案）

$$\int_{k_z^i - \Delta k_z/2}^{k_z^i + \Delta k_z/2} \delta(k_z - k_z^*) \, dk_z = \begin{cases} 1 & |k_z^i - k_z^*| < \Delta k_z/2 \\ 0 & \text{otherwise} \end{cases}$$

等价于将 $\delta$ 与宽度 $\Delta k_z$ 的 boxcar 卷积后采样。**误差 $O(\Delta k_z)$**。
球面在 $k_z$ 方向被量化为"台阶"——$k_z^*$ 被拉到最近的网格点。

```python
k_idx = jnp.round((kz_ideal - fz_shift - fz[0]) / dfz).astype(int)
spec = spec.at[k_idx, ...].add(weights)  # 注意：应为 .add() 而非 .set()
```

#### 方案 B：线性插值（2 点分配）

将 $\delta$ 的积分按距离反比分配到相邻两个 $k_z$ 平面上：

$$w_{\text{lo}} = 1 - \text{frac}(k_z^* / \Delta k_z), \quad w_{\text{hi}} = \text{frac}(k_z^* / \Delta k_z)$$

等价于将 $\delta$ 与宽度 $2\Delta k_z$ 的 hat 函数卷积后采样。**误差 $O(\Delta k_z^2)$**。

```python
kz_continuous = (kz_ideal - fz_shift - fz[0]) / dfz
kz_lo = jnp.floor(kz_continuous).astype(int)
frac = kz_continuous - kz_lo
spec = spec.at[kz_lo,     ...].add(weights * (1.0 - frac))
spec = spec.at[kz_lo + 1, ...].add(weights * frac)
```

计算量约为最近邻的 2×。

#### 方案 C：立方插值（4 点分配）

误差 $O(\Delta k_z^3)$，计算量约 4×，对于大多数场景过度。

#### 方案 D：体素相交积分（精确）

在 $(k_x, k_y)$ 已对齐网格的前提下，球面在单个 $(k_x, k_y)$ 柱内的 $k_z$ 截面是一个**点**。
分配到两个 $k_z$ 层的**线性插值就是精确的体素积分**——没有更多的几何信息可以利用。

因此对于这个特定问题，**方案 B（线性插值）即为精确解**，不需要更复杂的 3D 体素求交。

### 3.4 其他问题

#### `.set()` vs `.add()`

不同照明角度的 Ewald 球冠在 3D 频率空间中必然有重叠（低频区域）。当前代码使用 `.set()` 会
覆写之前角度的值。**必须改为 `.add()`** 以正确累加重叠区域的贡献。

#### 倾斜因子 $1/(2i\kappa)$

当前所有球面点赋 uniform 权重 1.0，缺少传递函数中的 $1/(2i\kappa)$ 因子。需要在累加时乘上
oblique factor（与 `_make_oblique_factor` 一致的截断处理）。

#### $F_{\text{re}}$ 与 $F_{\text{im}}$ 的分离

传递函数中 $F_{\text{re}}$ 的系数是纯虚数，$F_{\text{im}}$ 的系数是纯实数。直接离散化时应当
分别构造 `H_real`（从球的虚部系数）和 `H_imag`（从球的实部系数）。

### 3.5 方案对比

| 方案 | $k_z$ 误差 | 计算量 (vs 最近邻) | 推荐场景 |
|------|-----------|-------------------|---------|
| A：最近邻 | $O(\Delta k_z)$ | 1× | 快速原型 |
| **B：线性插值** | **$O(\Delta k_z^2)$** | **≈ 2×** | **生产代码** |
| C：立方插值 | $O(\Delta k_z^3)$ | ≈ 4× | 过度的精度需求 |
| D：体素相交 | 精确（等价于 B） | ≈ 2× | 与 B 相同 |

### 3.6 对现有代码的具体修改建议

当前 `temp_ewald_cap_test_fast.py` 需要以下修改即可达到方案 B：

1. **`.set()` → `.add()`**：消除球冠重叠覆写
2. **最近邻 → 线性插值**：`jnp.round` → `jnp.floor` + 上下两层分配
3. **加入 oblique factor**：乘 $1/(4\pi F_z)$（含 $\kappa \to 0$ 截断）
4. **分离 H_real / H_imag**：分别构造纯虚和纯实的球壳权重
5. **输出格式**：`(nz, ny, nx, nchan)` complex64，与现有求解器兼容