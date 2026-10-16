---
id: source-visko-tpu-case-20261015
title: 新增跟踪Visko：Orbis实时世界模型披露TPU部署案例
type: source
domain:
- companies
- infra
lifecycle: published
tags:
- daily-research
created: '2026-10-15'
updated: '2026-10-15'
summary: Visko CEO与Google Cloud工程师10月15日联合介绍Orbis：文本/图像起始、可持续输入提示改变视频流；公开demo为9月1日，TPU合作始于8月，所述30天部署是历史过程，本期新增是技术案例披露。官网核对Orbis/Morphe/Kinesis归属及Visko
  Platform, Inc.页脚，法定注册与融资未核。
evidence_kind: reported
verification: source-checked
sources:
- https://cloud.google.com/blog/products/media-entertainment/how-visko-streams-real-time-world-models-on-google-cloud-tpus/
related: []
aliases: []
source: raw/2026-10-16/f7095b910e01e0aa98af83be2b39c8367882e5924043d0dd98fe5a910f100bb0.body
url: https://cloud.google.com/blog/products/media-entertainment/how-visko-streams-real-time-world-models-on-google-cloud-tpus/
published_at: '2026-10-15T16:00:00+00:00'
source_category: official
raw_path: raw/2026-10-16/f7095b910e01e0aa98af83be2b39c8367882e5924043d0dd98fe5a910f100bb0.body
sha256: f7095b910e01e0aa98af83be2b39c8367882e5924043d0dd98fe5a910f100bb0
fetched_at: '2026-10-16T01:11:21.873676+00:00'
source_updated_at: null
announced_at: null
date_precision: timestamp
reading_scope: Google Cloud案例全文与Visko官网可见产品；厂商联合案例，未复现。
retrieval_method: full-text
evidence:
- source: raw/2026-10-16/f7095b910e01e0aa98af83be2b39c8367882e5924043d0dd98fe5a910f100bb0.body
  locator: Google Cloud案例全文与Visko官网可见产品；厂商联合案例，未复现。
  version: sha256:f7095b910e01e0aa98af83be2b39c8367882e5924043d0dd98fe5a910f100bb0
last_verified: '2026-10-15'
verification_note: Agent已阅读所列范围并逐项核对事实与来源支持关系；公司/作者及媒体陈述为reported，没有独立审计、账户验证或实验复现。
reviewed_by: Codex
reviewed_at: '2026-10-16'
reviewed_content_sha256: 49886605fdb42d3e0e7d566028748863078fe04a75ab88004d4a4589161e7fb4
---

# 新增跟踪Visko：Orbis实时世界模型披露TPU部署案例

## Key Takeaways

Visko CEO与Google Cloud工程师10月15日联合介绍Orbis：文本/图像起始、可持续输入提示改变视频流；公开demo为9月1日，TPU合作始于8月，所述30天部署是历史过程，本期新增是技术案例披露。官网核对Orbis/Morphe/Kinesis归属及Visko Platform, Inc.页脚，法定注册与融资未核。

案例报告BF16、batch1、单TPU slice，视频1664×936/18fps并配同步音频，通过Ulysses上下文并行及局部JAX改写实现约1.07倍播放速度。TPU代际、切片规格、软件commit和完整负载未给齐；未将5.8倍音频局部加速当全链路收益，也不做GPU/TPU成本排名。

## Detailed Notes

Google Cloud案例全文与Visko官网可见产品；厂商联合案例，未复现。 已检索published及显式草稿，并按URL/hash查重；这是本期所列增量。

## Evidence

[原始来源](https://cloud.google.com/blog/products/media-entertainment/how-visko-streams-real-time-world-models-on-google-cloud-tpus/)；归档 `raw/2026-10-16/f7095b910e01e0aa98af83be2b39c8367882e5924043d0dd98fe5a910f100bb0.body`，sha256 `f7095b910e01e0aa98af83be2b39c8367882e5924043d0dd98fe5a910f100bb0`。

reported与source-checked分别表示陈述性质和支持关系核对，审核发布不提高为独立复现。

## Questions Raised

判断：持续交互视频把供给瓶颈转为逐块截止时间与长会话稳定性，云端协同优化服务可能受益。反例是约7%余量不足抵抗抖动、多人并发或网络开销；观察长会话卡顿、并发SLO、单位会话成本与真实付费。
