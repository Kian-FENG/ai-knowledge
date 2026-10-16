---
id: source-nemotron35-super-vl-20261015
title: NVIDIA发布Nemotron 3.5 Super VL，强调多模态专用Agent定制
type: source
domain:
- models
- infra
lifecycle: published
tags:
- daily-research
created: '2026-10-15'
updated: '2026-10-15'
summary: NVIDIA 10月15日介绍120B总参数/12B激活的多模态MoE，支持文本、图像、文档和视频理解及工具调用；发布基础、后训练、NVFP4检查点，配套数据与训练资源。
evidence_kind: reported
verification: source-checked
sources:
- https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/
related: []
aliases: []
source: raw/2026-10-16/bed3b5b7e11a3d7128346829f8ec5ecb56c07cc53b36596d2a58ee17e09a40d0.body
url: https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/
published_at: '2026-10-15T18:01:00+00:00'
source_category: official
raw_path: raw/2026-10-16/bed3b5b7e11a3d7128346829f8ec5ecb56c07cc53b36596d2a58ee17e09a40d0.body
sha256: bed3b5b7e11a3d7128346829f8ec5ecb56c07cc53b36596d2a58ee17e09a40d0
fetched_at: '2026-10-16T01:11:21.665027+00:00'
source_updated_at: null
announced_at: null
date_precision: timestamp
reading_scope: 官方技术博客全文，Architecture / customization / mixed precision / release；未复现性能。
retrieval_method: full-text
evidence:
- source: raw/2026-10-16/bed3b5b7e11a3d7128346829f8ec5ecb56c07cc53b36596d2a58ee17e09a40d0.body
  locator: 官方技术博客全文，Architecture / customization / mixed precision / release；未复现性能。
  version: sha256:bed3b5b7e11a3d7128346829f8ec5ecb56c07cc53b36596d2a58ee17e09a40d0
last_verified: '2026-10-15'
verification_note: Agent已阅读所列范围并逐项核对事实与来源支持关系；公司/作者及媒体陈述为reported，没有独立审计、账户验证或实验复现。
reviewed_by: Codex
reviewed_at: '2026-10-16'
reviewed_content_sha256: 5567fc156d338767ab22931bd462edaf28426b110e4adb2fee5f1bbd1d4a761c
---

# NVIDIA发布Nemotron 3.5 Super VL，强调多模态专用Agent定制

## Key Takeaways

NVIDIA 10月15日介绍120B总参数/12B激活的多模态MoE，支持文本、图像、文档和视频理解及工具调用；发布基础、后训练、NVFP4检查点，配套数据与训练资源。

新增是Super VL模型和定制生态；公司说明NVFP4在Blackwell使用4位权重/激活，其他平台可为4位权重/16位激活。客户成本/延迟倍数、排行榜及未来效果未具备本项目完整可比harness，均未用于排名；已读技术博客，未逐份读取模型卡/许可/技术报告或验证服务商交付。

## Detailed Notes

官方技术博客全文，Architecture / customization / mixed precision / release；未复现性能。 已检索published及显式草稿，并按URL/hash查重；这是本期所列增量。

## Evidence

[原始来源](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/)；归档 `raw/2026-10-16/bed3b5b7e11a3d7128346829f8ec5ecb56c07cc53b36596d2a58ee17e09a40d0.body`，sha256 `bed3b5b7e11a3d7128346829f8ec5ecb56c07cc53b36596d2a58ee17e09a40d0`。

reported与source-checked分别表示陈述性质和支持关系核对，审核发布不提高为独立复现。

## Questions Raised

判断：统一视觉与工具调用减少多模型交接，适合组织专用Agent；训练数据、策略和部署支撑仍决定成本。反例是量化误差或工具行为回归；观察同一工作流成功率、后训练投入与完整任务账单。
