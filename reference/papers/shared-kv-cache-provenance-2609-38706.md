---
id: paper-shared-kv-cache-provenance-2609-38706
title: 共享 KV cache 研究关注跨配置复用的来源一致性
type: paper
domain:
- infra
lifecycle: published
tags:
- inference
created: '2026-10-02'
updated: '2026-10-02'
summary: 本期 arXiv 公告收录该论文，原始投稿时间为9月30日。作者研究共享缓存键是否保留 adapter、权重配置和隔离域等信息。
evidence_kind: reported
verification: source-checked
sources:
- https://arxiv.org/abs/2609.38706
related: []
aliases: []
source: raw/2026-10-02/7edc88134d645b0b2d19a874d6368d072484354e59777a479ba68b478e69c075.body
url: https://arxiv.org/abs/2609.38706
published_at: '2026-09-30T00:41:44+00:00'
source_category: paper
last_verified: '2026-10-02'
verification_note: 核对所列来源及阅读范围；仅验证出处支持这些陈述，未独立测量或复现。
announced_at: '2026-10-01T00:00:00-04:00'
evidence:
- source: raw/2026-10-02/7edc88134d645b0b2d19a874d6368d072484354e59777a479ba68b478e69c075.body
  locator: Abstract；Submission history，v1；arXiv RSS公告日期
  version: sha256:7edc88134d645b0b2d19a874d6368d072484354e59777a479ba68b478e69c075
reviewed_by: Codex
reviewed_at: '2026-10-02'
reviewed_content_sha256: 844219148c2d7e10a543587d19912359ec0a38002f9bbcf2988eb1db13086f81
---

# 共享 KV cache 研究关注跨配置复用的来源一致性

## Key Takeaways

- 本期 arXiv 公告收录该论文，原始投稿时间为9月30日。作者研究共享缓存键是否保留 adapter、权重配置和隔离域等信息。
- 摘要报告在特定 vLLM/SGLang 配置下观察到错误复用，并提出 provenance contract。本期未阅读全文测试矩阵或独立复现。

## Evidence

原文：[Preserving Provenance in Shared KV Caches for LLM Serving](https://arxiv.org/abs/2609.38706)。阅读范围：abstract-and-submission-history。归档文件：`raw/2026-10-02/7edc88134d645b0b2d19a874d6368d072484354e59777a479ba68b478e69c075.body`；hash见frontmatter。

## Limitations

已检查来源所述内容，不代表独立验证公司效果、未来计划或论文结果。具体适用范围以来源为准。
