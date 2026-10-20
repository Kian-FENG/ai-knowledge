---
id: source-microsoft-agentic-insider-20261019
title: 微软将内部Agent纳入持续风险控制，Guardian方案仍须验证
type: source
domain:
- infra
- products
lifecycle: published
tags: []
created: '2026-10-20'
updated: '2026-10-20'
summary: 微软10月19日官方文章提出按身份、权限、数据、端点、网络、云与运行时管理内部Agent，利用Project Perception的信号、动态上下文和Guardian
  Agents监督行动。增量是将既有安全栈的适用对象扩展到内部Agent。
evidence_kind: reported
verification: source-checked
sources:
- https://blogs.microsoft.com/blog/2026/10/19/securing-the-agentic-insider/
related: []
aliases: []
source: raw/2026-10-21/b65c4a8755c2289c14b6ea14c844c01e9e903d6ec0c303dc78dc547f9848a95a.txt
url: https://blogs.microsoft.com/blog/2026/10/19/securing-the-agentic-insider/
published_at: '2026-10-19T00:00:00+08:00'
source_category: official
raw_path: raw/2026-10-21/b65c4a8755c2289c14b6ea14c844c01e9e903d6ec0c303dc78dc547f9848a95a.txt
sha256: b65c4a8755c2289c14b6ea14c844c01e9e903d6ec0c303dc78dc547f9848a95a
fetched_at: '2026-10-20T22:08:29.400466+00:00'
reading_scope: 官方主文agentic insiders、Project Perception三层控制与model transparency；主文已读，链接产品资格/实测未核。
last_verified: '2026-10-20'
verification_note: Agent已阅读所列范围并核对支持关系；reported不等于独立审计或复现，审核发布不提高核验等级。
evidence:
- source: raw/2026-10-21/b65c4a8755c2289c14b6ea14c844c01e9e903d6ec0c303dc78dc547f9848a95a.txt
  locator: 官方主文agentic insiders、Project Perception三层控制与model transparency；主文已读，链接产品资格/实测未核。
  version: sha256:b65c4a8755c2289c14b6ea14c844c01e9e903d6ec0c303dc78dc547f9848a95a
reviewed_by: Codex
reviewed_at: '2026-10-21'
reviewed_content_sha256: fc861775a22d34b6f99d5919f85b91d4c2817b54985b7a58d272e540c3b860c4
---

# 微软将内部Agent纳入持续风险控制，Guardian方案仍须验证

## Key Takeaways

微软10月19日官方文章提出按身份、权限、数据、端点、网络、云与运行时管理内部Agent，利用Project Perception的信号、动态上下文和Guardian Agents监督行动。增量是将既有安全栈的适用对象扩展到内部Agent。

## Detailed Notes

这是厂商架构与治理路线陈述，未公布统一SKU、价格、完整可用范围或对照实验；“持续监督每一步”不视为已覆盖所有生产场景。来源只有日期，窗口边界不确定。

## Evidence

[原始来源](https://blogs.microsoft.com/blog/2026/10/19/securing-the-agentic-insider/)。官方主文agentic insiders、Project Perception三层控制与model transparency；主文已读，链接产品资格/实测未核。 原始路径、采集时间与hash见元数据。

## Questions Raised

判断（derived）：执行前控制可能扩大身份与安全平台在Agent预算中的占比；反例是额外延迟、误拦截以及监督Agent自身失效。观察策略覆盖率、绕过率、误报和关键路径延迟。
