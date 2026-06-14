# Edge ML & In-Network Inference / 边缘ML与网络内推理

Systems research on deploying ML inference at the network edge, including in-network computation on programmable switches, edge video analytics, and vision language model deployment on resource-constrained devices.

For full paper details, see `references/paper-catalog.md`.

## 论文列表 / Paper List

1. **SPLIDT: Partitioned Decision Trees for Scalable Stateful Inference at Line Rate** [NSDI 2026]
   Implements stateful decision tree inference at line rate on programmable switches by partitioning trees across pipeline stages. / 通过跨流水线阶段分区决策树，在可编程交换机上实现线速状态推理。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/parvez) | [PDF](https://www.usenix.org/system/files/nsdi26-parvez.pdf)

2. **FENIX: Enabling In-Network DNN Inference with FPGA-Enhanced Programmable Switches** [NSDI 2026]
   Combines FPGA acceleration with programmable switches to enable DNN inference directly in the network data plane, reducing end-to-end latency. / 结合FPGA加速与可编程交换机，在网络数据面直接进行DNN推理，降低端到端延迟。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/gao) | [PDF](https://www.usenix.org/system/files/nsdi26-gao.pdf)

3. **Morphe: High-Fidelity Generative Video Streaming with Vision Foundation Model** [NSDI 2026]
   Uses vision foundation models at the edge for high-fidelity generative video streaming, reducing bandwidth while maintaining perceptual quality. / 在边缘使用视觉基础模型进行高保真生成式视频流传输，在保持感知质量的同时降低带宽。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/gong) | [PDF](https://www.usenix.org/system/files/nsdi26-gong.pdf)

4. **AVA: Towards Agentic Video Analytics with Vision Language Models** [NSDI 2026]
   Agentic framework for video analytics powered by vision language models, enabling interactive querying and analysis of video streams at the edge. / 视觉语言模型驱动的智能视频分析框架，支持在边缘交互式查询和分析视频流。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/yan) | [PDF](https://www.usenix.org/system/files/nsdi26-yan.pdf)

5. **Remembrall: Leaning into Memory for Accurate Video Analytics on System-on-Chip GPUs** [NSDI 2026]
   Leverages temporal memory across frames for accurate video analytics on SoC GPUs (e.g., Jetson), trading memory for accuracy within tight power budgets. / 利用帧间时序记忆在SoC GPU上进行精确视频分析，在有限功耗预算内以内存换精度。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/ramanujam) | [PDF](https://www.usenix.org/system/files/nsdi26-ramanujam.pdf)

## 实验指导 / Experiment Guide

### 典型实验配置 / Typical Setup
- **In-network ML**: Intel Tofino/Tofino2 可编程交换机, FPGA加速卡, P4编程
- **Edge Video**: Jetson Orin/AGX, Raspberry Pi + NPU, SoC GPU
- **Video datasets**: MOT16, VisDrone, COCO, 实时摄像头流
- **Power约束**: 15-30W for Jetson, <5W for microcontroller

### 常用指标 / Common Metrics
| Metric | 用途 | Papers |
|--------|------|--------|
| **Inference Throughput (fps)** | 推理帧率 | AVA, Remembrall, FENIX |
| **End-to-End Latency** | 端到端延迟 | SPLIDT (line rate), FENIX |
| **Accuracy (mAP, IoU)** | 检测/分析精度 | Remembrall, AVA |
| **Bandwidth Savings** | 带宽节省 | Morphe (generative streaming) |
| **Power Consumption (W)** | 功耗 | Remembrall (SoC GPU约束) |
| **Memory Footprint** | 内存占用 | Remembrall |

### 实验常见坑 / Common Pitfalls
- **硬件限制**: 可编程交换机资源 (stage count, ALU) 严格限制模型大小。SPLIDT/FENIX论文重点讨论如何在有限stage内完成推理。
- **Accuracy vs Latency tradeoff**: 边缘设备上提高推理精度通常意味着更高延迟。Remembrall用时间记忆换精度是代表性方案。
- **Dynamic conditions**: 真实场景光照/天气/遮挡变化大，仅用静态数据集测试不充分。
- **Generative streaming quality**: Morphe的生成式视频流需要同时评估PSNR/SSIM (像素精度)和LPIPS (感知质量)，单一指标不够。

## 评估与洞察 / Evaluation & Insights

### 类别级评价 / Category-Level Assessment

Edge ML research is shifting from running small models at the edge to bringing sophisticated capabilities (vision language models, generative streaming, in-network inference) to resource-constrained environments. Key trends:

- **In-network inference**: SPLIDT and FENIX push model execution into the network data plane—a fundamentally different deployment paradigm with line-rate constraints and programmable switch limitations
- **Foundation models at the edge**: Morphe and AVA demonstrate that vision foundation models and VLMs can operate at the edge, but require careful system design to overcome compute and bandwidth constraints
- **Hardware-software co-design**: Remembrall's SoC GPU memory management and FENIX's FPGA-switch co-design show that edge ML optimization requires deep hardware integration

### 论文亮点与局限 / Paper Highlights & Limitations

**SPLIDT** — Partitioned decision trees for line-rate stateful inference on programmable switches (Tofino). Enables in-network decision-making without server round-trips. **Limitation**: Decision tree models only; no support for DNNs. Switch pipeline stage resources are severely limited (typically 12-16 stages).

**FENIX** — FPGA-enhanced programmable switches enabling DNN inference in the network data plane, reducing end-to-end latency by avoiding server round-trips. **Limitation**: FPGA integration adds hardware cost and limits deployment to FPGA-equipped switches. Model size constrained by FPGA resources.

**AVA** — Agentic video analytics with VLMs, enabling interactive video queries at the edge. **Limitation**: VLM inference latency and cost remain high for real-time video; best for analytic workloads where interactive query time is acceptable.

**Morphe** — Vision foundation model-based high-fidelity generative video streaming, reducing bandwidth while maintaining perceptual quality. **Limitation**: Foundation model inference at the edge is compute-intensive; benefits require sufficient edge GPU capacity.

**Remembrall** — Temporal memory across frames for accurate SoC GPU-based video analytics (Jetson-class devices). **Limitation**: Memory-for-accuracy trade-off works within SoC GPU memory constraints; benefit plateaus when memory is saturated.

### 实用建议 / Practical Guidance

- **In-network processing**: SPLIDT for simple decision-making at line rate (anomaly detection, basic classification); FENIX when DNN accuracy is needed with <1ms latency budgets
- **Edge video analytics**: Remembrall for Jetson-based deployments with accuracy-critical requirements; AVA for interactive natural-language video querying
- **Bandwidth-sensitive streaming**: Morphe when bandwidth is the bottleneck (remote edge deployments, satellite links) and edge GPU capacity is available
- **Hardware requirements**: SPLIDT requires Tofino switches; FENIX requires FPGA-enhanced switches; Remembrall targets Jetson SoC GPUs

## 写作指导 / Writing Guide
- **核心数字**: latency (ms/frame), throughput (fps), accuracy (mAP) + power (W)
- **Evaluation必须**: (1) 多数据集 (2) 真实光照/天气/遮挡场景 (3) accuracy-latency-power tradeoff
- **审稿要点**: "在资源极度受限的设备上，你的overhead是多少"

## 实现指导 / Implementation Guide
- **交换机推理**: P4编程 (Tofino) + FPGA (FENIX), 模型需压缩到pipeline stage内
- **边缘推理**: Jetson + TensorRT, memory-for-accuracy tradeoff (Remembrall)
- **视频分析**: OpenCV + PyTorch, 帧间temporal memory

## 实验流程 / Experiment Pipeline
```
1. In-network: Tofino testbed, P4 program, line-rate测试
2. Edge: Jetson Orin/AGX, 多视频stream, power meter
3. 数据集: MOT16/VisDrone/COCO + 真实摄像头
4. 指标: fps, latency (ms), mAP, power (W), bandwidth (Mbps)
5. 动态场景: 光照变化/遮挡/多目标
```

## 注意事项 / Notes

- In-network ML (SPLIDT, FENIX) requires programmable switch hardware (Intel Tofino, FPGA-enhanced switches).
- Edge video analytics (AVA, Remembrall, Morphe) target resource-constrained deployments with strict power/latency budgets.
- Vision language models (AVA) and foundation models (Morphe) are increasingly deployed at the edge.
- 查看 `references/paper-catalog.md` 获取完整论文目录，包括作者和详细标签。
