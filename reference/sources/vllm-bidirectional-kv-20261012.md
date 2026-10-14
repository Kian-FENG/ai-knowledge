---
id: source-vllm-bidirectional-kv-20261012
title: vLLM双向KV传输：跨轮复用取决于留存、路由和网络成本
type: source
domain:
- infra
lifecycle: published
tags:
- daily-research
created: '2026-10-13'
updated: '2026-10-13'
summary: 官网日期仅2026-10-12；按项目既有Asia/Singapore来源解析，本期不纳入，不能用10月13日发现时间代替发布日期。
evidence_kind: reported
verification: source-checked
sources:
- https://vllm.ai/blog/2026-10-12-bidirectional-kvxfer-multiturn-agentic-workload
related: []
aliases: []
last_verified: '2026-10-13'
verification_note: Agent已阅读标注范围并核对有限陈述支持关系；不表示独立测量、融资审计或部署复现。 主文架构/路由/TTL、Performance、复现附录软硬件与patch；图表像素/全部脚本未审核。
source: raw/2026-10-14/9eedade2f5feeab1961f882f03504bef9d0af298d68edec2e4f3e84ca96866d5.body
url: https://vllm.ai/blog/2026-10-12-bidirectional-kvxfer-multiturn-agentic-workload
published_at: '2026-10-12T00:00:00+08:00'
source_category: official
raw_path: raw/2026-10-14/9eedade2f5feeab1961f882f03504bef9d0af298d68edec2e4f3e84ca96866d5.body
sha256: 9eedade2f5feeab1961f882f03504bef9d0af298d68edec2e4f3e84ca96866d5
fetched_at: '2026-10-14T01:09:11.137677+00:00'
reading_scope: 主文架构/路由/TTL、Performance、复现附录软硬件与patch；图表像素/全部脚本未审核。
date_precision: date-only
date_basis: published
evidence:
- source: raw/2026-10-14/9eedade2f5feeab1961f882f03504bef9d0af298d68edec2e4f3e84ca96866d5.body
  locator: 主文架构/路由/TTL、Performance、复现附录软硬件与patch；图表像素/全部脚本未审核。
  version: sha256:9eedade2f5feeab1961f882f03504bef9d0af298d68edec2e4f3e84ca96866d5
reviewed_by: Codex
reviewed_at: '2026-10-14'
reviewed_content_sha256: 3c17d1f077a6ada08e2fb8c948c00311d70ade14fbf88d68c1a553bb05466d1c
---

# vLLM双向KV传输：跨轮复用取决于留存、路由和网络成本

## Key Takeaways

官网日期仅2026-10-12；按项目既有Asia/Singapore来源解析，本期不纳入，不能用10月13日发现时间代替发布日期。

NIXL允许decode保留的KV回读到prefill，路由只传元数据，TTL和重算阈值决定是否复用。适用P/D分离、多轮会话且KV尚未过期；prefill本地缓存命中时收益不同。

文章实验为1P1D、两台p5en.48xlarge各8H200、EFA同AZ；vLLM0.29.0+PR40186、NIXL1.4.1、CUDA13、TP8示例，Qwen3-32B BF16与GLM-5-FP8，prefill关闭前缀缓存模拟丢失；prompt2k至24k/20k，max_num_seqs8不是已确认实际并发，输出长度/完整流量分布未确认。

1.6/3.3倍TTFT改善是该设置自报，未复现，不推导一般成本和当前稳定版全部支持；正文说v0.21+可用，具体复现实验仍有补丁依赖。

## Detailed Notes

阅读范围：主文架构/路由/TTL、Performance、复现附录软硬件与patch；图表像素/全部脚本未审核。

## Evidence

[原始来源](https://vllm.ai/blog/2026-10-12-bidirectional-kvxfer-multiturn-agentic-workload)。不可覆盖原始档案、采集时间和hash见元数据。浏览笔记明确为非逐字提取；日期未知不补采集日，日期占位不视为实际时刻。

## Questions Raised

判断（derived）：避免跨轮重算能改善长会话，但网络、显存保留与负载均衡有代价；观察KV留存率、尾延迟和端到端账单。
