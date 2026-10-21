---
id: source-sglang-omni-interaction-20261020
title: SGLang Omni将持续交互纳入图与会话运行时，保留不同语音架构的取舍
type: source
domain:
- infra
- products
lifecycle: published
tags: []
created: '2026-10-21'
updated: '2026-10-21'
summary: 官方博客列表标10月20日；主文以图组合模型、工具和交互控制，用持续会话协调状态、取消与客户端播放进度，覆盖原生全双工、轮次模型及级联方案。相对此前Stage–Process–GPU布局，新增是跨模型与跨轮次交互协调。
evidence_kind: reported
verification: source-checked
sources:
- https://www.sglang.io/blog/omni-interactive-runtime
related: []
aliases: []
source: raw/2026-10-22/fcb7bbea114fdf54d8e89e1aa2b5ba9ba221ddbc047e21952de11d76619f7807.body
url: https://www.sglang.io/blog/omni-interactive-runtime
published_at: '2026-10-20T00:00:00+08:00'
source_category: official
raw_path: raw/2026-10-22/fcb7bbea114fdf54d8e89e1aa2b5ba9ba221ddbc047e21952de11d76619f7807.body
sha256: fcb7bbea114fdf54d8e89e1aa2b5ba9ba221ddbc047e21952de11d76619f7807
fetched_at: '2026-10-21T22:09:59.209566+00:00'
reading_scope: 官方主文、Evaluation Results表格、样本与准入限制、Known Issues及工程附录已读；未复核外链代码revision、评分模型版本、完整精度或独立复现。主文HTTP读取成功；浏览工具不可达不记作没有新闻。
last_verified: '2026-10-21'
verification_note: Agent实际阅读所列范围并核对结论支持关系；公司和作者披露为reported，无独立复现；发布审核不提高核验等级。
evidence:
- source: raw/2026-10-22/fcb7bbea114fdf54d8e89e1aa2b5ba9ba221ddbc047e21952de11d76619f7807.body
  locator: 官方主文、Evaluation Results表格、样本与准入限制、Known Issues及工程附录已读；未复核外链代码revision、评分模型版本、完整精度或独立复现。主文HTTP读取成功；浏览工具不可达不记作没有新闻。
  version: sha256:fcb7bbea114fdf54d8e89e1aa2b5ba9ba221ddbc047e21952de11d76619f7807
date_precision: date-only
reviewed_by: Codex
reviewed_at: '2026-10-22'
reviewed_content_sha256: 5d928a944fee0344925c98fc921bd5d8b551605f2dabf402fa8c8cea7765326a
---

# SGLang Omni将持续交互纳入图与会话运行时，保留不同语音架构的取舍

## Key Takeaways

官方博客列表标10月20日；主文以图组合模型、工具和交互控制，用持续会话协调状态、取消与客户端播放进度，覆盖原生全双工、轮次模型及级联方案。相对此前Stage–Process–GPU布局，新增是跨模型与跨轮次交互协调。

## Detailed Notes

文章用MiniCPM-o 4.5、Qwen3-Omni和Qwen3-ASR-1.7B→Qwen3.8-27B（关闭thinking）→Qwen3-TTS CustomVoice，在每方案单H200、同Omni revision下比较Full-Duplex-Bench v1.5/v1.0；每v1.5类25对、v1.0子集10样本，并做128会话/并发级别的服务测试。

原生方案的打断语义、级联方案的音色连续性和轮次方案的误打断各有代价；16并发是级联配置的准入上限，GPU尚未饱和。没有一种方案全面占优，不能把单次容量直接推成架构上限或普遍成本排名。仅日期，前期未收录，边界不确定。

## Evidence

[原始来源](https://www.sglang.io/blog/omni-interactive-runtime)；`raw/2026-10-22/fcb7bbea114fdf54d8e89e1aa2b5ba9ba221ddbc047e21952de11d76619f7807.body`，hash `fcb7bbea114fdf54d8e89e1aa2b5ba9ba221ddbc047e21952de11d76619f7807`。

官方主文、Evaluation Results表格、样本与准入限制、Known Issues及工程附录已读；未复核外链代码revision、评分模型版本、完整精度或独立复现。主文HTTP读取成功；浏览工具不可达不记作没有新闻。

## Questions Raised

判断：语音助手的优化目标正扩展到用户实际听到的内容、打断后上下文一致性和持续会话成本；可替换组件让开源ASR/LLM/TTS更容易竞争。反例是协调开销抵消组件升级收益。观察误打断、播放历史一致性、长会话状态及同质量总成本。
