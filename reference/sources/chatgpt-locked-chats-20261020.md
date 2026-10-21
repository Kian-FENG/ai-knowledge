---
id: source-chatgpt-locked-chats-20261020
title: ChatGPT开始逐步推送锁定聊天，以账户PIN或设备认证隐藏会话
type: source
domain:
- products
lifecycle: published
tags: []
created: '2026-10-21'
updated: '2026-10-21'
summary: OpenAI 10月20日更新说明：锁定会话保留在账户中，但从普通历史、置顶与搜索隐藏，打开时用4位账户PIN或支持的设备认证。
evidence_kind: reported
verification: source-checked
sources:
- https://help.openai.com/en/articles/6825453-chatgpt-release-notes
related: []
aliases: []
source: raw/2026-10-22/8eeb64fd195c16fa98cf096770f90a7125dad4544706c0c91416aa4b2a811a6f.txt
url: https://help.openai.com/en/articles/6825453-chatgpt-release-notes
published_at: '2026-10-20T00:00:00+08:00'
source_category: official
raw_path: raw/2026-10-22/8eeb64fd195c16fa98cf096770f90a7125dad4544706c0c91416aa4b2a811a6f.txt
sha256: 8eeb64fd195c16fa98cf096770f90a7125dad4544706c0c91416aa4b2a811a6f
fetched_at: '2026-10-21T22:09:58.621228+00:00'
reading_scope: 仅完整阅读release notes的October 20 / Introducing locked chats小节及帮助文档入口；未实测各端或审核安全实现。
last_verified: '2026-10-21'
verification_note: Agent实际阅读所列范围并核对结论支持关系；公司和作者披露为reported，无独立复现；发布审核不提高核验等级。
evidence:
- source: raw/2026-10-22/8eeb64fd195c16fa98cf096770f90a7125dad4544706c0c91416aa4b2a811a6f.txt
  locator: 仅完整阅读release notes的October 20 / Introducing locked chats小节及帮助文档入口；未实测各端或审核安全实现。
  version: sha256:8eeb64fd195c16fa98cf096770f90a7125dad4544706c0c91416aa4b2a811a6f
date_precision: date-only
reviewed_by: Codex
reviewed_at: '2026-10-22'
reviewed_content_sha256: 71409d00f5f8f35611eb9299003652035a15048a195a96ddf38d89d1b46884e3
---

# ChatGPT开始逐步推送锁定聊天，以账户PIN或设备认证隐藏会话

## Key Takeaways

OpenAI 10月20日更新说明：锁定会话保留在账户中，但从普通历史、置顶与搜索隐藏，打开时用4位账户PIN或支持的设备认证。

## Detailed Notes

Free、Go、Plus、Pro在网页、iOS、Android及macOS/Windows新桌面端逐步推送；保留期限和模型改进设置不变。相对此前普通历史管理，增量是会话级访问控制，不应据此推断新增加密或企业合规承诺。

官方仅标日期，无首次发布小时；与前一期对照未收录，窗口边界不确定。

## Evidence

[原始来源](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)；`raw/2026-10-22/8eeb64fd195c16fa98cf096770f90a7125dad4544706c0c91416aa4b2a811a6f.txt`，hash `8eeb64fd195c16fa98cf096770f90a7125dad4544706c0c91416aa4b2a811a6f`。

仅完整阅读release notes的October 20 / Introducing locked chats小节及帮助文档入口；未实测各端或审核安全实现。

## Questions Raised

判断：更细的会话访问控制可能降低共享设备或旁观场景的使用顾虑，支持个人助手积累长期上下文；实际采用仍取决于恢复流程与用户对保留规则的理解。反例是PIN被共用或账户本身失陷。观察推送完成范围、恢复体验与用户使用数据。
