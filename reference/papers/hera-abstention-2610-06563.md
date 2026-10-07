---
id: paper-hera-abstention-2610-06563
title: HERA：让 harness 与任务环境共同演进，学习何时停止
type: paper
domain:
- models
- products
lifecycle: published
tags:
- daily-research
created: '2026-10-07'
updated: '2026-10-07'
summary: HERA 通过受控环境变更，把同一请求构造成可完成与不可完成的配对任务；执行失败诊断同时驱动 harness 调整和新环境生成，基础执行模型保持固定。
evidence_kind: reported
verification: source-checked
sources:
- https://arxiv.org/abs/2610.06563
related:
- paper-recursive-harness-synthesis-2610-03548
aliases: []
source: raw/2026-10-07/cc93ddb4b610b68eaa45a9c33891764ead5f0420bb731d95ca4b6cc13cd6a6b0.txt
url: https://arxiv.org/abs/2610.06563
published_at: '2026-10-05T15:49:12+00:00'
source_category: paper
raw_path: raw/2026-10-07/cc93ddb4b610b68eaa45a9c33891764ead5f0420bb731d95ca4b6cc13cd6a6b0.txt
sha256: cc93ddb4b610b68eaa45a9c33891764ead5f0420bb731d95ca4b6cc13cd6a6b0
fetched_at: '2026-10-07T01:16:05.110823+00:00'
last_verified: '2026-10-07'
reading_scope: 已读v1摘要、提交历史、引言部分和方法§3；未读完整实验、附录、代码或复现实验，不采用效果或成本数字。cs.AI公告日10月6日仅到日，提交2026-10-05T15:49:12Z不在本期；公告日窗口边界不确定。
verification_note: 已实际阅读并核对以下陈述与出处：arXiv v1 摘要/提交历史；HTML §3.1 Construction / §3.2
  Co-Evolution；cs.AI 10月6日公告第13条。与既有 RRSI/RSI 的增量在停止决策和环境–任务配对；未执行项目代码或验证作者成本结论。
evidence:
- source: raw/2026-10-07/cc93ddb4b610b68eaa45a9c33891764ead5f0420bb731d95ca4b6cc13cd6a6b0.txt
  locator: arXiv v1 摘要/提交历史；HTML §3.1 Construction / §3.2 Co-Evolution；cs.AI 10月6日公告第13条
  version: sha256:cc93ddb4b610b68eaa45a9c33891764ead5f0420bb731d95ca4b6cc13cd6a6b0
- source: raw/2026-10-07/29b5b4601d2ddc3a434e8bc0f889bde8d6aef03dc3ad8a01133c502c8bc66b90.txt
  locator: 'cs.AI recent: Tue, 6 Oct 2026；HEAR第9条、HERA第13条；各自摘要提交历史'
  version: sha256:29b5b4601d2ddc3a434e8bc0f889bde8d6aef03dc3ad8a01133c502c8bc66b90
announced_at: '2026-10-06'
submission_version: arXiv:2610.06563v1
reviewed_by: Codex
reviewed_at: '2026-10-07'
reviewed_content_sha256: 1f473d6efa0969d0278515354952bfbd2554a14545172dbc02d6c1319af53163
---

# HERA：让 harness 与任务环境共同演进，学习何时停止

## Problem and Method

HERA 通过受控环境变更，把同一请求构造成可完成与不可完成的配对任务；执行失败诊断同时驱动 harness 调整和新环境生成，基础执行模型保持固定。

已读方法包含独立 solver 验证、语义审查和 rescue 检查，以减少把仍可完成的任务错误标成不可完成；评估要求在可行任务行动、不可行任务停止。

v1 于 2026-10-05T15:49:12Z 提交，10 月 6 日列入 cs.AI 公告第13条。仅读摘要、引言部分与方法 §3，未完整审阅实验/附录；不采用摘要中的收益、跨模型排名或成本数字。公告日仅到日、窗口边界不确定。

## Results and Conditions

与既有 RRSI/RSI 的增量在停止决策和环境–任务配对；未执行项目代码或验证作者成本结论。

## Evidence

[原始来源](https://arxiv.org/abs/2610.06563)。定位：arXiv v1 摘要/提交历史；HTML §3.1 Construction / §3.2 Co-Evolution；cs.AI 10月6日公告第13条。原始路径、采集时间、版本和 hash 见元数据；source-checked 仅表示已核对所列有限陈述，不代表独立复现。

## Limitations and Implications

判断（derived）：企业 Agent 的价值还取决于识别缺失前提和停止无效操作，环境构造与失败反馈可能提升可靠性评估的区分度。自动生成的不可行标注仍可能漏掉替代路径，过度停止也会降低完成率；观察人工复核标签、可行任务误停率及跨业务迁移。

相关：

- [[reference/papers/recursive-harness-synthesis-2610-03548|paper-recursive-harness-synthesis-2610-03548]]
