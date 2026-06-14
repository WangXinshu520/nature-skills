# Platform Ports & Hardware Forks / 平台移植和硬件分支

将 autoresearch 适配到不同硬件/平台的移植版本。如果你的计算环境不是标准 Linux+CUDA，从这里开始。

For full descriptions, see `references/full-catalog.md`.

## 工具列表 / Tool List

- [gianfrancopiana/openclaw-autoresearch](https://github.com/gianfrancopiana/openclaw-autoresearch) — OpenClaw port of pi-autoresearch，任意优化目标的自主实验循环 (OpenClaw port with statistical confidence scoring)
- [miolini/autoresearch-macos](https://github.com/miolini/autoresearch-macos) — 广泛采用的macOS分支，适配Apple Silicon/MPS (Widely adopted macOS fork for Apple Silicon/MPS)
- [trevin-creator/autoresearch-mlx](https://github.com/trevin-creator/autoresearch-mlx) — MLX-native Apple Silicon port，移除PyTorch/CUDA依赖 (MLX-native, removes PyTorch/CUDA entirely)
- [jsegov/autoresearch-win-rtx](https://github.com/jsegov/autoresearch-win-rtx) — Windows-native RTX分支，面向消费级NVIDIA GPU (Windows-native for consumer NVIDIA GPUs)
- [iii-hq/n-autoresearch](https://github.com/iii-hq/n-autoresearch) — 多GPU基础设施，结构化实验追踪、自适应搜索、崩溃恢复 (Multi-GPU with crash recovery and adaptive search)
- [lucasgelfond/autoresearch-webgpu](https://github.com/lucasgelfond/autoresearch-webgpu) — 浏览器/WebGPU port，无需Python环境 (Browser/WebGPU port, no Python setup needed)
- [tonitangpotato/autoresearch-engram](https://github.com/tonitangpotato/autoresearch-engram) — 带持久认知记忆的分支，频率加权跨会话知识检索 (Persistent cognitive memory with frequency-weighted retrieval)
- **Colab/Kaggle T4 port** — 适配免费T4 GPU (Google Colab/Kaggle)，零成本零本地配置 (Free T4 GPUs with zero cost and zero local setup) — [upstream issue #208](https://github.com/karpathy/autoresearch/issues/208)
- [ArmanJR-Lab/autoautoresearch](https://github.com/ArmanJR-Lab/autoautoresearch) — Jetson AGX Orin port，Go二进制"创意总监"注入新颖性以逃离局部最优 (Jetson Orin with Go-based creative director injecting novelty)

## 平台速查 / Quick Platform Lookup

| 平台 / Platform | 推荐项目 / Recommended |
|---|---|
| Apple Silicon (MPS) | `miolini/autoresearch-macos` |
| Apple Silicon (MLX) | `trevin-creator/autoresearch-mlx` |
| Windows + RTX | `jsegov/autoresearch-win-rtx` |
| Browser/WebGPU | `lucasgelfond/autoresearch-webgpu` |
| Multi-GPU | `iii-hq/n-autoresearch` |
| Free GPU (Colab/Kaggle) | Colab/Kaggle T4 port |
| Jetson Orin | `ArmanJR-Lab/autoautoresearch` |
