---
id: source-rtx-spark-ecosystem-20261013
title: RTX Spark上市前生态更新：PAIR结束beta，Bolt模型仍待10月15日
type: source
domain:
- hardware
- products
lifecycle: published
tags:
- daily-research
created: '2026-10-13'
updated: '2026-10-13'
summary: NVIDIA 10月13日生态文章称RTX Spark笔记本计划10月16日上市，本期新增软件准备：PAIR当天退出beta、增加llama.cpp等支持；Broadcast2.3可下载，部分Agent已支持MXC。文章只有日期，边界不确定；前期硬件公告不重复算首发。
evidence_kind: reported
verification: source-checked
sources:
- https://blogs.nvidia.com/blog/local-ai-rtx-spark-laptops-software-updates/
related: []
aliases: []
last_verified: '2026-10-13'
verification_note: Agent已阅读标注范围并核对有限陈述支持关系；不表示独立测量、融资审计或部署复现。 官方生态主文Local agents、PAIR、Bolt、Broadcast、开发工具；未实测，未来时间均保留计划。
source: raw/2026-10-14/9a671723d5969ad1aea26c36c0ab04b39759985205a5bfa4118c9706172a22c8.body
url: https://blogs.nvidia.com/blog/local-ai-rtx-spark-laptops-software-updates/
published_at: '2026-10-13T00:00:00+08:00'
source_category: official
raw_path: raw/2026-10-14/9a671723d5969ad1aea26c36c0ab04b39759985205a5bfa4118c9706172a22c8.body
sha256: 9a671723d5969ad1aea26c36c0ab04b39759985205a5bfa4118c9706172a22c8
fetched_at: '2026-10-14T01:09:11.234937+00:00'
reading_scope: 官方生态主文Local agents、PAIR、Bolt、Broadcast、开发工具；未实测，未来时间均保留计划。
date_precision: date-only
date_basis: published
evidence:
- source: raw/2026-10-14/9a671723d5969ad1aea26c36c0ab04b39759985205a5bfa4118c9706172a22c8.body
  locator: 官方生态主文Local agents、PAIR、Bolt、Broadcast、开发工具；未实测，未来时间均保留计划。
  version: sha256:9a671723d5969ad1aea26c36c0ab04b39759985205a5bfa4118c9706172a22c8
reviewed_by: Codex
reviewed_at: '2026-10-14'
reviewed_content_sha256: 3d92a36fafa01ad41ebc546090fe31b130bb0ab9c0159b750dd17c792cb4c7ad
---

# RTX Spark上市前生态更新：PAIR结束beta，Bolt模型仍待10月15日

## Key Takeaways

NVIDIA 10月13日生态文章称RTX Spark笔记本计划10月16日上市，本期新增软件准备：PAIR当天退出beta、增加llama.cpp等支持；Broadcast2.3可下载，部分Agent已支持MXC。文章只有日期，边界不确定；前期硬件公告不重复算首发。

Nemotron3.5 Bolt 74B-A9B的24GB/2bit模型计划10月15日发布；Hermes的部分OpenShell/MXC和路由集成仍为月底计划。不能把即将发布的权重、许可或软件能力写成已经交付。

本文只采用最高128GB统一内存的厂商规格描述，不据此估算可运行模型上下文或吞吐。未核对所有模型卡、软件包和实机，拒用通用性能排名。

## Detailed Notes

阅读范围：官方生态主文Local agents、PAIR、Bolt、Broadcast、开发工具；未实测，未来时间均保留计划。

## Evidence

[原始来源](https://blogs.nvidia.com/blog/local-ai-rtx-spark-laptops-software-updates/)。不可覆盖原始档案、采集时间和hash见元数据。浏览笔记明确为非逐字提取；日期未知不补采集日，日期占位不视为实际时刻。

## Questions Raised

判断（derived）：本地模型、隔离与云路由一起降低使用摩擦，PC硬件及本地Agent开发者受益；内存竞争、应用兼容、云升级费或低利用率会抵消收益。观察10月15/16实际交付、同任务能耗/延迟、软件完整性和总体费用。
