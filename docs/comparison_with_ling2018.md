# 推导对比：本文 vs Ling 2018

## 0. 文件

- **本文**：`pgt_theory.tex`（已修正版，移除 cap 简写，修正直流项）
- **Ling 2018**：Ling et al., "High-throughput intensity diffraction tomography with a computational microscope", *Biomed. Opt. Express* 9(5), 2130–2143 (2018). Eq. (1)–(6).

---

## 1. 基本约定对比

这是理解两种推导之间关系最关键的一节。虽然两个推导的最终物理结论一致，但
**入射场的相位约定相反**，导致中间步骤中的许多符号不同。

### 1.1 入射场

| | 本文 | Ling 2018 |
|---|---|---|
| 入射场（实空间） | $\psi_{\text{inc}}(\mathbf{r}) = e^{+i \mathbf{k}_{\text{inc}} \cdot \mathbf{r}}$ | $f_i(\vec{r} \mid \vec{u}_i) = \sqrt{S} \, e^{-i (\vec{u}_i \cdot \vec{x} + \eta_i z)}$ |
| 指数符号 | $+i$ | $-i$ |
| 横向波矢 | $\mathbf{k}_{\text{inc},\perp}$ | $\vec{u}_i$ |
| 轴向波矢 | $k_{\text{inc},z} = \sqrt{k_m^2 - \|\mathbf{k}_{\text{inc},\perp}\|^2}$ | $\eta_i = \sqrt{k^2 - \|\vec{u}_i\|^2}$ |

**关键**：本文的 $e^{+i\mathbf{k}\cdot\mathbf{r}}$ 与 Ling 的 $e^{-i\vec{k}\cdot\mathbf{r}}$ 是相反的相位约定。
这意味着对于**物理上同一束照明**：
$$\boxed{\mathbf{k}_{\text{inc},\perp} \longleftrightarrow -\vec{u}_i, \qquad k_{\text{inc},z} \longleftrightarrow -\eta_i}$$

### 1.2 傅里叶变换

两者使用**相同的** FT 核 $e^{-i\mathbf{k}\cdot\mathbf{r}}$（或 $e^{-i\vec{u}\cdot\vec{x}}$）：

| | 本文 | Ling 2018 |
|---|---|---|
| 3D FT | $\widetilde{f}(\mathbf{k}) = \int f(\mathbf{r}) e^{-i\mathbf{k}\cdot\mathbf{r}} d^3\mathbf{r}$ | — |
| 2D FT | — | $\widetilde{f}(\vec{u}) = \int f(\vec{x}) e^{-i\vec{u}\cdot\vec{x}} d^2\vec{x}$ |

### 1.3 入射场 FT 的峰位置

由于相位约定相反，相同的 FT 核给出不同的峰位置：

- **本文**：$\mathcal{F}\{e^{+i\mathbf{k}_{\text{inc}}\cdot\mathbf{r}}\} = \delta^{(3)}(\mathbf{k} - \mathbf{k}_{\text{inc}})$ — 峰在 $+\mathbf{k}_{\text{inc}}$
- **Ling**：$\mathcal{F}\{e^{-i(\vec{u}_i\cdot\vec{x} + \eta_i z)}\} = \delta^{(2)}(\vec{u} + \vec{u}_i)$ — 峰在 $-\vec{u}_i$

这解释了两个推导中所有 "$\mathbf{k}_{\perp} + \mathbf{k}_{\text{inc},\perp}$" vs "$\vec{u} - \vec{u}_i$" 的符号差异。

### 1.4 散射势

| | 本文 | Ling 2018 |
|---|---|---|
| 定义 | $F(\mathbf{r}) = k_m^2\bigl(1 - \frac{n^2(\mathbf{r})}{n_m^2}\bigr)$ | $\Delta\epsilon(\vec{r}) = \epsilon(\vec{r}) - \epsilon_0 = n^2(\vec{r}) - n_m^2$ |
| 关系 | — | $F = -\frac{k_m^2}{n_m^2} \Delta\epsilon$ |

