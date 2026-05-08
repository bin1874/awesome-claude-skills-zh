<h1 align="center">Awesome Claude Skills（中文版）</h1>

<p align="center">
<a href="https://dashboard.composio.dev/login?utm_source=Github&utm_medium=Youtube&utm_campaign=2025-11&utm_content=AwesomeSkills">
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

精选的 1000+ 生产级 Claude Skills 和插件列表，用于提升 Claude.ai、Claude Code、Claude API 以及 Codex、Cursor、Gemini CLI、Antigravity 等编程智能体的生产力。

> 📖 本项目是 [awesome-claude-skills](https://github.com/composiohq/awesome-claude-skills) 的中文翻译版本，最后同步于 2026年5月
>
> 💡 中文版 GitHub Pages 站点：[https://lessup.github.io/awesome-claude-skills-zh](https://lessup.github.io/awesome-claude-skills-zh)


> **需要超越文本生成的技能？** Claude 可以发送邮件、创建 Issue、发布到 Slack，并在 1000+ 应用中执行真实操作。[了解如何使用 →](./connect/)

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

在询问时粘贴你的 API 密钥。（在 [dashboard.composio.dev](https://dashboard.composio.dev/login?utm_source=Github&utm_content=AwesomeSkills) 获取免费密钥）

### 3. 重启并试用

```bash
exit
claude
```

> **需要超越文本生成的技能？** Claude 可以发送邮件、创建 Issue、发布到 Slack，并在 1000+ 应用中执行真实操作。[了解如何使用 →](./connect/)

如果收到邮件，说明 Claude 已连接到 500+ 应用。

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
  - [辅助技术](#辅助技术)
  - [通过 Composio 的应用自动化](#通过-composio-的应用自动化)
- [入门指南](#入门指南)
- [创建技能](#创建技能)
- [贡献指南](#贡献指南)
- [资源](#资源)
- [许可证](#许可证)

## 什么是 Claude Skills？

Claude Skills 是可重用的指令包，教会 AI 智能体如何处理特定类型的任务。每个 skill 是一个包含 `SKILL.md` 文件的文件夹，其中包含 YAML frontmatter（名称、描述）和 Markdown 指令，可选地附带脚本、参考文档和资源文件。Anthropic 于 2025 年 10 月推出了该格式，并于 2025 年 12 月将其作为[开放标准](https://github.com/anthropics/skills)发布；现在已支持 Claude Code、Claude.ai、Claude API、OpenAI Codex、Cursor、Gemini CLI、Antigravity 和 Windsurf。

Skills 采用渐进式加载。在会话开始时，智能体只看到每个 skill 的名称和描述 —— 每个 skill 大约 100 个 token。完整的 SKILL.md 主体（通常在 5,000 个 token 以下）仅在智能体认为该 skill 与当前任务相关时才加载。`scripts/` 和 `references/` 中的辅助文件按需加载。这就是让单个智能体托管数百个 skills 而不会使其上下文窗口膨胀的原因。

Skills 不是 MCP 服务器，也不是工具。MCP 定义智能体如何连接到外部系统 —— 认证、传输、工具发现。工具是智能体调用的单个函数。Skills 定义工作流程 —— 做什么、按什么顺序、使用什么约束 —— 一旦智能体拥有所需的连接和工具。在生产环境中，这三层一起运行：MCP 用于访问，工具用于操作，skills 用于行为。

## 技能列表

### 文档处理

- [docx](https://github.com/anthropics/skills/tree/main/skills/docx) - Create, edit, analyze Word docs with tracked changes, comments, formatting.
- [pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) - Extract text, tables, metadata, merge & annotate PDFs.
- [pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) - Read, generate, and adjust slides, layouts, templates.
- [xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx) - Spreadsheet manipulation: formulas, charts, data transformations.
- [Markdown to EPUB Converter](https://github.com/smerchek/claude-epub-skill) - Converts markdown documents and chat summaries into professional EPUB ebook files. *By [@smerchek](https://github.com/smerchek)*
- [Master Claude for Legal](https://github.com/sboghossian/master-claude-for-legal) - Skill pack for legal teams. NDA triage, multi-party version diff, citation verifier, meeting brief, and the Friday-newsletter status synthesis pattern. Includes 10 reference docs (privilege, verification, long documents, practice areas) and 3 firm templates. Built from the public Anthropic Claude for Legal Teams webinar dataset. *By [@sboghossian](https://github.com/sboghossian)*

### 开发与代码工具

- [artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) - Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui).
- [aws-skills](https://github.com/zxkane/aws-skills) - AWS development with CDK best practices, cost optimization MCP servers, and serverless/event-driven architecture patterns.
- [Changelog Generator](./changelog-generator/) - Automatically creates user-facing changelogs from git commits by analyzing history and transforming technical commits into customer-friendly release notes.
- [Chrome Relay](https://chrome-relay.kushalsm.com/) - Drives the user's already-open Chrome session — cookies, SSO, extensions, localhost — through a local CLI bridge. Real-Chrome counterpart to Playwright Browser Automation; install via `npx skills add chrome-relay` + a [Chrome Web Store extension](https://chromewebstore.google.com/detail/chrome-relay/cpdiapbifblhlcpnmlmfpgfjlacebokb). No remote relay, no Playwright fixtures, no MCP server needed.
- [Claude Code Terminal Title](https://github.com/bluzername/claude-code-terminal-title) - Gives each Claud-Code terminal window a dynamic title that describes the work being done so you don't lose track of what window is doing what.
- [Connect](./connect/) - Connect Claude to any app. Send emails, create issues, post messages, update databases - take real actions across Gmail, Slack, GitHub, Notion, and 1000+ services.
- [D3.js Visualization](https://github.com/chrisvoncsefalvay/claude-d3js-skill) - Teaches Claude to produce D3 charts and interactive data visualizations. *By [@chrisvoncsefalvay](https://github.com/chrisvoncsefalvay)*
- [FFUF Web Fuzzing](https://github.com/jthack/ffuf_claude_skill) - Integrates the ffuf web fuzzer so Claude can run fuzzing tasks and analyze results for vulnerabilities. *By [@jthack](https://github.com/jthack)*
- [finishing-a-development-branch](https://github.com/obra/superpowers/tree/main/skills/finishing-a-development-branch) - Guides completion of development work by presenting clear options and handling chosen workflow.
- [Full-Page Screenshot](https://github.com/LewisLiu007/full-page-screenshot) - Captures full-page screenshots of web pages via Chrome DevTools Protocol with zero dependencies. *By [@LewisLiu007](https://github.com/LewisLiu007)*
- [great_cto](https://github.com/avelikiy/great_cto) - Claude Code plugin: 7 specialised subagents (tech-lead, senior-dev, qa-engineer, security-officer, devops, l3-support, project-auditor) orchestrating a full SDLC pipeline — architecture, TDD, 12-angle code review, QA, security audit, deploy. 11 project archetypes auto-detected, 13 compliance frameworks (GDPR/PCI-DSS/HIPAA/SOC2/ISO 27001), self-improving knowledge layer that learns from every incident. *By [@avelikiy](https://github.com/avelikiy)*
- [iOS Simulator](https://github.com/conorluddy/ios-simulator-skill) - Enables Claude to interact with iOS Simulator for testing and debugging iOS applications. *By [@conorluddy](https://github.com/conorluddy)*
- [jules](https://github.com/sanjay3290/ai-skills/tree/main/skills/jules) - Delegate coding tasks to Google Jules AI agent for async bug fixes, documentation, tests, and feature implementation on GitHub repos. *By [@sanjay3290](https://github.com/sanjay3290)*
- [LangSmith Fetch](./langsmith-fetch/) - Debug LangChain and LangGraph agents by automatically fetching and analyzing execution traces from LangSmith Studio. First AI observability skill for Claude Code. *By [@OthmanAdi](https://github.com/OthmanAdi)*
- [lean-ctx](https://github.com/yvgude/lean-ctx) - MCP server and context runtime for AI coding agents: session caching, AST-aware compression, and 90+ shell patterns to reduce token usage. Supports Claude Code, Cursor, Copilot, and other integrations. Install the Claude Code skill with `lean-ctx init --agent claude-code`; docs at [leanctx.com](https://leanctx.com). *By [@yvgude](https://github.com/yvgude)*
- [MCP Builder](./mcp-builder/) - Guides creation of high-quality MCP (Model Context Protocol) servers for integrating external APIs and services with LLMs using Python or TypeScript.
- [move-code-quality-skill](https://github.com/1NickPappas/move-code-quality-skill) - Analyzes Move language packages against the official Move Book Code Quality Checklist for Move 2024 Edition compliance and best practices.
- [OpenWeb](https://github.com/openweb-org/openweb) - Agent-native way to access any website. Calls the same APIs the website calls (JSON in, JSON out) with auth (cookies, JWT, CSRF, signing) auto-resolved per request. 90+ sites built in. *By [@openweb-org](https://github.com/openweb-org)*
- [Playwright Browser Automation](https://github.com/lackeyjb/playwright-skill) - Model-invoked Playwright automation for testing and validating web applications. *By [@lackeyjb](https://github.com/lackeyjb)*
- [prompt-engineering](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/customaize-agent/skills/prompt-engineering) - Teaches well-known prompt engineering techniques and patterns, including Anthropic best practices and agent persuasion principles.
- [pypict-claude-skill](https://github.com/omkamal/pypict-claude-skill) - Design comprehensive test cases using PICT (Pairwise Independent Combinatorial Testing) for requirements or code, generating optimized test suites with pairwise coverage.
- [reddit-fetch](https://github.com/ykdojo/claude-code-tips/tree/main/skills/reddit-fetch) - Fetches Reddit content via Gemini CLI when WebFetch is blocked or returns 403 errors.
- [Septim Agents Pack](https://septimlabs.com/tools/agents?utm_source=awesome-claude-skills&utm_medium=awesome-list&utm_campaign=oss-backlink) - 10 named Claude Code sub-agents (Atlas, Luca, Canon, Ember, Tally, Nova, Ward, Mira, Juno, Pip) covering planning, architecture, brand, marketing, finance, design, legal, customer, research, and coordination. Drop into `.claude/agents/`. *By [@septimlabs-code](https://github.com/septimlabs-code)*
- [Skill Creator](./skill-creator/) - Provides guidance for creating effective Claude Skills that extend capabilities with specialized knowledge, workflows, and tool integrations.
- [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) - Automatically converts any documentation website into a Claude AI skill in minutes. *By [@yusufkaraaslan](https://github.com/yusufkaraaslan)*
- [software-architecture](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/ddd/skills/software-architecture) - Implements design patterns including Clean Architecture, SOLID principles, and comprehensive software design best practices.
- [subagent-driven-development](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/sadd/skills/subagent-driven-development) - Dispatches independent subagents for individual tasks with code review checkpoints between iterations for rapid, controlled development.
- [test-driven-development](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) - Use when implementing any feature or bugfix, before writing implementation code.
- [using-git-worktrees](https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/) - Creates isolated git worktrees with smart directory selection and safety verification.
- [Webapp Testing](./webapp-testing/) - Tests local web applications using Playwright for verifying frontend functionality, debugging UI behavior, and capturing screenshots.

### 数据与分析

- [CSV Data Summarizer](https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill) - Automatically analyzes CSV files and generates comprehensive insights with visualizations without requiring user prompts. *By [@coffeefuelbump](https://github.com/coffeefuelbump)*
- [deep-research](https://github.com/sanjay3290/ai-skills/tree/main/skills/deep-research) - Execute autonomous multi-step research using Gemini Deep Research Agent for market analysis, competitive landscaping, and literature reviews. *By [@sanjay3290](https://github.com/sanjay3290)*
- [postgres](https://github.com/sanjay3290/ai-skills/tree/main/skills/postgres) - Execute safe read-only SQL queries against PostgreSQL databases with multi-connection support and defense-in-depth security. *By [@sanjay3290](https://github.com/sanjay3290)*
- [recursive-research](https://github.com/Anjos2/recursive-research) - Recursive research up to PhD level across any domain (science, tech, business, arts, humanities) with source tiering, WDM + Munger inversion for autonomous decisions, and disk checkpointing to survive context compaction. *By [@Anjos2](https://github.com/Anjos2)*
- [root-cause-tracing](https://github.com/obra/superpowers/tree/main/skills/root-cause-tracing) - Use when errors occur deep in execution and you need to trace back to find the original trigger.

### 商业与营销

- [Brand Build Skills](https://github.com/rampstackco/claude-skills) - 59-skill library covering the full website lifecycle: brand, design, content, SEO, dev, ops, growth, and research. Stack-agnostic with an Ahrefs MCP-powered SEO audit suite. Includes a meta-skill for writing your own. *By [@rampstackco](https://github.com/rampstackco)*
- [Brand Guidelines](./brand-guidelines/) - Applies Anthropic's official brand colors and typography to artifacts for consistent visual identity and professional design standards.
- [Competitive Ads Extractor](./competitive-ads-extractor/) - Extracts and analyzes competitors' ads from ad libraries to understand messaging and creative approaches that resonate.
- [Domain Name Brainstormer](./domain-name-brainstormer/) - Generates creative domain name ideas and checks availability across multiple TLDs including .com, .io, .dev, and .ai extensions.
- [Internal Comms](./internal-comms/) - Helps write internal communications including 3P updates, company newsletters, FAQs, status reports, and project updates using company-specific formats.
- [Lead Research Assistant](./lead-research-assistant/) - Identifies and qualifies high-quality leads by analyzing your product, searching for target companies, and providing actionable outreach strategies.

### 沟通与写作

- [article-extractor](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/article-extractor) - Extract full article text and metadata from web pages.
- [brainstorming](https://github.com/obra/superpowers/tree/main/skills/brainstorming) - Transform rough ideas into fully-formed designs through structured questioning and alternative exploration.
- [Content Research Writer](./content-research-writer/) - Assists in writing high-quality content by conducting research, adding citations, improving hooks, and providing section-by-section feedback.
- [family-history-research](https://github.com/emaynard/claude-family-history-research-skill) - Provides assistance with planning family history and genealogy research projects.
- [Meeting Insights Analyzer](./meeting-insights-analyzer/) - Analyzes meeting transcripts to uncover behavioral patterns including conflict avoidance, speaking ratios, filler words, and leadership style.
- [NotebookLM Integration](https://github.com/PleasePrompto/notebooklm-skill) - Lets Claude Code chat directly with NotebookLM for source-grounded answers based exclusively on uploaded documents. *By [@PleasePrompto](https://github.com/PleasePrompto)*
- [Twitter Algorithm Optimizer](./twitter-algorithm-optimizer/) - Analyze and optimize tweets for maximum reach using Twitter's open-source algorithm insights. Rewrite and edit tweets to improve engagement and visibility.

### 创意与媒体

- [Canvas Design](./canvas-design/) - Creates beautiful visual art in PNG and PDF documents using design philosophy and aesthetic principles for posters, designs, and static pieces.
- [imagen](https://github.com/sanjay3290/ai-skills/tree/main/skills/imagen) - Generate images using Google Gemini's image generation API for UI mockups, icons, illustrations, and visual assets. *By [@sanjay3290](https://github.com/sanjay3290)*
- [Image Enhancer](./image-enhancer/) - Improves image and screenshot quality by enhancing resolution, sharpness, and clarity for professional presentations and documentation.
- [Slack GIF Creator](./slack-gif-creator/) - Creates animated GIFs optimized for Slack with validators for size constraints and composable animation primitives.
- [Theme Factory](./theme-factory/) - Applies professional font and color themes to artifacts including slides, docs, reports, and HTML landing pages with 10 pre-set themes.
- [Video Downloader](./video-downloader/) - Downloads videos from YouTube and other platforms for offline viewing, editing, or archival with support for various formats and quality options.
- [youtube-transcript](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/youtube-transcript) - Fetch transcripts from YouTube videos and prepare summaries.
- [swiftui-design-skill](https://github.com/wholiver/swiftui-design-skill) - SwiftUI 前端设计 skill — 反 AI Slop 六条铁律、设计方向顾问、品牌资产协议、五维评审。支持 Claude Code / Cursor / Codex / OpenCode 等全部 AI agent 平台。 *By [@wholiver](https://github.com/wholiver)*
- [Pixelbin-Media-Generation](https://github.com/anandpareek-hub/pixelbin-claude-skill) - Generate and edit images & videos with 85+ API portfolio and build visually appealing website pages

### 生产力与组织

- [File Organizer](./file-organizer/) - Intelligently organizes files and folders by understanding context, finding duplicates, and suggesting better organizational structures.
- [Invoice Organizer](./invoice-organizer/) - Automatically organizes invoices and receipts for tax preparation by reading files, extracting information, and renaming consistently.
- [kaizen](https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/kaizen/skills/kaizen) - Applies continuous improvement methodology with multiple analytical approaches, based on Japanese Kaizen philosophy and Lean methodology.
- [n8n-skills](https://github.com/haunchen/n8n-skills) - Enables AI assistants to directly understand and operate n8n workflows.
- [Raffle Winner Picker](./raffle-winner-picker/) - Randomly selects winners from lists, spreadsheets, or Google Sheets for giveaways and contests with cryptographically secure randomness.
- [solo-skills](https://github.com/rockscy/solo-skills) - 7 bilingual (EN+中文) skills for solo founders and indie devs: launch tweets, customer emails, decision frameworks, postmortems. Each skill includes an explicit "When NOT to use" section.
- [Tailored Resume Generator](./tailored-resume-generator/) - Analyzes job descriptions and generates tailored resumes that highlight relevant experience, skills, and achievements to maximize interview chances.
- [ship-learn-next](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/ship-learn-next) - Skill to help iterate on what to build or learn next, based on feedback loops.
- [tapestry](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/tapestry) - Interlink and summarize related documents into knowledge networks.

### 协作与项目管理

- [git-pushing](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/git-pushing) - Automate git operations and repository interactions.
- [google-workspace-skills](https://github.com/sanjay3290/ai-skills/tree/main/skills) - Suite of Google Workspace integrations: Gmail, Calendar, Chat, Docs, Sheets, Slides, and Drive with cross-platform OAuth. *By [@sanjay3290](https://github.com/sanjay3290)*
- [outline](https://github.com/sanjay3290/ai-skills/tree/main/skills/outline) - Search, read, create, and manage documents in Outline wiki instances (cloud or self-hosted). *By [@sanjay3290](https://github.com/sanjay3290)*
- [review-implementing](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/review-implementing) - Evaluate code implementation plans and align with specs.
- [test-fixing](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/test-fixing) - Detect failing tests and propose patches or fixes.

### 安全与系统

- [computer-forensics](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/computer-forensics) - Digital forensics analysis and investigation techniques.
- [file-deletion](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/file-deletion) - Secure file deletion and data sanitization methods.
- [metadata-extraction](https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/metadata-extraction) - Extract and analyze file metadata for forensic purposes.
- [threat-hunting-with-sigma-rules](https://github.com/jthack/threat-hunting-with-sigma-rules-skill) - Use Sigma detection rules to hunt for threats and analyze security events.

### 辅助技术

- [ASD-AuDHD-PAI-Skills](https://github.com/emory/ASD-AuDHD-PAI-Skills) - New collection, first skill [pda-reframing](https://github.com/emory/ASD-AuDHD-PAI-Skills/blob/main/Skills/pda-reframing/SKILL.md) can reframe requests or decisions to defeat Persistent Demand Avoidance flavors of autism spectrum disorders, or people with ADHD that struggle to Start tasks and need help aligning with a task.

### 通过 Composio 的应用自动化

Pre-built workflow skills for 78 SaaS apps via [Rube MCP (Composio)](https://composio.dev). Each skill includes tool sequences, parameter guidance, known pitfalls, and quick reference tables — all using real tool slugs discovered from Composio's API.

**CRM & Sales**
- [Close Automation](./close-automation/) - Automate Close CRM: leads, contacts, opportunities, activities, and pipelines.
- [HubSpot Automation](./hubspot-automation/) - Automate HubSpot CRM: contacts, deals, companies, tickets, and email engagement.
- [Pipedrive Automation](./pipedrive-automation/) - Automate Pipedrive: deals, contacts, organizations, activities, and pipelines.
- [Salesforce Automation](./salesforce-automation/) - Automate Salesforce: objects, records, SOQL queries, and bulk operations.
- [Zoho CRM Automation](./zoho-crm-automation/) - Automate Zoho CRM: leads, contacts, deals, accounts, and modules.

**Project Management**
- [Asana Automation](./asana-automation/) - Automate Asana: tasks, projects, sections, assignments, and workspaces.
- [Basecamp Automation](./basecamp-automation/) - Automate Basecamp: to-do lists, messages, people, groups, and projects.
- [ClickUp Automation](./clickup-automation/) - Automate ClickUp: tasks, lists, spaces, goals, and time tracking.
- [Jira Automation](./jira-automation/) - Automate Jira: issues, projects, boards, sprints, and JQL queries.
- [Linear Automation](./linear-automation/) - Automate Linear: issues, projects, cycles, teams, and workflows.
- [Monday Automation](./monday-automation/) - Automate Monday.com: boards, items, columns, groups, and workspaces.
- [Notion Automation](./notion-automation/) - Automate Notion: pages, databases, blocks, comments, and search.
- [Todoist Automation](./todoist-automation/) - Automate Todoist: tasks, projects, sections, labels, and filters.
- [Trello Automation](./trello-automation/) - Automate Trello: boards, cards, lists, members, and checklists.
- [Wrike Automation](./wrike-automation/) - Automate Wrike: tasks, folders, projects, comments, and workflows.

**Communication**
- [Discord Automation](./discord-automation/) - Automate Discord: messages, channels, servers, roles, and reactions.
- [Intercom Automation](./intercom-automation/) - Automate Intercom: conversations, contacts, companies, tickets, and articles.
- [Microsoft Teams Automation](./microsoft-teams-automation/) - Automate Teams: messages, channels, teams, chats, and meetings.
- [Slack Automation](./slack-automation/) - Automate Slack: messages, channels, search, reactions, threads, and scheduling.
- [Telegram Automation](./telegram-automation/) - Automate Telegram: messages, chats, media, groups, and bots.
- [WhatsApp Automation](./whatsapp-automation/) - Automate WhatsApp: messages, media, templates, groups, and business profiles.

**Email**
- [Gmail Automation](./gmail-automation/) - Automate Gmail: send/reply, search, labels, drafts, and attachments.
- [Outlook Automation](./outlook-automation/) - Automate Outlook: emails, folders, contacts, and calendar integration.
- [Postmark Automation](./postmark-automation/) - Automate Postmark: transactional emails, templates, servers, and delivery stats.
- [SendGrid Automation](./sendgrid-automation/) - Automate SendGrid: emails, templates, contacts, lists, and campaign stats.

**Code & DevOps**
- [Bitbucket Automation](./bitbucket-automation/) - Automate Bitbucket: repos, PRs, branches, issues, and workspaces.
- [CircleCI Automation](./circleci-automation/) - Automate CircleCI: pipelines, workflows, jobs, and project configuration.
- [Datadog Automation](./datadog-automation/) - Automate Datadog: monitors, dashboards, metrics, incidents, and alerts.
- [GitHub Automation](./github-automation/) - Automate GitHub: issues, PRs, repos, branches, actions, and code search.
- [GitLab Automation](./gitlab-automation/) - Automate GitLab: issues, MRs, projects, pipelines, and branches.
- [PagerDuty Automation](./pagerduty-automation/) - Automate PagerDuty: incidents, services, schedules, escalation policies, and on-call.
- [Render Automation](./render-automation/) - Automate Render: services, deploys, and project management.
- [Sentry Automation](./sentry-automation/) - Automate Sentry: issues, events, projects, releases, and alerts.
- [Supabase Automation](./supabase-automation/) - Automate Supabase: SQL queries, table schemas, edge functions, and storage.
- [Vercel Automation](./vercel-automation/) - Automate Vercel: deployments, projects, domains, environment variables, and logs.

**Storage & Files**
- [Box Automation](./box-automation/) - Automate Box: files, folders, search, sharing, collaborations, and sign requests.
- [Dropbox Automation](./dropbox-automation/) - Automate Dropbox: files, folders, search, sharing, and batch operations.
- [Google Drive Automation](./google-drive-automation/) - Automate Google Drive: upload, download, search, share, and organize files.
- [OneDrive Automation](./one-drive-automation/) - Automate OneDrive: files, folders, search, sharing, permissions, and versioning.

**Spreadsheets & Databases**
- [Airtable Automation](./airtable-automation/) - Automate Airtable: records, tables, bases, views, and field management.
- [Coda Automation](./coda-automation/) - Automate Coda: docs, tables, rows, formulas, and automations.
- [Google Sheets Automation](./googlesheets-automation/) - Automate Google Sheets: read/write cells, formatting, formulas, and batch operations.

**Calendar & Scheduling**
- [Cal.com Automation](./cal-com-automation/) - Automate Cal.com: event types, bookings, availability, and scheduling.
- [Calendly Automation](./calendly-automation/) - Automate Calendly: events, invitees, event types, scheduling links, and availability.
- [Google Calendar Automation](./google-calendar-automation/) - Automate Google Calendar: events, attendees, free/busy, and recurring schedules.
- [Outlook Calendar Automation](./outlook-calendar-automation/) - Automate Outlook Calendar: events, attendees, reminders, and recurring schedules.

**Social Media**
- [Instagram Automation](./instagram-automation/) - Automate Instagram: posts, stories, comments, media, and business insights.
- [LinkedIn Automation](./linkedin-automation/) - Automate LinkedIn: posts, profiles, companies, images, and comments.
- [Reddit Automation](./reddit-automation/) - Automate Reddit: posts, comments, subreddits, voting, and moderation.
- [TikTok Automation](./tiktok-automation/) - Automate TikTok: video uploads, queries, and creator management.
- [Twitter Automation](./twitter-automation/) - Automate Twitter/X: tweets, search, users, lists, and engagement.
- [YouTube Automation](./youtube-automation/) - Automate YouTube: videos, channels, playlists, comments, and subscriptions.

**Marketing & Email Marketing**
- [ActiveCampaign Automation](./activecampaign-automation/) - Automate ActiveCampaign: contacts, deals, campaigns, lists, and automations.
- [Brevo Automation](./brevo-automation/) - Automate Brevo: contacts, email campaigns, transactional emails, and lists.
- [ConvertKit Automation](./convertkit-automation/) - Automate ConvertKit (Kit): subscribers, tags, sequences, broadcasts, and forms.
- [Klaviyo Automation](./klaviyo-automation/) - Automate Klaviyo: profiles, lists, segments, campaigns, and events.
- [Mailchimp Automation](./mailchimp-automation/) - Automate Mailchimp: audiences, campaigns, templates, segments, and reports.

**Support & Helpdesk**
- [Freshdesk Automation](./freshdesk-automation/) - Automate Freshdesk: tickets, contacts, agents, groups, and canned responses.
- [Freshservice Automation](./freshservice-automation/) - Automate Freshservice: tickets, assets, changes, problems, and service catalog.
- [Help Scout Automation](./helpdesk-automation/) - Automate Help Scout: conversations, customers, mailboxes, and tags.
- [Zendesk Automation](./zendesk-automation/) - Automate Zendesk: tickets, users, organizations, search, and macros.

**E-commerce & Payments**
- [Shopify Automation](./shopify-automation/) - Automate Shopify: products, orders, customers, inventory, and GraphQL queries.
- [Square Automation](./square-automation/) - Automate Square: payments, customers, catalog, orders, and locations.
- [Stripe Automation](./stripe-automation/) - Automate Stripe: charges, customers, products, subscriptions, and refunds.

**Design & Collaboration**
- [Canva Automation](./canva-automation/) - Automate Canva: designs, templates, assets, folders, and brand kits.
- [Confluence Automation](./confluence-automation/) - Automate Confluence: pages, spaces, search, CQL, labels, and versions.
- [DocuSign Automation](./docusign-automation/) - Automate DocuSign: envelopes, templates, signing, and document management.
- [Figma Automation](./figma-automation/) - Automate Figma: files, components, comments, projects, and team management.
- [Miro Automation](./miro-automation/) - Automate Miro: boards, sticky notes, shapes, connectors, and items.
- [Webflow Automation](./webflow-automation/) - Automate Webflow: CMS collections, items, sites, publishing, and assets.

**Analytics & Data**
- [Amplitude Automation](./amplitude-automation/) - Automate Amplitude: events, cohorts, user properties, and analytics queries.
- [Google Analytics Automation](./google-analytics-automation/) - Automate Google Analytics: reports, dimensions, metrics, and property management.
- [Mixpanel Automation](./mixpanel-automation/) - Automate Mixpanel: events, funnels, cohorts, annotations, and JQL queries.
- [PostHog Automation](./posthog-automation/) - Automate PostHog: events, persons, feature flags, insights, and annotations.
- [Segment Automation](./segment-automation/) - Automate Segment: sources, destinations, tracking, and warehouse connections.

**HR & People**
- [BambooHR Automation](./bamboohr-automation/) - Automate BambooHR: employees, time off, reports, and directory management.

**Automation Platforms**
- [Make Automation](./make-automation/) - Automate Make (Integromat): scenarios, connections, and execution management.

**Zoom & Meetings**
- [Zoom Automation](./zoom-automation/) - Automate Zoom: meetings, recordings, participants, webinars, and reports.

## 入门指南

### 在 Claude.ai 中使用技能

1. 在聊天界面中点击技能图标（🧩）。
2. 从市场添加技能或上传自定义技能。
3. Claude 会根据你的任务自动激活相关技能。

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

4. 技能会自动加载并在相关时激活。

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

参见 [Skills API 文档](https://docs.claude.com/en/api/skills-guide) 了解详情。

## 创建技能

### 技能结构

每个技能是一个包含带有 YAML frontmatter 的 `SKILL.md` 文件的文件夹：

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
description: 对此技能功能和使用时机的清晰描述。
---

# My Skill Name

技能用途和功能的详细描述。

## 何时使用此技能

- 使用场景 1
- 使用场景 2
- 使用场景 3

## 指令

[Claude 如何执行此技能的详细说明]

## 示例

[展示技能实际应用的示例]
```

### 技能最佳实践

- 专注于特定的、可重复的任务
- 包含清晰的示例和边缘情况
- 为 Claude 编写指令，而不是最终用户
- 跨 Claude.ai、Claude Code 和 API 进行测试
- 记录先决条件和依赖关系
- 包含错误处理指南

## 贡献指南

我们欢迎贡献！请阅读我们的[贡献指南](CONTRIBUTING.md)了解以下详情：

- 如何提交新技能
- 技能质量标准
- Pull Request 流程
- 行为准则

### 快速贡献步骤

1. 确保你的技能基于真实用例
2. 检查现有技能中是否有重复
3. 遵循技能结构模板
4. 跨平台测试你的技能
5. 提交带有清晰文档的 pull request

## 资源

### 官方文档

- [Claude Skills 概述](https://www.anthropic.com/news/skills) - 官方公告和功能
- [Skills 用户指南](https://support.claude.com/en/articles/12512180-using-skills-in-claude) - 如何在 Claude 中使用技能
- [创建自定义技能](https://support.claude.com/en/articles/12512198-creating-custom-skills) - 技能开发指南
- [Skills API 文档](https://docs.claude.com/en/api/skills-guide) - API 集成指南
- [Agent Skills 博客文章](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) - 工程深入探讨

### 社区资源

- [Anthropic Skills 仓库](https://github.com/anthropics/skills) - 官方示例技能
- [Claude 社区](https://community.anthropic.com) - 与其他用户讨论技能
- [Skills 市场](https://claude.ai/marketplace) - 发现和分享技能

### 灵感与用例

- [Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code) - 人们使用 Claude Code 的 50 种方式
- [Notion Skills](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0) - Notion 集成技能
- [Top Claude Skills](https://composio.dev/content/top-claude-skills)


## 加入社区

- [加入我们的 Discord](https://discord.com/invite/composio) - 与其他构建 Claude Skills 的开发者聊天
- [在 Twitter/X 上关注我们](https://x.com/composio) - 了解新技能和功能的最新动态
- 有问题？[support@composio.dev](mailto:support@composio.dev)

---

<p align="center">
  <b>加入 20,000+ 构建可交付智能体的开发者</b>
</p>

<p align="center">
  <a href="https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills">
    <img src="https://img.shields.io/badge/Get_Started_Free-4F46E5?style=for-the-badge" alt="Get Started"/>
  </a>
</p>

## 许可证

本仓库采用 Apache License 2.0 许可证。

个别技能可能有不同的许可证 - 请查看每个技能文件夹以获取具体的许可信息。

---

**注意**：Claude Skills 可在 Claude.ai、Claude Code 和 Claude API 中使用。一旦创建了技能，它就可以在所有平台间移植，使你的工作流程在你使用 Claude 的任何地方保持一致。

- [AgentsKB](https://agentskb.com) - 用经过研究的答案升级你的 AI。我们已完成研究，让你的 AI 第一次就能做对。
