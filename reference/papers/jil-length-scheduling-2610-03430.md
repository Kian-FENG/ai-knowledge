---
id: paper-jil-length-scheduling-2610-03430
title: JIL：输出长度预测可能成为请求调度的攻击面
type: paper
domain:
- infra
- models
lifecycle: published
tags:
- scheduling
- security
created: '2026-10-06'
updated: '2026-10-06'
summary: arXiv v1 于10月2日15:12:43 UTC 提交，出现在10月5日 cs.AI 近期公告组；本条按公告日纳入，具体公告时刻未知，窗口边界不确定，前一期无同事件。
evidence_kind: reported
verification: source-checked
sources:
- https://arxiv.org/abs/2610.03430
related:
- paper-shared-kv-cache-provenance-2609-38706
aliases: []
source: raw/2026-10-06/1272bc7de6ceb8f2c0bad11668e141ae88e4a7b1f87dc951959f6b05f3019ba5.txt
url: https://arxiv.org/abs/2610.03430
published_at: '2026-10-02T15:12:43+00:00'
source_category: paper
last_verified: '2026-10-06'
raw_path: raw/2026-10-06/1272bc7de6ceb8f2c0bad11668e141ae88e4a7b1f87dc951959f6b05f3019ba5.txt
sha256: 1272bc7de6ceb8f2c0bad11668e141ae88e4a7b1f87dc951959f6b05f3019ba5
fetched_at: '2026-10-06T01:14:55.749358+00:00'
reading_scope: arXiv v1 摘要、提交历史及cs.AI近期列表10月5日公告分组；未读24页全文、图表、实现或实验设置。不采用性能数值。
verification_note: 已阅读并核对声明范围与出处：arXiv:2610.03430v1 Abstract与Submission history；cs.AI
  recent Mon,5 Oct分组第17条。；只读摘要、提交历史和公告列表；未读24页全文、六幅图或实验配置，作者结果 reported，未复现。
evidence:
- source: raw/2026-10-06/1272bc7de6ceb8f2c0bad11668e141ae88e4a7b1f87dc951959f6b05f3019ba5.txt
  locator: arXiv:2610.03430v1 Abstract与Submission history；cs.AI recent Mon,5 Oct分组第17条。
  version: sha256:1272bc7de6ceb8f2c0bad11668e141ae88e4a7b1f87dc951959f6b05f3019ba5
announced_at: '2026-10-05'
date_basis: announced
version: arXiv:2610.03430v1
date_precision: date-only
date_timezone: unknown
reviewed_by: Codex
reviewed_at: '2026-10-06'
reviewed_content_sha256: b6f130b629b5dc6df4acdd02cc75a0acb054f9153841916f1b663784f255900d
---

# JIL：输出长度预测可能成为请求调度的攻击面

## Problem and Method

用对抗后缀操纵输出长度预测，让基于预测长度的调度给攻击请求更高优先级；以 TRAIL 为案例。

## Results and Conditions

作者摘要称两数据集、四模型及多种请求/部署配置；具体硬件、精度、并行、负载、软件版本与基线尚未阅读全文确认，不提取性能数值。

arXiv v1 于10月2日15:12:43 UTC 提交，出现在10月5日 cs.AI 近期公告组；本条按公告日纳入，具体公告时刻未知，窗口边界不确定，前一期无同事件。

## Evidence

arXiv:2610.03430v1 Abstract与Submission history；cs.AI recent Mon,5 Oct分组第17条。

[原始摘要页](https://arxiv.org/abs/2610.03430)；[公告列表](https://arxiv.org/list/cs.AI/recent)。版本、hash和raw路径见元数据。

## Limitations and Implications

只读摘要、提交历史和公告列表；未读24页全文、六幅图或实验配置，作者结果 reported，未复现。

判断（derived）：服务调度如果把可被提示词影响的预测信号用于资源分配，就需要同时考虑吞吐与公平性，多租户服务可能受影响。反例是其他调度器、预测模型和防御配置未必存在相同效果。后续阅读具体模型/硬件/负载/harness，并验证分档的效率代价；不能推断所有 vLLM 或生产服务存在漏洞。
