---
id: source-third-moment-agent-scale-20261014
title: Third Moment披露万Agent长时研究案例，扩展工作流定制推理路线
type: source
domain:
- companies
- products
lifecycle: published
tags:
- daily-research
created: '2026-10-14'
updated: '2026-10-14'
summary: OpenAI10月14日客户案例称Third Moment Research使用Codex、GPT-6系列及GPT-6.1 Sol运行1万个并发Agent，研究会话36–48小时；外层harness决定重试、终止或转人工，Daybreak用于环境安全测试。
evidence_kind: reported
verification: source-checked
sources:
- https://openai.com/index/third-moment-research
- source-third-moment-products-undated
related: []
aliases: []
source: raw/2026-10-15/ec8eb4c50b297369c3683ddcafab5fc5d3b4b1d9f14ca03ed5497d2c726fdac8.txt
url: https://openai.com/index/third-moment-research
published_at: '2026-10-14T07:00:00+00:00'
source_category: official
raw_path: raw/2026-10-15/ec8eb4c50b297369c3683ddcafab5fc5d3b4b1d9f14ca03ed5497d2c726fdac8.txt
sha256: ec8eb4c50b297369c3683ddcafab5fc5d3b4b1d9f14ca03ed5497d2c726fdac8
fetched_at: '2026-10-15T01:11:33.550900+00:00'
source_updated_at: null
announced_at: null
date_precision: timestamp
reading_scope: OpenAI案例主文及Third Moment官网全部可见产品流程；未独立验证并发、收益、融资或法定注册主体。
retrieval_method: agent-source-extract
evidence:
- source: raw/2026-10-15/ec8eb4c50b297369c3683ddcafab5fc5d3b4b1d9f14ca03ed5497d2c726fdac8.txt
  locator: OpenAI案例主文及Third Moment官网全部可见产品流程；未独立验证并发、收益、融资或法定注册主体。
  version: sha256:ec8eb4c50b297369c3683ddcafab5fc5d3b4b1d9f14ca03ed5497d2c726fdac8
- source: raw/2026-10-15/8bfcecf72752116cf94c6de824544fd7690ab1389f2c1f485ec19bd33e38c75c.body
  locator: 原始RSS/Atom对应URL条目及发布时间或公告日；正文结论以本次主文快照为准。
  version: sha256:8bfcecf72752116cf94c6de824544fd7690ab1389f2c1f485ec19bd33e38c75c
- source: raw/2026-10-15/e8e0d3e09b8e6e9aee9ad58de2c4907489835574b3bb481f6327416659c5866a.txt
  locator: 官网可见产品全文，Collect→Diagnose→Decide→Improve→Ship与Fully managed；未知发布日期。
  version: sha256:e8e0d3e09b8e6e9aee9ad58de2c4907489835574b3bb481f6327416659c5866a
last_verified: '2026-10-14'
verification_note: Agent已阅读所列范围并核对有限陈述与来源的支持关系；公司/作者披露未独立审计或复现。
reviewed_by: Codex
reviewed_at: '2026-10-15'
reviewed_content_sha256: 53ed7d07ec5fa35c2718853df6e81c0718d74f3b7f97b44ad27296cc99965f08
---

# Third Moment披露万Agent长时研究案例，扩展工作流定制推理路线

## Key Takeaways

OpenAI10月14日客户案例称Third Moment Research使用Codex、GPT-6系列及GPT-6.1 Sol运行1万个并发Agent，研究会话36–48小时；外层harness决定重试、终止或转人工，Daybreak用于环境安全测试。

其[官网](https://thirdmomentresearch.com/)（未知发布日期背景）提供按工作流改进的托管推理endpoint：采集轨迹、诊断、用户确认、评测与后训练/harness优化，再发布版本。新纳入跟踪的是既有公司，不宣称今日成立；官网日期未知。规模及效果均客户/供应商披露，无公开可比harness、成本或独立复现。

## Detailed Notes

OpenAI案例主文及Third Moment官网全部可见产品流程；未独立验证并发、收益、融资或法定注册主体。 本次新增已与已发布页和显式草稿检索查重。

## Evidence

[原始来源](https://openai.com/index/third-moment-research)。原文路径、URL、版本hash、采集时间、日期口径及定位见元数据。reported与source-checked分别记录，均不代表独立复现。

## Questions Raised

判断：专业工作流的失败轨迹和评测闭环可能形成区别于通用MaaS的服务壁垒，观测、隔离和调度基础设施受益。高token投入和人工确认可能限制单位经济，万Agent规模也不等于万份有效研究。观察付费客户、可复核改进、任务成本与人工复核量。
