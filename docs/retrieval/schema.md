# Retrieval schema

保留 LLM-Wiki 的八类：concept/source/paper/entity/technique/pattern/note/comparison。
domain 从 tags/domains.yaml 选择 1–2 个；summary、aliases 帮助中文和英文检索。
公司、模型、产品、社区用 entity_kind 区分；不要创建同一实体的重复中英文页面。

生命周期为 draft → reviewed → published，deprecated 退出默认读取。
证据来源 reported/derived/measured/unknown 与核验 unchecked/source-checked/replicated
独立。legacy confidence 只用于兼容过滤，不参与可信度加权。

sources、related、supersedes、applies_to、正文 wikilinks 使用统一解析器：
精确 ID、路径、唯一标题、alias、slug；歧义不猜，显式坏路径不回退。
specializes 只允许 concept ID，specialized_by 由读者生成。
--follow-sources 返回带类型的关系与 locator，不等于已阅读来源。

query JSON 状态为 success/empty/invalid-input；get_page 返回 metadata、body、freshness，
未发布或缺失为 not-found。所有工具和六个索引默认只含 published。
--tfidf 为词法向量，--semantic 仅兼容别名；中文 bigram 与可维护的词组别名共同召回。
所有日期采用真实日期，staleness 以 last_verified 和 data/refresh-cutoff.yaml 计算，
可传 --as-of；不拿 created/updated 当核验日期。
