---
id: source-mistral-large-4-preview-20261006
title: Mistral Large 4 进入 API 公开预览，权重仍待月底交付
type: source
domain:
- models
- products
lifecycle: published
tags:
- daily-research
created: '2026-10-07'
updated: '2026-10-07'
summary: Mistral Large 4 已在 Mistral Studio 提供 API 公开预览；官方计划月底发布权重，当前不能据此称为已开放权重或已确认最终许可。预览期间强化学习仍继续。
evidence_kind: reported
verification: source-checked
sources:
- https://mistral.ai/news/mistral-large-4/
related:
- source-reflection-beam-preview-20261005
aliases: []
source: raw/2026-10-07/813a8fcedf3017162789f813027295bba7cfa8750303d4ca9cfa602cf10d0be5.body
url: https://mistral.ai/news/mistral-large-4/
published_at: '2026-10-06T12:00:27+00:00'
source_category: official
raw_path: raw/2026-10-07/813a8fcedf3017162789f813027295bba7cfa8750303d4ca9cfa602cf10d0be5.body
sha256: 813a8fcedf3017162789f813027295bba7cfa8750303d4ca9cfa602cf10d0be5
fetched_at: '2026-10-07T01:10:29.673093+00:00'
last_verified: '2026-10-07'
reading_scope: 真实浏览器和 HTTP 正文均已读取；未核实最终权重、模型卡许可、第三方全部评测 harness 或硬件利用率。不采用跨口径领先排名。
verification_note: 已实际阅读并核对以下陈述与出处：官方主文公开预览/月底权重说明；模型参数与欧洲训练基础设施；RL environment 小节。真实浏览器和
  HTTP 正文均已读取；未核实最终权重、模型卡许可、第三方全部评测 harness 或硬件利用率。不采用跨口径领先排名。
evidence:
- source: raw/2026-10-07/813a8fcedf3017162789f813027295bba7cfa8750303d4ca9cfa602cf10d0be5.body
  locator: 官方主文公开预览/月底权重说明；模型参数与欧洲训练基础设施；RL environment 小节
  version: sha256:813a8fcedf3017162789f813027295bba7cfa8750303d4ca9cfa602cf10d0be5
reviewed_by: Codex
reviewed_at: '2026-10-07'
reviewed_content_sha256: d0ebd3903c3cb8799fb62b493c2c90f7cefcc9382e901fbbd293fc7c9a6135af
---

# Mistral Large 4 进入 API 公开预览，权重仍待月底交付

## Key Takeaways

Mistral Large 4 已在 Mistral Studio 提供 API 公开预览；官方计划月底发布权重，当前不能据此称为已开放权重或已确认最终许可。预览期间强化学习仍继续。

公司披露模型总参数约 1T、激活约 49B，原生多模态，训练使用自有欧洲数据中心的 3,800 个 NVIDIA Grace Blackwell GPU；这属于公司披露，不是本项目实测供给或成本。

官方介绍可组合强化学习环境、工具与奖励接口。相对前期 Beam 预览，新增一个独立模型供给选择；两者的评测、计算预算和交付状态不能混成统一排名。

## Detailed Notes

真实浏览器和 HTTP 正文均已读取；未核实最终权重、模型卡许可、第三方全部评测 harness 或硬件利用率。不采用跨口径领先排名。

## Evidence

[原始来源](https://mistral.ai/news/mistral-large-4/)。定位：官方主文公开预览/月底权重说明；模型参数与欧洲训练基础设施；RL environment 小节。原始路径、采集时间、版本和 hash 见元数据；source-checked 仅表示已核对所列有限陈述，不代表独立复现。

## Questions Raised

判断（derived）：预览 API 可先验证需求，后续权重交付才可能扩大自部署和区域主权选择，对封闭 API 厂商构成潜在竞争。若权重延迟或部署成本过高，API 预览并不改善私有化供给；观察实际权重、许可、量化支持与相同任务的总成本。

相关：

- [[reference/sources/reflection-beam-preview-20261005|source-reflection-beam-preview-20261005]]
