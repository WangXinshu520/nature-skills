# Vector Search & RAG Infrastructure / 向量搜索与RAG基础设施

Systems research on vector search engines, approximate nearest neighbor (ANN) algorithms, and retrieval-augmented generation (RAG) infrastructure. Covers indexing, storage, disaggregated architectures, and encrypted search.

For full paper details, see `references/paper-catalog.md`.

## 论文列表 / Paper List

1. **DistVS: Large-scale Vector Search with Compute-Memory Disaggregation** [NSDI 2026]
   Disaggregates compute and memory for large-scale vector search, enabling independent scaling of indexing and query serving components. / 计算与内存分离的大规模向量搜索，独立扩展索引和查询服务组件。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/yin) | [PDF](https://www.usenix.org/system/files/nsdi26-yin.pdf)

2. **Quake: Adaptive Indexing for Vector Search** [OSDI 2025]
   Adaptive indexing system for vector search that dynamically adjusts index structure based on query patterns and data distribution, achieving faster queries at lower memory cost. / 自适应索引系统，根据查询模式和数据分布动态调整索引结构，以更少内存实现更快查询。
   [Presentation](https://www.usenix.org/conference/osdi25/presentation/mohoney) | [PDF](https://www.usenix.org/system/files/osdi25-mohoney.pdf)

3. **Achieving Low-Latency Graph-Based Vector Search via Aligning Best-First Search Algorithm with SSD** [OSDI 2025]
   Aligns the best-first graph search algorithm with SSD access patterns to achieve low-latency vector search on disk-resident indices, bridging the memory-disk performance gap. / 将图搜索算法与SSD访问模式对齐，实现基于磁盘索引的低延迟向量搜索。
   [Presentation](https://www.usenix.org/conference/osdi25/presentation/guo) | [PDF](https://www.usenix.org/system/files/osdi25-guo.pdf)

4. **Compass: Encrypted Semantic Search with High Accuracy** [OSDI 2025]
   Encrypted semantic search system that achieves high accuracy while preserving data privacy, enabling secure vector search on sensitive datasets. / 加密语义搜索系统，在保护数据隐私的同时实现高精度向量搜索。
   [Presentation](https://www.usenix.org/conference/osdi25/presentation/zhu-jinhao) | [PDF](https://www.usenix.org/system/files/osdi25-zhu-jinhao.pdf)

## 实验指导 / Experiment Guide

### 典型实验配置 / Typical Setup
- **Datasets**: SIFT1M/SIFT1B, DEEP1B, GIST1M (标准ANN benchmark) + 真实RAG数据集 (如MS MARCO, Natural Questions)
- **Index types**: HNSW (graph-based), IVF (inverted file), PQ (product quantization)
- **Hardware**: CPU servers + SSD (磁盘索引实验) / GPU + RDMA (分离架构实验)
- **Query patterns**: 均匀随机 vs 真实查询 (真实查询有热点，和均匀分布性能差异大)

### 常用指标 / Common Metrics
| Metric | 用途 | Papers |
|--------|------|--------|
| **QPS** (Queries Per Second) | 查询吞吐 | DistVS, Quake |
| **Recall@K** (typically K=1/10/100) | 搜索精度 | All papers |
| **P50/P99 Latency** | 查询延迟分布 | Achieving Low-Latency (SSD) |
| **Index Build Time** | 索引构建开销 | Quake |
| **Memory/Storage Footprint** | 存储成本 | DistVS, Quake |

### 实验常见坑 / Common Pitfalls
- **Recall vs speed tradeoff**: 高recall和低延迟不可兼得，实验需在多个操作点测试
- **索引build时间计入total cost**: 只报告查询性能忽略索引构建时间是不公平的。Quake论文强调此点。
- **SSD vs DRAM**: SSD方案报告延迟时必须区分冷/热数据访问模式
- **隐私维度**: Compass为代表的加密搜索论文需额外评估加密开销和精度损失

## 评估与洞察 / Evaluation & Insights

### 类别级评价 / Category-Level Assessment

Vector search is a critical RAG infrastructure component with unique systems challenges: high storage demand (datasets + index), fine-grained I/O patterns, and the tension between accuracy, latency, and cost. Key trends:

- **Disaggregation for vector search**: DistVS applies the compute-memory disaggregation pattern to vector search, recognizing that index storage and compute have different scaling requirements
- **Adaptive over static indexing**: Quake's adaptive indexing represents a shift from one-size-fits-all indexes to workload-aware structures that evolve with query patterns
- **Storage-medium alignment**: The SSD-aligned search and DistVS multi-tier layout show that vector search optimization is increasingly about storage hierarchy alignment, not just algorithm design

### 论文亮点与局限 / Paper Highlights & Limitations

**DistVS** — Three-tier storage layout (low-precision vectors on compute server → high-precision on memory server → full-precision on SSD). Progressive pruning via PRESS algorithm aligns access patterns with storage hierarchy. **Limitation**: Multi-tier architecture adds deployment complexity; benefit depends on dataset size and vector dimensionality. Network latency between tiers can become a bottleneck.

**Quake** — Adaptive indexing that dynamically adjusts index structure based on query patterns and data distribution, reducing memory cost while maintaining query speed. **Limitation**: Adaptation period required before benefits materialize; best for stable or slowly-evolving workloads.

**SSD-Aligned Vector Search** — Aligns best-first graph search algorithms with SSD access patterns to achieve low-latency search on disk-resident indices. **Limitation**: SSD throughput limits the high end of performance; best for cost-sensitive deployments where memory is the constraint, not latency.

**Compass** — Encrypted semantic search preserving data privacy while maintaining high accuracy. **Limitation**: Encryption overhead limits throughput; best for privacy-sensitive domains (healthcare, finance) where raw vector access is unacceptable.

### 实用建议 / Practical Guidance

- **Large-scale RAG**: DistVS for vector search deployments where index size exceeds single-machine memory
- **Cost-sensitive search**: Quake for minimizing memory per query; SSD-aligned approach for disk-based indexing
- **Privacy-first RAG**: Compass when vectors contain sensitive information requiring encryption at rest and in transit
- **Performance benchmarking**: DistVS and Quake address different dimensions (scale vs. efficiency)—consider both for production planning

## 写作指导 / Writing Guide
- **核心数字**: QPS提升 + Recall@10保持 + Mem/Storage降低%
- **Evaluation必须**: (1) 多种数据集(SIFT/GIST/DEEP) (2) Recall-vs-QPS tradeoff curve (3) Index build time (4) Scalability with dataset size
- **审稿要点**: "你的系统在真实数据分布(有热点)下还能保持性能吗"

## 实现指导 / Implementation Guide
- **Index**: 改HNSW/IVF/PQ的C++实现, 内存布局优化
- **Search engine**: 修改query pipeline, 渐进式剪枝 (DistVS)
- **SSD优化**: Direct I/O + 4K对齐 + readahead
- **数据集**: SIFT1B (1B vectors, 128d), DEEP1B (1B, 96d)

## 实验流程 / Experiment Pipeline
```
1. 数据集: SIFT1M/SIFT1B, DEEP1B, GIST1M (+ 真实dataset)
2. index build → 测量build time + index size
3. query → Recall@1/10/100 vs QPS tradeoff
4. scalability → 1M→10M→100M→1B vectors
5. 隐私场景(Compass) → encryption overhead + accuracy loss
```

## 注意事项 / Notes

- Vector search is a core component of RAG pipelines; each paper addresses a different RAG scaling challenge.
- Quake and DistVS focus on scaling (index quality, resource disaggregation), while the SSD paper tackles cost-efficiency.
- Compass is relevant if you have privacy constraints on your vector search data.
- 查看 `references/paper-catalog.md` 获取完整论文目录，包括作者和详细标签。
