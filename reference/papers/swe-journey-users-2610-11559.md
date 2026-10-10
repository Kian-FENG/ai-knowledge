---
id: paper-swe-journey-users-2610-11559
title: SWE-Journey 将不同用户习惯纳入长时编码 Agent 评估
type: paper
domain:
- models
- products
lifecycle: published
tags:
- daily-research
created: '2026-10-10'
updated: '2026-10-10'
summary: arXiv 2610.11559v1于10月8日09:21:49Z提交、10月9日cs.CL公告；按公告日期进入本期，日期仅到日。
evidence_kind: reported
verification: source-checked
sources:
- https://arxiv.org/abs/2610.11559
related: []
aliases: []
source: raw/2026-10-10/fb0123950b335cb7681ceecdfcfc10ac1ec77f0c255a7323879fffa8ee53277d.body
url: https://arxiv.org/abs/2610.11559
published_at: '2026-10-08T09:21:49+00:00'
source_category: paper
raw_path: raw/2026-10-10/fb0123950b335cb7681ceecdfcfc10ac1ec77f0c255a7323879fffa8ee53277d.body
sha256: fb0123950b335cb7681ceecdfcfc10ac1ec77f0c255a7323879fffa8ee53277d
fetched_at: '2026-10-10T01:14:20.011532+00:00'
last_verified: '2026-10-10'
verification_note: 已核对本页有限陈述与实际读取的来源；arXiv摘要、Submission history及10月9日cs.CL公告列表第41项；未读全文/补充材料/完整harness。
  非独立复现。
reading_scope: arXiv摘要、Submission history及10月9日cs.CL公告列表第41项；未读全文/补充材料/完整harness。
evidence:
- source: raw/2026-10-10/fb0123950b335cb7681ceecdfcfc10ac1ec77f0c255a7323879fffa8ee53277d.body
  locator: arXiv摘要、Submission history及10月9日cs.CL公告列表第41项；未读全文/补充材料/完整harness。
  version: sha256:fb0123950b335cb7681ceecdfcfc10ac1ec77f0c255a7323879fffa8ee53277d
- source: raw/2026-10-10/77f93a65e1a064bd119148ce4e42bda8721154f8c5278f4694de0af8f1db2683.body
  locator: 官方RSS item guid oai:arXiv.org:2610.11559v1，Announce Type new，pubDate Fri,
    09 Oct 2026 00:00:00 -0400；午夜为列表公告日期标记，精确公告时刻未确认；abstract与abs版本对应。
  version: sha256:77f93a65e1a064bd119148ce4e42bda8721154f8c5278f4694de0af8f1db2683
date_precision: date-only
date_basis: announced
announced_at: '2026-10-09T00:00:00+08:00'
announcement_rss_offset: '-0400'
reviewed_by: Codex
reviewed_at: '2026-10-10'
reviewed_content_sha256: 6f07e101e8f2aec988d88cf984aaa7d2fa9d4457a184cba2ca153a1e6c3bd89e
---

# SWE-Journey 将不同用户习惯纳入长时编码 Agent 评估

## Problem and Method

arXiv 2610.11559v1于10月8日09:21:49Z提交、10月9日cs.CL公告；按公告日期进入本期，日期仅到日。

摘要描述weak-to-strong任务合成、持续演化仓库和4类模拟用户的多轮交互；相对单个issue解决率，本期增量是用户行为差异与长时工作流。仅读摘要，不采用缺模型版本、预算、harness和完整任务条件的跨用户分数。

## Results and Conditions

仅摘要与版本/公告日期核对；全文、实验设置和harness未读。无独立性能结论，不用摘要数字排名。

## Evidence

[原始来源](https://arxiv.org/abs/2610.11559)。原始路径、hash、采集时间与日期口径见元数据。source-checked仅表示所写披露有出处支持，非真实性独立审计。

## Limitations and Implications

判断（derived）：评估若纳入提问、找错与修复过程，可帮助产品识别非专业用户支持成本；模拟用户偏差和真实用户学习效应可能改变结果。观察真实用户验证、任务难度匹配及人工接管，而非把模拟结果外推为所有人表现。

公告日另由元数据中的官方RSS entry支持；RSS使用-0400午夜列表标记，实际公告时刻未核实，不视为精确发布时间。
