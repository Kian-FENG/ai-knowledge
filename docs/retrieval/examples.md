# 查询与入库回查示例

以下命令从项目根执行；其中 `PAGE` 使用实际命中的路径或 ID，不凭空猜路径。

## 按问题查询

```bash
scripts/python scripts/query.py "DeepSeek Qwen Kimi 模型能力" -n 8 --json
scripts/python scripts/query.py "推理成本" --domain infra --domain hardware --tfidf --json
scripts/python scripts/get_page.py PAGE --follow-sources --json
```

两次 `--domain` 表示 infra 或 hardware；加 `--type paper` 则同时要求论文类型。
读取命中正文后，再沿 evidence 读取来源。比较时保留模型版本、测试主体和限制。
“最新”还需在线核验；命令只覆盖本地知识，不等同于实时全网搜索。

## 浏览已入库的公司与资料

```bash
scripts/python scripts/query.py --type entity --domain companies -n 20 --json
scripts/python scripts/query.py --type source --type paper --domain infra --paths-only
```

不带关键词时返回满足过滤条件的已发布页，按路径排序，分数为 0；不是可信度或时间排名。
结果仍受 `-n` 限制。公司、模型、产品均可为 entity，具体身份查看 `entity_kind`。

## 从页面追溯原文

```bash
scripts/python scripts/get_page.py entity-volantis --follow-sources --json
scripts/python scripts/get_page.py reference/sources/volantis-series-a-20261001.md --follow-sources --json
scripts/python scripts/grep_wiki.py "Volantis" -i --json
```

这些页面是现有库内示例；使用时读取它们当前内容，不把示例当作新的在线核验。
如果返回 raw 路径，另行读取该文件并对照来源版本。来源可读不代表它支持所有相邻结论。

## 入库查重与发布后回查

```bash
scripts/python scripts/query.py "来源标题或对象别名" --include-unpublished --json
scripts/python scripts/grep_wiki.py "https://example.org/article" --include-unpublished --json
```

grep 只搜索正文；frontmatter 中的 URL、raw_path、sha256 还需检查元数据和归档记录。
不能因正文无 URL 命中就重复建页。`--include-unpublished` 是有意查重，不能用于把草稿
伪装成已发布结论。审核发布后去掉该选项：

```bash
scripts/python scripts/query.py "本次页面标题或别名" --json
scripts/python scripts/get_page.py PAGE --follow-sources --json
```

完成标准：页面在默认查询中可见，状态是 published，来源关系能定位到实际读过的证据。
若用户只要求起草，页面应保持不出现在默认查询中，并在交付时说明。
