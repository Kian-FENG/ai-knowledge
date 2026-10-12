---
id: source-odyssey3-preview-20261008
title: Odyssey-3研究预览：交互生成与闭环控制证据分开
type: source
domain:
- models
lifecycle: published
tags: []
created: '2026-10-12'
updated: '2026-10-12'
summary: 10月8日官方研究预览；自回归扩散处理视觉与控制，评分预算和机器人适用性限制外推。
evidence_kind: reported
verification: source-checked
sources:
- https://odyssey.systems/meet-odyssey-3
related: []
aliases: []
source: https://odyssey.systems/meet-odyssey-3
url: https://odyssey.systems/meet-odyssey-3
published_at: '2026-10-08'
source_category: official
date_precision: date-only
raw_path: raw/2026-10-12/ee7c8e21f8e5502fdd5fd8368caf8f6e9e9f5b87da1af967b94160dce7a5ebc6.txt
sha256: ee7c8e21f8e5502fdd5fd8368caf8f6e9e9f5b87da1af967b94160dce7a5ebc6
fetched_at: '2026-10-12T01:11:28.739274+00:00'
last_verified: '2026-10-11'
verification_note: Agent已阅读所列范围并核对支持关系；仅确认来源所述和归因，不等于独立验证、实测或账单审计。
reading_scope: 主文日期、模型方法、训练/蒸馏、research preview、评分口径及Flexion段；未取原始实验数据、未复现。
evidence:
- source: raw/2026-10-12/ee7c8e21f8e5502fdd5fd8368caf8f6e9e9f5b87da1af967b94160dce7a5ebc6.txt
  locator: 主文日期、模型方法、训练/蒸馏、research preview、评分口径及Flexion段；未取原始实验数据、未复现。
  version: sha256:ee7c8e21f8e5502fdd5fd8368caf8f6e9e9f5b87da1af967b94160dce7a5ebc6
reviewed_by: Codex
reviewed_at: '2026-10-12'
reviewed_content_sha256: 1eabc0c41a26325e0d8771c694a0770f7f9866c24d9bdb7dfd58ee452839af6b
---

# Odyssey-3研究预览：交互生成与闭环控制证据分开

## Key Takeaways

Odyssey-3以视觉观测和控制为条件生成后续观测，官方描述自回归扩散Transformer及视频、游戏输入、刚体模拟训练。后训练蒸馏以实现少步实时生成。Flash为公开研究预览，Pro及机器人API需联系；未确认开放权重或许可证。

## Detailed Notes

公告为2026-10-08，仅到日期；10月11日媒体再次介绍不构成本期首发。已读方法、评分说明与局限。66.1物理评分用best-of-8和一次选择，基础版本为四次平均；成本假设MI355X每GPU小时USD1且不含prompt rewriting，口径不一不排名。WorldMark为公司自评；Flexion合作演示不等价真实机器人控制部署证据。

## Evidence

来源URL、不可覆盖raw版本、hash、采集时间、定位及阅读范围见元数据。浏览材料为明确标注的有限事实摘录；IT之家保留原RSS响应。reported与source-checked独立，非measured/replicated。

## Questions Raised

可交互控制的误差累积、机器人策略适配、分发/许可、实际FPS和部署硬件、预览转正式可用。
