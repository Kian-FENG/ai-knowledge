---
id: source-gemini-argon-access-20261013
title: Gemini 4 Argon向付费产品与API开放，百万token由输入输出共用
type: source
domain:
- models
- products
lifecycle: published
tags:
- daily-research
created: '2026-10-13'
updated: '2026-10-13'
summary: Google于10月13日16:00 UTC宣布Argon全球推出：API付费层可在AI Studio/Gemini平台使用，Antigravity面向Ultra，Gemini
  App和AI Mode面向Ultra/Pro；具体地区和产品实际推送仍以账户为准。
evidence_kind: reported
verification: source-checked
sources:
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/
- https://cloud.google.com/blog/products/ai-machine-learning/gemini-4-argon-available-on-google-cloud/
related: []
aliases: []
last_verified: '2026-10-13'
verification_note: Agent已阅读标注范围并核对有限陈述支持关系；不表示独立测量、融资审计或部署复现。 官网原始HTML及完整文章关键主文/Get
  started/价格脚注；Google Cloud完整RSS定价交叉回读；未完整模型卡。
source: raw/2026-10-14/d171aceaca5a62781cca7a363c02536f0a86c4f9c4528c2854457dadff58faa0.body
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/
published_at: '2026-10-13T16:00:00+00:00'
source_category: official
raw_path: raw/2026-10-14/d171aceaca5a62781cca7a363c02536f0a86c4f9c4528c2854457dadff58faa0.body
sha256: d171aceaca5a62781cca7a363c02536f0a86c4f9c4528c2854457dadff58faa0
fetched_at: '2026-10-14T01:09:10.733713+00:00'
reading_scope: 官网原始HTML及完整文章关键主文/Get started/价格脚注；Google Cloud完整RSS定价交叉回读；未完整模型卡。
date_precision: timestamp
date_basis: published
evidence:
- source: raw/2026-10-14/d171aceaca5a62781cca7a363c02536f0a86c4f9c4528c2854457dadff58faa0.body
  locator: 官网原始HTML及完整文章关键主文/Get started/价格脚注；Google Cloud完整RSS定价交叉回读；未完整模型卡。
  version: sha256:d171aceaca5a62781cca7a363c02536f0a86c4f9c4528c2854457dadff58faa0
- source: raw/2026-10-14/1d7c5253f08dba47c1b1f542fa3f44f4869163aff12471a013204df035542835.body
  locator: Google Cloud完整RSS Get started：模型ID、引入价/标准价；非独立验证。
  version: sha256:1d7c5253f08dba47c1b1f542fa3f44f4869163aff12471a013204df035542835
reviewed_by: Codex
reviewed_at: '2026-10-14'
reviewed_content_sha256: 06c9a42915629213fbe2319fb1a64eac973f05a0be80745850afe6f7d1b2dc05
---

# Gemini 4 Argon向付费产品与API开放，百万token由输入输出共用

## Key Takeaways

Google于10月13日16:00 UTC宣布Argon全球推出：API付费层可在AI Studio/Gemini平台使用，Antigravity面向Ultra，Gemini App和AI Mode面向Ultra/Pro；具体地区和产品实际推送仍以账户为准。

API提供1M统一输入输出token限额，不等于输入1M外再输出1M。公开模型引入价USD2/百万输入、USD10/百万输出，缓存输入折扣95%；11月30日优惠结束后标准价USD4/20。未核对全部长上下文、缓存存储和工具收费细则。

相对较早模型预告，本期新增可用入口和价格；长任务、科学与代码能力为Google/客户披露，未逐项审计模型卡、harness、预算和外链PR，不采用厂商领先排名或加速倍数。

## Detailed Notes

阅读范围：官网原始HTML及完整文章关键主文/Get started/价格脚注；Google Cloud完整RSS定价交叉回读；未完整模型卡。

## Evidence

[原始来源](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)。不可覆盖原始档案、采集时间和hash见元数据。浏览笔记明确为非逐字提取；日期未知不补采集日，日期占位不视为实际时刻。

## Questions Raised

判断（derived）：广泛分发与优惠价可能推动企业试用长任务，Google云和开发者工具受益；长输出、重试及后续标准价可能增加每任务成本。观察同harness成功率、实际总费用、续用及优惠结束后的迁移。
