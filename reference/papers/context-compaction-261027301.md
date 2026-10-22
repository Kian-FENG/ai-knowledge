---
id: paper-context-compaction-261027301
title: 上下文压缩论文提醒：当前问题表现不能代替后续任务的证据保留
type: paper
domain:
- models
- infra
lifecycle: published
tags: []
created: '2026-10-22'
updated: '2026-10-22'
summary: arXiv 2610.27301v1于10月19日21:15:56 UTC投稿，10月21日RSS公告纳入本期；仅阅读摘要和v1历史，不把公告日当投稿日。
evidence_kind: reported
verification: source-checked
sources:
- https://arxiv.org/abs/2610.27301
related: []
aliases: []
source: raw/2026-10-23/406bdac6e476d8fb89a1b6a97777110b82616fd02e567b1cc2c0268f9ab7dba7.txt
url: https://arxiv.org/abs/2610.27301
published_at: '2026-10-19T21:15:56+00:00'
source_category: paper
last_verified: '2026-10-22'
verification_note: Agent实际阅读所列来源范围并核对支持关系；公司/作者披露保留reported，未独立实测。审核发布不等于独立核验。
raw_path: raw/2026-10-23/406bdac6e476d8fb89a1b6a97777110b82616fd02e567b1cc2c0268f9ab7dba7.txt
sha256: 406bdac6e476d8fb89a1b6a97777110b82616fd02e567b1cc2c0268f9ab7dba7
fetched_at: '2026-10-22T22:10:35.384307+00:00'
reading_scope: arXiv摘要、投稿历史及RSS公告已读；未读全文、附表/代码、置信区间和独立复现。
evidence:
- source: raw/2026-10-23/406bdac6e476d8fb89a1b6a97777110b82616fd02e567b1cc2c0268f9ab7dba7.txt
  locator: arXiv摘要、投稿历史及RSS公告已读；未读全文、附表/代码、置信区间和独立复现。
  version: sha256:406bdac6e476d8fb89a1b6a97777110b82616fd02e567b1cc2c0268f9ab7dba7
announced_at: '2026-10-21T00:00:00-04:00'
version: arXiv:2610.27301v1
reviewed_by: Codex
reviewed_at: '2026-10-23'
reviewed_content_sha256: f185e25460ae4b75128072d919b96b2b05bc91b073d984f3bb64df38236d437d
---

# 上下文压缩论文提醒：当前问题表现不能代替后续任务的证据保留

## Problem and Method

arXiv 2610.27301v1于10月19日21:15:56 UTC投稿，10月21日RSS公告纳入本期；仅阅读摘要和v1历史，不把公告日当投稿日。

作者用四个有证据标注的语料及Agent轨迹，将压缩方法与同token预算随机删除比较。摘要称MultiRC在25%预算下针对当前问题选句可改善当前题，却未显示对后续题优于随机删句；LLMLingua-2、Evidence Inference和需精确标识符的τ-bench结果各异，FEVER还暴露标签正确但保留证据不支持的风险。模型提到gpt-6-luna/Decisions API，具体快照、harness和统计原表未审，不作跨系统排名。

## Results and Conditions

仅摘要级记录作者方法和有限结果，不把摘要中的最大收益当成已复现性能。完整配置、统计和代码均待核。

## Evidence

[原始来源](https://arxiv.org/abs/2610.27301)；`raw/2026-10-23/406bdac6e476d8fb89a1b6a97777110b82616fd02e567b1cc2c0268f9ab7dba7.txt`，SHA-256 `406bdac6e476d8fb89a1b6a97777110b82616fd02e567b1cc2c0268f9ab7dba7`。

arXiv摘要、投稿历史及RSS公告已读；未读全文、附表/代码、置信区间和独立复现。

## Limitations and Implications

判断：持久Agent的记忆预算应按未来任务、证据与精确标识符验收，而不能只测摘要是否回答当前问题。反例是任务分布很窄，定向压缩反而足够。观察后续任务成功率、可追溯证据保留、标识符丢失及累计成本。
