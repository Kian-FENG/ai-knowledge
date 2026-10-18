---
id: source-deepseek-search-fetch-20261017
title: DeepSeek开放Search与Fetch，工具调用开始独立按成功请求计费
type: source
domain:
- products
lifecycle: published
tags: []
created: '2026-10-18'
updated: '2026-10-18'
summary: DeepSeek在10月17日更新日志宣布开放自研搜索能力。Search返回结构化搜索结果，Fetch返回单页Markdown；两者均是可独立调用的JSON
  API，并非发布一个新的对话订阅。指南无独立发布日期，事件日来自更新日志；日期精度到日，窗口边界仍不确定。
evidence_kind: reported
verification: source-checked
sources:
- https://api-docs.deepseek.com/updates/
- https://api-docs.deepseek.com/guides/search/
related: []
aliases: []
source: https://api-docs.deepseek.com/updates/
url: https://api-docs.deepseek.com/updates/
published_at: '2026-10-17T00:00:00+08:00'
source_category: official
raw_path: raw/2026-10-18/1655c11016644a95b5b45f25da1dd593837a24cdb0aa15dff52a317935ac3c07.body
sha256: 1655c11016644a95b5b45f25da1dd593837a24cdb0aa15dff52a317935ac3c07
fetched_at: '2026-10-18T10:01:03.648213+00:00'
last_verified: '2026-10-18'
verification_note: Change Log 2026-10-17 Opening up the in-house search API；指南Search/Fetch、Billing、Rate
  Limits全文；未调用API或独立核验检索质量。 source-checked仅确认上述支持关系；不表示独立验证、测量或复现。
evidence:
- source: raw/2026-10-18/1655c11016644a95b5b45f25da1dd593837a24cdb0aa15dff52a317935ac3c07.body
  locator: Change Log Date2026-10-17整节及脚注；此前日期仅背景
  version: sha256:1655c11016644a95b5b45f25da1dd593837a24cdb0aa15dff52a317935ac3c07
- source: raw/2026-10-18/2e85e4f1875cd03df16c4cffdefe57fd5b3c968eb8f74a8b4222d3e02c67dd75.body
  locator: 指南全文；公告日来自关联Change Log，指南本身无单独发布日期
  version: sha256:2e85e4f1875cd03df16c4cffdefe57fd5b3c968eb8f74a8b4222d3e02c67dd75
date_precision: date-only
reviewed_by: Codex
reviewed_at: '2026-10-18'
reviewed_content_sha256: b5b4d5c1a57f095c00d717d83406b12346f6e5d4f4ce9ee240232bbf2303c668
---

# DeepSeek开放Search与Fetch，工具调用开始独立按成功请求计费

## Key Takeaways

DeepSeek在10月17日更新日志宣布开放自研搜索能力。Search返回结构化搜索结果，Fetch返回单页Markdown；两者均是可独立调用的JSON API，并非发布一个新的对话订阅。指南无独立发布日期，事件日来自更新日志；日期精度到日，窗口边界仍不确定。

国际站指南标价：Search和Fetch分别USD0.75/1000次成功且非空的请求；失败、空搜索和超时不计费，返回结果数不改变单次价格。每账户两者各限5QPS，Fetch另有目标域名限制。

通过DeepSeek API在DeepSeek Harness、Claude Code或Codex使用的服务端工具调用目前免费，自北京时间2026年11月1日00:00开始按次计费；不能把这项临时优惠外推到所有独立API请求。相比既有模型token账单，新增独立工具供给与调用计价。

## Detailed Notes

Change Log 2026-10-17 Opening up the in-house search API；指南Search/Fetch、Billing、Rate Limits全文；未调用API或独立核验检索质量。

原始材料及本期published与显式草稿按对象、URL/hash查重；相同版本不重复建页，相关对象优先更新。

## Evidence

[原始来源](https://api-docs.deepseek.com/updates/)；归档 `raw/2026-10-18/1655c11016644a95b5b45f25da1dd593837a24cdb0aa15dff52a317935ac3c07.body`；SHA-256 `1655c11016644a95b5b45f25da1dd593837a24cdb0aa15dff52a317935ac3c07`；实际采集 2026-10-18T10:01:03.648213+00:00。

[原始来源](https://api-docs.deepseek.com/guides/search/)；归档 `raw/2026-10-18/2e85e4f1875cd03df16c4cffdefe57fd5b3c968eb8f74a8b4222d3e02c67dd75.body`；SHA-256 `2e85e4f1875cd03df16c4cffdefe57fd5b3c968eb8f74a8b4222d3e02c67dd75`；实际采集 2026-10-18T10:01:03.747591+00:00。

## Questions Raised

判断（derived）：搜索与抓取从模型附属功能变成可替换的Agent组件，有助开发者控制检索链路，也新增工具调用预算。反例是目标站点访问失败或结果质量不佳抵消低价；观察同任务检索成功率、有效引用率、调用次数和11月后的完整账单。
