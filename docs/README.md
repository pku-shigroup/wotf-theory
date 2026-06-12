# PGT Theory — 文档索引

## 理论推导

| 文件 | 内容 |
|------|------|
| [`derivation_report.md`](derivation_report.md) | `pgt_theory.tex` 错误分析：第 124–126 行 cap 简写中的符号错误，逐项对比正确/错误系数，Hermitian 对称性验证 |
| [`comparison_with_ling2018.md`](comparison_with_ling2018.md) | 本文推导 vs Ling 2018 的逐步对比：相位约定差异、$F \propto -\Delta\epsilon$ 映射、传递函数系数逐项验证 |

## 传递函数计算

| 文件 | 内容 |
|------|------|
| [`wotf_computation_analysis.md`](wotf_computation_analysis.md) | 传播-相关方法的数学原理（$(z, \mathbf{k}_\perp)$ 混合域 $\leftrightarrow$ 3D Ewald 球壳的等价性）；频谱泄露分析；直接离散化 Ewald 球壳的方案评估（最近邻 → 线性插值 → 体素相交） |
| [`ewald_discretization_methods.md`](ewald_discretization_methods.md) | Ewald 球壳直接离散化的具体方案对比：最近邻、线性插值、sinc 壳近似、体素相交。为什么线性插值对本场景是精确解 |
| [`ewald_cap_mapping.md`](ewald_cap_mapping.md) | 2D 频谱 ↔ Ewald 球壳的双向映射：前向 (project) 和伴随 (backproject) 算子的数学结构；伴随性三条件；完整代码示例；数值验证方法 |
| [`solver_analysis.md`](solver_analysis.md) | 三个求解器架构对比（CPU / GPU on-the-fly / GPU padded）；RTX 4090 性能预估；预计算 + 落盘的可行性分析 |

## 代码与可视化

| 路径 | 内容 |
|------|------|
| `../pgt_theory.tex` | 主推导文档（LaTeX） |
| `../visualize_caps.py` | Ewald 球冠可视化脚本 |
| `../figs/` | 输出的球冠图像 |
