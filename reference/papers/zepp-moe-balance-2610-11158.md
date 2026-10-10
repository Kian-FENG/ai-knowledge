---
id: paper-zepp-moe-balance-2610-11158
title: Zepp：MoE 调度把负载平衡视为约束而非唯一目标
type: paper
domain:
- infra
- models
lifecycle: published
tags:
- daily-research
created: '2026-10-10'
updated: '2026-10-10'
summary: arXiv 2610.11158v1于10月8日03:19:33Z提交，源站10月9日cs.DC公告；按公告日收录，不能改写成10月9日提交，日期边界仍不确定。
evidence_kind: reported
verification: source-checked
sources:
- https://arxiv.org/abs/2610.11158
related: []
aliases: []
source: raw/2026-10-10/aad793e8b41996246911dd54921349cdb392829831f3465e84f5c0334d6815c2.body
url: https://arxiv.org/abs/2610.11158
published_at: '2026-10-08T03:19:33+00:00'
source_category: paper
raw_path: raw/2026-10-10/aad793e8b41996246911dd54921349cdb392829831f3465e84f5c0334d6815c2.body
sha256: aad793e8b41996246911dd54921349cdb392829831f3465e84f5c0334d6815c2
fetched_at: '2026-10-10T01:14:19.922103+00:00'
last_verified: '2026-10-10'
verification_note: 已核对本页有限陈述与实际读取的来源；arXiv摘要、Submission history及10月9日cs.DC announcement列表；未读PDF/实验表/代码，性能数字不入结论。
  非独立复现。
reading_scope: arXiv摘要、Submission history及10月9日cs.DC announcement列表；未读PDF/实验表/代码，性能数字不入结论。
evidence:
- source: raw/2026-10-10/aad793e8b41996246911dd54921349cdb392829831f3465e84f5c0334d6815c2.body
  locator: arXiv摘要、Submission history及10月9日cs.DC announcement列表；未读PDF/实验表/代码，性能数字不入结论。
  version: sha256:aad793e8b41996246911dd54921349cdb392829831f3465e84f5c0334d6815c2
- source: raw/2026-10-10/77f93a65e1a064bd119148ce4e42bda8721154f8c5278f4694de0af8f1db2683.body
  locator: 官方RSS item guid oai:arXiv.org:2610.11158v1，Announce Type new，pubDate Fri,
    09 Oct 2026 00:00:00 -0400；午夜为列表公告日期标记，精确公告时刻未确认；abstract与abs版本对应。
  version: sha256:77f93a65e1a064bd119148ce4e42bda8721154f8c5278f4694de0af8f1db2683
date_precision: date-only
date_basis: announced
announced_at: '2026-10-09T00:00:00+08:00'
announcement_rss_offset: '-0400'
reviewed_by: Codex
reviewed_at: '2026-10-10'
reviewed_content_sha256: b8d1c8743b8a3065e9c5d9fabcf2b6315573f9e24c71c1ec2a7f14981ca5cc54
---

# Zepp：MoE 调度把负载平衡视为约束而非唯一目标

## Problem and Method

arXiv 2610.11158v1于10月8日03:19:33Z提交，源站10月9日cs.DC公告；按公告日收录，不能改写成10月9日提交，日期边界仍不确定。

摘要提出在GPU/NIC约束下优化通信瓶颈，协同专家复制/放置、通信拆并和执行重叠；相对只追求专家负载均衡，本期增量是审视平衡本身的代价。仅读摘要和版本历史，未采用缺完整硬件/精度/并行/工作负载条件的提速数字。

## Results and Conditions

仅摘要与版本/公告日期核对；全文、实验设置和harness未读。无独立性能结论，不用摘要数字排名。

## Evidence

[原始来源](https://arxiv.org/abs/2610.11158)。原始路径、hash、采集时间与日期口径见元数据。source-checked仅表示所写披露有出处支持，非真实性独立审计。

## Limitations and Implications

判断（derived）：通信约束可能改变MoE最佳部署方案，调度器与网络配置需联动；收益也可能被权重迁移和不稳定路由抵消。观察真实请求分布下尾时延与迁移开销，不能据摘要判断生产收益。

公告日另由元数据中的官方RSS entry支持；RSS使用-0400午夜列表标记，实际公告时刻未核实，不视为精确发布时间。
