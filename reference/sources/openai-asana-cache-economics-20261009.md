---
id: source-openai-asana-cache-economics-20261009
title: Asana 案例拆解浏览 Agent 的缓存与模型成本
type: source
domain:
- products
- infra
lifecycle: published
tags:
- daily-research
created: '2026-10-10'
updated: '2026-10-10'
summary: 相对昨日模型档位和任务预算，本期增量是缓存策略的任务级案例：144次运行，4模型×2历史预算×6策略×3重复；120K/480K是字符，任务为公共演示目录的32本书×6字段。
evidence_kind: reported
verification: source-checked
sources:
- https://openai.com/index/asana-browser-agent/
related: []
aliases: []
source: raw/2026-10-10/63f6c259189519ff6c3c55a01e44624c7f3c5d69e906f5016f32d1a697a61d81.txt
url: https://openai.com/index/asana-browser-agent/
published_at: '2026-10-09T07:00:00+00:00'
source_category: official
raw_path: raw/2026-10-10/63f6c259189519ff6c3c55a01e44624c7f3c5d69e906f5016f32d1a697a61d81.txt
sha256: 63f6c259189519ff6c3c55a01e44624c7f3c5d69e906f5016f32d1a697a61d81
fetched_at: '2026-10-10T01:14:10.274915+00:00'
last_verified: '2026-10-10'
verification_note: 已核对本页有限陈述与实际读取的来源；浏览已读完整主文；144-run、cache policy、cost/time与生产推广段。HTTP403，归档为浏览阅读后的限定事实摘录；图表只读标注，未取底层数据或实测。
  非独立复现。
reading_scope: 浏览已读完整主文；144-run、cache policy、cost/time与生产推广段。HTTP403，归档为浏览阅读后的限定事实摘录；图表只读标注，未取底层数据或实测。
evidence:
- source: raw/2026-10-10/63f6c259189519ff6c3c55a01e44624c7f3c5d69e906f5016f32d1a697a61d81.txt
  locator: 浏览已读完整主文；144-run、cache policy、cost/time与生产推广段。HTTP403，归档为浏览阅读后的限定事实摘录；图表只读标注，未取底层数据或实测。
  version: sha256:63f6c259189519ff6c3c55a01e44624c7f3c5d69e906f5016f32d1a697a61d81
date_precision: timestamp
date_basis: published
reviewed_by: Codex
reviewed_at: '2026-10-10'
reviewed_content_sha256: 2334b7854a9b3cacca10d727360e16df71a97df944d309f527b69855d64585aa
---

# Asana 案例拆解浏览 Agent 的缓存与模型成本

## Key Takeaways

相对昨日模型档位和任务预算，本期增量是缓存策略的任务级案例：144次运行，4模型×2历史预算×6策略×3重复；120K/480K是字符，任务为公共演示目录的32本书×6字段。

厂商估算原Model B至少USD36.21（未完成下界），同模型优化后USD1.24，再换GPT-6.1 Sol为USD0.47；标题76倍同时包含流程优化和换模型。Sol自身由USD1.97降至0.47，不能说模型本身便宜76倍。

优化截图保留与前缀复用已进入StackAI；GPT-6 Astra负责Codex实验，Sol负责优化后的运行。单一任务、3次重复，未独立复现。

## Detailed Notes

浏览已读完整主文；144-run、cache policy、cost/time与生产推广段。HTTP403，归档为浏览阅读后的限定事实摘录；图表只读标注，未取底层数据或实测。

## Evidence

[原始来源](https://openai.com/index/asana-browser-agent/)。原始路径、hash、采集时间与日期口径见元数据。source-checked仅表示所写披露有出处支持，非真实性独立审计。

## Questions Raised

判断（derived）：跨轮前缀稳定可减少重复计费，浏览Agent编排层可能因此创造超过模型价差的收益；动态页面、低命中率与失败重试会削弱节省。观察多任务正确完成率、缓存命中和每个成功任务总账单。
