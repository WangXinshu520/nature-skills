# Memory Disaggregation & RDMA Systems / 内存分离与RDMA系统

Systems research on disaggregated memory architectures, RDMA-based memory access, and hardware offloading for efficient resource pooling in data centers. Covers soft-RDMA, DPU-accelerated prefetching, RNIC offloading, and RDMA congestion control.

For full paper details, see `references/paper-catalog.md`.

## 论文列表 / Paper List

1. **BURST: Seeking High-performance, Interoperability and Scalability in Soft-RDMA** [NSDI 2026]
   Software-based RDMA (Soft-RDMA) implementation achieving near-hardware RDMA performance while maintaining interoperability across different RDMA implementations. / 基于软件的RDMA实现，达到接近硬件RDMA性能，同时跨不同RDMA实现保持互操作性。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/shen) | [PDF](https://www.usenix.org/system/files/nsdi26-shen.pdf)

2. **SYMPHONY: Enabling Compute-Memory Disaggregation in LLM Serving Systems** [NSDI 2026]
   Enables compute-memory disaggregation for LLM serving, allowing KV cache and model weights to reside on remote memory pools accessed via RDMA. / 实现LLM服务的计算-内存分离，KV缓存和模型权重通过RDMA访问远程内存池。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/agarwal) | [PDF](https://www.usenix.org/system/files/nsdi26-agarwal.pdf)

3. **OneSidedMW: Managing Disaggregated Memory Efficiently, Flexibly, and Securely with RNIC Offloading** [NSDI 2026]
   Offloads disaggregated memory management to RNICs (RDMA NICs) for efficient, flexible, and secure one-sided memory access without CPU involvement. / 将分离内存管理卸载到RNIC，实现高效、灵活、安全的单侧内存访问，无需CPU参与。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/wang-zixuan) | [PDF](https://www.usenix.org/system/files/nsdi26-wang-zixuan.pdf)

4. **PD3: Prefetching Data with DPUs for Disaggregated Memory** [NSDI 2026]
   Uses DPUs (Data Processing Units) to intelligently prefetch data from disaggregated memory pools, hiding remote access latency through predictive prefetching. / 使用DPU智能预取分离内存池数据，通过预测性预取隐藏远程访问延迟。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/sankhe) | [PDF](https://www.usenix.org/system/files/nsdi26-sankhe.pdf)

5. **HPCC: High Precision Congestion Control** [SIGCOMM]
   High-precision congestion control for RDMA networks using in-network telemetry (INT) to achieve near-zero queue buildup and ultra-low latency. / 利用网内遥测实现RDMA网络高精度拥塞控制，接近零排队和超低延迟。
   [PDF](https://dl.acm.org/doi/10.1145/3387514.3405895)

6. **TIMELY: RTT-based Congestion Control for the Datacenter** [SIGCOMM]
   RTT-based congestion control algorithm for RDMA in datacenters, using round-trip time measurements instead of ECN marks for faster and more accurate congestion signals. / 基于RTT的RDMA数据中心拥塞控制，使用往返时间测量替代ECN标记，更快更精确。
   [PDF](https://dl.acm.org/doi/10.1145/2785956.2787510)

7. **Swift: Delay is Simple and Effective for Congestion Control in the Datacenter** [SIGCOMM]
   Demonstrates that simple delay-based congestion control (target-delay=rtt−base_rtt) is highly effective for RDMA networks, achieving both high throughput and low latency. / 证明简单的延迟拥塞控制在RDMA网络中既高效又易实现，同时达到高吞吐和低延迟。
   [PDF](https://dl.acm.org/doi/10.1145/3387514.3406591)

8. **SwCC: Software-Programmable and Per-Packet Congestion Control in RDMA Engine** [NSDI]
   Software-programmable congestion control framework for RDMA NICs, enabling per-packet congestion control policies without firmware changes. / RDMA网卡上的软件可编程拥塞控制框架，无需固件修改即可实现逐包拥塞控制策略。
   [PDF](https://www.usenix.org/system/files/nsdi26-sankhe.pdf)

## 实验指导 / Experiment Guide

### 典型实验配置 / Typical Setup
- **Hardware**: GPU节点 (H100) + 专用内存节点 (大容量DRAM/NVM) + RDMA网络 (InfiniBand/RoCE)
- **RNIC/DPU**: ConnectX-7 with RNIC offloading, BlueField DPU
- **LLM serving场景**: 推理GPU访问远程KV cache (SYMPHONY), 典型TP=4/8
- **Micro-benchmark**: 单边RDMA read/write延迟和带宽, 多连接并发

### 常用指标 / Common Metrics
| Metric | 用途 | Papers |
|--------|------|--------|
| **Remote Access Latency (µs)** | 远程内存访问延迟 | BURST, OneSidedMW, PD3 |
| **Throughput (GB/s)** | 聚合带宽 | BURST, SYMPHONY |
| **TTFT / TPOT with Remote Memory** | LLM服务端到端指标 | SYMPHONY |
| **Prefetch Accuracy** | 预取命中率 | PD3 |
| **Congestion Window / Queue Depth** | 拥塞控制行为 | HPCC, TIMELY, Swift |
| **Flow Completion Time (FCT)** | 流完成时间 | SwCC, HPCC |

### 常用Baseline / Common Baselines
- **Local memory only**: 全部数据在本地GPU内存
- **Default RDMA (no offloading)**: 标准RDMA，无RNIC/DPU卸载
- **DCQCN**: 主流RDMA拥塞控制 (ECN-based)
- **Static prefetching**: 最简单的预取策略

### 实验常见坑 / Common Pitfalls
- **RDMA配置复杂**: MTU, QP数量, memory registration方式对性能影响巨大，需报告完整配置。
- **冷热数据分离**: 远程内存实验中，数据访问模式(冷/热)对结果影响大，仅测试均匀随机访问不够。
- **拥塞控制参数敏感**: HPCC/TIMELY/Swift的性能对参数设置(INT interval, RTT measurement window)非常敏感。
- **Prefetch overhead**: PD3的预取在访问模式规律时有效，在随机访问时反而可能增加延迟。

## 评估与洞察 / Evaluation & Insights

### 类别级评价 / Category-Level Assessment

Memory disaggregation and RDMA systems research addresses the hardware reality that GPU compute outpaces GPU memory growth. Key trends:

- **Disaggregation for LLM serving is here**: SYMPHONY demonstrates that remote KV cache access via RDMA is not only feasible but offers 2.4× latency reduction and 4× capacity increase—challenging the assumption that LLM serving must be memory-local
- **Hardware offloading from CPU to network**: OneSidedMW (RNIC offloading) and PD3 (DPU prefetching) push memory management closer to the network, freeing CPUs for compute. This is the systems-level equivalent of GPU kernel offloading
- **Software-defined RDMA**: BURST's soft-RDMA approach enables interoperability across RDMA implementations—critical for heterogeneous data centers where hardware RDMA from different vendors must coexist
- **Congestion control as foundation**: HPCC, TIMELY, Swift, and SwCC are foundational building blocks—without reliable congestion control, disaggregated memory cannot achieve predictable performance

### 论文亮点与局限 / Paper Highlights & Limitations

**SYMPHONY** — Compute-memory disaggregation for LLM serving with advisory prefetching (2.4× latency reduction over vLLM, 4× more requests). Priority-based KV cache management exploits neural network structure for allocation decisions. **Limitation**: Advisory request accuracy depends on workload predictability (strong for chatbots, weaker for adversarial/random queries). Remote memory access latency is bounded by RDMA round-trip time.

**BURST** — Software RDMA with near-hardware performance and cross-implementation interoperability. **Limitation**: Performance gap with hardware RDMA widens under heavy load; best for interoperability-critical deployments.

**OneSidedMW** — RNIC-offloaded disaggregated memory management with security guarantees. **Limitation**: RNIC-side computation capacity limits management sophistication; best for simple memory management operations.

**PD3** — DPU-based intelligent prefetching for disaggregated memory, hiding remote access latency. **Limitation**: Prefetch accuracy and benefit depend on access pattern predictability; prefetch misses waste DPU bandwidth.

**HPCC** — INT-based high-precision congestion control achieving near-zero queue buildup. **Limitation**: Requires INT-capable switches; deployment limited to INT-enabled infrastructure.

**TIMELY / Swift** — RTT-based and delay-based congestion control for RDMA networks, respectively. TIMELY uses NIC hardware timestamps; Swift uses simple delay target. **Limitation**: Accuracy depends on precise RTT measurement (TIMELY) or stable base RTT (Swift). Both can underperform HPCC in heavily oversubscribed networks.

### 实用建议 / Practical Guidance

- **LLM serving scaling**: SYMPHONY when KV cache memory is the primary bottleneck (common for multi-turn conversational AI)
- **RDMA interoperability**: BURST for multi-vendor RDMA environments where hardware RDMA APIs differ
- **Congestion control**: HPCC for INT-capable RDMA networks (highest precision); TIMELY or Swift for simpler deployment (no switch changes needed)
- **Hardware acceleration**: PD3 for DPU-equipped clusters; OneSidedMW for RNIC-equipped clusters where CPU offloading is the goal
- **Combined approach**: SYMPHONY (disaggregation) + HPCC (congestion control) + OneSidedMW (offloading) for a comprehensive disaggregated memory architecture

## 写作指导 / Writing Guide
- **核心数字**: remote access latency (µs), throughput (GB/s), LLM serving end-to-end metrics
- **Evaluation必须**: (1) micro-benchmark (latency/bandwidth vs message size) (2) end-to-end LLM serving (TTFT/TPOT) (3) 拥塞控制: FCT分布 (4) scalability with node count
- **审稿要点**: "远程内存的网络延迟是否成为新的瓶颈"

## 实现指导 / Implementation Guide
- **RDMA**: libibverbs + RDMA CM, one-sided READ/WRITE + two-sided SEND/RECV
- **RNIC/DPU offloading**: 固件级offloading或DPU program (BlueField DOCA)
- **拥塞控制**: kernel module or NIC firmware (HPCC INT-based, TIMELY RTT-based)
- **内存管理**: remote memory allocator + page fault handler

## 实验流程 / Experiment Pipeline
```
1. RDMA micro-benchmark: ib_write_lat/ib_read_bw
2. 拥塞控制: NS-3仿真 → RoCE testbed验证
3. 内存分离: 远程KV cache vs 本地, 测TTFT/TPOT/吞吐
4. Prefetch (PD3): hit rate vs access pattern, 测隐藏延迟
5. Scaling: 1→4→8→16 memory nodes, 测linear scalability
```

## 注意事项 / Notes

- Memory disaggregation is critical for GPU cluster efficiency, particularly for LLM serving where KV cache dominates memory usage.
- RDMA congestion control (HPCC, TIMELY, Swift) is foundational for reliable high-performance disaggregated memory access.
- Hardware offloading (OneSidedMW with RNIC, PD3 with DPU) is a key trend: pushing memory management closer to the network.
- 查看 `references/paper-catalog.md` 获取完整论文目录，包括作者和详细标签。