**$F$ 与 $\Delta\epsilon$ 符号相反**：$F \propto -\Delta\epsilon$。这意味着本文中 $\widetilde{F}$ 的每一项系数，
与 Ling 中 $\widetilde{\Delta\epsilon}$ 的对应系数**差一个全局负号**。

### 1.5 完整映射表

| 本文 | Ling 2018 | 关系 |
|------|-----------|------|
| $\mathbf{k}_{\perp}$ | $\vec{u}$ | 相同（均为强度谱的横向频率变量） |
| $\mathbf{k}_{\text{inc},\perp}$ | $-\vec{u}_i$ | 反号 |
| $k_{\text{inc},z}$ | $-\eta_i$ | 反号 |
| $\sqrt{k_m^2 - \|\mathbf{k}_{\perp}\|^2}$ | $\eta(\vec{u}) = \sqrt{k^2 - \|\vec{u}\|^2}$ | 相同 |
| $F(\mathbf{r})$ | $\Delta\epsilon(\vec{r})$ | $F = -\frac{k_m^2}{n_m^2} \Delta\epsilon$ |
| $P(\mathbf{k}_{\perp})$ | $P(\vec{u})$ | 相同（pupil 函数） |
| $k_m$ | $k$ | 相同（介质中波数） |

---

## 2. 逐步对比

### 2.1 散射场

**本文 Eq. (6)**（对 $z$ 做 FT 后的完整 3D 形式）：
$$\widetilde{\psi}_{\text{scat}}(\mathbf{k}) = P(\mathbf{k}_{\perp}) \frac{\delta\bigl(k_z - \sqrt{k_m^2 - |\mathbf{k}_{\perp}|^2}\bigr)}{2i k_z} \widetilde{F}(\mathbf{k} - \mathbf{k}_{\text{inc}}) \tag{A1}$$

**Ling Eq. (3)**（实空间，探测器平面 $z=0$）：
$$f_s(\vec{x}, 0 \mid \vec{u}_i) = \frac{i k_0^2}{2} \sqrt{S} \int \mathcal{F}^{-1}\!\left\{\widetilde{\Delta\epsilon}(\vec{u} + \vec{u}_i, z') \frac{e^{-i(\eta(\vec{u}) + \eta_i)z'}}{\eta(\vec{u})}\right\} dz' \tag{A2}$$

