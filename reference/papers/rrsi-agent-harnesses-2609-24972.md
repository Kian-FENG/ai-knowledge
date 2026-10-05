---
id: paper-rrsi-agent-harnesses-2609-24972
title: RRSI：约束 Agent harness 自我改进的过拟合
type: paper
domain:
- models
- infra
lifecycle: published
tags:
- agent
- harness
- evaluation
created: '2026-10-05'
updated: '2026-10-05'
summary: RRSI约束冻结模型外部harness的编辑和选择，以抑制对固定任务的过拟合；本次阅读v2摘要、投稿记录和官方README。
evidence_kind: reported
verification: source-checked
sources:
- https://arxiv.org/abs/2609.24972v2
- https://github.com/google-research/rrsi
related:
- paper-shared-kv-cache-provenance-2609-38706
- source-gemini-model-access-october-2026
aliases: []
source: raw/2026-10-05/4ead864bf088dba0461a4c1bc6772a29e8a0ea025452674c668e96a184c7ac91.body
url: https://arxiv.org/abs/2609.24972v2
published_at: '2026-09-21T17:54:49+00:00'
source_category: paper
source_updated_at: '2026-09-23T22:10:39+00:00'
upstream_version: arXiv:2609.24972v2; repository README snapshot
fetched_at: '2026-10-05T03:15:37.098105+00:00'
raw_path: raw/2026-10-05/4ead864bf088dba0461a4c1bc6772a29e8a0ea025452674c668e96a184c7ac91.body
sha256: 4ead864bf088dba0461a4c1bc6772a29e8a0ea025452674c668e96a184c7ac91
last_verified: '2026-10-05'
verification_note: 核对v2摘要、投稿记录和仓库README；未读论文全文、实验预算与统计细节，未执行代码或复现。
evidence:
- source: raw/2026-10-05/4ead864bf088dba0461a4c1bc6772a29e8a0ea025452674c668e96a184c7ac91.body
  locator: Abstract；Submission history（v1/v2）
  version: arXiv:2609.24972v2; sha256:4ead864bf088dba0461a4c1bc6772a29e8a0ea025452674c668e96a184c7ac91
- source: raw/2026-10-05/d77f43b9bd7c58ce7ef2248fde33c4b19c83273f7916e8113e1569de03293b05.body
  locator: Overview；Key features；LLM configuration；Main results；License
  version: sha256:d77f43b9bd7c58ce7ef2248fde33c4b19c83273f7916e8113e1569de03293b05
reviewed_by: Codex
reviewed_at: '2026-10-05'
reviewed_content_sha256: 6a8757b58a212d1e95443d3695a25fd39258e352392c205f96b29e085c880bff
---

# RRSI：约束 Agent harness 自我改进的过拟合

## Problem and Method

作者研究冻结模型外部的提示、工具、记忆和控制流程如何自动改进，以及固定演化任务造成的过拟合。RRSI 随时间收缩编辑预算，利用编辑历史引导探索，并在选择阶段筛除针对测试集的逻辑和不再有效或成本过高的改动。这里的自我改进发生在 Agent 系统层，不能等同于模型权重自训练。

## Results and Conditions

摘要报告跨编码、办公和工程设计任务的实验。仓库说明实例涉及 Terminal-Bench 2.1、Harvey LAB 和 EngDesign，并在域外任务上评估；配置以 Claude Opus 4.8 为冻结策略，另列 Gemini 3.5 Flash 实验。论文结果为作者披露，本次不提炼排行榜或普遍性能收益。

## Evidence

读取 arXiv v2 摘要、投稿记录及官方仓库 README。v1 于9月21日投稿，v2 于9月23日更新，均早于日报窗口；10月4日媒体报道不是论文首发。原始响应、URL、采集时间、hash 和定位见元数据。README 快照未固定上游 commit，不将其视为永恒版本。

## Limitations and Implications

未阅读全文实验预算、全部模型版本和重复实验统计，未独立复现。研究判断（derived）：改进 Agent 应同时追踪域外任务质量和运行成本；若只优化固定题集，训练集增益可能掩盖泛化损失。后续观察独立复现和跨模型、跨工作流迁移，不能由摘要推断生产环境收益。
