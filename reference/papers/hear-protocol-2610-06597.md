---
id: paper-hear-protocol-2610-06597
title: HEAR：把 Agent 工作流意图与推理引擎状态连接起来
type: paper
domain:
- infra
- models
lifecycle: published
tags:
- daily-research
created: '2026-10-07'
updated: '2026-10-07'
summary: HEAR 提议双向 Harness–Engine 协议：harness 提供工作流依赖、上下文生命周期和执行需求，引擎返回队列、KV 状态、能力及操作结果；协议语义与优化策略分开。
evidence_kind: reported
verification: source-checked
sources:
- https://arxiv.org/abs/2610.06597
related: []
aliases: []
source: raw/2026-10-07/0cfd459f94f18f46306aca2ad89b34a61c69e315a90619eea58e1ba282f79538.txt
url: https://arxiv.org/abs/2610.06597
published_at: '2026-10-05T16:07:33+00:00'
source_category: paper
raw_path: raw/2026-10-07/0cfd459f94f18f46306aca2ad89b34a61c69e315a90619eea58e1ba282f79538.txt
sha256: 0cfd459f94f18f46306aca2ad89b34a61c69e315a90619eea58e1ba282f79538
fetched_at: '2026-10-07T01:16:05.019572+00:00'
last_verified: '2026-10-07'
reading_scope: 已读v1摘要、提交历史、引言/协议§3及实验§4可见正文；未读附录、代码或复现实验。cs.AI 10月6日公告仅到日，v1实际提交2026-10-05T16:07:33Z不在本期；本条以公告日纳入且窗口边界不确定。本文不采用速度数字。
verification_note: 已实际阅读并核对以下陈述与出处：arXiv v1 摘要/提交历史；HTML §3 Protocol / §4 Experiments；cs.AI
  10月6日公告第9条。未逐项核对精度、软件版本、全部长度/并发设置及附录，不进行跨系统排名或复现声明。
evidence:
- source: raw/2026-10-07/0cfd459f94f18f46306aca2ad89b34a61c69e315a90619eea58e1ba282f79538.txt
  locator: arXiv v1 摘要/提交历史；HTML §3 Protocol / §4 Experiments；cs.AI 10月6日公告第9条
  version: sha256:0cfd459f94f18f46306aca2ad89b34a61c69e315a90619eea58e1ba282f79538
- source: raw/2026-10-07/29b5b4601d2ddc3a434e8bc0f889bde8d6aef03dc3ad8a01133c502c8bc66b90.txt
  locator: 'cs.AI recent: Tue, 6 Oct 2026；HEAR第9条、HERA第13条；各自摘要提交历史'
  version: sha256:29b5b4601d2ddc3a434e8bc0f889bde8d6aef03dc3ad8a01133c502c8bc66b90
announced_at: '2026-10-06'
submission_version: arXiv:2610.06597v1
reviewed_by: Codex
reviewed_at: '2026-10-07'
reviewed_content_sha256: 504815c713ea6a9ec9bcdc5bdd158df3e192f070d0b5fa1ace577b391ec3feff
---

# HEAR：把 Agent 工作流意图与推理引擎状态连接起来

## Problem and Method

HEAR 提议双向 Harness–Engine 协议：harness 提供工作流依赖、上下文生命周期和执行需求，引擎返回队列、KV 状态、能力及操作结果；协议语义与优化策略分开。

已读 §3 区分意图/控制、偏好/要求、观测/保证、接受/完成；§4 展示缓存协调和角色推理配置，策略收益随负载变化，没有单一策略在所有负载占优。

v1 于 2026-10-05T16:07:33Z 提交，10 月 6 日进入 cs.AI 公告列表；本期按公告日纳入（仅到日、边界不确定），不称今天首次投稿。已读摘要、协议及实验可见正文，未读附录与代码，不采用加速倍数。

## Results and Conditions

未逐项核对精度、软件版本、全部长度/并发设置及附录，不进行跨系统排名或复现声明。

## Evidence

[原始来源](https://arxiv.org/abs/2610.06597)。定位：arXiv v1 摘要/提交历史；HTML §3 Protocol / §4 Experiments；cs.AI 10月6日公告第9条。原始路径、采集时间、版本和 hash 见元数据；source-checked 仅表示已核对所列有限陈述，不代表独立复现。

## Limitations and Implications

判断（derived）：当多 Agent 任务争用缓存和队列，跨层信息可能帮助减少重复计算，同时保持依赖和等待约束；编排与服务框架接口可能成为竞争点。若状态过期或反馈开销超过收益，协议未必改善成本；观察时延尾部、信息新鲜度和跨框架适配。
