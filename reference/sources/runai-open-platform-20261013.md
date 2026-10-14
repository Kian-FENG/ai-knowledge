---
id: source-runai-open-platform-20261013
title: NVIDIA开源Run:ai完整平台，GPU调度与组织配额可分模块采用
type: source
domain:
- infra
- companies
lifecycle: published
tags:
- daily-research
created: '2026-10-13'
updated: '2026-10-13'
summary: NVIDIA 10月13日14:19:40 UTC技术文章称完整Run:ai平台源码公开，包含KAI Scheduler、GPU Fractioning
  Operator、KAI Resource Management和Workload Map，可整体或分模块采用。相对较早只开源调度器，本期增量是完整平台。
evidence_kind: reported
verification: source-checked
sources:
- https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/
related: []
aliases: []
last_verified: '2026-10-13'
verification_note: Agent已阅读标注范围并核对有限陈述支持关系；不表示独立测量、融资审计或部署复现。 官方正文How to adopt、四组件与Community
  Product条款；未执行代码、未独立复核所有仓库许可。
source: raw/2026-10-14/0a319b0b47198f1f35f34ff21d99061bdb507a7d5b9144f40c4af2721e02377c.body
url: https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/
published_at: '2026-10-13T14:19:40+00:00'
source_category: official
raw_path: raw/2026-10-14/0a319b0b47198f1f35f34ff21d99061bdb507a7d5b9144f40c4af2721e02377c.body
sha256: 0a319b0b47198f1f35f34ff21d99061bdb507a7d5b9144f40c4af2721e02377c
fetched_at: '2026-10-14T01:09:10.831948+00:00'
reading_scope: 官方正文How to adopt、四组件与Community Product条款；未执行代码、未独立复核所有仓库许可。
date_precision: timestamp
date_basis: published
evidence:
- source: raw/2026-10-14/0a319b0b47198f1f35f34ff21d99061bdb507a7d5b9144f40c4af2721e02377c.body
  locator: 官方正文How to adopt、四组件与Community Product条款；未执行代码、未独立复核所有仓库许可。
  version: sha256:0a319b0b47198f1f35f34ff21d99061bdb507a7d5b9144f40c4af2721e02377c
reviewed_by: Codex
reviewed_at: '2026-10-14'
reviewed_content_sha256: eed49fc9b41bda1197193bd195efbee28a8b0df6128ba5dcb20965a7a5444369
---

# NVIDIA开源Run:ai完整平台，GPU调度与组织配额可分模块采用

## Key Takeaways

NVIDIA 10月13日14:19:40 UTC技术文章称完整Run:ai平台源码公开，包含KAI Scheduler、GPU Fractioning Operator、KAI Resource Management和Workload Map，可整体或分模块采用。相对较早只开源调度器，本期增量是完整平台。

GPU Fractioning对接CUDA13.4原生显存配额；Workload Map描述工作负载结构，本身不调度、不排队或跨集群传播。文章列8家生态伙伴，不据此推导全部生产部署。

源码适用各自许可证；NGC Community Product仍需相应软件条款，不要求付费订阅但不含企业支持。未逐仓审核许可证、安装或测算利用率，因此不把开源直接等同免费运营。

## Detailed Notes

阅读范围：官方正文How to adopt、四组件与Community Product条款；未执行代码、未独立复核所有仓库许可。

## Evidence

[原始来源](https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/)。不可覆盖原始档案、采集时间和hash见元数据。浏览笔记明确为非逐字提取；日期未知不补采集日，日期占位不视为实际时刻。

## Questions Raised

判断（derived）：可组合调度、配额和GPU共享可能降低平台开发门槛，云服务商及集成商受益，也使支持和托管成为差异化。驱动版本、隔离要求与运维复杂度会限制节省；观察兼容性、真实利用率、故障恢复和支持成本。