**对比**：
- 本文的 $\widetilde{F}(\mathbf{k} - \mathbf{k}_{\text{inc}})$ 中，$\mathbf{k} - \mathbf{k}_{\text{inc}}$ 是散射矢量。
  Ling 的 $\widetilde{\Delta\epsilon}(\vec{u} + \vec{u}_i, z')$ 中 $\vec{u} + \vec{u}_i$ ——
  由于 $\mathbf{k}_{\text{inc},\perp} \leftrightarrow -\vec{u}_i$，本文的 $\mathbf{k}_{\perp} - \mathbf{k}_{\text{inc},\perp}$ 对应
  Ling 的 $\vec{u} - (-\vec{u}_i) = \vec{u} + \vec{u}_i$。✅
- 本文的 $\delta(k_z - \sqrt{k_m^2 - |\mathbf{k}_{\perp}|^2})$ 是 Ewald 球面，Ling 的 $\eta(\vec{u})$ 同样是。
- Ling 多出 $\sqrt{S}$（光源强度），本文隐含为 1。这不影响结构。

### 2.2 探测器平面的总场

**本文 Eq. (7)**（频域）：
$$\widetilde{\psi}_{\text{tot}}(\mathbf{k}) = \underbrace{P(\mathbf{k}_{\perp}) \delta^{(3)}(\mathbf{k} - \mathbf{k}_{\text{inc}})}_{\text{入射}} + \underbrace{P(\mathbf{k}_{\perp}) \frac{\delta(k_z - \eta(\mathbf{k}_{\perp}))}{2i k_z} \widetilde{F}(\mathbf{k} - \mathbf{k}_{\text{inc}})}_{\text{散射}}$$

**Ling**（实空间）：
$$f(\vec{x}, 0 \mid \vec{u}_i) = f_i(\vec{x}, 0 \mid \vec{u}_i) + f_s(\vec{x}, 0 \mid \vec{u}_i)$$

经过 pupil（与 $h$ 的卷积 = 频域乘 $P$）后取强度。

两者结构一致：入射 + 散射，经 pupil 滤波。

### 2.3 强度谱

**本文 Eq. (10)**：
$$\widetilde{I}(\mathbf{k}) = \widetilde{\psi}_{\text{tot}}^*(-\mathbf{k}) \ast \widetilde{\psi}_{\text{tot}}(\mathbf{k})$$

**Ling Eq. (2) 的 FT**：
$$\mathcal{F}\{I\} = \mathcal{F}\{(f * h)^*\} \ast \mathcal{F}\{f * h\}$$

结构相同。展开后忽略 s-s 项，保留 i-i 项和交叉项。

### 2.4 交叉项：第一项（cap 项）

**本文 $T_1 = \widetilde{\psi}_{\text{inc}}^*(-\mathbf{k}) \ast \widetilde{\psi}_{\text{scat}}(\mathbf{k})$**：
$$T_1 = P^*(\mathbf{k}_{\text{inc},\perp}) P(\mathbf{k}_{\perp} + \mathbf{k}_{\text{inc},\perp}) \frac{\delta\bigl(k_z + k_{\text{inc},z} - \kappa_+\bigr)}{2i(k_z + k_{\text{inc},z})} \widetilde{F}(\mathbf{k})$$

其中 $\kappa_+ = \sqrt{k_m^2 - |\mathbf{k}_{\perp} + \mathbf{k}_{\text{inc},\perp}|^2}$。

**Ling 的 $I_{is}$**（推导见下文第 3 节）：
$$\mathcal{F}\{I_{is}\} = \frac{i k_0^2}{2} S \, P^*(-\vec{u}_i) P(\vec{u} - \vec{u}_i) \int \widetilde{\Delta\epsilon}(\vec{u}, z') \frac{e^{-i(\eta(\vec{u} - \vec{u}_i) + \eta_i)z'}}{\eta(\vec{u} - \vec{u}_i)} dz'$$

**逐要素对应**（利用第 1.5 节的映射表）：

