【任务】
使用 dsh-wechat-mp-search MCP 工具，通过搜狗微信搜索，按用户要求检索相关的微信公众号文章。检索自动翻 3 页即可。对检符合要求的文章，获取标题和正文中用户想要的内容。如果没有符合要求的文章，也要如实反馈给用户。

【可用工具】
- MCP 工具（Hermes 中已配置 dsh-wechat-mp-search）：
  - weixin_search_all：自动翻页搜索
  - get_weixin_article_content：获取文章正文

【执行步骤】
1. 确认 MCP 连接正常：
   在 Hermes 中运行 `/reload-mcp`，确认工具列表中有 `mcp__dsh-wechat-mp-search__weixin_search_all` 和 `mcp__dsh-wechat-mp-search__get_weixin_article_content`。

2. 执行搜索（自动翻 3 页）：
   调用 `weixin_search_all`，参数：
   - max_pages = 3
   每个查询都设置 max_pages = 3，但总共不要超过 6 页请求。

3. 对搜索结果中的每篇文章，调用 `get_weixin_article_content` 获取正文：
   - 参数 real_url = 搜索结果中的 real_url
   - referer = 搜索结果中的 link（可选，建议带上）

4. 对获取到的每篇正文，进行概述：
   - 用 2-3 句话说明文章的主题和核心内容。
   - 重点关注价格、产量、消费、进出口量相关的信息。
   - 如果文章与主题无关，可以跳过或简要说明。

5. 输出格式：
   按文章发布时间从新到旧排列，每篇包含：
   - 标题
   - 发布时间
   - 相关内容
   - 原文链接（real_url）

【重要限制】
- 请求间隔至少 3 秒，翻页间隔至少 3 秒。
- 同一关键词一天内采集不要超过 50 页。
- 仅用于个人学习研究，控制请求频率，不公开分享数据。
- real_url 有时效性，获取正文后尽快处理。