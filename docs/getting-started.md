---
layout: default
title: 入门指南
nav_order: 3
permalink: /getting-started
---

# 入门指南

本指南将帮助你在不同平台上开始使用 Claude Skills。

---

## 概述

Claude Skills 可在三个平台上使用：

1. **Claude.ai** — 网页版对话界面
2. **Claude Code** — 本地终端应用
3. **Claude API** — 程序化接口

一个技能一旦创建，可以在所有平台间移植使用。

---

## 在 Claude.ai 中使用技能 {#claudeai}

Claude.ai 提供了内置的技能市场，你可以轻松添加和管理技能。

### 添加技能

1. 点击聊天界面中的 **技能图标**（🧩）
2. 选择 **"从市场添加技能"** 或 **"上传自定义技能"**
3. 浏览技能市场或上传本地的 `SKILL.md` 文件
4. 点击 **添加** 即可使用

### 使用技能

添加技能后，Claude 会根据你的对话内容自动激活相关技能。你也可以通过在提示中明确提及技能名称来激活它。

---

## 在 Claude Code 中使用技能 {#claude-code}

Claude Code 是 Anthropic 推出的终端应用，让你能够在本地开发环境中使用 Claude。

### 安装 Claude Code

```bash
# macOS (使用 Homebrew)
brew install claude-code

# 或使用 npm
npm install -g @anthropic-ai/claude-code

# 启动
claude
```

### 安装技能

```bash
# 1. 创建技能目录（如果不存在）
mkdir -p ~/.config/claude-code/skills/

# 2. 复制技能文件夹到该目录
cp -r /path/to/skill-name ~/.config/claude-code/skills/

# 3. 验证安装
ls ~/.config/claude-code/skills/
```

### 技能文件夹结构

每个技能是一个包含 `SKILL.md` 文件的文件夹：

```
~/.config/claude-code/skills/
├── skill-name/
│   ├── SKILL.md          # 必需的：技能说明和元数据
│   ├── scripts/          # 可选：辅助脚本
│   ├── templates/        # 可选：文档模板
│   └── resources/        # 可选：参考文件
```

### 验证技能

```bash
# 查看技能元数据（前 20 行）
head -20 ~/.config/claude-code/skills/skill-name/SKILL.md
```

你应该能看到类似这样的内容：

```yaml
---
name: skill-name
description: 技能的简要描述
---
```

### 启动 Claude Code

```bash
claude
```

技能会在启动时自动加载，并在相关对话中自动激活。

---

## 通过 API 使用技能 {#api}

你可以通过 Claude API 以编程方式使用技能。

### Python 示例

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    skills=["skill-id-here"],  # 指定要使用的技能
    messages=[
        {"role": "user", "content": "您的提示内容"}
    ]
)

print(response.content)
```

### API 参数说明

| 参数 | 类型 | 说明 |
|:---|:---|:---|
| `model` | string | Claude 模型版本 |
| `skills` | array | 要启用的技能 ID 列表 |
| `messages` | array | 对话消息列表 |
| `max_tokens` | integer | 最大生成 token 数 |

### 官方文档

- [Skills API 文档](https://docs.anthropic.com/en/api/skills-guide)

---

## 连接应用到 Claude

通过 **connect-apps** 插件，Claude 可以执行真实操作 —— 发送邮件、创建 Issue、发布到 Slack 等。

### 安装插件

```bash
# 进入项目目录后
claude --plugin-dir ./connect-apps-plugin
```

### 运行设置

```
/connect-apps:setup
```

### 获取 API 密钥

1. 访问 [platform.composio.dev](https://platform.composio.dev)
2. 注册或登录账号
3. 在 Dashboard 中获取你的 API 密钥
4. 在 Claude 询问时粘贴密钥

### 重启 Claude

```bash
exit
claude
```

### 支持的应用

| 类别 | 应用示例 |
|:---|:---|
| 邮件 | Gmail、Outlook、SendGrid |
| 项目管理 | Notion、Jira、Asana、Trello |
| 沟通 | Slack、Discord、Microsoft Teams |
| 代码 | GitHub、GitLab、Bitbucket |
| 存储 | Google Drive、Dropbox、OneDrive |
| 日历 | Google Calendar、Calendly |

[查看完整应用列表 →](https://composio.dev/toolkits)

---

## 创建自己的技能

### 基本技能结构

```
my-skill/
├── SKILL.md          # 必需的：技能说明和元数据
├── scripts/          # 可选：辅助脚本
├── templates/        # 可选：文档模板
└── resources/        # 可选：参考文件
```

### SKILL.md 模板

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

Claude 如何执行此技能的详细说明。

## 示例

展示技能实际应用的示例。
```

### 技能最佳实践

- ✅ 聚焦于特定的、可重复的任务
- ✅ 包含清晰的示例和边缘情况处理
- ✅ 为 Claude 编写说明，而非最终用户
- ✅ 在 Claude.ai、Claude Code 和 API 上测试
- ✅ 文档化前置条件和依赖
- ✅ 包含错误处理指导

### 使用 Skill Creator

本项目包含一个 **Skill Creator** 技能，可以帮助你创建高质量的 Claude Skills：

```bash
# 在 Claude Code 中加载 skill-creator
claude

# 然后说：
# "我想创建一个新的技能，用于..."
```

---

## 常见问题

### 技能没有生效？

1. 检查 `SKILL.md` 文件的 YAML frontmatter 格式是否正确
2. 确认技能文件夹位于正确的目录
3. 重启 Claude Code 以重新加载技能
4. 检查是否有语法错误

### 如何更新技能？

直接编辑 `SKILL.md` 文件并保存，Claude Code 会自动重新加载。

### 技能之间会冲突吗？

一般不会。Claude 会根据对话上下文选择最合适的技能。

---

## 下一步

- 浏览 [技能列表]({{ '/skills' | relative_url }}) 发现适合你的技能
- 查看 [GitHub 仓库](https://github.com/LessUp/awesome-claude-skills-zh) 获取所有技能文件
- 参考 [原项目](https://github.com/ComposioQ/awesome-claude-skills) 获取最新更新
