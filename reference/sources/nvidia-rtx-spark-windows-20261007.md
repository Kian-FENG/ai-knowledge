---
id: source-nvidia-rtx-spark-windows-20261007
title: RTX Spark 笔记本开放预订，NVIDIA 公布Windows本地Agent硬件路线
type: source
domain:
- hardware
- products
lifecycle: published
tags:
- daily-research
created: '2026-10-08'
updated: '2026-10-08'
summary: NVIDIA 在10月7日与Microsoft的Windows活动公告中称RTX Spark笔记本当天预订、10月16日可购买，紧凑桌面机11月上市；DGX
  Station Windows版仍为预览。区分预订、发售和未来交付。
evidence_kind: reported
verification: source-checked
sources:
- https://blogs.nvidia.com/blog/local-ai-rtx-spark-microsoft-windows-event/
related: []
aliases: []
source: raw/2026-10-08/92e91549cd3c7caa8b667465b987b226e15cd8b6867ad27186d1ce1bf7fcd31d.body
url: https://blogs.nvidia.com/blog/local-ai-rtx-spark-microsoft-windows-event/
published_at: '2026-10-07T18:45:28+00:00'
source_category: official
raw_path: raw/2026-10-08/92e91549cd3c7caa8b667465b987b226e15cd8b6867ad27186d1ce1bf7fcd31d.body
sha256: 92e91549cd3c7caa8b667465b987b226e15cd8b6867ad27186d1ce1bf7fcd31d
fetched_at: '2026-10-08T01:04:44.160865+00:00'
last_verified: '2026-10-08'
verification_note: 已阅读并核对所列有限陈述与原始来源的支持关系；NVIDIA官方feed-content全文，RTX Spark devices
  / DGX Station preview / Microsoft Windows Agent；未读取图表外链、实际试用或独立跑分。；未独立复现。
reading_scope: NVIDIA官方feed-content全文，RTX Spark devices / DGX Station preview / Microsoft
  Windows Agent；未读取图表外链、实际试用或独立跑分。
evidence:
- source: raw/2026-10-08/92e91549cd3c7caa8b667465b987b226e15cd8b6867ad27186d1ce1bf7fcd31d.body
  locator: NVIDIA官方feed-content全文，RTX Spark devices / DGX Station preview / Microsoft
    Windows Agent；未读取图表外链、实际试用或独立跑分。
  version: sha256:92e91549cd3c7caa8b667465b987b226e15cd8b6867ad27186d1ce1bf7fcd31d
reviewed_by: Codex
reviewed_at: '2026-10-08'
reviewed_content_sha256: b25b750f8a94e9a98d5533a5cbd64d79f46cf1f5c6d24d5173f0c5b87022ee69
---

# RTX Spark 笔记本开放预订，NVIDIA 公布Windows本地Agent硬件路线

## Key Takeaways

NVIDIA 在10月7日与Microsoft的Windows活动公告中称RTX Spark笔记本当天预订、10月16日可购买，紧凑桌面机11月上市；DGX Station Windows版仍为预览。区分预订、发售和未来交付。

公司披露RTX Spark最高128GB统一内存，Blackwell RTX GPU与Grace CPU通过600GB/s互连；这些为产品规格，不是本项目负载实测。FP4峰值不能作为实际LLM吞吐，未核实价格、功耗和长任务成本。

公告将本地Agent与Windows受控执行环境结合；相比昨日集群AICR，新增个人/工作站供给路径。证据为已读NVIDIA官方RSS完整正文，发布2026-10-07T18:45:28Z；独立硬件测试和微软全套政策未覆盖。

## Detailed Notes

NVIDIA官方feed-content全文，RTX Spark devices / DGX Station preview / Microsoft Windows Agent；未读取图表外链、实际试用或独立跑分。

## Evidence

[原始来源](https://blogs.nvidia.com/blog/local-ai-rtx-spark-microsoft-windows-event/)。定位与阅读范围：NVIDIA官方feed-content全文，RTX Spark devices / DGX Station preview / Microsoft Windows Agent；未读取图表外链、实际试用或独立跑分。 原始路径、hash、采集/事件时间见元数据；source-checked只表示所列陈述支持关系已核对，非独立结果验证。

## Questions Raised

判断（derived）：更大统一内存可能把部分Agent和开发任务迁至本地，设备与私有数据工作流受益，也可能减少某些云推理需求。散热、内存带宽或系统权限若限制长任务，本地方案未必更便宜；观察发售交付、持续吞吐、功耗与云端同任务总成本。
