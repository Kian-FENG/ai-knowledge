---
id: source-gemma-singapore-scam-20261014
title: DeepMind与新加坡GovTech微调端侧Gemma反诈模型，应用分阶段推出
type: source
domain:
- models
- products
lifecycle: published
tags:
- daily-research
created: '2026-10-14'
updated: '2026-10-14'
summary: DeepMind10月14日披露与GovTech微调Gemma，先以轻量分类器筛查，再由模型分析多轮对话；推理在设备上，应用需用户同意，推出将分阶段进行。
evidence_kind: reported
verification: source-checked
sources:
- https://deepmind.google/blog/on-device-ai-scam-detection-mddi/
related: []
aliases: []
source: raw/2026-10-15/78bd4a8b27b1a9c9d93f2142da22c8fd2ae4292e4bda153a44bc49f4d8bc0de2.txt
url: https://deepmind.google/blog/on-device-ai-scam-detection-mddi/
published_at: '2026-10-14T02:00:14+00:00'
source_category: official
raw_path: raw/2026-10-15/78bd4a8b27b1a9c9d93f2142da22c8fd2ae4292e4bda153a44bc49f4d8bc0de2.txt
sha256: 78bd4a8b27b1a9c9d93f2142da22c8fd2ae4292e4bda153a44bc49f4d8bc0de2
fetched_at: '2026-10-15T01:11:34.627934+00:00'
source_updated_at: null
announced_at: null
date_precision: timestamp
reading_scope: 官方主文On-device AI、Under the hood和Built on strict governance；未读取底层模型卡、测试集或独立测量。
retrieval_method: agent-source-extract
evidence:
- source: raw/2026-10-15/78bd4a8b27b1a9c9d93f2142da22c8fd2ae4292e4bda153a44bc49f4d8bc0de2.txt
  locator: 官方主文On-device AI、Under the hood和Built on strict governance；未读取底层模型卡、测试集或独立测量。
  version: sha256:78bd4a8b27b1a9c9d93f2142da22c8fd2ae4292e4bda153a44bc49f4d8bc0de2
- source: raw/2026-10-15/6091a594251823ff9e63fb24aca7a538061d2ad082c5298de8dc3078a6b1862c.body
  locator: 原始RSS/Atom对应URL条目及发布时间或公告日；正文结论以本次主文快照为准。
  version: sha256:6091a594251823ff9e63fb24aca7a538061d2ad082c5298de8dc3078a6b1862c
last_verified: '2026-10-14'
verification_note: Agent已阅读所列范围并核对有限陈述与来源的支持关系；公司/作者披露未独立审计或复现。
reviewed_by: Codex
reviewed_at: '2026-10-15'
reviewed_content_sha256: 7816e46128103b2e2b5c04e24d59d223a2d781b13cb69ea34e45a8892e7f3c09
---

# DeepMind与新加坡GovTech微调端侧Gemma反诈模型，应用分阶段推出

## Key Takeaways

DeepMind10月14日披露与GovTech微调Gemma，先以轻量分类器筛查，再由模型分析多轮对话；推理在设备上，应用需用户同意，推出将分阶段进行。

训练使用匿名化诈骗报告及情报数据，在GovTech管理的GCP环境内进行。相对通用安全能力，新增本地诈骗语境和端侧两阶段管线；未给出具体Gemma版本、模型大小、误报率、功耗或普遍可用应用清单。

## Detailed Notes

官方主文On-device AI、Under the hood和Built on strict governance；未读取底层模型卡、测试集或独立测量。 本次新增已与已发布页和显式草稿检索查重。

## Evidence

[原始来源](https://deepmind.google/blog/on-device-ai-scam-detection-mddi/)。原文路径、URL、版本hash、采集时间、日期口径及定位见元数据。reported与source-checked分别记录，均不代表独立复现。

## Questions Raised

判断：先筛查再调用模型可在隐私、功耗与检测深度间取舍，有利于端侧模型和本地数据合作。误报、对话访问权限和机型覆盖可能限制效果。观察实际应用交付、授权率、分语种漏报及电池消耗。
