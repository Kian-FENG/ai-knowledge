---
id: paper-refold-reversible-context-2610-07863
title: ReFold：保留完整历史，用可逆折叠控制长时Agent上下文
type: paper
domain:
- models
- infra
lifecycle: published
tags:
- daily-research
created: '2026-10-08'
updated: '2026-10-08'
summary: ReFold保留不可变完整历史，把重复工具输出和已完成轮次折成提示片段，可将原轮次恢复追加到提示，兼顾可逆性与prefix cache；不需要重新训练基础模型。相对昨日HEAR跨层协作，增量是harness内历史渲染方法。
evidence_kind: reported
verification: source-checked
sources:
- https://arxiv.org/abs/2610.07863
related: []
aliases: []
source: raw/2026-10-08/7d6f07925ad8cdc111d5a52a0d45e5f6e8a9d991619ceec59868f4e25c9a3dfe.txt
url: https://arxiv.org/abs/2610.07863
published_at: '2026-10-06T07:09:54+00:00'
source_category: paper
raw_path: raw/2026-10-08/7d6f07925ad8cdc111d5a52a0d45e5f6e8a9d991619ceec59868f4e25c9a3dfe.txt
sha256: 7d6f07925ad8cdc111d5a52a0d45e5f6e8a9d991619ceec59868f4e25c9a3dfe
fetched_at: '2026-10-08T01:13:11.892877+00:00'
last_verified: '2026-10-08'
verification_note: 已阅读并核对所列有限陈述与原始来源的支持关系；arXiv2610.07863v1摘要/提交历史；HTML方法§3及§4.1设置、部分表1；官方RSS与cs.CL
  Oct7列表。未完整审阅实验、附录/代码或独立复现。；未独立复现。
reading_scope: arXiv2610.07863v1摘要/提交历史；HTML方法§3及§4.1设置、部分表1；官方RSS与cs.CL Oct7列表。未完整审阅实验、附录/代码或独立复现。
evidence:
- source: raw/2026-10-08/7d6f07925ad8cdc111d5a52a0d45e5f6e8a9d991619ceec59868f4e25c9a3dfe.txt
  locator: arXiv2610.07863v1摘要/提交历史；HTML方法§3及§4.1设置、部分表1；官方RSS与cs.CL Oct7列表。未完整审阅实验、附录/代码或独立复现。
  version: sha256:7d6f07925ad8cdc111d5a52a0d45e5f6e8a9d991619ceec59868f4e25c9a3dfe
- source: raw/2026-10-08/9ffd30ff2f6e6ab740894389b16cbcfcf2465d3cda6c147112b5a0339a66e10f.body
  locator: 官方RSS Oct7公告候选 f2c1d7f20282ba4c458b
  version: sha256:9ffd30ff2f6e6ab740894389b16cbcfcf2465d3cda6c147112b5a0339a66e10f
announced_at: '2026-10-07'
date_precision: date-only
version: arxiv:2610.07863v1
reviewed_by: Codex
reviewed_at: '2026-10-08'
reviewed_content_sha256: 8ea3571ce18f2f6c3fc97812f2df00a6a587a5012278e7c3ec8f3654879d3baf
---

# ReFold：保留完整历史，用可逆折叠控制长时Agent上下文

## Problem and Method

ReFold保留不可变完整历史，把重复工具输出和已完成轮次折成提示片段，可将原轮次恢复追加到提示，兼顾可逆性与prefix cache；不需要重新训练基础模型。相对昨日HEAR跨层协作，增量是harness内历史渲染方法。

## Results and Conditions

已读方法与§4.1：mini-swe-agent，Qwen3.6-27B/35B-A3B，两张RTX6000 Ada、TP、vLLM prefix cache，temperature0、250步、每步至多16384输出、256K上下文，五个SWE/Terminal基准各50任务；精度、软件版本及完整结果/附录未审阅，不采用加速或成本倍数。

v1发表于2026-10-06T07:09:54Z，10月7日cs.CL公告；按公告日纳入，日期仅到日、边界不确定，不能称今天首次投稿。

## Evidence

[原始来源](https://arxiv.org/abs/2610.07863)。定位与阅读范围：arXiv2610.07863v1摘要/提交历史；HTML方法§3及§4.1设置、部分表1；官方RSS与cs.CL Oct7列表。未完整审阅实验、附录/代码或独立复现。 原始路径、hash、采集/事件时间见元数据；source-checked只表示所列陈述支持关系已核对，非独立结果验证。

## Limitations and Implications

判断（derived）：可逆折叠可能减少持续Agent的历史重复计算并保留追溯入口，harness与缓存服务环节可能受益。折叠选择错误、恢复开销或过期工具结果会削弱效果；观察同任务成功率、恢复率、KV占用与并发尾时延。

arXiv2610.07863v1摘要/提交历史；HTML方法§3及§4.1设置、部分表1；官方RSS与cs.CL Oct7列表。未完整审阅实验、附录/代码或独立复现。
