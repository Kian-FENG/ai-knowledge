---
id: paper-kv-residency-261022863
title: KV驻留论文提示：Agent的显存成本还取决于空闲留存与部署位置
type: paper
domain:
- infra
- models
lifecycle: published
tags: []
created: '2026-10-20'
updated: '2026-10-20'
summary: arXiv 2610.22863v1于10月16日03:09:13 UTC投稿，RSS公告为19日00:00（-04:00）；本期按公告收录，不能称19日首次投稿。摘要研究M365四类生产工作流、逾1.21亿模型调用。
evidence_kind: reported
verification: source-checked
sources:
- https://arxiv.org/abs/2610.22863
related:
- source-vllm-bidirectional-kv-20261012
aliases: []
source: raw/2026-10-21/19bbe8901e6bdbdb3178ce1da9eebfabd90343663457cb2ed61636e202c1d7b8.txt
url: https://arxiv.org/abs/2610.22863
published_at: '2026-10-16T03:09:13+00:00'
source_category: paper
raw_path: raw/2026-10-21/19bbe8901e6bdbdb3178ce1da9eebfabd90343663457cb2ed61636e202c1d7b8.txt
sha256: 19bbe8901e6bdbdb3178ce1da9eebfabd90343663457cb2ed61636e202c1d7b8
fetched_at: '2026-10-20T22:08:29.592468+00:00'
reading_scope: arXiv摘要与Submission history v1；HTML全文404，未审PDF、完整实验、代码或独立复现。
last_verified: '2026-10-20'
verification_note: Agent已阅读所列范围并核对支持关系；reported不等于独立审计或复现，审核发布不提高核验等级。
evidence:
- source: raw/2026-10-21/19bbe8901e6bdbdb3178ce1da9eebfabd90343663457cb2ed61636e202c1d7b8.txt
  locator: arXiv摘要与Submission history v1；HTML全文404，未审PDF、完整实验、代码或独立复现。
  version: sha256:19bbe8901e6bdbdb3178ce1da9eebfabd90343663457cb2ed61636e202c1d7b8
announced_at: '2026-10-19T00:00:00-04:00'
upstream_version: v1
reviewed_by: Codex
reviewed_at: '2026-10-21'
reviewed_content_sha256: da660ed5f8a1d90000e23370a056e75ed8f2ff200d678b8133a6bfa18d96a293
---

# KV驻留论文提示：Agent的显存成本还取决于空闲留存与部署位置

## Problem and Method

arXiv 2610.22863v1于10月16日03:09:13 UTC投稿，RSS公告为19日00:00（-04:00）；本期按公告收录，不能称19日首次投稿。摘要研究M365四类生产工作流、逾1.21亿模型调用。

方法包括轨迹驱动回放、空闲上限、多分辨率KV留存和跨部署复用分析；用Llama-2-70B布局替代保密模型的容量估算不是生产集群实测HBM。只读摘要与版本史，未审全文表图、代码及量化误差，不推广其数值收益。

## Results and Conditions

作者摘要级陈述，适用条件和未读范围见上述说明。缺完整预算与负载，不作一般化性能或因果结论。

## Evidence

[原始论文](https://arxiv.org/abs/2610.22863)。arXiv摘要与Submission history v1；HTML全文404，未审PDF、完整实验、代码或独立复现。

## Limitations and Implications

判断（derived）：推导：缓存策略与路由可能共同决定长程Agent成本，内存分层和会话编排受益；反例是量化质量损失、迁移网络代价或不同业务闲置分布。观察真实业务留存时间、重算率与端到端质量。
