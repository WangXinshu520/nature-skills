# General-Purpose Descendants / 通用自主改进循环

直接基于 `karpathy/autoresearch` 模式推广的通用自主改进循环工具。核心特征是 "propose → evaluate → keep-or-revert"。

For full descriptions, see `references/full-catalog.md`.

## 工具列表 / Tool List

- [kayba-ai/recursive-improve](https://github.com/kayba-ai/recursive-improve) — 递归自我改进框架，捕获执行轨迹、分析失败模式、应用针对性修复 (Recursive self-improvement with execution trace analysis)
- [vukrosic/auto-research](https://github.com/vukrosic/auto-research) — 基于文件的开放自主AI研究实验室控制面板 (File-based control plane for open autonomous AI research lab)
- [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) — Claude Code skill，将autoresearch推广为可复用循环 (Claude Code skill generalizing autoresearch into reusable loop)
- [leo-lilinxiao/codex-autoresearch](https://github.com/leo-lilinxiao/codex-autoresearch) — Codex-native autoresearch skill，支持断点续传和多实验并行 (Codex-native with resume and parallel experiments)
- [SeeleAI/Thoth](https://github.com/SeeleAI/Thoth) — Dashboard-first 运行环境，持久化运行、锁定工作项、可视化判据 (Dashboard-first runtime with durable runs and visible ledgers)
- [supratikpm/gemini-autoresearch](https://github.com/supratikpm/gemini-autoresearch) — Gemini CLI skill，支持Google Search验证和真·无人值守模式 (Gemini-native with Google Search grounding and headless mode)
- [davebcn87/pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) — pi扩展+仪表盘，持久化实验循环/实时指标/置信度追踪 (pi extension with dashboard and persistent experiment loops)
- [drivelineresearch/autoresearch-claude-code](https://github.com/drivelineresearch/autoresearch-claude-code) — Claude Code port of pi-autoresearch，附带生物力学案例 (Claude Code port with biomechanics case study)
- [greyhaven-ai/autocontext](https://github.com/greyhaven-ai/autocontext) — 闭环控制面板，支持评估、持久知识、分阶段验证 (Closed-loop with evaluation, persistent knowledge, staged validation)
- [jmilinovich/goal-md](https://github.com/jmilinovich/goal-md) — 推广为 GOAL.md 模式，agent 必须先构建可量化的适应度函数 (GOAL.md pattern requiring measurable fitness function first)
- [james-s-tayler/lazy-developer](https://github.com/james-s-tayler/lazy-developer) — Claude Code skill，按优先级序列编排多目标优化 (Multi-goal optimization across coverage, test speed, build speed, complexity)
- [mutable-state-inc/autoresearch-at-home](https://github.com/mutable-state-inc/autoresearch-at-home) — 协作分支，支持实验认领、共享最佳配置同步、蜂群协调 (Collaborative fork with experiment claiming and swarm coordination)
- [zkarimi22/autoresearch-anything](https://github.com/zkarimi22/autoresearch-anything) — 推广到任何可量化指标：prompt、API性能、落地页、测试套件等 ("If you can measure it, you can optimize it")
- [Entrpi/autoresearch-everywhere](https://github.com/Entrpi/autoresearch-everywhere) — 跨平台扩展，自动检测硬件配置并启动循环 (Cross-platform auto-detecting hardware config)
- [ShengranHu/ADAS](https://github.com/ShengranHu/ADAS) — ICLR 2025，元智能体自动设计新的智能体架构 (Meta-agents inventing novel agent architectures via code)
- [MaximeRobeyns/self_improving_coding_agent](https://github.com/MaximeRobeyns/self_improving_coding_agent) — SICA：自我改进编程智能体，ICLR 2025 Workshop (Self-Improving Coding Agent editing its own codebase)
- [peterskoett/self-improving-agent](https://github.com/peterskoett/self-improving-agent) — 替代性自我改进架构，含反思和元学习循环 (Alternative self-improving architecture with reflection and meta-learning)
- [metauto-ai/HGM](https://github.com/metauto-ai/HGM) — Huxley-Gödel Machine，对SWE-bench进行元级优化 (Meta-level optimization for SWE-bench performance)
- [gepa-ai/gepa](https://github.com/gepa-ai/gepa) — ICLR 2026 Oral，反思式prompt进化，超越GRPO (Reflective prompt evolution outperforming RL on benchmarks)
- [sentient-agi/EvoSkill](https://github.com/sentient-agi/EvoSkill) — 自动技能发现，从失败轨迹中进化可复用技能 (Automated skill discovery from failed trajectories)
- [MrTsepa/autoevolve](https://github.com/MrTsepa/autoevolve) — GEPA-inspired self-play，变异代码策略、头对头评估、Elo排名 (GEPA-inspired self-play with Elo/Bradley-Terry rating)
- [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) — 智能体蜂群智能，并行GPU研究方向、分布式工作 (Agent swarm with parallel GPU research directions)
- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) — 综合技能库，含双环架构 (Comprehensive skill library with two-loop architecture)
- [WecoAI/aideml](https://github.com/WecoAI/aideml) — AIDE：树搜索ML工程智能体，自主迭代改进模型 (Tree-search ML engineering agent)
- [weco.ai](https://weco.ai) — Weco云平台，带可观测性和实验追踪的AIDE生产化 (Cloud platform for AIDE with observability and experiment tracking)
