# Need: 我想跑一个自主改进循环 / Start an Autonomous Improvement Loop

当用户想对某个可量化目标运行 "propose → evaluate → keep-or-revert" 自主改进循环。

## 起步推荐 / Starter Picks

首选两个最通用的入门项目：

1. **[kayba-ai/recursive-improve](https://github.com/kayba-ai/recursive-improve)**
   递归自我改进框架。智能体捕获执行轨迹、分析失败模式、应用针对性修复，以 keep-or-revert 评估每次改动。最接近原始 `karpathy/autoresearch` 的设计哲学，活跃维护。

2. **[WecoAI/aideml](https://github.com/WecoAI/aideml)**
   AIDE：树搜索 ML 工程智能体。自主生成代码、运行实验、根据评估指标迭代改进。有成熟的云平台 `weco.ai` 支持。适合 ML 实验自动化。

## 进阶选项 / Advanced Options

- **[gepa-ai/gepa](https://github.com/gepa-ai/gepa)** — ICLR 2026 Oral。反射式 prompt 进化，用自然语言反思替代 RL 来优化任何文本参数。如果你的优化目标可以用自然语言参数描述，这是目前最强的方法之一。

- **[sentient-agi/EvoSkill](https://github.com/sentient-agi/EvoSkill)** — 自动技能发现。从失败轨迹中进化出可复用技能和 prompt，支持 Claude Code、Codex CLI、OpenCode 等多种运行时。

- **[ShengranHu/ADAS](https://github.com/ShengranHu/ADAS)** — ICLR 2025。元智能体自动设计新的智能体架构。如果你不只满足于参数调优，想探索新的智能体结构，从这里开始。

## 如果你用 Claude Code / If You Use Claude Code

- **[drivelineresearch/autoresearch-claude-code](https://github.com/drivelineresearch/autoresearch-claude-code)** — 最干净的 Claude Code 移植版，附带生物力学案例研究
- **[uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch)** — 推广到软件、文档、安全等可量化目标
- **[james-s-tayler/lazy-developer](https://github.com/james-s-tayler/lazy-developer)** — 多目标优化（覆盖率、测试速度、构建速度、复杂度）

## 注意事项 / Notes

- 所有自主改进循环都需要一个**可量化的评估指标**（fitness function）。如果你的优化目标无法被自动评估，这个模式不适用。
- 建议用小规模实验先验证循环逻辑，再放大到长时间运行。
- 查看 `references/full-catalog.md` 获取完整的 General-purpose descendants 列表（25+ 工具）。
