# CaseB_Crawler

这是一个基于 **Hermes Agent** 的爬虫案例项目，用来展示在个人研究场景下，如何组合不同网页抓取工具、MCP、Skill 与 Excel 生成脚本，完成公开网页与微信公众号公开文章的信息检索、提取、整理和交付。

English intro: This repository is a Hermes Agent crawler case study for personal research. It demonstrates how to combine built-in web tools, MCP servers, Skills, browser-based extraction, and Python Excel scripts to collect public web / WeChat article information and organize the results into structured spreadsheets.

> 本项目仅用于学习与个人研究。请遵守目标网站/平台的 robots.txt、服务条款、版权、隐私与当地法律法规；不要高频请求、不要抓取非公开数据、不要绕过强访问控制或验证码。

## 项目做了什么

如想复刻，请参考教程：https://github.com/shortyZhou/Hermes/blob/main/7.%20%E6%A1%88%E4%BE%8B%EF%BC%9A%E7%88%AC%E8%99%AB.pdf

### A. 直接爬取网站 / 网页内容

适用于已知目标网站或网页 URL 的场景，例如公司官网、行业资讯页、单篇微信公众号网页版文章等。

使用方式：

1. 先用 Hermes 内置 `web_search` / `web_extract` 获取公开网页文本。
2. 如果内容缺失，再用浏览器渲染、CSS 选择器定位或动态抓取工具补充。
3. 将抓取结果整理为结构化表格，输出到 Excel。

对应文件：

- Workflow prompt：`prompts/A_prompt.md`
- 结果生成脚本：`create_result_python/create_A_result_1.py`、`create_result_python/create_A_result_2.py`
- 结果表格：`results/A_result_1.xlsx`、`results/A_result_2.xlsx`

### B. 基于搜狗微信搜索跨公众号检索

适用于不知道具体公众号后台数据、只想按关键词搜索微信公众号公开文章的场景。

使用方式：

1. 通过 `dsh-wechat-mp-search` MCP 调用搜狗微信搜索。
2. 自动翻页获取候选文章。
3. 对相关结果读取文章正文。
4. 提取价格、产量、消费、进出口等主题信息。
5. 整理为 Excel。

对应文件：

- Workflow prompt：`prompts/B_prompt.md`
- 结果生成脚本：`create_result_python/create_B_result.py`
- 结果表格：`results/B_result.xlsx`

### C. 基于微信公众平台官方后台/API 的公众号检索

适用于知道公众号名称，并且愿意通过自己的微信公众号后台扫码登录、合法获取访问凭证的场景。

使用方式：

1. 使用 `wechat-search` CLI 扫码登录微信公众平台。
2. 搜索目标公众号并获取 `fakeid`。
3. 按较低频率抓取该公众号近期文章。
4. 提取用户指定主题信息。

对应文件：

- Workflow prompt：`prompts/C_prompt.md`

## 仓库结构

```text
.
├── prompts/                         # 三类爬虫 workflow prompt 与 SOUL 示例
│   ├── A_prompt.md
│   ├── B_prompt.md
│   ├── C_prompt.md
│   ├── SOUL.md
│   └── SOUL2.md
├── create_result_python/             # 将提取结果整理为 Excel 的 Python 脚本
│   ├── create_A_result_1.py
│   ├── create_A_result_2.py
│   └── create_B_result.py
├── results/                          # 案例输出 Excel
│   ├── A_result_1.xlsx
│   ├── A_result_2.xlsx
│   └── B_result.xlsx
├── .hermes/                          # 项目级 Hermes 插件 / Skill 配置
│   ├── plugins/
│   └── skills/
├── start-hermes-project-plugins.bat   # Windows 启动入口
├── start-hermes-project-plugins.sh    # Bash 启动入口
└── .gitignore                         # 排除本地环境、缓存、日志、依赖副本
```

## 已安装 / 使用但 GitHub 页面上可能看不到的工具

GitHub 只显示被 Git 跟踪的文件。为了避免把虚拟环境、缓存、日志和依赖副本上传，以下内容被 `.gitignore` 排除了，因此你在本地能看到，但 GitHub repo 页面上不会直接显示。

### 1. Hermes Agent 内置工具

这些不是 repo 代码，而是 Hermes Agent 运行环境自带能力：

| 工具 | 用途 | 来源 |
|---|---|---|
| `web_search` | 搜索公开网页信息 | https://hermes-agent.nousresearch.com/docs/user-guide/features/tools |
| `web_extract` | 抽取网页 / PDF 文本内容 | https://hermes-agent.nousresearch.com/docs/user-guide/features/tools |
| Browser / Preview / browser automation tools | 打开网页、渲染页面、定位动态内容 | https://hermes-agent.nousresearch.com/docs |
| file / terminal / skills / MCP tools | 文件读写、命令执行、Skill 与 MCP 调用 | https://hermes-agent.nousresearch.com/docs |

### 2. Scrapling CLI 与 Scrapling Skill

| 项目 | 本地状态 | 用途 | 来源 |
|---|---|---|---|
| `scrapling` CLI | 安装在 Hermes Agent Python 环境中；本地检测版本为 `0.4.15` | 静态抓取、动态页面抓取、stealth 模式、反爬场景下的轻量补充方案 | https://github.com/D4Vinci/Scrapling |
| `scrapling` Skill | 项目级 Skill 文件已提交：`.hermes/skills/research/scrapling/SKILL.md` | 给 Agent 提供 Scrapling 使用流程、命令、注意事项 | https://github.com/D4Vinci/Scrapling |

