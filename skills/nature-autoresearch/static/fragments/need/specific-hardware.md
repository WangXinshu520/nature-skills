# Need: 我有特定硬件 / Specific Hardware

当用户想在非标准环境（Mac/Windows/WebGPU/Jetson/多GPU等）上运行自主改进循环。

## 按平台推荐 / Recommendations by Platform

### Apple Silicon (Mac)
首选 **[miolini/autoresearch-macos](https://github.com/miolini/autoresearch-macos)** —
广泛采用的 macOS 分支，适配 Apple Silicon/MPS，同时保留原始循环形态。
如果不想依赖 PyTorch，用 **[trevin-creator/autoresearch-mlx](https://github.com/trevin-creator/autoresearch-mlx)** — MLX-native，完全移除 PyTorch/CUDA 依赖。

### Windows + NVIDIA RTX
**[jsegov/autoresearch-win-rtx](https://github.com/jsegov/autoresearch-win-rtx)** —
Windows-native RTX 分支，面向消费级 NVIDIA GPU，有明确的 VRAM 门槛和实用的桌面配置路径。

### 浏览器/WebGPU
**[lucasgelfond/autoresearch-webgpu](https://github.com/lucasgelfond/autoresearch-webgpu)** —
让智能体在浏览器中生成训练代码、运行实验、将结果反馈回循环，完全无需 Python 环境配置。

### 多 GPU
**[iii-hq/n-autoresearch](https://github.com/iii-hq/n-autoresearch)** —
多 GPU 基础设施，结构化实验追踪、自适应搜索策略、崩溃恢复、可查询编排。

### 免费 GPU (Google Colab / Kaggle T4)
**Colab/Kaggle T4 port** —
适配免费 T4 GPU，零成本零本地配置。关键改动：Flash Attention 3 → PyTorch SDPA，移除 H100-only kernel 依赖。详见 [upstream issue #208](https://github.com/karpathy/autoresearch/issues/208)。

### Jetson AGX Orin
**[ArmanJR-Lab/autoautoresearch](https://github.com/ArmanJR-Lab/autoautoresearch)** —
Jetson Orin port，带一个 Go 写的"创意总监"，注入新颖性（arxiv 论文 + DeepSeek Reasoner）以逃离局部最优。

## 注意事项 / Notes

- 平台移植版本可能落后于上游更新。使用前检查 fork 的最后活跃时间。
- 如果需要跨平台方案，考虑 **[Entrpi/autoresearch-everywhere](https://github.com/Entrpi/autoresearch-everywhere)** — 自动检测硬件配置并启动循环。
- 对于 WebGPU port，注意浏览器环境的性能限制。
- 查看 `references/full-catalog.md` 获取完整的 Platform ports 列表。
