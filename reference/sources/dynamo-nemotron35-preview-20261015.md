---
id: source-dynamo-nemotron35-preview-20261015
title: Dynamo提供Nemotron Super VL实验配方，尚非QA生产版本
type: source
domain:
- infra
- models
lifecycle: published
tags:
- daily-research
created: '2026-10-15'
updated: '2026-10-15'
summary: Dynamo v1.6.0-nemotron-3.5-super-vl-dev.1（tip5f601db）加入Nemotron3.5 Super
  VL的vLLM与TensorRT-LLM实验支持；明确非QA门禁、非生产推荐。配方以NVFP4权重、FP8 KV、MTP、会话亲和及最长1M上下文组织部署。
evidence_kind: reported
verification: source-checked
sources:
- https://github.com/ai-dynamo/dynamo/releases/tag/v1.6.0-nemotron-3.5-super-vl-dev.1
related: []
aliases: []
source: raw/2026-10-16/2d23cacd2bd2feeb27bdce05e071266b911bdd70b7699322953042e526b326e8.body
url: https://github.com/ai-dynamo/dynamo/releases/tag/v1.6.0-nemotron-3.5-super-vl-dev.1
published_at: null
source_category: release
raw_path: raw/2026-10-16/2d23cacd2bd2feeb27bdce05e071266b911bdd70b7699322953042e526b326e8.body
sha256: 2d23cacd2bd2feeb27bdce05e071266b911bdd70b7699322953042e526b326e8
fetched_at: '2026-10-16T01:03:07.954725+00:00'
source_updated_at: '2026-10-15T22:09:49+00:00'
announced_at: null
date_precision: timestamp
reading_scope: 官方Atom完整release，Summary / versions / recipes / Known Issues；无部署实验。
retrieval_method: feed-content
evidence:
- source: raw/2026-10-16/2d23cacd2bd2feeb27bdce05e071266b911bdd70b7699322953042e526b326e8.body
  locator: 官方Atom完整release，Summary / versions / recipes / Known Issues；无部署实验。
  version: sha256:2d23cacd2bd2feeb27bdce05e071266b911bdd70b7699322953042e526b326e8
last_verified: '2026-10-15'
verification_note: Agent已阅读所列范围并逐项核对事实与来源支持关系；公司/作者及媒体陈述为reported，没有独立审计、账户验证或实验复现。
reviewed_by: Codex
reviewed_at: '2026-10-16'
reviewed_content_sha256: eea04361ec763b0d54bb26653cb2cc87796a0517eae14a7141613a0dd5d40a1d
---

# Dynamo提供Nemotron Super VL实验配方，尚非QA生产版本

## Key Takeaways

Dynamo v1.6.0-nemotron-3.5-super-vl-dev.1（tip5f601db）加入Nemotron3.5 Super VL的vLLM与TensorRT-LLM实验支持；明确非QA门禁、非生产推荐。配方以NVFP4权重、FP8 KV、MTP、会话亲和及最长1M上下文组织部署。

相对昨日GLM/SGLang快照，新增不同模型及后端。vLLM基于cu134 nightly bb87d227，TensorRT-LLM1.3.0rc29/CUDA13.1，后者配方仅覆盖B200。VR200公布结果使用合成MTP接受长度，配方默认自然接受；未把其配置清单当通用实测性能。

## Detailed Notes

官方Atom完整release，Summary / versions / recipes / Known Issues；无部署实验。 已检索published及显式草稿，并按URL/hash查重；这是本期所列增量。

## Evidence

[原始来源](https://github.com/ai-dynamo/dynamo/releases/tag/v1.6.0-nemotron-3.5-super-vl-dev.1)；归档 `raw/2026-10-16/2d23cacd2bd2feeb27bdce05e071266b911bdd70b7699322953042e526b326e8.body`，sha256 `2d23cacd2bd2feeb27bdce05e071266b911bdd70b7699322953042e526b326e8`。

reported与source-checked分别表示陈述性质和支持关系核对，审核发布不提高为独立复现。

## Questions Raised

判断：混合模型落地需要同时处理状态恢复、缓存转移与路由；配方降低初试成本，但成熟度决定运营风险。反例是自然接受率和多模态正确性削弱收益；观察稳定release、真实轨迹与完整并发测试。
