---
id: source-claude-anthropic-managed-gcp-20261022
title: Claude新增Anthropic管理的Google Cloud接入，完整平台能力进入云承诺采购
type: source
domain:
- products
- companies
lifecycle: published
tags: []
created: '2026-10-24'
updated: '2026-10-23'
summary: Anthropic于10月22日宣布Claude Models on Google Cloud（Anthropic managed）GA：复用Google
  Cloud IAM、统一发票并抵扣已有消费承诺，当前有US和Global端点。增量是原生Claude API功能和beta与本家同日提供。
evidence_kind: reported
verification: source-checked
sources:
- https://claude.com/resources/articles/claude-models-on-google-cloud-anthropic-managed
related: []
aliases: []
source: raw/2026-10-24/96c80c970d9632231f80c8a095cf419447dd97fbabd7b69f4a3dc53dee02ee3d.txt
url: https://claude.com/resources/articles/claude-models-on-google-cloud-anthropic-managed
published_at: '2026-10-22T00:00:00+08:00'
source_category: official
last_verified: '2026-10-23'
verification_note: Agent阅读所列来源并核对有限结论；reported保留披露主体归因，derived是研究推导，未独立复现。
reading_scope: Anthropic官方公告主文完整阅读，包含两种管理方式、端点、价格和折扣提示；未实测购买、API或审合同。Google对应文章超时，不宣称双边正文均核完。
raw_path: raw/2026-10-24/96c80c970d9632231f80c8a095cf419447dd97fbabd7b69f4a3dc53dee02ee3d.txt
sha256: 96c80c970d9632231f80c8a095cf419447dd97fbabd7b69f4a3dc53dee02ee3d
fetched_at: '2026-10-23T22:08:47.734543+00:00'
evidence:
- source: raw/2026-10-24/96c80c970d9632231f80c8a095cf419447dd97fbabd7b69f4a3dc53dee02ee3d.txt
  locator: Anthropic官方公告主文完整阅读，包含两种管理方式、端点、价格和折扣提示；未实测购买、API或审合同。Google对应文章超时，不宣称双边正文均核完。
  version: sha256:96c80c970d9632231f80c8a095cf419447dd97fbabd7b69f4a3dc53dee02ee3d
date_precision: date-only
reviewed_by: Codex
reviewed_at: '2026-10-24'
reviewed_content_sha256: 0455e517e07dee33d3146c67efb5ff7a6d82d691685f6d877f972a39e917d9e0
---

# Claude新增Anthropic管理的Google Cloud接入，完整平台能力进入云承诺采购

## Key Takeaways

Anthropic于10月22日宣布Claude Models on Google Cloud（Anthropic managed）GA：复用Google Cloud IAM、统一发票并抵扣已有消费承诺，当前有US和Global端点。增量是原生Claude API功能和beta与本家同日提供。

## Detailed Notes

Anthropic运营服务并担任数据处理方；原有Google managed方式继续存在，适合需要Google处理数据、严格区域驻留或Google原生集成的客户。Managed Agents等仍为beta，不随接入方式GA自动转正。

该接入提供Fable 5.1、Opus 5.5、Sonnet 5.5和Haiku 5.5；Opus 5.5 Fast Mode也GA，公告输入/输出价分别USD8/40每百万token。已有折扣需事前确认，不能追溯应用。仅日精度，18:00边界不确定，前期未收录。

## Evidence

[原始来源](https://claude.com/resources/articles/claude-models-on-google-cloud-anthropic-managed)；原始版本 `raw/2026-10-24/96c80c970d9632231f80c8a095cf419447dd97fbabd7b69f4a3dc53dee02ee3d.txt`，SHA-256 `96c80c970d9632231f80c8a095cf419447dd97fbabd7b69f4a3dc53dee02ee3d`。

Anthropic官方公告主文完整阅读，包含两种管理方式、端点、价格和折扣提示；未实测购买、API或审合同。Google对应文章超时，不宣称双边正文均核完。

## Questions Raised

判断：云采购和原生功能更新可同时满足，降低企业在新能力与已有预算之间的取舍；云平台和模型商扩大分发。反例是数据处理方、驻留要求或折扣损失限制迁移。观察端点覆盖、折扣、模型配额与beta实际可用性。
