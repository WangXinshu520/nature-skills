# Evaluation & Benchmarks / 评估和基准测试

评估 AI 智能体在科研/ML工程任务上表现的基准测试套件。用于验证你的智能体的研究能力。

For full descriptions, see `references/full-catalog.md`.

## 工具列表 / Tool List

- [snap-stanford/MLAgentBench](https://github.com/snap-stanford/MLAgentBench) — 评估AI智能体在ML实验任务上的基准套件，13个任务从CIFAR-10到BabyLM (13 tasks from CIFAR-10 to BabyLM)
- [openai/mle-bench](https://github.com/openai/mle-bench) — OpenAI的ML工程基准，衡量AI智能体在ML工程上的表现 (OpenAI's benchmark for ML engineering performance)
- [chchenhui/mlrbench](https://github.com/chchenhui/mlrbench) — MLR-Bench：评估AI智能体在开放ML研究上的表现，201个NeurIPS/ICLR/ICML workshop任务 (201 tasks from NeurIPS/ICLR/ICML workshops)
- [gersteinlab/ML-Bench](https://github.com/gersteinlab/ML-Bench) — 评估LLM和智能体在仓库级代码ML任务上的表现 (Repository-level code ML task evaluation)
- [THUDM/AgentBench](https://github.com/THUDM/AgentBench) — 综合LLM-as-Agent评估基准，跨8个不同环境，ICLR 2024 (8 distinct environments, ICLR 2024)

## 选择指南 / Selection Guide

| 目标 / Goal | 推荐基准 / Recommended Benchmark |
|---|---|
| 通用ML实验能力 | `snap-stanford/MLAgentBench` |
| ML工程能力 | `openai/mle-bench` |
| 开放性ML研究能力 | `chchenhui/mlrbench` |
| 仓库级代码ML任务 | `gersteinlab/ML-Bench` |
| 通用Agent能力 | `THUDM/AgentBench` |
