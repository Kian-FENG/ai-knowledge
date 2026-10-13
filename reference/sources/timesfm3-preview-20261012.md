---
id: source-timesfm3-preview-20261012
title: BigQuery TimesFM 3.0预览支持多变量时间序列预测
type: source
domain:
- models
- products
lifecycle: published
tags:
- daily-research
created: '2026-10-12'
updated: '2026-10-12'
summary: Google Cloud 10月12日文章宣布TimesFM 3.0在BigQuery进入预览，330M参数，原生多变量预测，并通过AI.FORECAST的SQL入口使用。相对2.0/2.5仅单变量，本期增量是关联目标及协变量。
evidence_kind: reported
verification: source-checked
sources:
- https://cloud.google.com/blog/products/data-analytics/bigquery-timesfm-3-0-with-multivariate-time-series-forecasting/
related: []
aliases: []
source: raw/2026-10-13/c4de36f79e6a9f0771c94fce032c1bf505867ae96db34dac9faf1a551a96007e.body
url: https://cloud.google.com/blog/products/data-analytics/bigquery-timesfm-3-0-with-multivariate-time-series-forecasting/
published_at: '2026-10-12T16:00:00+00:00'
source_category: official
raw_path: raw/2026-10-13/c4de36f79e6a9f0771c94fce032c1bf505867ae96db34dac9faf1a551a96007e.body
sha256: c4de36f79e6a9f0771c94fce032c1bf505867ae96db34dac9faf1a551a96007e
fetched_at: '2026-10-13T01:09:50.186050+00:00'
last_verified: '2026-10-12'
verification_note: 已阅读所标范围并核对有限陈述支持关系；source-checked不表示融资审计、模型独立评测或部署复现。官方主文TimesFM3
  preview、330M、多变量/协变量、AI.FORECAST SQL和migration；外链评测未读。
reading_scope: 官方主文TimesFM3 preview、330M、多变量/协变量、AI.FORECAST SQL和migration；外链评测未读。
evidence:
- source: raw/2026-10-13/c4de36f79e6a9f0771c94fce032c1bf505867ae96db34dac9faf1a551a96007e.body
  locator: 官方主文TimesFM3 preview、330M、多变量/协变量、AI.FORECAST SQL和migration；外链评测未读。
  version: sha256:c4de36f79e6a9f0771c94fce032c1bf505867ae96db34dac9faf1a551a96007e
date_precision: timestamp
date_basis: published
reviewed_by: Codex
reviewed_at: '2026-10-13'
reviewed_content_sha256: 60f05fc998ee849aaa8ba6537038b4428a02a41751970710a5249a8e2d3a5b71
---

# BigQuery TimesFM 3.0预览支持多变量时间序列预测

## Key Takeaways

Google Cloud 10月12日文章宣布TimesFM 3.0在BigQuery进入预览，330M参数，原生多变量预测，并通过AI.FORECAST的SQL入口使用。相对2.0/2.5仅单变量，本期增量是关联目标及协变量。

文中区分仅历史可用的协变量和可提前知道的未来协变量；不能将未来未知的真实数据泄漏进预测。文章给出单变量/异常检测迁移及对话分析示例。

已读完整主文和SQL示例；GIFT-Eval、FEV-Bench、TIME的领先为厂商披露，未读具体评测版本/预算/外链表格，不作排名。地区、价格与权重许可未核实。

## Detailed Notes

官方主文TimesFM3 preview、330M、多变量/协变量、AI.FORECAST SQL和migration；外链评测未读。

## Evidence

[原始来源](https://cloud.google.com/blog/products/data-analytics/bigquery-timesfm-3-0-with-multivariate-time-series-forecasting/)。原始路径、hash、采集时间及版本见元数据；有限摘录/摘要范围与缺失条件不被自动发布改变。

## Questions Raised

判断（derived）：零样本多变量预测嵌入数据库可降低构建专用模型和数据搬运门槛，已有SQL数据栈受益。分布漂移、协变量不可得或治理不足会削弱效果；观察分行业回测、基线误差、上线漂移、协变量泄漏和完整查询费用。
