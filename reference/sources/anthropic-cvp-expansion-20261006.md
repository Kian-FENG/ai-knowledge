---
id: source-anthropic-cvp-expansion-20261006
title: Anthropic 扩展 CVP：网络安全模型访问按资格和用途分层
type: source
domain:
- products
- models
lifecycle: published
tags:
- daily-research
created: '2026-10-07'
updated: '2026-10-07'
summary: Anthropic 将 Glasswing 与 Cyber Verification Program 合并为分层访问体系：Defense Access、Red
  Team Access、Specialized Access；不同层级对应资格审核、允许用途与不同保护措施。
evidence_kind: reported
verification: source-checked
sources:
- https://www.anthropic.com/news/cyber-verification-program
related: []
aliases: []
source: raw/2026-10-07/d07a3b5bbec14cb68e2ce4757e6d20d5dcdd7f6de5b52896ac31cc8d7cdd9f07.body
url: https://www.anthropic.com/news/cyber-verification-program
published_at: '2026-10-06'
source_category: official
raw_path: raw/2026-10-07/d07a3b5bbec14cb68e2ce4757e6d20d5dcdd7f6de5b52896ac31cc8d7cdd9f07.body
sha256: d07a3b5bbec14cb68e2ce4757e6d20d5dcdd7f6de5b52896ac31cc8d7cdd9f07
fetched_at: '2026-10-07T01:09:48.649113+00:00'
last_verified: '2026-10-07'
reading_scope: 已读正文与访问/保留规则；未复现 CyScenarioBench，不用不同保护设置的结果作模型普遍能力或安全性排名。
verification_note: 已实际阅读并核对以下陈述与出处：Introducing the expanded Cyber Verification Program；访问层级、平台与
  data retention / safeguards 说明。已读正文与访问/保留规则；未复现 CyScenarioBench，不用不同保护设置的结果作模型普遍能力或安全性排名。
evidence:
- source: raw/2026-10-07/d07a3b5bbec14cb68e2ce4757e6d20d5dcdd7f6de5b52896ac31cc8d7cdd9f07.body
  locator: Introducing the expanded Cyber Verification Program；访问层级、平台与 data retention
    / safeguards 说明
  version: sha256:d07a3b5bbec14cb68e2ce4757e6d20d5dcdd7f6de5b52896ac31cc8d7cdd9f07
reviewed_by: Codex
reviewed_at: '2026-10-07'
reviewed_content_sha256: 0d4a077d432353612539e714f489b79b3046c63c3a1627577c93db27977d450e
date_precision: date-only
---

# Anthropic 扩展 CVP：网络安全模型访问按资格和用途分层

## Key Takeaways

Anthropic 将 Glasswing 与 Cyber Verification Program 合并为分层访问体系：Defense Access、Red Team Access、Specialized Access；不同层级对应资格审核、允许用途与不同保护措施。

公告列出 Opus 5.5、Sonnet 5.5、Mythos 5.1 等模型，涉及 Claude、Vertex AI、Microsoft Foundry；Bedrock 路径受 EFS 资格约束。数据保留用于监控；特定既有 Fable/Mythos 零保留客户存在例外，未来 EFS 安排尚未完成。

增量是模型能力的交付与治理规则；不是所有模型对所有个人开放。正文只有 10 月 6 日日期，时区与窗口边界不确定，已对照前期去重。

## Detailed Notes

已读正文与访问/保留规则；未复现 CyScenarioBench，不用不同保护设置的结果作模型普遍能力或安全性排名。

## Evidence

[原始来源](https://www.anthropic.com/news/cyber-verification-program)。定位：Introducing the expanded Cyber Verification Program；访问层级、平台与 data retention / safeguards 说明。原始路径、采集时间、版本和 hash 见元数据；source-checked 仅表示已核对所列有限陈述，不代表独立复现。

## Questions Raised

判断（derived）：实际可用能力由模型与访问层级共同决定，合规组织可能获得更适合授权测试的工具，平台采购和数据保留政策会影响采用。厂商演示不能证明普遍安全或效果；观察审核等待时间、可用平台、授权范围和真实误报率。
