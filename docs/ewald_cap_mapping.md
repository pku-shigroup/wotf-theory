# Ewald 球壳 ↔ 二维频谱的双向映射

## 问题

在迭代 ODT / intensity-constrained PGT 重建中，需要两个互为伴随的算子：

- **前向 (project)**：从 3D 频谱 $V(\mathbf{k})$ 提取 Ewald 球面上的值 → 2D 频谱 $b_i(\mathbf{k}_\perp)$
- **伴随 (backproject)**：将 2D 频谱 $b_i(\mathbf{k}_\perp)$ 散射回 3D 频谱的 Ewald 球面上

两者必须满足 $\texttt{backproject} = \texttt{project}^*$（伴随性），否则迭代重建不收敛。

---

## 1. 数学结构

### 1.1 连续形式

对第 $i$ 个照明角度 $\mathbf{f}_i = (f_x^i, f_y^i, f_z^i)$，Ewald 球面为：

$$\kappa_i(\mathbf{k}_\perp) = \sqrt{f_m^2 - |\mathbf{k}_\perp + \mathbf{f}_{\perp}^i|^2} - f_z^i$$

**前向算子** $A_i: L^2(\mathbb{R}^3) \to L^2(\mathbb{R}^2)$：

$$b_i(\mathbf{k}_\perp) = w_i(\mathbf{k}_\perp) \cdot V\bigl(\mathbf{k}_\perp + \mathbf{f}_{\perp}^i,\; \kappa_i(\mathbf{k}_\perp)\bigr)$$

其中 $w_i$ 包含 pupil、$1/(2i\kappa)$ 等复权重。

**伴随算子** $A_i^*: L^2(\mathbb{R}^2) \to L^2(\mathbb{R}^3)$：

$$(A_i^* b_i)(\mathbf{k}) = w_i^*(\mathbf{k}_\perp - \mathbf{f}_{\perp}^i) \cdot b_i(\mathbf{k}_\perp - \mathbf{f}_{\perp}^i) \cdot \delta\bigl(k_z - \kappa_i(\mathbf{k}_\perp - \mathbf{f}_{\perp}^i)\bigr)$$

$A_i^*$ 将 2D 图像中的每个像素"涂抹"到 3D 空间中对应的 Ewald 球面位置上。

### 1.2 离散化

在你的方案中，$(\mathbf{k}_\perp, \mathbf{f}_{\perp}^i)$ 均被 snap 到 Cartesian 网格上，
因此 $\mathbf{k}_\perp + \mathbf{f}_{\perp}^i$ 和 $\mathbf{k}_\perp - \mathbf{f}_{\perp}^i$
（通过 `sx, sy`）均天然落在整数索引上。唯一需要处理的维度是 $k_z$。

对每个 $(k_x, k_y)$ 柱，问题退化为 1D：

$$b[k_x, k_y] = w \cdot V[k_x + s_x, k_y + s_y,\; k_z^*]$$

其中 $k_z^* = \kappa_i(k_x, k_y)$ 一般不在网格点上，需要插值。

---

## 2. 伴随性的关键条件

### 条件 1：前向和伴随使用**相同的插值核**

设前向的插值为（以线性插值为例）：

$$V(k_z^*) = (1 - \alpha) \cdot V[k_{\text{lo}}] + \alpha \cdot V[k_{\text{lo}} + 1], \quad \alpha = \frac{k_z^* - k_z[k_{\text{lo}}]}{\Delta k_z}$$

在矩阵形式中，前向算子是一个稀疏矩阵 $A$，其第 $j$ 行（对应一个 $(k_x, k_y, i)$ 测量）的非零元为：
$$A_{j, k_{\text{lo}}} = w \cdot (1-\alpha), \quad A_{j, k_{\text{lo}}+1} = w \cdot \alpha$$

伴随算子 $A^*$ 是 $A$ 的共轭转置。同一列的非零元恰好是：
$$A^*_{k_{\text{lo}}, j} = w^* \cdot (1-\alpha), \quad A^*_{k_{\text{lo}}+1, j} = w^* \cdot \alpha$$

**即：伴随操作必须用相同的 $\alpha$ 将 $b$ 按权重分配回相同的两个 $k_z$ 层。**

### 条件 2：伴随操作用 `.add()` 而非 `.set()`

$A^*$ 的列是 $A$ 的行的共轭转置。$A$ 的每一行有多个非零元（分布到多个 $k_z$ 层），
所以 $A^*$ 的每一列也有多个非零元。当多个测量（不同角度、不同 $(k_x, k_y)$）
映射到同一个 3D voxel 时，它们的贡献必须**累加**。

`.set()` 等价于忽略 $A^*$ 中其他行的贡献——破坏了伴随性。

### 条件 3：照明偏移的符号

前向：$V$ 的索引偏移 $+s_x, +s_y$
伴随：$b$ 的索引偏移 $-s_x, -s_y$

