---
id: source-sglang-unified-memory-20261022
title: SGLang详解混合模型统一缓存，淘汰收益依赖大块分配条件
type: source
domain:
- infra
- models
lifecycle: published
tags: []
created: '2026-10-24'
updated: '2026-10-23'
summary: SGLang于10月22日技术文章解释GPU上统一缓存池：全注意力KV和循环状态共享容量，后续扩展到滑窗KV；这不等同CPU迁移或CUDA统一虚拟内存，CPU/外存缓存由HiCache处理。本期是设计与实验披露，不当作当天新正式release。
evidence_kind: reported
verification: source-checked
sources:
- https://www.sglang.io/blog/unified-memory
related: []
aliases: []
source: raw/2026-10-24/1dabf10160eafa192c0345680362a339c9a21ee7c916862a6959d91c51fb6698.body
url: https://www.sglang.io/blog/unified-memory
published_at: '2026-10-22T00:00:00+08:00'
source_category: official
last_verified: '2026-10-23'
verification_note: Agent阅读所列来源并核对有限结论；reported保留披露主体归因，derived是研究推导，未独立复现。
reading_scope: 官方可视化文章全部可提取主文、教学示例和Results已读；标题日期由官网博客列表确认，未审PR代码/合并时刻和完整benchmark脚本，未复现。
raw_path: raw/2026-10-24/1dabf10160eafa192c0345680362a339c9a21ee7c916862a6959d91c51fb6698.body
sha256: 1dabf10160eafa192c0345680362a339c9a21ee7c916862a6959d91c51fb6698
fetched_at: '2026-10-23T22:08:48.243045+00:00'
evidence:
- source: raw/2026-10-24/1dabf10160eafa192c0345680362a339c9a21ee7c916862a6959d91c51fb6698.body
  locator: 官方可视化文章全部可提取主文、教学示例和Results已读；标题日期由官网博客列表确认，未审PR代码/合并时刻和完整benchmark脚本，未复现。
  version: sha256:1dabf10160eafa192c0345680362a339c9a21ee7c916862a6959d91c51fb6698
date_precision: date-only
reviewed_by: Codex
reviewed_at: '2026-10-24'
reviewed_content_sha256: d6a1d1d06f70971097ddd23e167c09b603884cb60402ef519a0e990f35660c1e
---

# SGLang详解混合模型统一缓存，淘汰收益依赖大块分配条件

## Key Takeaways

SGLang于10月22日技术文章解释GPU上统一缓存池：全注意力KV和循环状态共享容量，后续扩展到滑窗KV；这不等同CPU迁移或CUDA统一虚拟内存，CPU/外存缓存由HiCache处理。本期是设计与实验披露，不当作当天新正式release。

## Detailed Notes

标题收益比较的两组都已使用Unified Memory，仅改变按可回收共享容量停止淘汰的规则。测试为Qwen3.5-4B、RTX5090 32GB、Triton，28个约390-token前缀、7000-token压力请求、28次重访，6次运行中位数：保留10→19个前缀，重访总时间4.105→2.548秒。

压力请求分成4个2048-token块时，两种策略都保留17个前缀；整体吞吐无稳定变化。精度、完整软件revision、并行、输出长度/调度并发未完整核实；只作此实验的报告值，不推导普遍吞吐提升。支持后端与K/V head大小仍有限制。

## Evidence

[原始来源](https://www.sglang.io/blog/unified-memory)；原始版本 `raw/2026-10-24/1dabf10160eafa192c0345680362a339c9a21ee7c916862a6959d91c51fb6698.body`，SHA-256 `1dabf10160eafa192c0345680362a339c9a21ee7c916862a6959d91c51fb6698`。

官方可视化文章全部可提取主文、教学示例和Results已读；标题日期由官网博客列表确认，未审PR代码/合并时刻和完整benchmark脚本，未复现。

## Questions Raised

判断：混合架构部署的成本可由缓存容量与分配策略决定，重复前缀负载和显存受限环境可能受益。反例是分块预填充抹平差异或搬移开销主导。观察真实请求分布、分配粒度、命中、P99、碎片与固定质量下显存成本。
