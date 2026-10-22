---
id: entity-recursive
title: Recursive
type: entity
domain:
- companies
- products
lifecycle: published
tags: []
created: '2026-10-22'
updated: '2026-10-22'
summary: Recursive Superintelligence, Inc.为官网页尾主体，官网发布页链接RecursiveSI模型卡；Flint与Eureka
  Machine归属已核。法定注册地、成立时间与融资账目未独立核实。
evidence_kind: reported
verification: source-checked
sources:
- source-recursive-flint-20261021
related: []
aliases: []
entity_kind: company
last_verified: '2026-10-22'
verification_note: 官网署名/页尾与产品链接核对身份和归属；未独立核验注册、财务或客户效果。
evidence:
- source: raw/2026-10-23/e54200d4862ef8401ce380ca0988ea179a7422a3ff304b39ac7fa3bb5d531515.txt
  locator: Recursive发布主文、官方更新列表、HF许可标签及vLLM同日全文已读；未审完整LICENSE、全部checkpoint/config、图像数据、PR合并时刻或部署复现。
  version: sha256:e54200d4862ef8401ce380ca0988ea179a7422a3ff304b39ac7fa3bb5d531515
- source: raw/2026-10-23/47091cb8cdb77a4c56871defcc46c57624580f3a92f4750078a15337476ee9df.body
  locator: Recursive发布主文、官方更新列表、HF许可标签及vLLM同日全文已读；未审完整LICENSE、全部checkpoint/config、图像数据、PR合并时刻或部署复现。
  version: sha256:47091cb8cdb77a4c56871defcc46c57624580f3a92f4750078a15337476ee9df
reviewed_by: Codex
reviewed_at: '2026-10-23'
reviewed_content_sha256: 1f53722ff043594dc9b16c17b59814a613fa2809185f34e13ba9c468cb890ebb
---

# Recursive

## Identity and Scope

Recursive Superintelligence, Inc.为官网页尾主体，官网发布页链接RecursiveSI模型卡；Flint与Eureka Machine归属已核。法定注册地、成立时间与融资账目未独立核实。

## Products and Capabilities

Flint本地编码模型与自动化模型研发系统Eureka Machine；开放权重不等于全部研发流程开放。

## Development Timeline

Recursive官方更新列表将Flint发布日期标为10月21日：40B总参数、每token激活约2.5B的MoE编码模型，官方与链接模型卡标为Apache-2.0权重。Eureka Machine参与数据、训练和推理优化是公司披露，不等于已证明开放式递归自我改进。 新纳入跟踪不等于本期成立。

## Evidence

[[reference/sources/recursive-flint-20261021|Recursive发布Flint开放权重，本地编码与自动化研发共同优化]]

## Open Questions

判断：小激活MoE与模型专用运行栈有机会把部分编码任务留在本地，硬件和本地工具生态受益；能力与效率也更依赖整套交付。反例是长任务失败、内存容量或后端限制抵消API节省。观察固定任务质量、内存、长上下文延迟及上游正式支持。
