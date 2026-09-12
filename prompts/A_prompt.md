【任务】
用户指定要爬取的网站/网页，使用 Hermes 的网页抓取能力配合 Scrapling CLI、Scrapling skill 和 mcp-webscraper，检索并提取指定内容。

【执行步骤】
1. 使用 `web_extract` 工具尝试抓取指定的网站/网页信息，输出为 Markdown 格式。
2. 分析抓取结果。
3. 如果 `web_extract` 返回的内容不完整或缺失信息，使用 `browser_navigate` 和 `browser_snapshot` 工具查看页面结构，定位相关内容的 CSS 选择器。
4. 如果页面是 JavaScript 动态渲染的，使用 Scrapling 的 `dynamic` 或 `stealth` 模式重新抓取。
5. 将提取到的信息整理为结构化的 Markdown 格式输出。
6. 把 Markdown 格式的输出打印到当前会话框。

【重要提醒】
- 默认使用谷歌浏览器打开网址。
- 请求间隔建议保持 3-5 秒，避免对目标网站造成负担。
- 仅用于个人研究，不要公开分享或用于商业用途。
- 如果遇到反爬机制，优先尝试 Scrapling skill 的 stealth 模式。
