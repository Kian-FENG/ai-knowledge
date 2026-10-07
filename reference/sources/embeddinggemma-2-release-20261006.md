---
id: source-embeddinggemma-2-release-20261006
title: EmbeddingGemma 2 发布多模态开放嵌入模型，支持端侧检索
type: source
domain:
- models
- products
lifecycle: published
tags:
- daily-research
created: '2026-10-07'
updated: '2026-10-07'
summary: Google 发布 740M 参数的 EmbeddingGemma 2，支持文本、代码、图像、视频和音频嵌入；官方称使用 Apache 2.0 许可，Hugging
  Face 和 Kaggle 权重已可获取，Model Garden 支持仍是后续计划。
evidence_kind: reported
verification: source-checked
sources:
- https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/
related: []
aliases: []
source: raw/2026-10-07/6d6f2207b2a86ae5bf8483ff520669fd238c7fd6ded98e0b6eeffa6aa5f91e1e.body
url: https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/
published_at: '2026-10-06T16:00:00+00:00'
source_category: official
raw_path: raw/2026-10-07/6d6f2207b2a86ae5bf8483ff520669fd238c7fd6ded98e0b6eeffa6aa5f91e1e.body
sha256: 6d6f2207b2a86ae5bf8483ff520669fd238c7fd6ded98e0b6eeffa6aa5f91e1e
fetched_at: '2026-10-07T01:10:29.765339+00:00'
last_verified: '2026-10-07'
reading_scope: ' 日期已核对抓取HTML的JSON-LD datePublished/dateModified；原19:57:04为发现候选时间口径，不作发布时间。'
verification_note: 已实际阅读并核对以下陈述与出处：主文多模态/模块参数、Matryoshka和端侧说明、许可与获取渠道。已读公告正文；模型卡、全部框架支持和实际端侧性能未逐项核验，所有数字保留厂商归因。
  原始HTML JSON-LD核对datePublished=16:00Z、dateModified=16:43:55.153470Z，修正发现候选时刻19:57:04Z。
evidence:
- source: raw/2026-10-07/6d6f2207b2a86ae5bf8483ff520669fd238c7fd6ded98e0b6eeffa6aa5f91e1e.body
  locator: 主文多模态/模块参数、Matryoshka和端侧说明、许可与获取渠道
  version: sha256:6d6f2207b2a86ae5bf8483ff520669fd238c7fd6ded98e0b6eeffa6aa5f91e1e
reviewed_by: Codex
reviewed_at: '2026-10-07'
reviewed_content_sha256: b3090c802284ece8ee76b0901e53a325841720e206fb4d1459103c0f750b71f3
source_updated_at: '2026-10-06T16:43:55.153470+00:00'
---

# EmbeddingGemma 2 发布多模态开放嵌入模型，支持端侧检索

## Key Takeaways

Google 发布 740M 参数的 EmbeddingGemma 2，支持文本、代码、图像、视频和音频嵌入；官方称使用 Apache 2.0 许可，Hugging Face 和 Kaggle 权重已可获取，Model Garden 支持仍是后续计划。

模型基于 Gemma 4，模块分为 270M 文本、170M 视觉、300M 音频；支持 8K 输入和 768 维嵌入，通过 Matryoshka Representation Learning 可截为 512/256/128 维。

相对文字嵌入，新增多模态统一检索与可裁剪模块。公告 Pixel 设备的量化权重内存数字不等于全流程峰值内存；本次不据此比较端侧时延或耗电。

## Detailed Notes

已读公告正文；模型卡、全部框架支持和实际端侧性能未逐项核验，所有数字保留厂商归因。

## Evidence

[原始来源](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/)。定位：主文多模态/模块参数、Matryoshka和端侧说明、许可与获取渠道。原始路径、采集时间、版本和 hash 见元数据；source-checked 仅表示已核对所列有限陈述，不代表独立复现。

## Questions Raised

判断（derived）：本地多模态索引有机会让个人助手检索私有媒体并减少上传需求，端侧设备与本地检索应用受益。下游生成若仍走云端，嵌入在本地并不保证整个流程数据不出设备；观察量化后召回质量、功耗、峰值内存与产品权限。
