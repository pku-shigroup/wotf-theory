# PGT Theory — 交叉项推导错误分析

## 范围

`pgt_theory.tex` 第 107–126 行：$\widetilde{I}_{i-s}$（i-s 交叉项）的推导。

**前提**：散射势 $F(\mathbf{r}) = k_m^2(1 - n^2/n_m^2)$ 中 $n$ 可为复数（有吸收），$F(\mathbf{r})$ 未必是实函数。因此 $F_{\text{re}}(\mathbf{k})$、$F_{\text{im}}(\mathbf{k})$ 无奇偶性，
**$F_{\text{re}}(-\mathbf{k})$ 不能化简为 $\pm F_{\text{re}}(\mathbf{k})$，$F_{\text{im}}(-\mathbf{k})$ 同理**。推导必须显式保留 $\mathbf{k}$ 与 $-\mathbf{k}$ 的参数区别。

---

## 1. 前置公式

入射场与散射场（频域，pupil $P$ 为实函数）：

$$\widetilde{\psi}_{\text{inc}}(\mathbf{k}) = P(\mathbf{k}_{\perp}) \, \delta^{(3)}(\mathbf{k} - \mathbf{k}_{\text{inc}}) \tag{I}$$

$$\widetilde{\psi}_{\text{scat}}(\mathbf{k}) = P(\mathbf{k}_{\perp}) \, \frac{\delta\bigl(k_z - \sqrt{k_m^2 - |\mathbf{k}_{\perp}|^2}\bigr)}{2i k_z} \, \widetilde{F}(\mathbf{k} - \mathbf{k}_{\text{inc}}) \tag{S}$$

强度谱交叉项（忽略 s-s 项）：

$$\widetilde{I}_{i-s} = \underbrace{\widetilde{\psi}_{\text{inc}}^*(-\mathbf{k}) \ast \widetilde{\psi}_{\text{scat}}(\mathbf{k})}_{T_1} \;+\; \underbrace{\widetilde{\psi}_{\text{scat}}^*(-\mathbf{k}) \ast \widetilde{\psi}_{\text{inc}}(\mathbf{k})}_{T_2} \tag{C}$$

---

## 2. $T_1$ 与 $T_2$ 的计算（第 107–123 行，正确）

