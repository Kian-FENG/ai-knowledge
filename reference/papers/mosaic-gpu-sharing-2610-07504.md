---
id: paper-mosaic-gpu-sharing-2610-07504
title: Mosaic 提议用内核干扰预测选择GPU共置或SM分区
type: paper
domain:
- infra
lifecycle: published
tags:
- daily-research
created: '2026-10-08'
updated: '2026-10-08'
summary: Mosaic摘要提出内核级干扰预测，结合线程块放置、内存层级、SM内部干扰的解析与轻量学习模型；MosaicSched做在线准入，在全GPU共置与SM分区间选择，以满足尾时延SLO。是论文方案，未核实社区合并、正式发布或生产采用。
evidence_kind: reported
verification: source-checked
sources:
- https://arxiv.org/abs/2610.07504
related: []
aliases: []
source: raw/2026-10-08/8eed4f3c238ca262a0469571f4513c24c3e323cb87401a87998a57c3e8d43a53.txt
url: https://arxiv.org/abs/2610.07504
published_at: '2026-10-05T23:09:45+00:00'
source_category: paper
raw_path: raw/2026-10-08/8eed4f3c238ca262a0469571f4513c24c3e323cb87401a87998a57c3e8d43a53.txt
sha256: 8eed4f3c238ca262a0469571f4513c24c3e323cb87401a87998a57c3e8d43a53
fetched_at: '2026-10-08T01:13:12.018430+00:00'
last_verified: '2026-10-08'
verification_note: 已阅读并核对所列有限陈述与原始来源的支持关系；arXiv2610.07504v1摘要、Submission history；cs.DC
  Oct7公告与RSS。仅读摘要，不称全文审阅或独立复现。；未独立复现。
reading_scope: arXiv2610.07504v1摘要、Submission history；cs.DC Oct7公告与RSS。仅读摘要，不称全文审阅或独立复现。
evidence:
- source: raw/2026-10-08/8eed4f3c238ca262a0469571f4513c24c3e323cb87401a87998a57c3e8d43a53.txt
  locator: arXiv2610.07504v1摘要、Submission history；cs.DC Oct7公告与RSS。仅读摘要，不称全文审阅或独立复现。
  version: sha256:8eed4f3c238ca262a0469571f4513c24c3e323cb87401a87998a57c3e8d43a53
- source: raw/2026-10-08/9ffd30ff2f6e6ab740894389b16cbcfcf2465d3cda6c147112b5a0339a66e10f.body
  locator: 官方RSS Oct7公告候选 8fa89a6af5613f0e9c9a
  version: sha256:9ffd30ff2f6e6ab740894389b16cbcfcf2465d3cda6c147112b5a0339a66e10f
announced_at: '2026-10-07'
date_precision: date-only
version: arxiv:2610.07504v1
reviewed_by: Codex
reviewed_at: '2026-10-08'
reviewed_content_sha256: 2cf84bc062a49c20a04610df9e8df9b437ebc65cf090b0b995a1f7e2ae3a99c4
---

# Mosaic 提议用内核干扰预测选择GPU共置或SM分区

## Problem and Method

Mosaic摘要提出内核级干扰预测，结合线程块放置、内存层级、SM内部干扰的解析与轻量学习模型；MosaicSched做在线准入，在全GPU共置与SM分区间选择，以满足尾时延SLO。是论文方案，未核实社区合并、正式发布或生产采用。

## Results and Conditions

v1提交于2026-10-05T23:09:45Z，10月7日cs.DC公告。本次仅读摘要和提交历史；四种GPU架构的具体硬件、精度、并发/长度、基线及软件版本未读，不引用倍数或视为任意负载的时延保证。公告日仅到日，边界不确定。

## Evidence

[原始来源](https://arxiv.org/abs/2610.07504)。定位与阅读范围：arXiv2610.07504v1摘要、Submission history；cs.DC Oct7公告与RSS。仅读摘要，不称全文审阅或独立复现。 原始路径、hash、采集/事件时间见元数据；source-checked只表示所列陈述支持关系已核对，非独立结果验证。

## Limitations and Implications

判断（derived）：能预测干扰时，共享调度可在利用率和服务尾时延间更精细取舍，推理云与调度框架可能受益。负载迁移、预测误差或准入开销可能破坏SLO；观察校准成本、p99违约率与不同GPU/任务分布的泛化。

arXiv2610.07504v1摘要、Submission history；cs.DC Oct7公告与RSS。仅读摘要，不称全文审阅或独立复现。
