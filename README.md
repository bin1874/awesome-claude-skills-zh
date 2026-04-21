<h1 align="center">Awesome Claude Skills（中文版）</h1>

<p align="center">
  <strong>📖 本项目是 <a href="https://github.com/ComposioQ/awesome-claude-skills">awesome-claude-skills</a> 的中文翻译版本</strong>
</p>

<p align="center">
<a href="https://platform.composio.dev/?utm_source=Github&utm_medium=Youtube&utm_campaign=2025-11&utm_content=AwesomeSkills">
  <img width="1280" height="640" alt="Composio banner" src="https://github.com/user-attachments/assets/e91255af-e4ba-4d71-b1a8-bd081e8a234a">
</a>


</p>

<p align="center">
  <a href="https://awesome.re">
    <img src="https://awesome.re/badge.svg" alt="Awesome" />
  </a>
  <a href="https://makeapullrequest.com">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome" />
  </a>
  <a href="https://www.apache.org/licenses/LICENSE-2.0">
    <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square" alt="License: Apache-2.0" />
  </a>
</p>
<div>
<p align="center">
  <a href="https://twitter.com/composio">
    <img src="https://img.shields.io/badge/Follow on X-000000?style=for-the-badge&logo=x&logoColor=white" alt="Follow on X" />
  </a>
  <a href="https://www.linkedin.com/company/composiohq/">
    <img src="https://img.shields.io/badge/Follow on LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Follow on LinkedIn" />
  </a>
  <a href="https://discord.com/invite/composio">
    <img src="https://img.shields.io/badge/Join our Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Join our Discord" />
  </a>
  </p>
</div>

精选的实用 Claude Skills 列表，用于提升 Claude.ai、Claude Code 和 Claude API 的生产力。


> **需要超越文本生成的技能？** Claude 可以发送邮件、创建 Issue、发布到 Slack，并在 1000+ 应用中执行操作。[了解如何使用 →](./connect/)

---

## 快速开始：将 Claude 连接到 500+ 应用

**connect-apps** 插件让 Claude 执行真实操作 - 发送邮件、创建 Issue、发布到 Slack。它在底层使用 Composio 处理认证并连接到 500+ 应用。

### 1. 安装插件

```bash
claude --plugin-dir ./connect-apps-plugin
```

### 2. 运行设置

```
/connect-apps:setup
```

在询问时粘贴你的 API 密钥。（在 [platform.composio.dev](https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills) 获取免费密钥）

### 3. 重启并试用

```bash
exit
claude
```

> **需要超越文本生成的技能？** Claude 可以发送邮件、创建 Issue、发布到 Slack，并在 1000+ 应用中执行操作。[了解如何使用 →](./connect/)

如果你收到邮件，说明 Claude 现在已连接到 500+ 应用。