这是因为 $A$ 中 $V$ 在 $(k_x + s_x, k_y + s_y)$ 处取值，伴随算子中 2D 测量
在同一 $(k_x, k_y)$ 处取值，但写到 $V$ 的 $(k_x + s_x, k_y + s_y)$ 位置。

等价地看伴随操作：对每个 $(k_x, k_y)$，取 $b_i[k_x, k_y]$，将其写到
$V[k_x + s_x, k_y + s_y, :]$ 的 $k_z^*$ 层。符号与前向一致——不需要额外翻转。

---

## 3. 具体实现

### 3.1 前向：`ewaldcap2image`

```python
def ewaldcap2image(spectrum_3d, fx, fy, fz, f_vecs,
                   pupil_det, oblique_factor):
    """Project 3D spectrum onto Ewald caps → 2D spectra.

    Parameters
    ----------
    spectrum_3d : (nz, ny, nx) complex64
    fx, fy, fz : 1D frequency axes
    f_vecs : (nangles, 3) — (fx_shift, fy_shift, fz_shift) per angle
    pupil_det : (ny, nx) — detection pupil mask
    oblique_factor : (ny, nx) — 1/(4π·Fz) weights

    Returns
    -------
    images_2d : (ny, nx, nangles) complex64
    """
    dfz = fz[1] - fz[0]
    fz0 = fz[0]
    fm = jnp.sqrt(jnp.max(fx)**2 + jnp.max(fy)**2 + jnp.max(fz)**2)  # or from params

    images = []
    for a in range(len(f_vecs)):
        fx_s, fy_s, fz_s = f_vecs[a]

        # Snap illumination shifts to grid
        sx = jnp.round(fx_s / (fx[1] - fx[0])).astype(int)
        sy = jnp.round(fy_s / (fy[1] - fy[0])).astype(int)

        # Shifted kx, ky after applying illumination offset
        # Forward: V is evaluated at (kx + sx, ky + sy)
        # We iterate over all (kx, ky) in the image and read V accordingly
        kx_shifted = fx[:, None] + fx_s   # broadcast
        ky_shifted = fy[None, :] + fy_s

        # Ewald sphere for this angle
        r_sq = kx_shifted**2 + ky_shifted**2
        inside = r_sq <= (fm)**2  # propagating waves only
        kz_ideal = jnp.where(inside,
            jnp.sqrt(jnp.maximum(fm**2 - r_sq, 0.0)) - fz_s,
            jnp.nan)

        # kz index (floating point)
        kz_cont = (kz_ideal - fz0) / dfz
        kz_lo = jnp.floor(kz_cont).astype(int)
        kz_lo = jnp.clip(kz_lo, 0, nz - 2)
        alpha = kz_cont - kz_lo  # fraction for upper neighbor

        # Read V at the two kz layers with shifted kx, ky
        # Need to handle the shifted indices
        i_idx = jnp.arange(nx) + sx
        j_idx = jnp.arange(ny) + sy
        i_idx = jnp.clip(i_idx, 0, nx - 1)
        j_idx = jnp.clip(j_idx, 0, ny - 1)

        V_lo = spectrum_3d[kz_lo, j_idx[:, None], i_idx[None, :]]
        V_hi = spectrum_3d[kz_lo + 1, j_idx[:, None], i_idx[None, :]]

        # Linear interpolation
        V_at_cap = (1.0 - alpha) * V_lo + alpha * V_hi

        # Apply weight
        img = oblique_factor * pupil_det * V_at_cap
        img = jnp.where(inside, img, 0.0 + 0j)
        images.append(img)

    return jnp.stack(images, axis=-1)
```

### 3.2 伴随：`image2ewaldcap`

```python
def image2ewaldcap(images_2d, nz, ny, nx, fx, fy, fz, f_vecs,
                   pupil_det, oblique_factor):
    """Backproject 2D spectra onto Ewald caps → 3D spectrum.

    Parameters
    ----------
    images_2d : (ny, nx, nangles) complex64
    nz, ny, nx : int — 3D grid dimensions
    fx, fy, fz : 1D frequency axes
    f_vecs : (nangles, 3)
    pupil_det, oblique_factor : (ny, nx)

    Returns
    -------
    spectrum_3d : (nz, ny, nx) complex64
    """
    dfz = fz[1] - fz[0]
    fz0 = fz[0]
    fm = jnp.sqrt(jnp.max(fx)**2 + jnp.max(fy)**2 + jnp.max(fz)**2)

    spectrum_3d = jnp.zeros((nz, ny, nx), dtype=jnp.complex64)

    for a in range(len(f_vecs)):
        fx_s, fy_s, fz_s = f_vecs[a]
        sx = jnp.round(fx_s / (fx[1] - fx[0])).astype(int)
        sy = jnp.round(fy_s / (fy[1] - fy[0])).astype(int)

        kx_shifted = fx[:, None] + fx_s
        ky_shifted = fy[None, :] + fy_s
        r_sq = kx_shifted**2 + ky_shifted**2
        inside = r_sq <= fm**2

        kz_ideal = jnp.where(inside,
            jnp.sqrt(jnp.maximum(fm**2 - r_sq, 0.0)) - fz_s,
            jnp.nan)

        kz_cont = (kz_ideal - fz0) / dfz
        kz_lo = jnp.floor(kz_cont).astype(int)
        kz_lo = jnp.clip(kz_lo, 0, nz - 2)
        alpha = kz_cont - kz_lo

        # Weighted image value
        img = images_2d[..., a]
        weighted = jnp.conj(oblique_factor) * pupil_det * img
        weighted = jnp.where(inside, weighted, 0.0 + 0j)

        # Scatter to 3D: same interpolation weights as forward!
        # V[kz_lo]     += (1 - alpha) * weighted
        # V[kz_lo + 1] += alpha       * weighted
        # Shifted by (sx, sy) in kx, ky

        i_idx = jnp.arange(nx) + sx
        j_idx = jnp.arange(ny) + sy
        i_idx = jnp.clip(i_idx, 0, nx - 1)
        j_idx = jnp.clip(j_idx, 0, ny - 1)

        spectrum_3d = spectrum_3d.at[
            kz_lo, j_idx[:, None], i_idx[None, :]
        ].add((1.0 - alpha) * weighted)

        spectrum_3d = spectrum_3d.at[
            kz_lo + 1, j_idx[:, None], i_idx[None, :]
        ].add(alpha * weighted)

    return spectrum_3d
```

