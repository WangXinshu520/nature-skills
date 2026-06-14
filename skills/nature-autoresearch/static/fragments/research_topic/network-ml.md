# Network ML & AI for Networking / 网络机器学习与AI网络

Systems research on applying machine learning to network systems, and building network infrastructure optimized for AI workloads. Covers congestion control, traffic engineering, network simulation, and AI cluster network design.

For full paper details, see `references/paper-catalog.md`.

## 论文列表 / Paper List

1. **UNUM: A New Framework for Network Control** [NSDI 2026]
   A unified network control framework that leverages ML for end-to-end network management, replacing fragmented control-plane components. / 统一的ML驱动网络控制框架，替代碎片化的控制面组件。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/chen-jiayi) | [PDF](https://www.usenix.org/system/files/nsdi26-chen-jiayi.pdf)

2. **PolicyCache: Intra-flow Learning in Congestion Control** [NSDI 2026]
   Learns optimal congestion control policies within individual flows, adapting in real-time to changing network conditions without prior training. / 在单个流内学习最优拥塞控制策略，无需预训练即可实时适应网络变化。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/tian) | [PDF](https://www.usenix.org/system/files/nsdi26-tian.pdf)

3. **Making Logic a First-Class Citizen in Generative ML for Networking** [NSDI 2026]
   Incorporates logical constraints and domain knowledge into generative ML models for networking tasks, improving correctness and generalization. / 将逻辑约束和领域知识融入网络任务的生成式ML模型，提升正确性和泛化能力。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/he) | [PDF](https://www.usenix.org/system/files/nsdi26-he.pdf)

4. **Geminet: Learning the Duality-based Topology-Agnostic Update Operator for Lightweight Traffic Engineering in Changing Topologies** [NSDI 2026]
   Learns a topology-agnostic traffic engineering operator using duality theory, enabling lightweight re-optimization when network topologies change. / 基于对偶理论学习拓扑无关的流量工程算子，网络拓扑变化时可轻量重新优化。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/liu-ximeng) | [PDF](https://www.usenix.org/system/files/nsdi26-liu-ximeng.pdf)

5. **Matryoshka: Realizing Hyperscale Data Center Network Design for the AI Era** [NSDI 2026]
   Nested topology design for hyperscale data center networks optimized for AI training and inference traffic patterns. / 为AI训练和推理流量优化的超大规模数据中心嵌套拓扑设计。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/cai) | [PDF](https://www.usenix.org/system/files/nsdi26-cai.pdf)

6. **Arcadia: Enabling AI Network Cross-Layer Design and Operations with A Simulation Platform at Scale** [NSDI 2026]
   Large-scale simulation platform for cross-layer AI network design, from physical topology to collective communication scheduling. / 大规模仿真平台支持从物理拓扑到集合通信调度的跨层AI网络设计。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/wang-zhaodong) | [PDF](https://www.usenix.org/system/files/nsdi26-wang-zhaodong.pdf)

7. **PrvTel: Lightweight Models for Private and Accurate Telemetry Data Retention** [NSDI 2026]
   Uses lightweight ML models to enable accurate network telemetry while preserving data privacy through differential privacy mechanisms. / 使用轻量ML模型实现精确网络遥测，同时通过差分隐私机制保护数据。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/zhou-yajie) | [PDF](https://www.usenix.org/system/files/nsdi26-zhou-yajie.pdf)

8. **Defeating Slow-and-Low Threats via Diffusion Model-based Generative Inference** [NSDI 2026]
   Uses diffusion models for generative inference to detect slow-and-low network attacks that evade traditional threshold-based detection. / 使用扩散模型生成式推理检测躲避传统阈值检测的低频慢速网络攻击。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/mirnajafizadeh) | [PDF](https://www.usenix.org/system/files/nsdi26-mirnajafizadeh.pdf)

## 实验指导 / Experiment Guide

### 典型实验配置 / Typical Setup
- **Congestion Control**: NS3仿真器 or 真实RDMA testbed (ConnectX-5/6/7), RoCEv2网络, 胖树/CLOS拓扑
- **Traffic Engineering**: 真实拓扑 (B4, Jupiter), 仿真器 + 生产trace
- **AI Cluster Design**: 大规模仿真 (如Arcadia), GPU训练trace驱动
- **Telemetry**: INT-capable交换机 (Tofino), 差分隐私机制

### 常用指标 / Common Metrics
| Metric | 用途 | Papers |
|--------|------|--------|
| **Flow Completion Time (FCT)** | 流完成时间 | PolicyCache, Geminet |
| **Link Utilization** | 链路利用率 | UNUM, Geminet |
| **Convergence Time** | 控制收敛速度 | PolicyCache (intra-flow learning) |
| **Detection Rate / FPR** | 攻击检测 | Defeating Slow-and-Low |
| **Privacy Budget (ε)** | 差分隐私预算 | PrvTel |

### 实验常见坑 / Common Pitfalls
- **仿真vs真实**: 仿真器结果与真实硬件差距大，尤其在高负载下。需要交叉验证。
- **拓扑敏感性**: 流量工程方案在不同拓扑(胖树/CLOS/Jellyfish)上性能差异可能很大。
- **Dynamic topology**: Geminet等需要拓扑变化场景评估，仅测试固定拓扑不够。
- **长尾延迟**: 网络实验需要报告P99/P999延迟，不能只看平均。

## 评估与洞察 / Evaluation & Insights

### 类别级评价 / Category-Level Assessment

Network ML research sits at the intersection of two rapidly evolving fields. Key trends:

- **Generative ML for networking**: Making Logic and Defeating Slow-and-Low demonstrate that generative approaches (logical constraints + diffusion models) can solve networking problems traditional ML and rule-based systems handle poorly. This is a paradigm shift from discriminative to generative models in networking.
- **AI cluster network design as a systems problem**: Matryoshka and Arcadia address the reality that AI cluster networks need to be co-designed with training workloads—network topology, routing, and collective communication scheduling are interdependent.
- **Learning over pre-programming**: PolicyCache's intra-flow learning for congestion control and Geminet's topology-agnostic traffic engineering show that learned policies can adapt to conditions pre-programmed approaches cannot handle.

### 论文亮点与局限 / Paper Highlights & Limitations

**PolicyCache** — Learns congestion control policies within individual flows without prior training, adapting in real-time to changing network conditions. **Limitation**: Cold-start period until policy learning converges; best for long-lived flows where learning amortizes.

**UNUM** — Unified ML-driven network control framework replacing fragmented control-plane components. **Limitation**: Integration with existing network control planes (BGP, SDN controllers) is non-trivial and may require organizational buy-in.

**Geminet** — Topology-agnostic traffic engineering via duality theory, enabling lightweight re-optimization when topologies change. **Limitation**: Duality-based optimization assumes convexity of traffic engineering objectives; non-convex constraints may degrade quality.

**Matryoshka** — Nested topology design for hyperscale AI data center networks. **Limitation**: Design-time optimization; does not adapt to dynamic workload changes. Best for greenfield deployments where topology can be controlled.

**Arcadia** — Cross-layer simulation platform for AI network design from physical topology to collective communication. **Limitation**: Simulation fidelity depends on modeling accuracy; validation against real hardware is essential.

**Making Logic** — Incorporates logical constraints into generative ML for networking to improve correctness and generalization. **Limitation**: Requires domain experts to encode logical constraints; benefit proportional to constraint quality.

### 实用建议 / Practical Guidance

- **Congestion control**: PolicyCache for environments with long-lived flows (training workloads); pair with HPCC/TIMELY/Swift (from memory-disaggregation) for RDMA networks
- **Network design**: Matryoshka for greenfield AI cluster network design; Arcadia for simulating before deployment
- **Traffic engineering**: Geminet for dynamic topologies (cloud environments); UNUM for unified control plane replacement
- **Security**: Defeating Slow-and-Low for detecting sophisticated network attacks that evade traditional detection

## 写作指导 / Writing Guide
- **Motivation要点**: 明确区分"ML for networking" vs "networking for ML", 建立清晰的positioning
- **Evaluation必须**: (1) 仿真 + 真实testbed双验证 (2) 不同拓扑下的性能 (3) 动态vs静态场景对比 (4) 与传统(non-ML)方案的对比
- **关键**: network论文的实验必须包含真实拓扑和trace

## 实现指导 / Implementation Guide
- **仿真环境**: NS-3 (congestion control) / 自研simulator (Arcadia风格)
- **真实testbed**: 可编程交换机 (Tofino) + RoCE网络
- **ML组件**: 轻量模型 (inference在数据面完成) / 在线学习 (PolicyCache风格)

## 实验流程 / Experiment Pipeline
```
1. 仿真验证: NS-3 + 多种拓扑 (fat-tree/CLOS/Jellyfish)
2. Trace驱动: 使用生产datacenter trace
3. 真实testbed: ≥16节点, 验证仿真结果
4. 指标: FCT (P50/P99), Link Utilization, Convergence Time
5. 隐私实验 (PrvTel): 测ε vs accuracy tradeoff
```

## 注意事项 / Notes

- ML-for-networking research increasingly uses generative AI (diffusion models, LLMs) vs. traditional supervised learning.
- AI cluster network design (Matryoshka, Arcadia) is critical infrastructure for training at 10K+ GPU scale.
- Congestion control papers (PolicyCache) complement RDMA congestion work in the memory-disaggregation section.
- 查看 `references/paper-catalog.md` 获取完整论文目录，包括作者和详细标签。