注意：Scrapling CLI 的安装包和浏览器依赖不应提交到 GitHub；repo 里只保留 Skill 使用说明和 workflow prompt。

### 3. `mcp-webscraper` MCP

| 项目 | 本地状态 | 用途 | 来源 |
|---|---|---|---|
| `mcp-webscraper` | 项目级 Hermes 插件配置已提交；其 `_vendor/` 依赖目录被忽略 | 通过 MCP 提供静态抓取、动态抓取、批量抓取、网站 crawl 等能力 | https://github.com/samirsaci/mcp-webscraper |

已提交的配置 / 源码入口：

- `.hermes/plugins/mcp-webscraper/plugin.json`
- `.hermes/plugins/mcp-webscraper/mcp.json`
- `.hermes/plugins/mcp-webscraper/server/run_server.py`
- `.hermes/plugins/mcp-webscraper/server/scrapping.py`
- `.hermes/plugins/mcp-webscraper/server/pyproject.toml`
- `.hermes/plugins/mcp-webscraper/server/requirements.txt`

没有上传的本地内容：

- `.hermes/plugins/mcp-webscraper/server/_vendor/`
- `.hermes/plugins/mcp-webscraper/server/.venv/`
- `.hermes/plugins/mcp-webscraper/server/scraping_server.log`

这些都是依赖副本、虚拟环境或运行日志，可以通过 `pyproject.toml` / `requirements.txt` 重新安装，不适合放进 GitHub。

### 4. `dsh-wechat-mp-search` MCP

| 项目 | 本地状态 | 用途 | 来源 |
|---|---|---|---|
| `dsh-wechat-mp-search` | 项目级 Hermes 插件配置已提交；运行时通过 `npx -y dsh-wechat-mp-search@0.1.0` 启动 | 通过搜狗微信搜索微信公众号公开文章，并读取文章正文 | npm: https://www.npmjs.com/package/dsh-wechat-mp-search；GitHub: https://github.com/iTraceur/dsh-wechat-mp-search |

已提交的配置：

- `.hermes/plugins/dsh-wechat-mp-search/plugin.json`
- `.hermes/plugins/dsh-wechat-mp-search/mcp.json`

注意：npm 包本体不在 repo 内，因为它由 `npx` 运行时拉取。

### 5. `wechat-search` CLI / `wechat-search-skill`

| 项目 | 本地状态 | 用途 | 来源 |
|---|---|---|---|
| `wechat-search.exe` | 安装在本地 `.venv/Scripts/`，该目录被 `.gitignore` 忽略 | 登录微信公众平台、搜索公众号、抓取目标公众号文章列表与正文 | https://github.com/qbu11/weixin-public-account-skill |
| `wechat-search-skill==1.0.0` | 安装在本地 `.venv/Lib/site-packages/`，未上传 | `wechat-search` CLI 对应的 Python 包 / Skill 数据 | https://github.com/qbu11/weixin-public-account-skill |

为什么 GitHub 看不到：

- `.venv/` 是本机 Python 虚拟环境，包含大量第三方包和可执行文件。
- 这些内容应通过安装命令重建，而不是提交到仓库。

### 6. `wechat-article-spider` MCP / CLI 相关配置

| 项目 | 本地状态 | 用途 | 来源 |
|---|---|---|---|
| `wechat-article-spider` | Hermes crawler profile 中仍有启用记录；当前 repo 下未发现完整 `.hermes/plugins/wechat-article-spider/` 目录 | 微信公众号文章搜索、读取、文章列表查询等；与 `wechat-search` 属于同一类微信公众平台 API 工作流 | https://github.com/qbu11/wechat-article-spider |

当前检测到的 profile 配置指向：

```text
C:/Users/24779/Desktop/AI related/CaseB_Crawler/.hermes/plugins/wechat-article-spider/server/server.py
```

但当前仓库工作区没有这个完整目录。因此 README 中把它标为“profile 中配置过 / 曾启用过”，而不是标为“repo 内已提交”。如果后续要继续使用，需要重新安装或恢复对应 `.hermes/plugins/wechat-article-spider/` 目录。

## 被 `.gitignore` 排除的本地内容

当前 `.gitignore` 主要排除了：

```gitignore
.venv/
__pycache__/
*.py[cod]
crawl_tmp/
*.log
.env
.env.*
*.pem
*.key
*.p12
*.pfx
.hermes/plugins/mcp-webscraper/server/_vendor/
```

这些内容不上传的原因：

- `.venv/`：本地 Python 虚拟环境，可重建，体积大。
- `crawl_tmp/`：抓取缓存和临时渲染结果，可能包含临时页面文本，不适合作为正式交付。
- `*.log`：运行日志，可能包含本机路径或临时调试信息。
- `_vendor/`：插件依赖副本，可由依赖清单重建。
- `.env` / key 文件：可能包含密钥，必须避免提交。

## 合规与风险提示

- 本 repo 的示例目标以公开网页 / 公开文章为主。
- 对会员登录、验证码、强访问控制页面，不应默认绕过；需要合法授权或人工介入。
- 微信相关工具可能涉及平台访问限制，必须低频请求。
- 微信 `real_url` 可能有时效性，历史结果仅作为案例参考。
- Excel 结果中对图片走势图、OCR 或视觉近似值已标注不确定性；不应当作精确官方数据。
