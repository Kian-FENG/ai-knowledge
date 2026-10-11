---
id: source-microsoft-decision-1-20261009
title: Microsoft Decision-1 将预定义选项评分做成低价 API
type: source
domain:
- models
- products
lifecycle: published
tags: []
created: '2026-10-10'
updated: '2026-10-10'
summary: 官方10月9日背景：基于Qwen3.5-9B后训练的结构化决策评分，当前给Foundry/OpenRouter入口；未独立核验性能。
evidence_kind: reported
verification: source-checked
sources:
- https://commandline.microsoft.com/microsoft-decision-1-model-foundry/
related: []
aliases: []
source: https://commandline.microsoft.com/microsoft-decision-1-model-foundry/
url: https://commandline.microsoft.com/microsoft-decision-1-model-foundry/
published_at: '2026-10-09T00:00:00+08:00'
source_category: official
last_verified: '2026-10-10'
verification_note: Agent已读所列范围并逐项核对归因与支持关系；仅核对来源所述，不是独立验证结果、法律主体、性能或生产效果。
announced_at: null
date_precision: date-only
raw_path: raw/2026-10-11/e2cebb1e437dd8bfcbf59310e8061e677452517940ab8d8c243ba48dbd619302.txt
sha256: e2cebb1e437dd8bfcbf59310e8061e677452517940ab8d8c243ba48dbd619302
fetched_at: '2026-10-11T01:07:29.776152+00:00'
reading_scope: 官方完整主文How works、Robustness、Safety、Pricing与Editor note；未审图表底层数据。
evidence:
- source: raw/2026-10-11/e2cebb1e437dd8bfcbf59310e8061e677452517940ab8d8c243ba48dbd619302.txt
  locator: 官方完整主文How works、Robustness、Safety、Pricing与Editor note；未审图表底层数据。
  version: sha256:e2cebb1e437dd8bfcbf59310e8061e677452517940ab8d8c243ba48dbd619302
source_name: Microsoft Command Line
reviewed_by: Codex
reviewed_at: '2026-10-11'
reviewed_content_sha256: fabd654798436bb05263b104cc02bea1b8a9fd84a35468fd80cf5786e6140591
---

# Microsoft Decision-1 将预定义选项评分做成低价 API

## Key Takeaways

- Microsoft官方正文说Decision-1以Qwen3.5-9B后训练，为预定义yes/no、多选和rating选项返回概率分数，目标为分类、路由、验证和工作流控制。
- 当前已读页面给Microsoft Foundry及OpenRouter入口；输入每百万token USD0.042、输出免费。未实测地域、账号或账单。
- 厂商比较36个benchmark、近150000题并描述8种输入扰动；缺完整harness、模型快照、硬件、输入分布和预算，本页不据此跨模型排名。

## Detailed Notes

发布日期仅2026.10.09，时区/小时未知；页面注明后来加入Jev准确率与校准比较，但更新时刻未知。搜索缓存称OpenRouter coming soon和不同runner-up；以本次已读版本记录当前入口，不将未定时更新算成10月10日发布。只读正文与附录，未读图表底层数据或模型卡。

## Evidence

来源：[Microsoft Command Line](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/)。原始路径、hash、采集时间、版本及阅读范围见元数据。浏览阅读后保存的材料为限定事实摘录，非原HTTP快照；cxmt来源为原RSS响应。核对不等于独立复现。

## Questions Raised

模型version、option概率校准、O.O.D.与输入扰动、完整harness/预算；固定选项之外的拒判/人工升级机制。
