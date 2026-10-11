---
id: note-agent-decisions-and-authority-20261010
title: Agent 决策 API 与执行权限开始分层，低价评分不能替代独立控制
type: note
domain:
- products
- infra
lifecycle: published
tags: []
created: '2026-10-10'
updated: '2026-10-10'
summary: 把Composer用户提交、Decision-1预定义评分、Stacklok执行治理及纳德拉外部控制原则连接起来；背景日期与本期观点分开。
evidence_kind: derived
verification: source-checked
sources:
- source-codex-composer-predictions-20261009
- source-microsoft-decision-1-20261009
- source-stacklok-agent-architecture-20261010
- source-nadella-agent-containment-20261010
related:
- source-codex-composer-predictions-20261009
- source-microsoft-decision-1-20261009
- source-stacklok-agent-architecture-20261010
- source-nadella-agent-containment-20261010
aliases: []
last_verified: '2026-10-10'
verification_note: Agent已读所列范围并逐项核对归因与支持关系；仅核对来源所述，不是独立验证结果、法律主体、性能或生产效果。
evidence:
- source: raw/2026-10-11/4c8674c76ff516e8e78dd6768242a96bc6ee2af12c255ca653b305fa49a4f390.txt
  locator: 所列来源明确功能/价格/权限边界；以下机制解释为Agent推导，未独立测量。
  version: sha256:4c8674c76ff516e8e78dd6768242a96bc6ee2af12c255ca653b305fa49a4f390
- source: raw/2026-10-11/e2cebb1e437dd8bfcbf59310e8061e677452517940ab8d8c243ba48dbd619302.txt
  locator: 所列来源明确功能/价格/权限边界；以下机制解释为Agent推导，未独立测量。
  version: sha256:e2cebb1e437dd8bfcbf59310e8061e677452517940ab8d8c243ba48dbd619302
- source: raw/2026-10-11/327d9ed2706e7fa4b40efe736a4413f71aebf9834324ac901b965cac0fe1e999.txt
  locator: 所列来源明确功能/价格/权限边界；以下机制解释为Agent推导，未独立测量。
  version: sha256:327d9ed2706e7fa4b40efe736a4413f71aebf9834324ac901b965cac0fe1e999
- source: raw/2026-10-11/aa7dd5f00a45b7fcbe36040c24fe52f435990ef02364c0f2f6af7beefff0f51f.txt
  locator: 所列来源明确功能/价格/权限边界；以下机制解释为Agent推导，未独立测量。
  version: sha256:aa7dd5f00a45b7fcbe36040c24fe52f435990ef02364c0f2f6af7beefff0f51f
reviewed_by: Codex
reviewed_at: '2026-10-11'
reviewed_content_sha256: 1c22b51a3dfacc529ec4fe0d1649c7880054cc000f622e4b8ed28359c1fb1e83
---

# Agent 决策 API 与执行权限开始分层，低价评分不能替代独立控制

## What Is New

10月10日纳德拉公开文章要求将模型能力与执行授权分开；本次另补入10月9日Composer/Decision-1和未知日期Stacklok背景。不能把补读或网页更新日当新品日期。

## Synthesis

Composer减少用户下一次输入的摩擦，建议仍须人工提交；Decision-1把固定选项选择做成评分API；Stacklok定位共享身份、审计和工具策略。它们分别影响意图输入、工作流决策、动作执行，机制相关但可用范围与证据不同。

判断：低价/低延迟评分若在真实任务下保持校准，可减少Agent连续循环的费用与等待，路由与人工升级服务可能受益；但模型概率既不授予权限，也不证明操作安全。独立权限执行和审计设施承担不能由评分API替代的职责。反例是分类选项遗漏、分布变化、错误高置信或外部工具未被停止机制覆盖，低价调用仍会扩大错误动作。

纳德拉的文章是倡议，Stacklok的描述是公司产品主张，均不构成已证明的强制控制。模型自身或另一个模型审计不能自动证明执行链完整。结合已存的[[research/synthesis/persistent-agents-session-budget-20261008|持续Agent预算与会话研究]]，后续比较应同时看完整任务费用、权限覆盖和可复现日志，不能只比每token报价。

## Evidence

[[reference/sources/codex-composer-predictions-20261009|source-codex-composer-predictions-20261009]]

[[reference/sources/microsoft-decision-1-20261009|source-microsoft-decision-1-20261009]]

[[reference/sources/stacklok-agent-architecture-20261010|source-stacklok-agent-architecture-20261010]]

[[reference/sources/nadella-agent-containment-20261010|source-nadella-agent-containment-20261010]]

## Watchpoints

固定模型和harness的真实工作流成功率/校准、人工升级率、完整任务账单；暂停后子进程/远程工具是否仍执行，审计是否覆盖所有关键动作，产品许可及生产部署。
