---
id: paper-recursive-harness-synthesis-2610-03548
title: 任务与 harness 共同演进：推理数据合成的自我改进研究
type: paper
domain:
- models
- infra
lifecycle: published
tags:
- data-synthesis
- harness
created: '2026-10-06'
updated: '2026-10-06'
summary: arXiv v1 于10月2日16:30:15 UTC 提交，出现在10月5日 cs.AI 公告组；按公告日纳入，具体时刻未知，边界不确定，与前期去重无同事件。
evidence_kind: reported
verification: source-checked
sources:
- https://arxiv.org/abs/2610.03548
related:
- paper-rrsi-agent-harnesses-2609-24972
aliases: []
source: raw/2026-10-06/22bc08a0ead1f6cb890dc4914980cf682c4a7fc8e192dcadf36264fe3451fe87.txt
url: https://arxiv.org/abs/2610.03548
published_at: '2026-10-02T16:30:15+00:00'
source_category: paper
last_verified: '2026-10-06'
raw_path: raw/2026-10-06/22bc08a0ead1f6cb890dc4914980cf682c4a7fc8e192dcadf36264fe3451fe87.txt
sha256: 22bc08a0ead1f6cb890dc4914980cf682c4a7fc8e192dcadf36264fe3451fe87
fetched_at: '2026-10-06T01:14:55.838145+00:00'
reading_scope: arXiv v1 摘要、提交历史及cs.AI近期列表10月5日公告分组；未读全文、基准版本或实验harness。不采用成绩排名。
verification_note: 已阅读并核对声明范围与出处：arXiv:2610.03548v1 Abstract与Submission history；cs.AI
  recent Mon,5 Oct分组第12条。；只读摘要、提交历史和公告列表；模型版本、APEX版本、mean-16预算与全文实验未核实，不采用成绩排名。
evidence:
- source: raw/2026-10-06/22bc08a0ead1f6cb890dc4914980cf682c4a7fc8e192dcadf36264fe3451fe87.txt
  locator: arXiv:2610.03548v1 Abstract与Submission history；cs.AI recent Mon,5 Oct分组第12条。
  version: sha256:22bc08a0ead1f6cb890dc4914980cf682c4a7fc8e192dcadf36264fe3451fe87
announced_at: '2026-10-05'
date_basis: announced
version: arXiv:2610.03548v1
date_precision: date-only
date_timezone: unknown
reviewed_by: Codex
reviewed_at: '2026-10-06'
reviewed_content_sha256: d1bd24d81dc132fab496f069daf246efb0d1f9269e8529759d0f9bdb723a613b
---

# 任务与 harness 共同演进：推理数据合成的自我改进研究

## Problem and Method

在线失败→可复用技能；批次后修订技能、提示和工作流，模型权重及验证标准固定，以更难有效任务及有限成本增长作为修订条件。

## Results and Conditions

作者摘要报告数学、代码、科学任务，以及下游 SFT/GRPO 收益；尚未阅读完整实验harness/模型版本/评测版本，定量结果不用于比较。

arXiv v1 于10月2日16:30:15 UTC 提交，出现在10月5日 cs.AI 公告组；按公告日纳入，具体时刻未知，边界不确定，与前期去重无同事件。

## Evidence

arXiv:2610.03548v1 Abstract与Submission history；cs.AI recent Mon,5 Oct分组第12条。

[原始摘要页](https://arxiv.org/abs/2610.03548)；[公告列表](https://arxiv.org/list/cs.AI/recent)。版本、hash和raw路径见元数据。

## Limitations and Implications

只读摘要、提交历史和公告列表；模型版本、APEX版本、mean-16预算与全文实验未核实，不采用成绩排名。

判断（derived）：推理数据价值可能来自可改进的生成流程，而不仅是模型规模，数据供应商和训练团队有机会积累工作流资产。反例是难度增长可能只是针对固定求解器，训练收益未必跨基准迁移。观察验证防泄漏、迭代预算、独立测试集和下游迁移效果；摘要成绩缺完整harness，故不作模型排名，也不与既有 RRSI 混为同一论文。
