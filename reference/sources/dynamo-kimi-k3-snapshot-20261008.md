---
id: source-dynamo-kimi-k3-snapshot-20261008
title: Dynamo 发布 Kimi-K3 实验快照，明确不适合生产
type: source
domain:
- infra
- models
lifecycle: published
tags:
- daily-research
created: '2026-10-09'
updated: '2026-10-09'
summary: v1.5.0-kimi-k3-post.1标为非QA-gated实验快照；底层镜像为Dynamo1.5.1、SGLang0.5.18、CUDA13、Python3.12，不能混作1.5稳定新增能力。
evidence_kind: reported
verification: source-checked
sources:
- https://github.com/ai-dynamo/dynamo/releases/tag/v1.5.0-kimi-k3-post.1
related: []
aliases: []
source: raw/2026-10-09/9e828406b13242ee5faa5c04eb4b74c5f32df8dacb070c97a375c6537a300e87.body
url: https://github.com/ai-dynamo/dynamo/releases/tag/v1.5.0-kimi-k3-post.1
published_at: null
source_category: release
raw_path: raw/2026-10-09/9e828406b13242ee5faa5c04eb4b74c5f32df8dacb070c97a375c6537a300e87.body
sha256: 9e828406b13242ee5faa5c04eb4b74c5f32df8dacb070c97a375c6537a300e87
fetched_at: '2026-10-09T01:09:31.340601+00:00'
last_verified: '2026-10-09'
verification_note: 已阅读原始来源并核对所列有限陈述；GitHub发布正文完整阅读；experimental、versions、recipes、precision及known
  limitations，tag a0dcfbf6d3aa788e8dba806189f1611d9293a52f；未跑benchmark或读全部PR。；未独立复现或审计。
reading_scope: GitHub发布正文完整阅读；experimental、versions、recipes、precision及known limitations，tag
  a0dcfbf6d3aa788e8dba806189f1611d9293a52f；未跑benchmark或读全部PR。
evidence:
- source: raw/2026-10-09/9e828406b13242ee5faa5c04eb4b74c5f32df8dacb070c97a375c6537a300e87.body
  locator: GitHub发布正文完整阅读；experimental、versions、recipes、precision及known limitations，tag
    a0dcfbf6d3aa788e8dba806189f1611d9293a52f；未跑benchmark或读全部PR。
  version: sha256:9e828406b13242ee5faa5c04eb4b74c5f32df8dacb070c97a375c6537a300e87
date_precision: timestamp
retrieval_method: http-extracted
source_updated_at: '2026-10-08T20:14:58+00:00'
version: v1.5.0-kimi-k3-post.1@a0dcfbf6d3aa788e8dba806189f1611d9293a52f
reviewed_by: Codex
reviewed_at: '2026-10-09'
reviewed_content_sha256: a2555dcc21af91c5de4731e52c73acfaf5bb2ad01c9ee414e4eb2b7768249bbb
---

# Dynamo 发布 Kimi-K3 实验快照，明确不适合生产

## Key Takeaways

v1.5.0-kimi-k3-post.1标为非QA-gated实验快照；底层镜像为Dynamo1.5.1、SGLang0.5.18、CUDA13、Python3.12，不能混作1.5稳定新增能力。

官方提供GB300上的聚合与1P1D分离配方：均16张GB300，聚合两worker采用DCP8/TP8，分离配合Mooncake NVLink传KV；模型experts为MXFP4、KV为FP8。

相对昨日Dynamo1.5.1补丁，这是新模型部署实验包；未新增Kimi模型发布事件。公布吞吐用了合成接受长度4.05，不是真实DSpark验证；另有长prefill健康检查、logprobs/stop_token_ids和JSON解码限制，不采用性能排名。

## Detailed Notes

GitHub发布正文完整阅读；experimental、versions、recipes、precision及known limitations，tag a0dcfbf6d3aa788e8dba806189f1611d9293a52f；未跑benchmark或读全部PR。。仅有日期的来源存在窗口边界不确定；已对照2026-10-07日报与已发布/草稿知识查重。来源发布与审核不等于独立验证。

## Evidence

[官方来源](https://github.com/ai-dynamo/dynamo/releases/tag/v1.5.0-kimi-k3-post.1)。原始路径、版本hash、采集时间、发布时间/更新时间和定位见元数据。公司与维护者陈述为reported。

## Questions Raised

判断（derived）：模型部署生态开始提供明确的缓存、精度和拆分配方，可缩短评估准备时间，GB300与KV传输生态受益。但生产稳定性及真实投机接受率尚是约束；观察真实任务吞吐、错误率、重启和H200等硬件覆盖。
