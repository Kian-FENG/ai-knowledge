---
id: paper-target-regeneration-261029013
title: 推测解码论文：目标模型重生成基线会缩小草稿训练目标的增益
type: paper
domain:
- models
- infra
lifecycle: published
tags: []
created: '2026-10-24'
updated: '2026-10-23'
summary: arXiv 2610.29013v1初次投稿为10月21日00:26:37 UTC，官方RSS于10月22日00:00 EDT公告，属于本期；公告不等于当天初投。只读摘要及版本史。
evidence_kind: reported
verification: source-checked
sources:
- https://arxiv.org/abs/2610.29013
related: []
aliases: []
source: raw/2026-10-24/0a4646e22511cba4a6f5b72a6c4d7fd275a05c2b6f59f13bafe9d11fa28118a1.txt
url: https://arxiv.org/abs/2610.29013
published_at: '2026-10-21T00:26:37+00:00'
source_category: paper
last_verified: '2026-10-23'
verification_note: Agent阅读所列来源并核对有限结论；reported保留披露主体归因，derived是研究推导，未独立复现。
reading_scope: arXiv摘要、v1提交历史和已归档官方RSS公告字段已读；未读19页PDF、6图15表、代码或复现。
raw_path: raw/2026-10-24/0a4646e22511cba4a6f5b72a6c4d7fd275a05c2b6f59f13bafe9d11fa28118a1.txt
sha256: 0a4646e22511cba4a6f5b72a6c4d7fd275a05c2b6f59f13bafe9d11fa28118a1
fetched_at: '2026-10-23T22:08:48.740632+00:00'
evidence:
- source: raw/2026-10-24/0a4646e22511cba4a6f5b72a6c4d7fd275a05c2b6f59f13bafe9d11fa28118a1.txt
  locator: arXiv摘要、v1提交历史和已归档官方RSS公告字段已读；未读19页PDF、6图15表、代码或复现。
  version: sha256:0a4646e22511cba4a6f5b72a6c4d7fd275a05c2b6f59f13bafe9d11fa28118a1
date_precision: timestamp
announced_at: '2026-10-22T00:00:00-04:00'
version: arXiv:2610.29013v1
reviewed_by: Codex
reviewed_at: '2026-10-24'
reviewed_content_sha256: b47a18117af5d85ad0aa383512696f5d9740291ccfe04b3d0a9569ff0abba6ba
---

# 推测解码论文：目标模型重生成基线会缩小草稿训练目标的增益

## Problem and Method

arXiv 2610.29013v1初次投稿为10月21日00:26:37 UTC，官方RSS于10月22日00:00 EDT公告，属于本期；公告不等于当天初投。只读摘要及版本史。

## Results and Conditions

作者在同一语料四种版本上比较交叉熵、目标token蒸馏及验证存活位置门控；摘要报告目标贪心重生成后，蒸馏增益缩小、门控增益很小或消失，并在额外视觉与文本设置检查。未核模型版本、硬件、完整训练预算和harness，不采速度排名。

## Evidence

[原始来源](https://arxiv.org/abs/2610.29013)；原始版本 `raw/2026-10-24/0a4646e22511cba4a6f5b72a6c4d7fd275a05c2b6f59f13bafe9d11fa28118a1.txt`，SHA-256 `0a4646e22511cba4a6f5b72a6c4d7fd275a05c2b6f59f13bafe9d11fa28118a1`。

arXiv摘要、v1提交历史和已归档官方RSS公告字段已读；未读19页PDF、6图15表、代码或复现。

## Limitations and Implications

判断：评估草稿训练方法时，数据重写与训练长度可能解释部分收益，模型供应商和推理框架需要更强基线。反例是其他目标或在线分布仍有增益。观察目标重生成基线、等监督长度、训练成本及端到端收益。
