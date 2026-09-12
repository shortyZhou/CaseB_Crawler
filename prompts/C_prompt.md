【任务】
使用 wechat-search 工具和相关 Skill，检索公众号用户指定公众号的指定内容。不要批量爬取其他公众号。

【可用工具】
- wechat-search CLI
- weixin-public-account-skill
- 其他任何适配的工具

【执行步骤】
1. 确认登录状态：
   执行 `wechat-search status`，如果未登录或凭证过期，执行 `wechat-search login` 并扫码登录。

2. 搜索目标公众号，获取 fakeid：
   执行 `wechat-search search` `用户指定公众号名称`
   从返回结果中记录 fakeid。

3. 爬取最近一周的文章（含正文）：
   执行 `wechat-search scrape` `用户指定公众号名称` --`用户想要的操作`

4. 对取出的文章，提取用户想要的内容

【重要限制】
- 请求间隔必须 ≥ 3 分钟，严禁高频请求。
- 仅用于个人研究，不要公开分享或用于商业用途。
- 不要爬取除用户指定公众号以外的其他公众号。