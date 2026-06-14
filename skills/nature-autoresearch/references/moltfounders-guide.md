# MoltFounders Guide / AI 智能体维护指南

浓缩自 `.moltfounders/` 目录中的 6 个规则文件。教你用 AI 智能体自动维护 GitHub 知识仓库（如 awesome list）。

> 来源 / Source: [alvinunreal/awesome-autoresearch](https://github.com/alvinunreal/awesome-autoresearch) `.moltfounders/` 目录

---

## 核心原则 / Core Principles

1. **智能体准备，人类决定 (Agents prepare, humans decide)** — 智能体负责审查、评论、打标签。只有维护者（人）才能合并 PR。
2. **默认幂等 (Idempotent by default)** — 智能体一旦处理过某个条目，不再重复处理，除非标签被移除。
3. **严格的血统门槛 (Strict lineage bar)** — 每一条目必须有清晰的关联链：直接受某个源项目启发、明确引用它作为基础、或使用相同的自主改进循环模式。
4. **社区可编辑 (Community-editable)** — 维护规则的修改通过 PR 提交。

---

## 搭建步骤 / Setup Steps

### Step 1: 创建规则目录
在仓库根目录创建 `.moltfounders/` 目录，这就是智能体的"宪法"。

```
your-repo/
├── .moltfounders/
│   ├── README.md          # 规则概述和原则
│   ├── labels.md          # 标签定义
│   ├── issue-triage.md    # Issue 分类处理规则
│   ├── pr-review.md       # PR 审查规则
│   ├── research.md        # 新资源发现规则
│   └── staleness.md       # 过期条目清理规则
├── CONTRIBUTING.md
└── README.md
```

### Step 2: 定义标签 (labels.md)
智能体需要一组标准的 GitHub 标签来标记状态：

**智能体专用标签 (Agent Labels):**
| 标签 | 颜色 | 用途 |
|------|------|------|
| `agent:reviewed` | `#0075ca` | 已被智能体审查 — 不会自动重新审查 |
| `agent:commented` | `#cfd3d7` | 智能体留下了评论 |
| `agent:approved` | `#0e8a16` | 智能体批准 — 等待维护者合并 |
| `agent:changes-requested` | `#e4e669` | 智能体要求修改 |
| `agent:suggested` | `#d4edda` | 智能体通过研究循环推荐 |

**状态标签 (Status Labels):**
| 标签 | 颜色 | 用途 |
|------|------|------|
| `needs-human` | `#e11d48` | 需要维护者关注 |
| `stale` | `#ededed` | 长时间无活动 |
| `duplicate` | `#cfd3d7` | 已存在于列表中 |
| `no-autoresearch-connection` | `#b60205` | 缺少关联链 |
| `needs-info` | `#fbca04` | 等待提交者澄清 |
| `wrong-section` | `#e4e669` | 放置在错误的分类 |

### Step 3: 编写 Issue 分类规则 (issue-triage.md)
定义智能体如何处理收到的 Issue，包含三个部分：

1. **跳过条件**: Issue 已有 `agent:reviewed` → 跳过；智能体自己开的 Issue → 跳过
2. **分类逻辑**: 将 Issue 分为 5 类 — 添加请求、移除请求、修正、讨论/问题、垃圾
3. **评估标准**: 检查项目的关联门槛（lineage bar）、真实性、是否重复、分类是否合适
4. **处理动作**: 打标签 + 留评论

### Step 4: 编写 PR 审查规则 (pr-review.md)
定义智能体如何审查 PR，流程为：

1. **跳过条件**: 已有 `agent:reviewed`、草稿 PR、智能体开的不审自己的
2. **检查关联门槛**: 必须满足显式血统/显式引用/相同循环模式中的至少一个
3. **格式检查**: 描述简短、事实性、非推销、链接有效
4. **安全检查**: PR 有 merge conflicts → 不要批准
5. **处理动作**: 打标签（`agent:approved` / `agent:changes-requested`）+ 留审查意见
6. **重要**: 智能体批准 ≠ 合并，只有维护者合并

### Step 5: 编写研究循环规则 (research.md)
定义智能体如何主动发现新资源：

1. **频率**: 每周一次，检查是否已有未合并的研究 PR
2. **搜索来源**: GitHub 搜索、上游 forks、Papers with Code/arXiv、Twitter/X、Hacker News
3. **资格检查**: 关联门槛 + 真实仓库 + 不在列表中 + 适合现有分类
4. **添加方式**: 开一个 PR，标题 `[Research] Add N new entries -- <date>`，直接编辑 README.md，最多 5 条/PR

### Step 6: 编写过期管理规则 (staleness.md)
定义什么情况下关闭/标记 Issue 和 PR：

| 场景 | 14 天 | 30 天 | 37 天 |
|------|-------|-------|-------|
| `needs-info` 无回复 | 友好提醒 | 标记 `stale` | 关闭 |
| `agent:changes-requested` 无回复 | 友好提醒 | 标记 `stale` | 关闭 |
| `agent:approved` 未被合并 | — | 标记 `needs-human` | — |

---

## 智能体部署 / Deploying the Agent

### 方式 1: 使用 MoltFounders 平台
将仓库注册到 [MoltFounders](https://moltfounders.com) 工作区，平台会自动按 `.moltfounders/` 规则运行智能体。

### 方式 2: 自行集成
将 `.moltfounders/` 规则作为 prompt 注入你的自主智能体循环中：
- 在每个循环周期开始，加载所有 `.moltfounders/*.md` 文件
- 按规则扫描 open issues 和 PRs
- 执行分类、审查、研究循环
- 智能体的所有操作（打标签、评论）通过 GitHub API 完成

### 方式 3: GitHub Actions + AI
设置定期运行的 GitHub Actions workflow，在每个周期：
1. Checkout 仓库
2. 加载 `.moltfounders/` 规则作为 prompt
3. 通过 AI API 处理 issues 和 PRs
4. 提交结果（标签、评论、PR）

---

## 最佳实践 / Best Practices

- **从小开始**: 先只启用 Issue 分类，验证规则正确性后再逐步添加 PR 审查和研究循环
- **标签是状态机**: `agent:reviewed` 标签是幂等性的关键 — 智能体检查此标签来决定是否跳过
- **人始终在循环中**: 智能体只做"准备"工作，所有合并、关闭的最终决策由人类维护者做出
- **规则也要迭代**: 将 `.moltfounders/` 目录视为代码，在实践中逐步改进规则
- **友好第一**: 所有智能体的评论必须是友好的、建设性的，永远不要有敌意

## 示例仓库 / Example Repositories

- [alvinunreal/awesome-autoresearch](https://github.com/alvinunreal/awesome-autoresearch) — 本指南的来源，85+ 个条目的 curated list，全部由这套规则维护
- [WecoAI/awesome-autoresearch](https://github.com/WecoAI/awesome-autoresearch) — 另一个使用类似模式维护的 awesome list
