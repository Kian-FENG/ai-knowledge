---
id: paper-parallelism-slo-261019405
title: 论文以SLO和goodput选择并行配置，不把TP或PP当固定最优
type: paper
domain:
- infra
- models
lifecycle: published
tags:
- daily-research
created: '2026-10-15'
updated: '2026-10-15'
summary: arXiv2610.19405v1实际投稿为10月14日01:53:24UTC，RSS公告日为10月15日；本期收录公告，非当天首次投稿。仅阅读摘要与版本史。
evidence_kind: reported
verification: source-checked
sources:
- https://arxiv.org/abs/2610.19405
related: []
aliases: []
source: raw/2026-10-16/d888203848278d32cf84765a62cd470fd1a1197761752ded1792127c9f5d8900.body
url: https://arxiv.org/abs/2610.19405
published_at: '2026-10-14T01:53:24+00:00'
source_category: paper
raw_path: raw/2026-10-16/d888203848278d32cf84765a62cd470fd1a1197761752ded1792127c9f5d8900.body
sha256: d888203848278d32cf84765a62cd470fd1a1197761752ded1792127c9f5d8900
fetched_at: '2026-10-16T01:11:22.191460+00:00'
source_updated_at: null
announced_at: '2026-10-15T00:00:00-04:00'
date_precision: date-only
reading_scope: arXiv abstract / submission history；15页正文、7图未读，公告仅日精度。
retrieval_method: abstract
evidence:
- source: raw/2026-10-16/d888203848278d32cf84765a62cd470fd1a1197761752ded1792127c9f5d8900.body
  locator: arXiv abstract / submission history；15页正文、7图未读，公告仅日精度。
  version: sha256:d888203848278d32cf84765a62cd470fd1a1197761752ded1792127c9f5d8900
last_verified: '2026-10-15'
verification_note: Agent已阅读所列范围并逐项核对事实与来源支持关系；公司/作者及媒体陈述为reported，没有独立审计、账户验证或实验复现。
upstream_version: v1
reviewed_by: Codex
reviewed_at: '2026-10-16'
reviewed_content_sha256: a5a10db1d9f5194d3334cbfd0a13d0e2181c37e621bf36a32ae5abcb1720c8a9
---

# 论文以SLO和goodput选择并行配置，不把TP或PP当固定最优

## Problem and Method

arXiv2610.19405v1实际投稿为10月14日01:53:24UTC，RSS公告日为10月15日；本期收录公告，非当天首次投稿。仅阅读摘要与版本史。

作者构建TTFT–ITL可行集合及Pareto边界，以满足SLO的goodput分析TP/PP和长上下文取舍。摘要报告不同负载与约束下最优区域迁移；硬件、模型、精度、并发和完整SLO未从全文核查，因此不外推“PP总比TP好”。

## Results and Conditions

arXiv abstract / submission history；15页正文、7图未读，公告仅日精度。 已检索published及显式草稿，并按URL/hash查重；这是本期所列增量。

## Evidence

[原始来源](https://arxiv.org/abs/2610.19405)；归档 `raw/2026-10-16/d888203848278d32cf84765a62cd470fd1a1197761752ded1792127c9f5d8900.body`，sha256 `d888203848278d32cf84765a62cd470fd1a1197761752ded1792127c9f5d8900`。

reported与source-checked分别表示陈述性质和支持关系核对，审核发布不提高为独立复现。

## Limitations and Implications

判断：部署选择应围绕业务延迟约束而非单一吞吐，服务平台可用满足SLO的请求量衡量资源效率。反例是不同互联或请求分布改变边界；后续核对实验矩阵、代码及真实服务轨迹。