| 要素 | 本文 $T_1$ | Ling $I_{is}$ | 映射验证 |
|------|-----------|---------------|---------|
| 入射 pupil | $P^*(\mathbf{k}_{\text{inc},\perp})$ | $P^*(-\vec{u}_i)$ | $\mathbf{k}_{\text{inc},\perp} \to -\vec{u}_i$ → $P^*(-\vec{u}_i)$ ✅ |
| 散射 pupil | $P(\mathbf{k}_{\perp} + \mathbf{k}_{\text{inc},\perp})$ | $P(\vec{u} - \vec{u}_i)$ | $\mathbf{k}_{\perp}+\mathbf{k}_{\text{inc},\perp} \to \vec{u}+(-\vec{u}_i) = \vec{u}-\vec{u}_i$ ✅ |
| Ewald 半径 | $\kappa_+ = \sqrt{k_m^2 - \|\mathbf{k}_{\perp} + \mathbf{k}_{\text{inc},\perp}\|^2}$ | $\eta(\vec{u} - \vec{u}_i)$ | 同上 ✅ |
| 轴向相位 | $e^{-i(\kappa_+ - k_{\text{inc},z})z}$（delta 积分后） | $e^{-i(\eta(\vec{u} - \vec{u}_i) + \eta_i)z'}$ | $\kappa_+-k_{\text{inc},z} \to \eta-(-\eta_i) = \eta+\eta_i$ ✅ |
| 散射势 | $\widetilde{F}(\mathbf{k})$（3D，参数 $\mathbf{k}$） | $\widetilde{\Delta\epsilon}(\vec{u}, z')$（2D 切片，参数 $\vec{u}$） | 一致 ✅ |
| 前置因子 | $\frac{1}{2i\kappa_+}$ | $\frac{i k_0^2}{2} S \frac{1}{\eta}$ | 见下文 2.6 节 |

### 2.5 交叉项：第二项（z-reversed cap 项）

**本文 $T_2 = \widetilde{\psi}_{\text{scat}}^*(-\mathbf{k}) \ast \widetilde{\psi}_{\text{inc}}(\mathbf{k})$**：
$$T_2 = P(\mathbf{k}_{\text{inc},\perp}) P^*(-\mathbf{k}_{\perp} + \mathbf{k}_{\text{inc},\perp}) \frac{\delta\bigl(-k_z + k_{\text{inc},z} - \kappa_-\bigr)}{2i(k_z - k_{\text{inc},z})} \widetilde{F}^*(-\mathbf{k})$$

其中 $\kappa_- = \sqrt{k_m^2 - |\mathbf{k}_{\perp} - \mathbf{k}_{\text{inc},\perp}|^2}$。

Delta 条件：$-k_z + k_{\text{inc},z} = \kappa_- \implies k_z - k_{\text{inc},z} = -\kappa_-$。

**Ling 的 $I_{si}$**：
$$\mathcal{F}\{I_{si}\} = -\frac{i k_0^2}{2} S \, P(-\vec{u}_i) P^*(-\vec{u} - \vec{u}_i) \int \widetilde{\Delta\epsilon}^*(-\vec{u}, z') \frac{e^{i(\eta(\vec{u} + \vec{u}_i) + \eta_i)z'}}{\eta(\vec{u} + \vec{u}_i)} dz'$$

**逐要素对应**：

| 要素 | 本文 $T_2$ | Ling $I_{si}$ | 映射验证 |
|------|-----------|---------------|---------|
| 入射 pupil | $P(\mathbf{k}_{\text{inc},\perp})$ | $P(-\vec{u}_i)$ | $\mathbf{k}_{\text{inc},\perp} \to -\vec{u}_i$ ✅ |
| 散射 pupil | $P^*(-\mathbf{k}_{\perp} + \mathbf{k}_{\text{inc},\perp})$ | $P^*(-\vec{u} - \vec{u}_i)$ | $-\mathbf{k}_{\perp}+\mathbf{k}_{\text{inc},\perp} \to -\vec{u}+(-\vec{u}_i) = -(\vec{u}+\vec{u}_i)$ ✅ |
| Ewald 半径 | $\kappa_- = \sqrt{k_m^2 - \|\mathbf{k}_{\perp} - \mathbf{k}_{\text{inc},\perp}\|^2}$ | $\eta(\vec{u} + \vec{u}_i)$ | $\mathbf{k}_{\perp}-\mathbf{k}_{\text{inc},\perp} \to \vec{u}-(-\vec{u}_i) = \vec{u}+\vec{u}_i$ ✅ |
| 散射势参数 | $-\mathbf{k}$（注意是 $-\mathbf{k}$，不是 $\mathbf{k}$） | $-\vec{u}$（$\widetilde{\Delta\epsilon}^*(-\vec{u}, z')$） | 一致 ✅ |
| 轴向相位 | $e^{+i(\kappa_- - k_{\text{inc},z})z}$ | $e^{+i(\eta(\vec{u}+\vec{u}_i) + \eta_i)z'}$ | $\kappa_--k_{\text{inc},z} \to \eta-(-\eta_i) = \eta+\eta_i$ ✅ |

**关键**：本文 $T_2$ 中的 $\widetilde{F}^*(-\mathbf{k})$ —— 注意参数是 $-\mathbf{k}$ 而非 $\mathbf{k}$。
这对应 Ling 中 $\widetilde{\Delta\epsilon}^*(-\vec{u}, z')$ 的参数 $-\vec{u}$。该差异是 $T_2$ 来源于
$\widetilde{\psi}_{\text{scat}}^*(-\mathbf{k})$ 的直接后果，在本文和 Ling 的推导中都是一致的。

### 2.6 前置因子详细对比

本文 $T_1$ 利用 delta 将分母中的 $k_z + k_{\text{inc},z}$ 替换为 $\kappa_+$：

$$\frac{1}{2i(k_z + k_{\text{inc},z})} \xrightarrow{\text{delta}} \frac{1}{2i\kappa_+} = -\frac{i}{2\kappa_+}$$

本文 $T_2$ 利用 delta：$k_z - k_{\text{inc},z} = -\kappa_-$：

$$\frac{1}{2i(k_z - k_{\text{inc},z})} \xrightarrow{\text{delta}} \frac{1}{2i(-\kappa_-)} = \frac{i}{2\kappa_-}$$

现在提取系数（忽略公共实因子 $\frac{k_0^2}{2}S$ 等）：

#### $T_1$ / $I_{is}$ （cap 项）系数

分解 $\widetilde{F} = F_{\text{re}} + iF_{\text{im}}$：

$$\begin{aligned}
T_1^{\text{coeff}} &= -\frac{i}{2\kappa_+} \cdot (F_{\text{re}} + iF_{\text{im}}) \\
&= \underbrace{(-i)}_{F_{\text{re}}} \cdot \frac{F_{\text{re}}}{2\kappa_+} + \underbrace{(+1)}_{F_{\text{im}}} \cdot \frac{F_{\text{im}}}{2\kappa_+}
\end{aligned}$$

Ling Eq. (5)–(6) 中 $I_{is}$ 的系数（忽略 $\frac{k_0^2}{2}S/\eta$）：

$$\begin{aligned}
I_{is}^{\text{coeff}} &= (+i) \cdot (\Delta\epsilon_{\text{Re}} + i\Delta\epsilon_{\text{Im}}) \\
&= \underbrace{(+i)}_{\Delta\epsilon_{\text{Re}}} \cdot \Delta\epsilon_{\text{Re}} + \underbrace{(-1)}_{\Delta\epsilon_{\text{Im}}} \cdot \Delta\epsilon_{\text{Im}}
\end{aligned}$$

由于 $F = -\text{const} \cdot \Delta\epsilon$：

$$\begin{aligned}
\text{本文 } F_{\text{re}} \text{ 系数 } (-i) &\longleftrightarrow \text{Ling } \Delta\epsilon_{\text{Re}} \text{ 系数 } (+i) \quad \text{✅} \\
\text{本文 } F_{\text{im}} \text{ 系数 } (+1) &\longleftrightarrow \text{Ling } \Delta\epsilon_{\text{Im}} \text{ 系数 } (-1) \quad \text{✅}
\end{aligned}$$

#### $T_2$ / $I_{si}$ （z-rev cap 项）系数

本文 $T_2$：

$$T_2^{\text{coeff}} = \frac{i}{2\kappa_-} \cdot (F_{\text{re}}(-\mathbf{k}) - iF_{\text{im}}(-\mathbf{k}))$$

$$\begin{aligned}
&= \underbrace{(+i)}_{F_{\text{re}}} \cdot \frac{F_{\text{re}}(-\mathbf{k})}{2\kappa_-} + \underbrace{(+1)}_{F_{\text{im}}} \cdot \frac{F_{\text{im}}(-\mathbf{k})}{2\kappa_-}
\end{aligned}$$

Ling Eq. (5)–(6) 中 $I_{si}$ 的系数：

$$\begin{aligned}
I_{si}^{\text{coeff}} &= (-i) \cdot (\Delta\epsilon_{\text{Re}}(-\vec{u}) - i\Delta\epsilon_{\text{Im}}(-\vec{u})) \\
&= \underbrace{(-i)}_{\Delta\epsilon_{\text{Re}}} \cdot \Delta\epsilon_{\text{Re}}(-\vec{u}) + \underbrace{(-1)}_{\Delta\epsilon_{\text{Im}}} \cdot \Delta\epsilon_{\text{Im}}(-\vec{u})
\end{aligned}$$

$F = -\text{const} \cdot \Delta\epsilon$ 变换后：

$$\begin{aligned}
\text{本文 } F_{\text{re}} \text{ 系数 } (+i) &\longleftrightarrow \text{Ling } \Delta\epsilon_{\text{Re}} \text{ 系数 } (-i) \quad \text{✅} \\
\text{本文 } F_{\text{im}} \text{ 系数 } (+1) &\longleftrightarrow \text{Ling } \Delta\epsilon_{\text{Im}} \text{ 系数 } (-1) \quad \text{✅}
\end{aligned}$$

---

## 3. Ling 2018 交叉项推导（补充）

以下是 Ling 2018 Eq. (5)–(6) 的推导过程，便于与本文逐一核对。

### 3.1 频域表示

入射场经 pupil 后在频域：
$$\mathcal{F}\{f_i * h\} = \sqrt{S} \, P(-\vec{u}_i) \, \delta(\vec{u} + \vec{u}_i)$$

其复共轭的 FT：
$$\mathcal{F}\{(f_i * h)^*\} = [\mathcal{F}\{f_i * h\}(-\vec{u})]^* = \sqrt{S} \, P^*(-\vec{u}_i) \, \delta(\vec{u} - \vec{u}_i)$$

散射场经 pupil 后（由 Eq. (3) 取 2D FT）：
$$\mathcal{F}\{f_s * h\} = \frac{i k_0^2}{2} \sqrt{S} \, P(\vec{u}) \int \widetilde{\Delta\epsilon}(\vec{u} + \vec{u}_i, z') \frac{e^{-i(\eta(\vec{u}) + \eta_i)z'}}{\eta(\vec{u})} dz'$$

### 3.2 交叉项 $I_{is} = (f_i * h)^* (f_s * h)$

$$\begin{aligned}
\mathcal{F}\{I_{is}\} &= \mathcal{F}\{(f_i * h)^*\} \ast \mathcal{F}\{f_s * h\} \\
&= \int d^2\vec{u}' \, \sqrt{S} P^*(-\vec{u}_i) \delta(\vec{u}' - \vec{u}_i) \\
&\quad \times \frac{i k_0^2}{2} \sqrt{S} P(\vec{u} - \vec{u}') \int \widetilde{\Delta\epsilon}(\vec{u} - \vec{u}' + \vec{u}_i, z') \frac{e^{-i(\eta(\vec{u} - \vec{u}') + \eta_i)z'}}{\eta(\vec{u} - \vec{u}')} dz' \\[4pt]
&= \frac{i k_0^2}{2} S \, P^*(-\vec{u}_i) P(\vec{u} - \vec{u}_i) \int \widetilde{\Delta\epsilon}(\vec{u}, z') \frac{e^{-i(\eta(\vec{u} - \vec{u}_i) + \eta_i)z'}}{\eta(\vec{u} - \vec{u}_i)} dz'
\end{aligned}$$

