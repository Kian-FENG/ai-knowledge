---
id: source-claude-formal-verification-20261022
title: Anthropic与Theorem披露123库形式证明，保证范围仍受规格与机器模型约束
type: source
domain:
- models
- infra
lifecycle: published
tags: []
created: '2026-10-24'
updated: '2026-10-23'
summary: Anthropic于10月22日披露与Theorem合作：Claude对123个OSS-Fuzz库的239个入口，在修复发现问题后生成Rocq证明。增量是把已有fuzz入口转为针对编译后RISC-V二进制的无崩溃规格，再由独立证明检查器检查。
evidence_kind: reported
verification: source-checked
sources:
- https://www.anthropic.com/research/formal-verification
related: []
aliases: []
source: raw/2026-10-24/50e28562821c757f54bea3967715dd84c0777206b2644b922cba5cbe0ca9c843.body
url: https://www.anthropic.com/research/formal-verification
published_at: '2026-10-22T00:00:00+08:00'
source_category: official
last_verified: '2026-10-23'
verification_note: Agent阅读所列来源并核对有限结论；reported保留披露主体归因，derived是研究推导，未独立复现。
reading_scope: 官方Introduction、Turning tests into proofs、Finding/fixing、成本与复用子实验、Limitations及脚注已读；附录、证明仓库和Rocq独立执行未审。不是独立复现。
raw_path: raw/2026-10-24/50e28562821c757f54bea3967715dd84c0777206b2644b922cba5cbe0ca9c843.body
sha256: 50e28562821c757f54bea3967715dd84c0777206b2644b922cba5cbe0ca9c843
fetched_at: '2026-10-23T22:08:48.033014+00:00'
evidence:
- source: raw/2026-10-24/50e28562821c757f54bea3967715dd84c0777206b2644b922cba5cbe0ca9c843.body
  locator: 官方Introduction、Turning tests into proofs、Finding/fixing、成本与复用子实验、Limitations及脚注已读；附录、证明仓库和Rocq独立执行未审。不是独立复现。
  version: sha256:50e28562821c757f54bea3967715dd84c0777206b2644b922cba5cbe0ca9c843
date_precision: date-only
reviewed_by: Codex
reviewed_at: '2026-10-24'
reviewed_content_sha256: 84ae94f7b7a280c37e5c1fd95bd3dae02dd4bbf573f3996ac980c19c39e5b920
---

# Anthropic与Theorem披露123库形式证明，保证范围仍受规格与机器模型约束

## Key Takeaways

Anthropic于10月22日披露与Theorem合作：Claude对123个OSS-Fuzz库的239个入口，在修复发现问题后生成Rocq证明。增量是把已有fuzz入口转为针对编译后RISC-V二进制的无崩溃规格，再由独立证明检查器检查。

## Detailed Notes

保证限于小于64MB输入、单线程静态RISC-V Linux、固定内存预算及建模的系统响应；未覆盖全部入口、所有ASan漏检或调用方误用，规格和机器语义本身仍需可信。不能写成这些库完全无bug或任意x86/ARM生产部署已安全。

能力结果为研究团队披露；小任务对比使用36个任务、每任务3次独立单Agent尝试、每次5M token预算。模型效率比较为Opus 5.5对Opus 5的特定子实验，未转作一般代码能力排名。大规模实验的完整模型配置、总预算与公开证明复核尚缺。

## Evidence

[原始来源](https://www.anthropic.com/research/formal-verification)；原始版本 `raw/2026-10-24/50e28562821c757f54bea3967715dd84c0777206b2644b922cba5cbe0ca9c843.body`，SHA-256 `50e28562821c757f54bea3967715dd84c0777206b2644b922cba5cbe0ca9c843`。

官方Introduction、Turning tests into proofs、Finding/fixing、成本与复用子实验、Limitations及脚注已读；附录、证明仓库和Rocq独立执行未审。不是独立复现。

## Questions Raised

判断：当证明生成成本下降，安全验证服务可从抽样测试扩展到可检查的限定保证，规格工程与可信语义成为重要环节。反例是证明了错误规格、修改代码取巧或维护成本过高。观察独立检查通过、补丁功能保真、目标平台覆盖与每个有效保证的全成本。
