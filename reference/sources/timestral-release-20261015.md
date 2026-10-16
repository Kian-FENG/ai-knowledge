---
id: source-timestral-release-20261015
title: Mistral推出Timestral时序模型，最大209M并支持已知未来协变量
type: source
domain:
- models
- products
lifecycle: published
tags:
- daily-research
created: '2026-10-15'
updated: '2026-10-15'
summary: Mistral 10月15日发布首个时序基础模型家族Timestral，参数5M/28M/123M/209M、上下文32768时间步、21分位数预测，支持多变量、过去与已知未来协变量。公告称已发布GitHub仓库，通过Forge提供定制和本地/VPC/隔离部署，许可标为Modified
  MIT。
evidence_kind: reported
verification: source-checked
sources:
- https://mistral.ai/news/timestral/
related: []
aliases: []
source: raw/2026-10-16/f306f7226035b25040e52fa772fb681f54b5c48c9dedce24f176e2433e93c3da.body
url: https://mistral.ai/news/timestral/
published_at: '2026-10-15T12:00:00+00:00'
source_category: official
raw_path: raw/2026-10-16/f306f7226035b25040e52fa772fb681f54b5c48c9dedce24f176e2433e93c3da.body
sha256: f306f7226035b25040e52fa772fb681f54b5c48c9dedce24f176e2433e93c3da
fetched_at: '2026-10-16T01:11:21.563620+00:00'
source_updated_at: null
announced_at: null
date_precision: timestamp
reading_scope: 官网完整公告，family / contributions / Forge / specs；无独立复现。
retrieval_method: full-text
evidence:
- source: raw/2026-10-16/f306f7226035b25040e52fa772fb681f54b5c48c9dedce24f176e2433e93c3da.body
  locator: 官网完整公告，family / contributions / Forge / specs；无独立复现。
  version: sha256:f306f7226035b25040e52fa772fb681f54b5c48c9dedce24f176e2433e93c3da
last_verified: '2026-10-15'
verification_note: Agent已阅读所列范围并逐项核对事实与来源支持关系；公司/作者及媒体陈述为reported，没有独立审计、账户验证或实验复现。
reviewed_by: Codex
reviewed_at: '2026-10-16'
reviewed_content_sha256: c75dcb2cbdea7561fab0589a88c9ff482ee28d5f1a8dd4eb006900c95508e434
---

# Mistral推出Timestral时序模型，最大209M并支持已知未来协变量

## Key Takeaways

Mistral 10月15日发布首个时序基础模型家族Timestral，参数5M/28M/123M/209M、上下文32768时间步、21分位数预测，支持多变量、过去与已知未来协变量。公告称已发布GitHub仓库，通过Forge提供定制和本地/VPC/隔离部署，许可标为Modified MIT。

相对Large4通用模型预览，新增为数值预测专用路线。GIFT-Eval/TIME/fev-bench领先为Mistral自测，基准版本与完整harness未核；CPU延迟缺具体型号/完整软件配置，未采用其数值排名。技术报告仍待发布，完整许可条款未审。

## Detailed Notes

官网完整公告，family / contributions / Forge / specs；无独立复现。 已检索published及显式草稿，并按URL/hash查重；这是本期所列增量。

## Evidence

[原始来源](https://mistral.ai/news/timestral/)；归档 `raw/2026-10-16/f306f7226035b25040e52fa772fb681f54b5c48c9dedce24f176e2433e93c3da.body`，sha256 `f306f7226035b25040e52fa772fb681f54b5c48c9dedce24f176e2433e93c3da`。

reported与source-checked分别表示陈述性质和支持关系核对，审核发布不提高为独立复现。

## Questions Raised

判断：小型数值模型可与语言Agent分工，把预测和解释分开，制造、能源和计划系统可能减少GPU依赖。反例是生产分布漂移、数据泄漏或校准不足；观察滚动回测、区间覆盖、域内重训和决策收益。
