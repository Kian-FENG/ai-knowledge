---
id: source-gemini-model-access-october-2026
title: Gemini 个人账户模型访问分层：10月生效安排
type: source
domain:
- products
- companies
lifecycle: published
tags:
- model-access
- subscription
created: '2026-10-05'
updated: '2026-10-05'
summary: Google帮助页披露个人账户10月模型访问调整；无订阅从10月9日起生效，页面发布日期未知。
evidence_kind: reported
verification: source-checked
sources:
- https://support.google.com/gemini/answer/17004136
related:
- paper-rrsi-agent-harnesses-2609-24972
aliases: []
source: raw/2026-10-05/9509f8630a3c14456dd5e021e4eebe71ae6967cb8b6c9f58d53e6a875e23a1f0.txt
url: https://support.google.com/gemini/answer/17004136
published_at: null
source_category: official
effective_at: '2026-10-09'
date_note: 官网未显示发布/更新时间；effective_at仅适用于无订阅个人账户。
fetched_at: '2026-10-05T03:17:28.077435+00:00'
raw_path: raw/2026-10-05/9509f8630a3c14456dd5e021e4eebe71ae6967cb8b6c9f58d53e6a875e23a1f0.txt
sha256: 9509f8630a3c14456dd5e021e4eebe71ae6967cb8b6c9f58d53e6a875e23a1f0
last_verified: '2026-10-05'
verification_note: 读取官方帮助页及模型访问表；核对生效日期和账户范围，未核实实际部署、价格或使用效果。
evidence:
- source: raw/2026-10-05/9509f8630a3c14456dd5e021e4eebe71ae6967cb8b6c9f58d53e6a875e23a1f0.txt
  locator: Effective dates；Access after the change；Scope（官方帮助页第27–40行的阅读笔记）
  version: sha256:9509f8630a3c14456dd5e021e4eebe71ae6967cb8b6c9f58d53e6a875e23a1f0
reviewed_by: Codex
reviewed_at: '2026-10-05'
reviewed_content_sha256: a562065c7e79cf0adb311ccc7cd8c00e785881d7d30390017e2a7fb9b36dc2cb
---

# Gemini 个人账户模型访问分层：10月生效安排

## Key Takeaways

- Google 官方帮助页说明：无订阅个人账户从2026年10月9日起调整；AI Plus 生效日以用户收到的邮件为准。
- 调整后无订阅仅可访问 Flash-Lite，AI Plus 增加 Flash，AI Pro/Ultra 还可访问 Pro。
- 发布日期未知，本页作为背景入库，未列为10月4日首发新闻。

## Detailed Notes

范围限于 Gemini Apps 个人账户，不能据此推断 API、Workspace 或企业合同。本次没有核实套餐价格、所有地区上线时间和用户采用效果。

研究判断（derived）：用模型访问权区分套餐，可能改变免费入口的升级动机。后续观察留存、升级率及较小模型能否满足任务；如果任务质量仍可满足，权限调整未必推动付费。

## Evidence

实际读取完整官方帮助页，归档为 Agent 阅读笔记，非 HTTP 原始响应。URL、采集时间、hash 和定位见元数据；网页没有发布日期，不以采集日代替。

## Questions Raised

AI Plus 邮件何时生效？各地区是否同一安排？公开使用数据能否验证升级与流失影响？