### 3.3 伴随性验证

对任意 $V$（3D）和 $b$（2D 多角度），伴随性要求：

$$\langle A V, b \rangle_{2D} = \langle V, A^* b \rangle_{3D}$$

其中 $\langle \cdot, \cdot \rangle$ 是标准 Hermitian 内积。

**数值验证方法**：

```python
# 随机测试
V = random_normal((nz, ny, nx)) + 1j * random_normal(...)
b = random_normal((ny, nx, nangles)) + 1j * random_normal(...)

# 计算 (A V, b)
AV = ewaldcap2image(V, ...)
inner1 = jnp.sum(jnp.conj(AV) * b)

# 计算 (V, A* b)
Asb = image2ewaldcap(b, ...)
inner2 = jnp.sum(jnp.conj(V) * Asb)

# 应满足 |inner1 - inner2| < 1e-6 * |inner1|
```

### 3.4 归一化（Preconditioner）

在迭代重建中，有效的步长需要估计 $A^*A$ 的对角线（每个 3D voxel 被采样的"次数"）：

```python
def compute_preconditioner(nz, ny, nx, fx, fy, fz, f_vecs,
                           pupil_det, oblique_factor):
    """Compute diagonal of A*A as a preconditioner for iterative reconstruction."""
    ones_2d = jnp.ones((ny, nx, len(f_vecs)), dtype=jnp.complex64)
    prec = image2ewaldcap(ones_2d, nz, ny, nx, fx, fy, fz, f_vecs,
                          pupil_det, oblique_factor).real
    # prec[kz, ky, kx] = sum over angles of |w(kx-sx, ky-sy)|² · interpolation_weight
    # Clip to avoid division by zero in unsampled regions
    prec = jnp.maximum(prec, 1e-8)
    return prec
```

---

## 4. 精度分析

### 4.1 误差来源

| 来源 | 影响 | 如何控制 |
|------|------|---------|
| $k_z$ 插值阶数 | 球面几何保真度 | 线性插值：$O(\Delta k_z^2)$，对此问题已精确 |
| snap2grid 量化照明角 | 照明方向偏移 | $\Delta k_\perp$ 足够小时可忽略 |
| oblique factor 截断 ($\kappa \to 0$) | 赤道附近权重 | 用 `_make_oblique_factor` 的截断策略 |

### 4.2 为什么线性插值对这个场景是精确的

$(k_x, k_y)$ 已天然落在 Cartesian 网格上，每个 $(k_x, k_y)$ 柱内的 Ewald 球面截面是一个点
$k_z^*$。将 $k_z^*$ 按距离线性分配到相邻两层 $(k_{\text{lo}}, k_{\text{lo}}+1)$，等价于在
$k_z$ 方向对体素 $[k_{\text{lo}}\Delta k_z, (k_{\text{lo}}+2)\Delta k_z]$ 做精确的
$\int \delta(k_z - k_z^*) \, dk_z$ 体素积分。

更高阶的插值（立方等）不会带来额外的精度增益，因为 $\delta$ 函数的分布已经在这两层之间被精确捕获。

---

## 5. 与现有代码的对应

| 概念 | `ewald_cap_test.py` 当前状态 | 需要改成 |
|------|---------------------------|---------|
| 离散化 | 最近邻（`jnp.round`） | 线性插值（`jnp.floor` + 两层） |
| 累加方式 | `.set()` | `.add()` |
| 权重 | uniform 1.0 | `oblique_factor * pupil_det` |
| 前向/伴随 | 未区分 | 显式分离两个函数 |
| 伴随验证 | 无 | 数值内积测试 |
| 预条件器 | 无 | $A^*A$ 对角线估计 |