# Need: 我想评估我的智能体 / Evaluate My Agent

当用户想用标准化基准测试评估其 AI 智能体的研究/ML工程能力。

## 按评估目标推荐 / Recommendations by Evaluation Goal

### 通用 ML 实验能力
**[snap-stanford/MLAgentBench](https://github.com/snap-stanford/MLAgentBench)** —
13 个任务从 CIFAR-10 到 BabyLM，全面评估智能体在 ML 实验的各个环节（数据探索、模型选择、超参调优、结果分析）的表现。

### ML 工程能力
**[openai/mle-bench](https://github.com/openai/mle-bench)** —
OpenAI 推出的基准，衡量 AI 智能体在 ML 工程任务上的表现。如果你在做 SWE-bench 类似方向的评估，这是一个重要的参考基准。

### 开放性 ML 研究能力
**[chchenhui/mlrbench](https://github.com/chchenhui/mlrbench)** —
MLR-Bench，201 个来自 NeurIPS/ICLR/ICML workshop 的开放性 ML 研究任务。如果你想知道你的智能体在真正的开放研究问题上表现如何（不是固定的 train/test split），用这个。

### 仓库级代码 ML 任务
**[gersteinlab/ML-Bench](https://github.com/gersteinlab/ML-Bench)** —
评估 LLM 和智能体在仓库级代码上的 ML 任务表现。适合评估代码理解能力。

### 通用 Agent 能力
**[THUDM/AgentBench](https://github.com/THUDM/AgentBench)** —
跨 8 个不同环境（操作系统、数据库、知识图谱、数字卡牌游戏、横向思维谜题、家政、网页购物、网页浏览），ICLR 2024。适合做更广泛的 agent 能力评估。

## 注意事项 / Notes

- 不同基准测试的难度和覆盖范围差异很大。建议从小规模基准（如 MLAgentBench 的单个任务）开始逐步扩展。
- `openai/mle-bench` 需要较多的计算资源。
- `mlrbench` 偏重论文阅读和 idea 生成能力，更适合评估全流程研究智能体。
- 查看 `references/full-catalog.md` 获取完整的 Benchmark 列表。