**[查看所有支持的应用 →](https://composio.dev/toolkits)**

---

## 目录

- [什么是 Claude Skills？](#什么是-claude-skills)
- [技能列表](#技能列表)
  - [文档处理](#文档处理)
  - [开发与代码工具](#开发与代码工具)
  - [数据与分析](#数据与分析)
  - [商业与营销](#商业与营销)
  - [沟通与写作](#沟通与写作)
  - [创意与媒体](#创意与媒体)
  - [生产力与组织](#生产力与组织)
  - [协作与项目管理](#协作与项目管理)
  - [安全与系统](#安全与系统)
  - [通过 Composio 的应用自动化](#通过-composio-的应用自动化)
- [入门指南](#入门指南)
- [创建技能](#创建技能)
- [贡献指南](#贡献指南)
- [资源](#资源)
- [许可证](#许可证)

## 什么是 Claude Skills？

Claude Skills 是可定制的工作流程，教会 Claude 根据你的独特需求执行特定任务。Skills 让 Claude 能够在所有 Claude 平台上以可重复、标准化的方式执行任务。

## 技能列表

### 文档处理

- [docx](https://github.com/anthropics/skills/tree/main/skills/docx) - 创建、编辑、分析 Word 文档，支持修订追踪、批注、格式化。
- [pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) - 提取文本、表格、元数据，合并与批注 PDF。
- [pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) - 读取、生成和调整幻灯片、布局、模板。
- [xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx) - 电子表格操作：公式、图表、数据转换。
- [Markdown to EPUB Converter](https://github.com/smerchek/claude-epub-skill) - 将 Markdown 文档和聊天摘要转换为专业的 EPUB 电子书文件。*作者 [@smerchek](https://github.com/smerchek)*

### 开发与代码工具

- [artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) - 使用现代前端 Web 技术（React、Tailwind CSS、shadcn/ui）创建复杂多组件 claude.ai HTML artifacts 的工具套件。
- [aws-skills](https://github.com/zxkane/aws-skills) - AWS 开发，包含 CDK 最佳实践、成本优化 MCP 服务器，以及无服务器/事件驱动架构模式。
- [Changelog Generator](./changelog-generator/) - 通过分析 git 历史记录，自动从 git 提交创建面向用户的变更日志，将技术性提交转换为用户友好的发布说明。
- [Claude Code Terminal Title](https://github.com/bluzername/claude-code-terminal-title) - 为每个 Claude-Code 终端窗口设置动态标题，描述正在进行的工作，让你不会混淆各窗口的任务。
- [D3.js Visualization](https://github.com/chrisvoncsefalvay/claude-d3js-skill) - 教会 Claude 生成 D3 图表和交互式数据可视化。*作者 [@chrisvoncsefalvay](https://github.com/chrisvoncsefalvay)*
- [FFUF Web Fuzzing](https://github.com/jthack/ffuf_claude_skill) - 集成 ffuf Web 模糊测试工具，让 Claude 可以运行模糊测试任务并分析漏洞结果。*作者 [@jthack](https://github.com/jthack)*
- [finishing-a-development-branch](https://github.com/obra/superpowers/tree/main/skills/finishing-a-development-branch) - 通过呈现清晰选项并处理选定的工作流程，指导完成开发工作。
- [iOS Simulator](https://github.com/conorluddy/ios-simulator-skill) - 让 Claude 能够与 iOS 模拟器交互，用于测试和调试 iOS 应用。*作者 [@conorluddy](https://github.com/conorluddy)*
- [jules](https://github.com/sanjay3290/ai-skills/tree/main/skills/jules) - 将编码任务委托给 Google Jules AI 智能体，用于 GitHub 仓库的异步 Bug 修复、文档编写、测试和功能实现。*作者 [@sanjay3290](https://github.com/sanjay3290)*
- [LangSmith Fetch](./langsmith-fetch/) - 通过自动从 LangSmith Studio 获取和分析执行追踪来调试 LangChain 和 LangGraph 智能体。首个用于 Claude Code 的 AI 可观测性技能。*作者 [@OthmanAdi](https://github.com/OthmanAdi)*
- [MCP Builder](./mcp-builder/) - 指导创建高质量的 MCP（Model Context Protocol）服务器，用于将外部 API 和服务与 LLM 集成，支持 Python 或 TypeScript。
- [move-code-quality-skill](https://github.com/1NickPappas/move-code-quality-skill) - 根据官方 Move Book 代码质量检查清单分析 Move 语言包，检查 Move 2024 Edition 合规性和最佳实践。
- [Playwright Browser Automation](https://github.com/lackeyjb/playwright-skill) - 模型调用的 Playwright 自动化，用于测试和验证 Web 应用。*作者 [@lackeyjb](https://github.com/lackeyjb)*
- [prompt-engineering](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/customaize-agent/skills/prompt-engineering) - 教授知名的提示词工程技术和模式，包括 Anthropic 最佳实践和智能体说服原则。
- [pypict-claude-skill](https://github.com/omkamal/pypict-claude-skill) - 使用 PICT（成对独立组合测试）为需求或代码设计全面的测试用例，生成具有成对覆盖的优化测试套件。
- [reddit-fetch](https://github.com/ykdojo/claude-code-tips/tree/main/skills/reddit-fetch) - 当 WebFetch 被阻止或返回 403 错误时，通过 Gemini CLI 获取 Reddit 内容。
- [Skill Creator](./skill-creator/) - 提供创建有效 Claude Skills 的指导，扩展具有专业知识、工作流程和工具集成的能力。
- [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) - 在几分钟内自动将任何文档网站转换为 Claude AI 技能。*作者 [@yusufkaraaslan](https://github.com/yusufkaraaslan)*
- [software-architecture](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/ddd/skills/software-architecture) - 实现设计模式，包括整洁架构（Clean Architecture）、SOLID 原则和全面的软件设计最佳实践。
- [subagent-driven-development](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/sadd/skills/subagent-driven-development) - 派遣独立的子智能体执行单独任务，在迭代之间设置代码审查检查点，实现快速、受控的开发。
- [test-driven-development](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) - 在实现任何功能或修复 Bug 时使用，在编写实现代码之前使用。
- [using-git-worktrees](https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/) - 创建隔离的 git worktree，具有智能目录选择和安全验证。
- [Connect](./connect/) - 将 Claude 连接到任何应用。发送邮件、创建 Issue、发布消息、更新数据库 - 在 Gmail、Slack、GitHub、Notion 和 1000+ 服务中执行真实操作。
- [Webapp Testing](./webapp-testing/) - 使用 Playwright 测试本地 Web 应用，验证前端功能、调试 UI 行为并截取屏幕截图。

### 数据与分析

- [CSV Data Summarizer](https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill) - 自动分析 CSV 文件并生成带有可视化的全面洞察，无需用户提示。*作者 [@coffeefuelbump](https://github.com/coffeefuelbump)*
- [deep-research](https://github.com/sanjay3290/ai-skills/tree/main/skills/deep-research) - 使用 Gemini Deep Research Agent 执行自主多步骤研究，用于市场分析、竞争格局和文献综述。*作者 [@sanjay3290](https://github.com/sanjay3290)*
- [postgres](https://github.com/sanjay3290/ai-skills/tree/main/skills/postgres) - 对 PostgreSQL 数据库执行安全的只读 SQL 查询，支持多连接和纵深防御安全策略。*作者 [@sanjay3290](https://github.com/sanjay3290)*
- [root-cause-tracing](https://github.com/obra/superpowers/tree/main/skills/root-cause-tracing) - 当错误发生在执行深处时使用，需要追溯找到原始触发点。

### 商业与营销

- [Brand Guidelines](./brand-guidelines/) - 将 Anthropic 官方品牌颜色和字体应用到 artifacts，确保一致的视觉识别和专业的设计标准。
- [Competitive Ads Extractor](./competitive-ads-extractor/) - 从广告库中提取和分析竞争对手的广告，了解产生共鸣的信息传递和创意方法。
- [Domain Name Brainstormer](./domain-name-brainstormer/) - 生成创意域名想法，并检查多个 TLD 的可用性，包括 .com、.io、.dev 和 .ai 扩展名。
- [Internal Comms](./internal-comms/) - 帮助撰写内部沟通内容，包括 3P 更新、公司通讯、FAQ、状态报告和项目更新，使用公司特定格式。
- [Lead Research Assistant](./lead-research-assistant/) - 通过分析你的产品、搜索目标公司并提供可执行的推广策略，识别和筛选高质量线索。

### 沟通与写作

- [article-extractor](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/article-extractor) - 从网页中提取完整文章文本和元数据。
- [brainstorming](https://github.com/obra/superpowers/tree/main/skills/brainstorming) - 通过结构化提问和替代方案探索，将粗略想法转化为成熟设计。
- [Content Research Writer](./content-research-writer/) - 通过进行研究、添加引用、改进开头和提供分段反馈来协助撰写高质量内容。
- [family-history-research](https://github.com/emaynard/claude-family-history-research-skill) - 提供家族历史和家谱研究项目的规划协助。
- [Meeting Insights Analyzer](./meeting-insights-analyzer/) - 分析会议转录，揭示行为模式，包括冲突回避、发言比例、填充词和领导风格。
- [NotebookLM Integration](https://github.com/PleasePrompto/notebooklm-skill) - 让 Claude Code 直接与 NotebookLM 聊天，获取基于上传文档的源依据答案。*作者 [@PleasePrompto](https://github.com/PleasePrompto)*
- [Twitter Algorithm Optimizer](./twitter-algorithm-optimizer/) - 使用 Twitter 开源算法洞察分析和优化推文以获得最大触达。重写和编辑推文以提高参与度和可见性。

### 创意与媒体

- [Canvas Design](./canvas-design/) - 使用设计理念和美学原则在 PNG 和 PDF 文档中创建精美的视觉艺术，用于海报、设计和静态作品。
- [imagen](https://github.com/sanjay3290/ai-skills/tree/main/skills/imagen) - 使用 Google Gemini 的图像生成 API 生成图像，用于 UI 模型、图标、插图和视觉资产。*作者 [@sanjay3290](https://github.com/sanjay3290)*
- [Image Enhancer](./image-enhancer/) - 通过提高分辨率、锐度和清晰度来改善图像和截图质量，用于专业演示和文档。
- [Slack GIF Creator](./slack-gif-creator/) - 创建针对 Slack 优化的动态 GIF，包含大小约束验证器和可组合动画基元。
- [Theme Factory](./theme-factory/) - 将专业字体和颜色主题应用到 artifacts，包括幻灯片、文档、报告和 HTML 落地页，提供 10 种预设主题。
- [Video Downloader](./video-downloader/) - 从 YouTube 和其他平台下载视频，用于离线观看、编辑或归档，支持多种格式和质量选项。
- [youtube-transcript](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/youtube-transcript) - 从 YouTube 视频获取转录并准备摘要。

### 生产力与组织

- [File Organizer](./file-organizer/) - 通过理解上下文、查找重复项和建议更好的组织结构，智能地组织文件和文件夹。
- [Invoice Organizer](./invoice-organizer/) - 通过读取文件、提取信息和一致地重命名，自动组织发票和收据以准备税务。
- [kaizen](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/kaizen/skills/kaizen) - 应用持续改进方法论，采用多种分析方法，基于日本改善（Kaizen）理念和精益方法论。
- [n8n-skills](https://github.com/haunchen/n8n-skills) - 让 AI 助手直接理解和操作 n8n 工作流。
- [Raffle Winner Picker](./raffle-winner-picker/) - 从列表、电子表格或 Google Sheets 中随机选择抽奖和竞赛的获胜者，使用加密安全的随机性。
- [Tailored Resume Generator](./tailored-resume-generator/) - 分析职位描述并生成定制简历，突出相关经验、技能和成就，最大化面试机会。
- [ship-learn-next](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/ship-learn-next) - 帮助迭代决定下一步构建或学习什么，基于反馈循环。
- [tapestry](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/tapestry) - 将相关文档互连并摘要为知识网络。

### 协作与项目管理

- [git-pushing](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/git-pushing) - 自动化 git 操作和仓库交互。
- [google-workspace-skills](https://github.com/sanjay3290/ai-skills/tree/main/skills) - Google Workspace 集成套件：Gmail、日历、Chat、Docs、Sheets、Slides 和 Drive，支持跨平台 OAuth。*作者 [@sanjay3290](https://github.com/sanjay3290)*
- [outline](https://github.com/sanjay3290/ai-skills/tree/main/skills/outline) - 在 Outline wiki 实例（云端或自托管）中搜索、读取、创建和管理文档。*作者 [@sanjay3290](https://github.com/sanjay3290)*
- [review-implementing](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/review-implementing) - 评估代码实现计划并与规格对齐。
- [test-fixing](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/test-fixing) - 检测失败的测试并提出补丁或修复。

### 安全与系统

- [computer-forensics](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/computer-forensics) - 数字取证分析和调查技术。
- [file-deletion](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/file-deletion) - 安全文件删除和数据清理方法。
- [metadata-extraction](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/metadata-extraction) - 提取和分析文件元数据用于取证目的。
- [threat-hunting-with-sigma-rules](https://github.com/jthack/threat-hunting-with-sigma-rules-skill) - 使用 Sigma 检测规则搜寻威胁并分析安全事件。

### 通过 Composio 的应用自动化

通过 [Composio](https://composio.dev) 为 78 个 SaaS 应用提供的预构建工作流技能。每个技能包含工具序列、参数指导、已知陷阱和快速参考表 — 全部使用从 Composio API 发现的真实工具。

> **注意**：这些技能需要通过 Composio 平台使用，请访问 [Composio Skills](https://github.com/ComposioQ/awesome-claude-skills/tree/main/skills/composio-skills) 获取完整列表和详细说明。

**CRM 与销售**：Close、HubSpot、Pipedrive、Salesforce、Zoho CRM

**项目管理**：Asana、Basecamp、ClickUp、Jira、Linear、Monday.com、Notion、Todoist、Trello、Wrike

**沟通**：Discord、Intercom、Microsoft Teams、Slack、Telegram、WhatsApp

**邮件**：Gmail、Outlook、Postmark、SendGrid

**代码与 DevOps**：Bitbucket、CircleCI、Datadog、GitHub、GitLab、PagerDuty、Render、Sentry、Supabase、Vercel

**存储与文件**：Box、Dropbox、Google Drive、OneDrive

**电子表格与数据库**：Airtable、Coda、Google Sheets

**日历与调度**：Cal.com、Calendly、Google Calendar、Outlook Calendar

**社交媒体**：Instagram、LinkedIn、Reddit、TikTok、Twitter/X、YouTube

**营销与邮件营销**：ActiveCampaign、Brevo、ConvertKit、Klaviyo、Mailchimp

**支持与帮助台**：Freshdesk、Freshservice、Help Scout、Zendesk

**电商与支付**：Shopify、Square、Stripe

**设计与协作**：Canva、Confluence、DocuSign、Figma、Miro、Webflow

**分析与数据**：Amplitude、Google Analytics、Mixpanel、PostHog、Segment

**人力资源**：BambooHR

**自动化平台**：Make (Integromat)

**会议**：Zoom

## 入门指南

### 在 Claude.ai 中使用技能

1. 点击聊天界面中的技能图标（🧩）。
2. 从市场添加技能或上传自定义技能。
3. Claude 根据你的任务自动激活相关技能。

### 在 Claude Code 中使用技能

1. 将技能放在 `~/.config/claude-code/skills/`：
   ```bash
   mkdir -p ~/.config/claude-code/skills/
   cp -r skill-name ~/.config/claude-code/skills/
   ```

2. 验证技能元数据：
   ```bash
   head ~/.config/claude-code/skills/skill-name/SKILL.md
   ```

3. 启动 Claude Code：
   ```bash
   claude
   ```

4. 技能自动加载并在相关时激活。

### 通过 API 使用技能

使用 Claude Skills API 以编程方式加载和管理技能：

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    skills=["skill-id-here"],
    messages=[{"role": "user", "content": "Your prompt"}]
)
```

详见 [Skills API 文档](https://docs.claude.com/en/api/skills-guide)。

## 创建技能

### 技能结构

每个技能是一个包含 `SKILL.md` 文件的文件夹，带有 YAML frontmatter：

```
skill-name/
├── SKILL.md          # 必需：技能说明和元数据
├── scripts/          # 可选：辅助脚本
├── templates/        # 可选：文档模板
└── resources/        # 可选：参考文件
```

### 基础技能模板

```markdown
---
name: my-skill-name
description: 清晰描述此技能的功能和使用时机。
---

# My Skill Name

技能用途和能力的详细描述。

## 何时使用此技能

- 用例 1
- 用例 2
- 用例 3

## 说明

[Claude 如何执行此技能的详细说明]

## 示例

[展示技能实际应用的示例]
```

### 技能最佳实践

- 聚焦于特定的、可重复的任务
- 包含清晰的示例和边缘情况
- 为 Claude 编写说明，而非最终用户
- 在 Claude.ai、Claude Code 和 API 上测试
- 文档化前置条件和依赖
- 包含错误处理指导

## 贡献指南

我们欢迎贡献！请阅读我们的[贡献指南](CONTRIBUTING.md)了解：

- 如何提交新技能
- 技能质量标准
- Pull Request 流程
- 行为准则

### 快速贡献步骤

1. 确保你的技能基于真实用例
2. 检查现有技能是否有重复
3. 遵循技能结构模板
4. 跨平台测试你的技能
5. 提交带有清晰文档的 Pull Request

## 资源

### 官方文档

- [Claude Skills 概览](https://www.anthropic.com/news/skills) - 官方公告和功能
- [Skills 用户指南](https://support.claude.com/en/articles/12512180-using-skills-in-claude) - 如何在 Claude 中使用技能
- [创建自定义技能](https://support.claude.com/en/articles/12512198-creating-custom-skills) - 技能开发指南
- [Skills API 文档](https://docs.claude.com/en/api/skills-guide) - API 集成指南
- [Agent Skills 博客文章](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) - 工程深入解析

### 社区资源

- [Anthropic Skills 仓库](https://github.com/anthropics/skills) - 官方示例技能
- [Claude 社区](https://community.anthropic.com) - 与其他用户讨论技能
- [Skills 市场](https://claude.ai/marketplace) - 发现和分享技能

### 灵感与用例

- [Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code) - 50 种人们使用 Claude Code 的方式
- [Notion Skills](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0) - Notion 集成技能


## 加入社区

- [加入我们的 Discord](https://discord.com/invite/composio) - 与其他构建 Claude Skills 的开发者交流
- [在 Twitter/X 上关注](https://x.com/composio) - 了解新技能和功能动态
- 有问题？[support@composio.dev](mailto:support@composio.dev)

---

<p align="center">
  <b>加入 20,000+ 开发者，构建可交付的智能体</b>
</p>

<p align="center">
  <a href="https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills">
    <img src="https://img.shields.io/badge/Get_Started_Free-4F46E5?style=for-the-badge" alt="Get Started"/>
  </a>
</p>

## 许可证

本仓库采用 Apache License 2.0 许可。

个别技能可能有不同许可证 - 请查看每个技能文件夹获取具体许可信息。

---

**注意**：Claude Skills 可在 Claude.ai、Claude Code 和 Claude API 中使用。一旦创建技能，它可在所有平台间移植，使你的工作流程在你使用 Claude 的任何地方保持一致。

- [AgentsKB](https://agentskb.com) - 用研究过的答案升级你的 AI。我们已完成研究，让你的 AI 第一次就能做对。

---

## 关于本翻译 / About This Translation

本项目是 [awesome-claude-skills](https://github.com/ComposioQ/awesome-claude-skills) 的中文翻译版本。

**原项目地址**: https://github.com/ComposioQ/awesome-claude-skills
**原作者**: [Composio](https://github.com/ComposioQ)
**原项目许可证**: Apache License 2.0

### 翻译目的

本翻译旨在为中文开发者社区提供 Claude Skills 的本地化资源，降低语言障碍，
帮助更多开发者理解和使用 Claude Skills 生态系统。

### 声明

- 本翻译版本与原项目保持独立更新
- 所有内容版权归原项目作者所有
- 翻译内容采用与原项目相同的许可证
- 如发现翻译错误或改进建议，欢迎提交 Issue 或 PR
