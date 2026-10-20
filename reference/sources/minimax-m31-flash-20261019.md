---
id: source-minimax-m31-flash-20261019
title: MiniMax M3.1 Flash上线API与订阅，权重仍待发布
type: source
domain:
- models
- products
lifecycle: published
tags: []
created: '2026-10-20'
updated: '2026-10-20'
summary: MiniMax 10月19日宣布M3.1 Flash正式上线API、M Plan和MiniMax Code；权重将稍后发布，Pro仍为后续计划。相对此前M3与预览版，增量是正式服务与新的价格表。
evidence_kind: reported
verification: source-checked
sources:
- https://www.minimax.io/blog/minimax-m31f
related: []
aliases: []
source: raw/2026-10-21/ec858e02aba510a17b6f02333d634b63bf88cfce18674e03b04c3a5b16b0f4d6.body
url: https://www.minimax.io/blog/minimax-m31f
published_at: '2026-10-19T00:00:00+08:00'
source_category: official
raw_path: raw/2026-10-21/ec858e02aba510a17b6f02333d634b63bf88cfce18674e03b04c3a5b16b0f4d6.body
sha256: ec858e02aba510a17b6f02333d634b63bf88cfce18674e03b04c3a5b16b0f4d6
fetched_at: '2026-10-20T22:07:44.600187+00:00'
reading_scope: 官方正文2026-10-19、Pricing、可用渠道与weights later；主文已读，图表像素/评测harness未审。
last_verified: '2026-10-20'
verification_note: Agent已阅读所列范围并核对支持关系；reported不等于独立审计或复现，审核发布不提高核验等级。
evidence:
- source: raw/2026-10-21/ec858e02aba510a17b6f02333d634b63bf88cfce18674e03b04c3a5b16b0f4d6.body
  locator: 官方正文2026-10-19、Pricing、可用渠道与weights later；主文已读，图表像素/评测harness未审。
  version: sha256:ec858e02aba510a17b6f02333d634b63bf88cfce18674e03b04c3a5b16b0f4d6
reviewed_by: Codex
reviewed_at: '2026-10-21'
reviewed_content_sha256: cfd21e3dc3be09b1d160f9bec29d7a0bb267a78505d6d3335eefdaec982f74f0
---

# MiniMax M3.1 Flash上线API与订阅，权重仍待发布

## Key Takeaways

MiniMax 10月19日宣布M3.1 Flash正式上线API、M Plan和MiniMax Code；权重将稍后发布，Pro仍为后续计划。相对此前M3与预览版，增量是正式服务与新的价格表。

## Detailed Notes

公告列USD/百万token：输入0.15、输出0.60、缓存输入0.015。速度、综合任务降本和榜单名次是厂商主张，缺完整harness、预算与负载，不据此对模型排名。日期仅到日，窗口边界不确定，前一期未收录。

## Evidence

[原始来源](https://www.minimax.io/blog/minimax-m31f)。官方正文2026-10-19、Pricing、可用渠道与weights later；主文已读，图表像素/评测harness未审。 原始路径、采集时间与hash见元数据。

## Questions Raised

判断（derived）：低输出单价可能降低长程Agent的试错预算，应用商受益、其他API面临价格压力；反例是更多重试抵消单价优势。观察固定任务成功率、完整账单和权重实际交付。
