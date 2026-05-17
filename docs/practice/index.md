---
title: 实践
---

# 实践指南

<Abs title="章节概述" :keywords="['入门指南', '实战手册', 'Claude Code', 'Claude.ai', 'API']">
本章提供 Claude Skills 的实践应用指南。从入门安装到高级实战场景，帮助读者快速上手并有效使用技能系统。
</Abs>

## 章节内容

| 章节 | 内容概要 |
|:---|:---|
| [入门指南](./getting-started) | 安装、配置、基本使用 |
| [实战手册](./playbooks) | 任务场景、技能组合、最佳实践 |

## 平台选择

Claude Skills 可在三个平台上使用：

| 平台 | 特点 | 适用场景 |
|:---|:---|:---|
| Claude.ai | 网页版，技能市场 | 快速体验、无代码使用 |
| Claude Code | 终端版，本地环境 | 开发工作流、深度定制 |
| Claude API | 程序化接口 | 应用集成、自动化 |

## 快速开始

```bash
# 安装 Claude Code
npm install -g @anthropic-ai/claude-code

# 创建技能目录
mkdir -p ~/.config/claude-code/skills/

# 复制技能
cp -r /path/to/skill-name ~/.config/claude-code/skills/

# 启动
claude
```