### 3.3 交叉项 $I_{si} = (f_s * h) (f_i * h)^*$

$I_{si} = I_{is}^*$，故 $\mathcal{F}\{I_{si}\} = [\mathcal{F}\{I_{is}\}(-\vec{u})]^*$：

$$\begin{aligned}
\mathcal{F}\{I_{si}\} &= \left[ \frac{i k_0^2}{2} S \, P^*(-\vec{u}_i) P(-\vec{u} - \vec{u}_i) \int \widetilde{\Delta\epsilon}(-\vec{u}, z') \frac{e^{-i(\eta(-\vec{u} - \vec{u}_i) + \eta_i)z'}}{\eta(-\vec{u} - \vec{u}_i)} dz' \right]^* \\[4pt]
&= -\frac{i k_0^2}{2} S \, P(-\vec{u}_i) P^*(-\vec{u} - \vec{u}_i) \int \widetilde{\Delta\epsilon}^*(-\vec{u}, z') \frac{e^{i(\eta(\vec{u} + \vec{u}_i) + \eta_i)z'}}{\eta(\vec{u} + \vec{u}_i)} dz'
\end{aligned}$$

其中用到 $[i]^* = -i$、$\eta(-\vec{u} - \vec{u}_i) = \eta(\vec{u} + \vec{u}_i)$。

