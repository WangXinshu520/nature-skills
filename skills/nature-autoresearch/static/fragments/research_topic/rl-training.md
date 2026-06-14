# RL Training Infrastructure / 强化学习训练基础设施

Systems research on infrastructure for reinforcement learning (RL) training, particularly RL post-training for LLMs (RLHF/RLVR). Covers rollout management, resource harvesting, and reward service disaggregation.

For full paper details, see `references/paper-catalog.md`.

## 论文列表 / Paper List

1. **RollPacker: Taming Long-Tail Rollouts for RL Post-Training with Tail Batching** [NSDI 2026]
   Addresses the long-tail problem in RL rollout generation by dynamically batching tail rollouts, improving GPU utilization during RLHF training. / 通过动态批处理长尾rollout解决RL训练中的长尾问题，提高RLHF训练时的GPU利用率。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/gao-wei) | [PDF](https://www.usenix.org/system/files/nsdi26-gao-wei.pdf)

2. **RLBoost: Harvesting Preemptible Cloud Resources for Cost-Efficient Reinforcement Learning on LLMs** [NSDI 2026]
   Exploits preemptible cloud instances for cost-efficient RL training on LLMs, with graceful state recovery when instances are reclaimed. / 利用可抢占云实例进行成本高效的LLM RL训练，实例回收时优雅恢复状态。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/wu-yongji) | [PDF](https://www.usenix.org/system/files/nsdi26-wu-yongji.pdf)

3. **DistRS: Disaggregated Reward Service for RLVR with Batch-Level Constraint** [NSDI 2026]
   Disaggregates the reward computation service from the training loop in RL with verifiable rewards (RLVR), enabling independent scaling of reward models and training actors. / 在可验证奖励RL中将奖励计算服务从训练循环中分离，独立扩展奖励模型和训练actor。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/zhu-ruidong) | [PDF](https://www.usenix.org/system/files/nsdi26-zhu-ruidong.pdf)

## 实验指导 / Experiment Guide

### 典型实验配置 / Typical Setup
- **Frameworks**: OpenRLHF, DeepSpeed-Chat, veRL, Ray
- **RL类型**: PPO (RLHF) 或 GRPO/REINFORCE (RLVR)
- **GPU配置**: 训练actor × N + 推理rollout × M + 奖励模型 × K 三类GPU资源
- **云资源**: AWS Spot/阿里云抢占式 (RLBoost场景)

### 常用指标 / Common Metrics
| Metric | 用途 | Papers |
|--------|------|--------|
| **Rollout GPU Utilization** | Rollout阶段GPU使用率 | RollPacker |
| **Training Iteration Time** | 单步训练(含rollout+reward)耗时 | DistRS, RollPacker |
| **Cost per Training Step** | 成本效率 | RLBoost (preemptible vs on-demand) |
| **Reward Computation Throughput** | 奖励计算吞吐 | DistRS |
| **Recovery Overhead** | 抢占后恢复开销 | RLBoost |

### 常用Baseline / Common Baselines
- **Synchronous rollouts** (no batching): 最简单的rollout模式
- **On-demand instances only**: 全按需实例 (vs preemptible)
- **In-process reward computation**: 训练进程内计算奖励 (vs 分离)

### 实验常见坑 / Common Pitfalls
- **长尾rollout效应**: rollout长度分布有长尾，少数极长rollout拖慢整批。RollPacker重点解决此问题。
- **奖励模型和训练分离**: reward computation和training actor的资源需求不同 (计算 vs 通信密集型), 共置浪费，分离可弹性扩缩(DistRS)。
- **抢占恢复时间**: 可抢占实例的实验需要测量recovery时间+数据损失，不能只看稳态性能。
- **多集群异构**: RL训练常跨多集群/多region部署，网络延迟差异大，需要分别测试。

## 评估与洞察 / Evaluation & Insights

### 类别级评价 / Category-Level Assessment

RL training infrastructure for LLMs (RLHF/RLVR) is a rapidly growing systems research area driven by the post-training phase of major LLM releases (Gemini, GPT-4, LLaMA). Key trends:

- **Tail problem dominance**: RollPacker shows that long-tail rollouts are the primary GPU utilization bottleneck in RLHF training—a classic systems problem (tail latency / stragglers) emerging in a new context
- **Disaggregation for RL**: DistRS applies the resource disaggregation pattern to RL training, separating reward computation from the training loop. This mirrors broader systems trends (disaggregated serving, disaggregated storage)
- **Cost-conscious training**: RLBoost targets the practical reality that RL training on LLMs is expensive—preemptible instances offer a path to cost reduction previously unexplored for RL workloads

### 论文亮点与局限 / Paper Highlights & Limitations

**RollPacker** — Dynamic tail batching for long-tail RL rollouts, improving GPU utilization by grouping rollouts of different lengths into balanced batches. **Limitation**: Batching benefits depend on rollout length distribution; best when there is significant length variance across rollouts.

**RLBoost** — Harvesting preemptible cloud instances for cost-efficient LLM RL training with graceful state recovery. **Limitation**: Preemptible instance availability varies by cloud provider and region; recovery overhead increases with checkpoint frequency. Best for cost-sensitive training where occasional preemption is acceptable.

**DistRS** — Disaggregated reward computation from the training loop, enabling independent scaling of reward models and training actors. **Limitation**: Added communication overhead between reward service and trainers; benefit depends on reward compute cost relative to training actor compute cost.

### 实用建议 / Practical Guidance

- **GPU utilization**: RollPacker when RL rollout lengths vary significantly (common in RLHF with diverse prompts)
- **Cost reduction**: RLBoost for cloud-based RLHF where preemptible instances offer 60-80% discount
- **Architecture design**: DistRS when reward model inference is a significant fraction of training time (large reward models, verification-based RL)
- **Complementary usage**: RollPacker (efficiency) + RLBoost (cost) + DistRS (scalability) address orthogonal dimensions

## 写作指导 / Writing Guide
- **Positioning**: 明确区分"systems contribution" vs "RL algorithm contribution", 你是系统论文
- **Evaluation核心**: (1) rollout batching效率 (2) 成本对比 ($/step) (3) 抢占恢复overhead (4) 奖励计算吞吐
- **审稿要点**: "你的系统效率提升是否独立于RL算法"

## 实现指导 / Implementation Guide
- **基于OpenRLHF/veRL扩展**: 修改rollout manager + reward service
- **抢占恢复**: checkpoint + state serialization + graceful recovery
- **奖励分离**: gRPC/Ray-based reward service, batch-level constraint

## 实验流程 / Experiment Pipeline
```
1. RLHF setup: PPO with actor/critic/reward models
2. Rollout实验: 测量GPU利用率 vs rollout长度分布
3. 抢占实验: 模拟spot回收, 测recovery时间
4. 成本分析: on-demand vs spot, $/step
5. 分离实验: 对比in-process vs 分离reward compute
```

## 注意事项 / Notes

- All three papers target LLM post-training (RLHF/RLVR), which is a rapidly growing area.
- RollPacker and RLBoost address resource efficiency; DistRS addresses architectural modularity.
- RL training infrastructure is distinct from RL algorithm research — these are systems papers.
- 查看 `references/paper-catalog.md` 获取完整论文目录，包括作者和详细标签。