$T_1$（由 $\delta^{(3)}(\mathbf{k}' + \mathbf{k}_{\text{inc}})$ 取 $\mathbf{k}' = -\mathbf{k}_{\text{inc}}$）：

$$T_1(\mathbf{k}) = P(\mathbf{k}_{\text{inc},\perp}) P(\mathbf{k}_{\perp} + \mathbf{k}_{\text{inc},\perp}) \;
      \frac{\delta\bigl(k_z + k_{\text{inc},z} - \sqrt{k_m^2 - |\mathbf{k}_{\perp} + \mathbf{k}_{\text{inc},\perp}|^2}\bigr)}
           {2i(k_z + k_{\text{inc},z})} \; \widetilde{F}(\mathbf{k})$$

$T_2$（由 $\delta^{(3)}(\mathbf{k} - \mathbf{k}' - \mathbf{k}_{\text{inc}})$ 取 $\mathbf{k}' = \mathbf{k} - \mathbf{k}_{\text{inc}}$，
原文用 $- \frac{1}{2i(-k_z)}$ 代替 $[\frac{1}{2i(-k_z)}]^*$，数学等价）：

$$T_2(\mathbf{k}) = P(\mathbf{k}_{\text{inc},\perp}) P(-\mathbf{k}_{\perp} + \mathbf{k}_{\text{inc},\perp}) \;
      \frac{\delta\bigl(-k_z + k_{\text{inc},z} - \sqrt{k_m^2 - |\mathbf{k}_{\perp} - \mathbf{k}_{\text{inc},\perp}|^2}\bigr)}
           {2i(k_z - k_{\text{inc},z})} \; \widetilde{F}^*(-\mathbf{k})$$

**$T_1$、$T_2$ 与原文第 118–123 行一致，没有错误。** ✅

---

## 3. 化简到紧凑形式

定义两个实值 Ewald 球帽：

$$\kappa_+ = \sqrt{k_m^2 - |\mathbf{k}_{\perp} + \mathbf{k}_{\text{inc},\perp}|^2}, \qquad
  \kappa_- = \sqrt{k_m^2 - |\mathbf{k}_{\perp} - \mathbf{k}_{\text{inc},\perp}|^2}$$

$$C_+(\mathbf{k}) = \frac{P(\mathbf{k}_{\text{inc},\perp}) P(\mathbf{k}_{\perp} + \mathbf{k}_{\text{inc},\perp})}
                       {2\kappa_+} \; \delta(k_z + k_{\text{inc},z} - \kappa_+) \qquad (\text{cap} \to -\mathbf{k}_{\text{inc}})$$

$$C_-(\mathbf{k}) = \frac{P(\mathbf{k}_{\text{inc},\perp}) P(-\mathbf{k}_{\perp} + \mathbf{k}_{\text{inc},\perp})}
                       {2\kappa_-} \; \delta(-k_z + k_{\text{inc},z} - \kappa_-) \qquad (\text{z-rev cap} \to \mathbf{k}_{\text{inc}})$$

利用 delta 替换分母中的 $k_z$：

$$T_1 = -i \, C_+(\mathbf{k}) \, \widetilde{F}(\mathbf{k}) \qquad
  \left(\frac{1}{2i\kappa_+} = -\frac{i}{2\kappa_+}\right)$$

$$T_2 = +i \, C_-(\mathbf{k}) \, \widetilde{F}^*(-\mathbf{k}) \qquad
  \left(\frac{1}{-2i\kappa_-} = \frac{i}{2\kappa_-}\right)$$

将 $\widetilde{F}(\mathbf{k}) = F_{\text{re}}(\mathbf{k}) + iF_{\text{im}}(\mathbf{k})$、
$\widetilde{F}^*(-\mathbf{k}) = F_{\text{re}}(-\mathbf{k}) - iF_{\text{im}}(-\mathbf{k})$ 代入：

$$\boxed{
\begin{aligned}
\widetilde{I}_{i-s}(\mathbf{k})
&= -i C_+(\mathbf{k}) F_{\text{re}}(\mathbf{k}) + C_+(\mathbf{k}) F_{\text{im}}(\mathbf{k}) \\
&\quad + i C_-(\mathbf{k}) F_{\text{re}}(-\mathbf{k}) + C_-(\mathbf{k}) F_{\text{im}}(-\mathbf{k})
\end{aligned}}
\tag{正确}$$
---

## 4. 原文第 124–126 行的表达式与逐项对比

原文写为：

$$-\ii(\text{cap} \to \mathbf{-\mathbf{k}_{\text{inc}}} + \text{z-reversed cap} \to \mathbf{\mathbf{k}_{\text{inc}}}) F_{\text{re}}$$
$$+\ii(\text{z-reversed cap} \to \mathbf{\mathbf{k}_{\text{inc}}} - \text{cap} \to \mathbf{-\mathbf{k}_{\text{inc}}}) F_{\text{im}}$$

按记号的自然语义展开（cap → $-\mathbf{k}_{\text{inc}}$ 来源于 $T_1$，被作用函数的参数为 $\mathbf{k}$；
z-rev cap → $\mathbf{k}_{\text{inc}}$ 来源于 $T_2$，被作用函数的参数为 $-\mathbf{k}$）：

$$\widetilde{I}_{i-s}^{\text{(原文)}} = -i C_+ F_{\text{re}}(\mathbf{k}) - i C_- F_{\text{re}}(-\mathbf{k})
                                     - i C_+ F_{\text{im}}(\mathbf{k}) + i C_- F_{\text{im}}(-\mathbf{k})$$

### 逐项对比

| 项 | 正确系数 | 原文系数 |
|----|---------|----------|
| $C_+ F_{\text{re}}(\mathbf{k})$ | $-i$ | $-i$ |
| $C_- F_{\text{re}}(-\mathbf{k})$ | **$+i$** | $-i$ |
| $C_+ F_{\text{im}}(\mathbf{k})$ | **$+1$** | $-i$ |
| $C_- F_{\text{im}}(-\mathbf{k})$ | **$+1$** | $+i$ |

**四个项中三个错误。** 根因：$T_2 = +i C_- \widetilde{F}^*(-\mathbf{k})$ 被错误地沿用了 $T_1$ 的 $-i$ 因子；
且 $F_{\text{im}}$ 项中 $i \times i = -1$ 和 $i \times (-i) = +1$ 的抵消未被正确执行。

---

## 5. 与 Ling 2018 的独立验证

Ling et al., *Biomed. Opt. Express* (2018) 的 Eq. (5)–(6) 给出了相同物理系统的传递函数。
以下将本文推导、Ling 2018、以及原文第 124–126 行三者的系数进行对比。

### 5.1 记号映射

| 本文 | Ling 2018 |
|------|-----------|
| $\mathbf{k}_{\perp}$ | $\vec{u}$ |
| $\mathbf{k}_{\text{inc},\perp}$ | $\vec{u}_i$ |
| $k_{\text{inc},z}$ | $\eta_i = \sqrt{k^2 - \|\vec{u}_i\|^2}$ |
| $\sqrt{k_m^2 - \|\mathbf{k}_{\perp}\|^2}$ | $\eta(\vec{u})$ |
| $F(\mathbf{r})$ | $-\text{const} \cdot \Delta\epsilon(\vec{r})$ |
| $F_{\text{re}}$ | $-\text{const} \cdot \Delta\epsilon_{\text{Re}}$ |
| $F_{\text{im}}$ | $-\text{const} \cdot \Delta\epsilon_{\text{Im}}$ |

其中 $F = k_m^2(1-n^2/n_m^2) = -(k_m^2/n_m^2)(n^2-n_m^2) = -\text{const} \cdot \Delta\epsilon$。

### 5.2 系数对比

忽略公共实因子 $\frac{k_0^2}{2} S \cdot \frac{1}{\eta}$，仅比较 $i$ 与 $\pm 1$ 的复系数：

| | Ling 2018 ($H_{\text{Re}}, H_{\text{Im}}$) | 本文正确推导 (对 $F$) | 本文正确推导 (对 $\Delta\epsilon$) | 原文第 124–126 行 (对 $F$) | 原文 (对 $\Delta\epsilon$) |
|---|---|---|---|---|---|
| Cap × $\text{Re}$ | $+i$ | $-i$ | **$+i$** ✅ | $-i$ | $+i$ |
| Z-rev cap × $\text{Re}$ | $-i$ | $+i$ | **$-i$** ✅ | $-i$ | **$+i$** ❌ |
| Cap × $\text{Im}$ | $-1$ | $+1$ | **$-1$** ✅ | $-i$ | **$+i$** ❌ |
| Z-rev cap × $\text{Im}$ | $-1$ | $+1$ | **$-1$** ✅ | $+i$ | **$-i$** ❌ |

- **本文正确推导** 经 $F \propto -\Delta\epsilon$ 变换后与 Ling 2018 **完全一致**。✅
- **原文第 124–126 行** 有 3/4 项与 Ling 2018 不符。❌

### 5.3 Ling 2018 Eq. (5)–(6) 原文

$$H_{\mathrm{Re}} = \frac{\mathrm{i} k_0^{2}}{2} S \left\{P^{*}(-\vec{u}_i) \frac{e^{-\mathrm{i}[\eta_i + \eta(\vec{u} - \vec{u}_i)] z}}{\eta(\vec{u} - \vec{u}_i)} P(\vec{u} - \vec{u}_i) - P(-\vec{u}_i) \frac{e^{\mathrm{i}[\eta_i + \eta(\vec{u} + \vec{u}_i)] z}}{\eta(\vec{u} + \vec{u}_i)} P^{*}(-\vec{u} - \vec{u}_i) \right\}$$

$$H_{\mathrm{Im}} = -\frac{k_0^{2}}{2} S \left\{P^{*}(-\vec{u}_i) \frac{e^{-\mathrm{i}[\eta_i + \eta(\vec{u} - \vec{u}_i)] z}}{\eta(\vec{u} - \vec{u}_i)} P(\vec{u} - \vec{u}_i) + P(-\vec{u}_i) \frac{e^{\mathrm{i}[\eta_i + \eta(\vec{u} + \vec{u}_i)] z}}{\eta(\vec{u} + \vec{u}_i)} P^{*}(-\vec{u} - \vec{u}_i) \right\}$$

---

## 6. Hermitian 对称性验证

$T_2$ 应为 $T_1$ 的厄米共轭：$T_2(\mathbf{k}) = T_1^*(-\mathbf{k})$。此性质与 $F$ 的奇偶性**完全无关**。

正确表达式通过检验（仅用到 $C_+(-\mathbf{k}) = C_-(\mathbf{k})$）：

$$T_1^*(-\mathbf{k}) = [-i C_+(-\mathbf{k}) \widetilde{F}(-\mathbf{k})]^*
                     = i C_-(\mathbf{k}) \widetilde{F}^*(-\mathbf{k}) = T_2(\mathbf{k}) \quad ✅$$

原文表达式不能通过：

$$\widetilde{I}_{i-s}^{\text{(原文)}}(-\mathbf{k}) = \widetilde{I}_{i-s}^{\text{(原文)}*}(\mathbf{k})
\;\Longrightarrow\; C_+ F_{\text{re}}(\mathbf{k}) + C_- F_{\text{re}}(-\mathbf{k}) = 0$$

这对一般散射势不成立。❌

---

## 7. 修正后的表达式

$$\boxed{
\begin{aligned}
\widetilde{I}_{i-s}(\mathbf{k})
= &\; -i C_+(\mathbf{k}) F_{\text{re}}(\mathbf{k}) + C_+(\mathbf{k}) F_{\text{im}}(\mathbf{k}) \\
  &\; + i C_-(\mathbf{k}) F_{\text{re}}(-\mathbf{k}) + C_-(\mathbf{k}) F_{\text{im}}(-\mathbf{k})
\end{aligned}}
$$

---

## 8. 附：其他次要问题

1. **Eq. (6)**：傅里叶变换遗漏 $2\pi$ 因子（取决于约定，可能在全文中抵消）。
2. **第 113–115 行复共轭写法**：用 $-\frac{1}{2i(-k_z)}$ 代替 $[\frac{1}{2i(-k_z)}]^*$ 虽然等价，但**很可能是导致后续符号错误的直接原因**——$T_1$ 的 $-i$ 因子与 $T_2$ 的「$-$ 号 + 未共轭分母」技巧在整理紧凑记号时极易混淆。
3. **i-i 项**：$\widetilde{I}_{i-i} = P(\mathbf{k}_{\text{inc},\perp}) P(\mathbf{k}_{\perp}+\mathbf{k}_{\text{inc},\perp}) \delta^{(3)}(\mathbf{k})$，简写为 $\delta^{(3)}(\mathbf{k})$ 需假设照明在 NA 范围内。