### 3.4 合并为 $H_{\text{Re}}$ 和 $H_{\text{Im}}$

将 $\mathcal{F}\{I_{is}\} + \mathcal{F}\{I_{si}\}$ 按 $\widetilde{\Delta\epsilon}_{\text{Re}}$ 和 $\widetilde{\Delta\epsilon}_{\text{Im}}$ 分组：

$$\begin{aligned}
\widetilde{I}_{\text{cross}}(\vec{u}, 0 \mid \vec{u}_i) &= \frac{i k_0^2}{2} S \Bigg[ P^*(-\vec{u}_i) P(\vec{u} - \vec{u}_i) \int \frac{e^{-i(\eta(\vec{u}-\vec{u}_i) + \eta_i)z'}}{\eta(\vec{u} - \vec{u}_i)} \bigl(\widetilde{\Delta\epsilon}_{\text{Re}}(\vec{u}, z') + i\widetilde{\Delta\epsilon}_{\text{Im}}(\vec{u}, z')\bigr) dz' \\
&\quad - P(-\vec{u}_i) P^*(-\vec{u} - \vec{u}_i) \int \frac{e^{i(\eta(\vec{u}+\vec{u}_i) + \eta_i)z'}}{\eta(\vec{u} + \vec{u}_i)} \bigl(\widetilde{\Delta\epsilon}_{\text{Re}}(-\vec{u}, z') - i\widetilde{\Delta\epsilon}_{\text{Im}}(-\vec{u}, z')\bigr) dz' \Bigg]
\end{aligned}$$

展开并按 $\widetilde{\Delta\epsilon}_{\text{Re}}$、$\widetilde{\Delta\epsilon}_{\text{Im}}$ 分组即得 Eq. (5)–(6)。

---

## 4. 总结：两个推导的一致性

| 检验项 | 结论 |
|--------|------|
| Ewald 球几何（cap 项） | 一致（经 $\mathbf{k}_{\text{inc},\perp} \leftrightarrow -\vec{u}_i$ 映射） |
| Ewald 球几何（z-rev cap 项） | 一致 |
| Cap 项 $F_{\text{re}}/\Delta\epsilon_{\text{Re}}$ 的复系数 | $(-i) \leftrightarrow (+i)$，经 $F \propto -\Delta\epsilon$ 一致 ✅ |
| Cap 项 $F_{\text{im}}/\Delta\epsilon_{\text{Im}}$ 的复系数 | $(+1) \leftrightarrow (-1)$，经 $F \propto -\Delta\epsilon$ 一致 ✅ |
| Z-rev cap 项 $F_{\text{re}}/\Delta\epsilon_{\text{Re}}$ 的复系数 | $(+i) \leftrightarrow (-i)$，经 $F \propto -\Delta\epsilon$ 一致 ✅ |
| Z-rev cap 项 $F_{\text{im}}/\Delta\epsilon_{\text{Im}}$ 的复系数 | $(+1) \leftrightarrow (-1)$，经 $F \propto -\Delta\epsilon$ 一致 ✅ |
| Pupil 因子 | 一致 |
| 传播相位 | 一致 |
| $T_2$ 的参数 $-\mathbf{k}$ vs $I_{si}$ 的参数 $-\vec{u}$ | 一致 |

**最终结论：本文推导（修正后）与 Ling 2018 完全一致。**

两个推导之间所有表观差异都可以用以下三个因素解释：

1. **入射场相位约定相反**：本文 $e^{+i\mathbf{k}\cdot\mathbf{r}}$ vs Ling $e^{-i\vec{k}\cdot\vec{r}}$，
   导致 $\mathbf{k}_{\text{inc}} \leftrightarrow -(\vec{u}_i, \eta_i)$。

2. **散射势定义差一个负号**：$F = -\frac{k_m^2}{n_m^2} \Delta\epsilon$。

3. **3D vs 2D+$z$ 形式**：本文用完整 3D FT（含 $\delta(k_z - \dots)$），
   Ling 用 2D 切片积分（含 $e^{\pm i(\eta+\eta_i)z}$ 相位因子）。
   两者通过 $\int dk_z \, \delta(k_z - \dots) e^{i k_z z} = e^{i(\dots)z}$ 等价。