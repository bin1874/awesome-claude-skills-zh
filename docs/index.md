---
layout: default
title: 首页
nav_order: 1
permalink: /
---

<div class="hero">
  <h1>🧩 Awesome Claude Skills</h1>
  <p class="subtitle">精选的实用 Claude Skills 列表，提升 Claude.ai、Claude Code 和 Claude API 的生产力</p>
  <div class="badges">
    <img src="https://awesome.re/badge.svg" alt="Awesome">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome">
    <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square" alt="License">
  </div>
</div>

<div class="translation-notice">
  <p>
    <strong>📖 中文翻译版本</strong><br>
    本项目是 <a href="https://github.com/ComposioQ/awesome-claude-skills" target="_blank">awesome-claude-skills</a> 的中文翻译版本，
    旨在为中文开发者社区提供 Claude Skills 的本地化资源。
  </p>
</div>

## 什么是 Claude Skills？

**Claude Skills** 是可定制的工作流程，教会 Claude 根据你的独特需求执行特定任务。

Skills 让 Claude 能够在所有 Claude 平台上以可重复、标准化的方式执行任务：

- **Claude.ai** — 网页版对话中的智能助手
- **Claude Code** — 本地终端的 AI 编程伙伴  
- **Claude API** — 程序化调用的 AI 能力

---

## 数据统计

<div class="stats">
  <div class="stat-item">
    <div class="stat-number">30+</div>
    <div class="stat-label">精选技能</div>
  </div>
  <div class="stat-item">
    <div class="stat-number">10</div>
    <div class="stat-label">分类领域</div>
  </div>
  <div class="stat-item">
    <div class="stat-number">500+</div>
    <div class="stat-label">应用集成</div>
  </div>
  <div class="stat-item">
    <div class="stat-number">3</div>
    <div class="stat-label">支持平台</div>
  </div>
</div>

---

## 技能分类

<div class="features">
  <div class="feature-card">
    <h3><span class="icon">📄</span> 文档处理</h3>
    <p>Word、PDF、PPT、Excel 文档的创建、编辑和分析，以及 EPUB 电子书转换</p>
  </div>
  <div class="feature-card">
    <h3><span class="icon">💻</span> 开发工具</h3>
    <p>MCP Builder、Webapp Testing、Git 工作流、代码质量分析等开发利器</p>
  </div>
  <div class="feature-card">
    <h3><span class="icon">📊</span> 数据分析</h3>
    <p>CSV 处理、PostgreSQL 查询、深度研究助手、数据可视化</p>
  </div>
  <div class="feature-card">
    <h3><span class="icon">📈</span> 商业营销</h3>
    <p>品牌指南、竞品广告分析、线索研究、域名创意、内部沟通</p>
  </div>
  <div class="feature-card">
    <h3><span class="icon">💬</span> 沟通写作</h3>
    <p>内容研究、会议分析、Twitter 优化、头脑风暴、NotebookLM 集成</p>
  </div>
  <div class="feature-card">
    <h3><span class="icon">🎨</span> 创意媒体</h3>
    <p>图像增强、GIF 创建、视频下载、Canvas 设计、主题应用</p>
  </div>
  <div class="feature-card">
    <h3><span class="icon">⚡</span> 生产力</h3>
    <p>文件组织、发票整理、简历生成、n8n 工作流、持续改进</p>
  </div>
  <div class="feature-card">
    <h3><span class="icon">🔌</span> 应用自动化</h3>
    <p>通过 Composio 连接 500+ SaaS 应用，实现真实操作</p>
  </div>
</div>

---

## 支持平台

<div class="platform-grid">
  <div class="platform-card">
    <h4>🌐 Claude.ai</h4>
    <p>在网页版 Claude 中直接使用技能，从市场添加或上传自定义技能</p>
    <a href="{{ '/getting-started#claudeai' | relative_url }}" class="platform-link">了解详情 →</a>
  </div>
  <div class="platform-card">
    <h4>💻 Claude Code</h4>
    <p>本地终端使用的强大 AI 编程助手，将技能放在配置目录即可自动加载</p>
    <a href="{{ '/getting-started#claude-code' | relative_url }}" class="platform-link">了解详情 →</a>
  </div>
  <div class="platform-card">
    <h4>🔌 Claude API</h4>
    <p>程序化调用 Claude，通过 API 集成技能到你的应用和工作流</p>
    <a href="{{ '/getting-started#api' | relative_url }}" class="platform-link">了解详情 →</a>
  </div>
</div>

---

## 热门技能

| 技能 | 描述 | 分类 |
|:---|:---|:---|
| **MCP Builder** | 创建高质量的 MCP 服务器，支持 Python 或 TypeScript | 开发工具 |
| **Skill Creator** | 创建有效 Claude Skills 的指导工具 | 开发工具 |
| **Content Research Writer** | 撰写高质量内容，自动研究和引用 | 沟通写作 |
| **Canvas Design** | 创建精美的视觉艺术、海报和设计 | 创意媒体 |
| **Brand Guidelines** | 将 Anthropic 品牌颜色和字体应用到 artifacts | 商业营销 |
| **File Organizer** | 智能组织文件和文件夹 | 生产力 |
| **Connect Apps** | 连接 500+ 应用执行真实操作 | 应用自动化 |

---

## 快速开始

### 在 Claude Code 中使用技能

```bash
# 1. 创建技能目录
mkdir -p ~/.config/claude-code/skills/

# 2. 复制技能文件
cp -r skill-name ~/.config/claude-code/skills/

# 3. 启动 Claude Code
claude

# 技能自动加载并在相关时激活
```

### 连接应用到 Claude

通过 **connect-apps** 插件，让 Claude 执行真实操作：

```bash
# 安装插件
claude --plugin-dir ./connect-apps-plugin

# 运行设置
/connect-apps:setup
```

在 [platform.composio.dev](https://platform.composio.dev) 获取免费 API 密钥，让 Claude 能够发送邮件、创建 Issue、发布到 Slack 等。

---

<div class="cta-section">
  <h3>开始探索</h3>
  <p>发现适合你的技能，提升 Claude 生产力</p>
  <a href="{{ '/skills' | relative_url }}" class="cta-button">浏览技能列表</a>
  <a href="{{ '/getting-started' | relative_url }}" class="cta-button secondary">入门指南</a>
</div>

---

## 关于本翻译

本项目是 [awesome-claude-skills](https://github.com/ComposioQ/awesome-claude-skills) 的中文翻译版本。

- **原项目**: [ComposioQ/awesome-claude-skills](https://github.com/ComposioQ/awesome-claude-skills)
- **许可证**: Apache License 2.0
- **翻译目的**: 为中文开发者社区提供 Claude Skills 的本地化资源
- **贡献**: 欢迎提交 Issue 和 PR 改进翻译

完整内容和所有技能详情请查看 [GitHub 仓库](https://github.com/LessUp/awesome-claude-skills-zh)。
