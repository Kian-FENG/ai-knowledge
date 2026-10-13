---
id: paper-kv-repurpose-20261012
title: KV-Repurpose论文公告：非前缀缓存复用需要质量约束
type: paper
domain:
- infra
- models
lifecycle: published
tags:
- daily-research
created: '2026-10-12'
updated: '2026-10-12'
summary: arXiv本期RSS以10月12日公告KV-Repurpose v1；提交历史为10月9日06:17:10 UTC。公告只有日期、具体时刻不明，不把较早提交写成今天首发；前期未收录。
evidence_kind: reported
verification: source-checked
sources:
- https://arxiv.org/abs/2610.13060
related: []
aliases: []
source: raw/2026-10-13/4bf96e1ebd1be5fd0e3b3bbbb1ddca9530a9fafbc3bbe8656b038bca1f9d301d.body
url: https://arxiv.org/abs/2610.13060v1
published_at: '2026-10-09T06:17:10+00:00'
source_category: paper
raw_path: raw/2026-10-13/4bf96e1ebd1be5fd0e3b3bbbb1ddca9530a9fafbc3bbe8656b038bca1f9d301d.body
sha256: 4bf96e1ebd1be5fd0e3b3bbbb1ddca9530a9fafbc3bbe8656b038bca1f9d301d
fetched_at: '2026-10-13T01:18:24.416140+00:00'
last_verified: '2026-10-12'
verification_note: 已阅读所标范围并核对有限陈述支持关系；source-checked不表示融资审计、模型独立评测或部署复现。arXiv2610.13060v1
  Abstract与Submission history；公告日另见本期RSS原始归档。仅摘要阅读。
reading_scope: arXiv2610.13060v1 Abstract与Submission history；公告日另见本期RSS原始归档。仅摘要阅读。
evidence:
- source: raw/2026-10-13/4bf96e1ebd1be5fd0e3b3bbbb1ddca9530a9fafbc3bbe8656b038bca1f9d301d.body
  locator: arXiv2610.13060v1 Abstract与Submission history；公告日另见本期RSS原始归档。仅摘要阅读。
  version: sha256:4bf96e1ebd1be5fd0e3b3bbbb1ddca9530a9fafbc3bbe8656b038bca1f9d301d
- source: raw/2026-10-13/18048760837ac7c65976259c86c3c659d3f4045f328358d8d08437001aab5981.body
  locator: RSS item https://arxiv.org/abs/2610.13060；Announce Type new、pubDate日期（00:00不能当精确公告时刻）公告日2026-10-12，无准确小时。
  version: sha256:18048760837ac7c65976259c86c3c659d3f4045f328358d8d08437001aab5981
date_precision: date-only
date_basis: announced
announced_at: '2026-10-12T00:00:00-04:00'
paper_version: v1
reviewed_by: Codex
reviewed_at: '2026-10-13'
reviewed_content_sha256: c95db921a1b2cdf17b5742aa3bee0f0a97e103472617cede11f024d87a150961
---

# KV-Repurpose论文公告：非前缀缓存复用需要质量约束

## Problem and Method

arXiv本期RSS以10月12日公告KV-Repurpose v1；提交历史为10月9日06:17:10 UTC。公告只有日期、具体时刻不明，不把较早提交写成今天首发；前期未收录。

摘要提出vLLM基础的分段KV复用测试床，包含缓存感知调度、prompt组织、容量与工作负载监控。作者报告朴素复用在单文档问答/摘要中较能保持质量，但跨文档推理有明显限制。

仅读摘要、版本与提交历史，未读论文全文/代码、硬件和精确软件配置；因此不采纳缓存命中率/TTFT为普遍性能结论，开源许可也未从仓库独立核验。

## Results and Conditions

arXiv2610.13060v1 Abstract与Submission history；公告日另见本期RSS原始归档。仅摘要阅读。

## Evidence

[原始来源](https://arxiv.org/abs/2610.13060)。原始路径、hash、采集时间及版本见元数据；有限摘录/摘要范围与缺失条件不被自动发布改变。

## Limitations and Implications

判断（derived）：在检索文档重复而prompt前缀不同的场景，复用可能降低预填充，RAG平台受益。跨文档依赖改变会使缓存失真；观察质量分层、容量和命中率、TTFT分布及隔离策略，而非只看缓存命中。
