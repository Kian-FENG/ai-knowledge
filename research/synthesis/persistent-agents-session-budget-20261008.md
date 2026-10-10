---
id: note-persistent-agents-session-budget-20261008
title: 持续Agent的竞争开始连接身份、会话缓存与任务预算
type: note
domain:
- products
- infra
lifecycle: published
tags:
- agent-economics
- session-cache
created: '2026-10-09'
updated: '2026-10-10'
summary: 持续Agent的任务成本由模型、缓存与运行时共同决定；Asana案例新增策略拆分证据，Anthropic内部联网整改提示权限治理同样属于任务生命周期。
evidence_kind: derived
verification: source-checked
sources:
- source-google-gemini-work-agent-20261008
- source-legalon-codex-budget-routing-20261008
- source-openai-sol-ultrafast-20261008
- source-dynamo-session-aware-20261008
- source-openai-asana-cache-economics-20261009
- source-anthropic-unintended-actions-20261009
related:
- note-interactive-agents-cost-and-local-supply-20261007
- source-vllm-v0310-20261005
aliases: []
last_verified: '2026-10-10'
verification_note: 已回读既有来源页并核对新增Asana浏览主文与Anthropic研究；仅derived综合，未实测、未审计账单或安全日志。
evidence:
- source: raw/2026-10-09/c0d72d079cd9df7fe0d29b387182dadcc1e6103dd106a7f5c5fd99d9866cadca.body
  locator: 官网完整正文；Gemini agent、multi-agent、security、cost controls、industry specialization段；未实测账户、计费或行业预览。
  version: sha256:c0d72d079cd9df7fe0d29b387182dadcc1e6103dd106a7f5c5fd99d9866cadca
- source: raw/2026-10-09/90a849ebe580482e21886d290c6bb01610af03d507a5f62f8369c5690e9ca772.txt
  locator: OpenAI案例正文模型选择、预算治理、estimated daily costs和ROI建设段；HTTP403，使用浏览工具已读段落摘录；未访问客户账单。
  version: sha256:90a849ebe580482e21886d290c6bb01610af03d507a5f62f8369c5690e9ca772
- source: raw/2026-10-09/752145521d5c5936b92fd7c658d7fb35fb4489322ccde4dd11cb630aadf0bc31.body
  locator: HTTP Changelog Oct8小节及官方pricing Standard/Ultrafast表；另已读Ultrafast指南Availability/连接开销。浏览搜索缓存的Changelog未显示该项，采用实际HTTP版本并记录差异；未调用API。
  version: sha256:752145521d5c5936b92fd7c658d7fb35fb4489322ccde4dd11cb630aadf0bc31
- source: raw/2026-10-09/3e0dd4787e839b18b62f3ac334e87ef8c68eebc430d3ff45b9ff51a71d26d730.body
  locator: 技术文章完整正文；session headers、program-aware scheduling、experimental shared-pool和proposed
    KvHint段；未逐项读PR、运行harness或独立复现。
  version: sha256:3e0dd4787e839b18b62f3ac334e87ef8c68eebc430d3ff45b9ff51a71d26d730
- source: raw/2026-10-10/63f6c259189519ff6c3c55a01e44624c7f3c5d69e906f5016f32d1a697a61d81.txt
  locator: 浏览已读完整主文；144-run、cache policy、cost/time与生产推广段。HTTP403，归档为浏览阅读后的限定事实摘录；图表只读标注，未取底层数据或实测。
  version: sha256:63f6c259189519ff6c3c55a01e44624c7f3c5d69e906f5016f32d1a697a61d81
- source: raw/2026-10-10/1fd900a82f56e73f47c0e1bc540754f05752cf535074ab8ef3dcd44466e82ad8.body
  locator: 已读完整研究正文的incident categories、context、mitigations和preliminary assessment；不复述利用细节；未读内部原始日志或独立验证。
  version: sha256:1fd900a82f56e73f47c0e1bc540754f05752cf535074ab8ef3dcd44466e82ad8
reviewed_by: Codex
reviewed_at: '2026-10-10'
reviewed_content_sha256: 56f0c0490c4a6665e75f8b59155dddf093966ab7d46a91ee6e20a37038d39eb1
---

# 持续Agent的竞争开始连接身份、会话缓存与任务预算

## What Is New

2026-10-08披露把持久运行的身份、预算暂停与会话缓存联系起来。相对10月7日交互UI、缓存计价和本地供给研究，增量是任务从产品到服务端的生命周期治理。

[[reference/sources/google-gemini-work-agent-20261008|Google 发布 Gemini 工作 Agent：云端持续执行、任务身份与项目预算结合]]

[[reference/sources/legalon-codex-budget-routing-20261008|LegalOn 案例把模型分工与预算管理同时纳入编码 Agent 采用]]

[[reference/sources/openai-sol-ultrafast-20261008|GPT-6.1 Sol 新增 Ultrafast：以更高单价购买低延迟服务]]

[[reference/sources/dynamo-session-aware-20261008|Dynamo 按 Agent 会话管理缓存和准入，部分接口仍是提案]]

## Synthesis

判断（derived）：单任务成本同时受模型/服务档位选择、失败重试、跨轮缓存淘汰和沙箱运行时长影响。Google项目预算暂停与Dynamo工具边界背压都尝试限制持续执行的资源外溢，但面向不同控制层，不能视作等价机制。LegalOn案例表明组织分工也重要，仍缺独立账单和因果评估。

高价值实时任务可能购买Ultrafast；长期后台任务更可能优化工作集存活与低价模型分工。对基础设施和编排平台的价值，应以完整任务成功率和账单评估；报价降低或快档加速不必然带来总体节省。

## Evidence

所引公司/维护者披露为reported；本页机制解释为derived。source-checked仅核对判断的有限前提，未证明收益。Dynamo共享池是实验性，KvHint仍是提案；Google行业版本为预览。

## Watchpoints

观察成功任务成本、模型升级/重试率、缓存重复prefill、尾时延、预算暂停恢复和权限审计。反例是工具与人工等待主导、低缓存复用、路由误判导致返工，或暂停损害交付；这些会削弱预期收益。

## 2026-10-09 Update

Asana补充同模型缓存策略与换模型的拆分：原Model B至少36.21美元、优化1.24美元、再换Sol0.47美元，76倍不能归于模型单因素。单任务三次重复限制外推。

[[reference/sources/openai-asana-cache-economics-20261009|Asana任务级缓存证据]]

Anthropic内部联网整改把权限、监测与沙箱加入生命周期治理；暂停/监测控制与Dynamo资源准入作用层不同，不能认为缓存优化自动解决越界。

[[reference/sources/anthropic-unintended-actions-20261009|内部评估联网边界与整改披露]]

判断（derived）：长期Agent平台需要同时衡量正确完成任务成本和允许范围内的完成率。缓存越好也可能延长错误路径的持续运行，必须观察重试、权限拒绝、人工接管与实际账单。
