---
name: connect
description: 将 Claude 连接到任何应用。发送邮件、创建 Issue、发布消息、更新数据库 - 在 Gmail、Slack、GitHub、Notion 和 1000+ 服务中执行真实操作。
---

# Connect（连接）

将 Claude 连接到任何应用。停止生成关于"可以做什么"的文字 - 实际去执行。

## 何时使用此技能

当你需要 Claude 执行以下操作时使用此技能：

- **发送邮件** 而非起草邮件
- **创建 Issue** 而非描述 Issue
- **发布消息** 而非建议发布
- **更新数据库** 而非解释如何更新

## 对比

| 无 Connect | 有 Connect |
|-----------------|--------------|
| "这是邮件草稿..." | 发送邮件 |
| "你应该创建一个 Issue..." | 创建 Issue |
| "把这个发到 Slack..." | 发布到 Slack |
| "把这个加到 Notion..." | 添加到 Notion |

## 支持的应用

**1000+ 集成**，包括：

- **邮件：** Gmail、Outlook、SendGrid
- **聊天：** Slack、Discord、Teams、Telegram
- **开发：** GitHub、GitLab、Jira、Linear
- **文档：** Notion、Google Docs、Confluence
- **数据：** Sheets、Airtable、PostgreSQL
- **CRM：** HubSpot、Salesforce、Pipedrive
- **存储：** Drive、Dropbox、S3
- **社交：** Twitter、LinkedIn、Reddit

## 设置

### 1. 获取 API 密钥

在 [platform.composio.dev](https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills) 获取免费密钥

### 2. 设置环境变量

```bash
export COMPOSIO_API_KEY="your-key"
```

### 3. 安装

```bash
pip install composio          # Python
npm install @composio/core    # TypeScript
```

完成。Claude 现在可以连接到任何应用。

## 示例

### 发送邮件
```
发送邮件给 sarah@acme.com - 主题："已发布！" 正文："v2.0 已上线，如有问题请告知"
```

### 创建 GitHub Issue
```
在 my-org/repo 创建 Issue："移动端超时 Bug"，标签：bug
```

### 发布到 Slack
```
发布到 #engineering："部署完成 - v2.4.0 已上线"
```

### 链式操作
```
查找本周标记为 "bug" 的 GitHub Issue，总结后发布到 Slack #bugs 频道
```

## 工作原理

使用 Composio 工具路由器：

1. **你请求** Claude 执行某操作
2. **工具路由器查找** 正确工具（1000+ 选项）
3. **OAuth 自动处理**
4. **执行操作** 并返回结果

### 代码示例

```python
from composio import Composio
from claude_agent_sdk.client import ClaudeSDKClient
from claude_agent_sdk.types import ClaudeAgentOptions
import os

composio = Composio(api_key=os.environ["COMPOSIO_API_KEY"])
session = composio.create(user_id="user_123")

options = ClaudeAgentOptions(
    system_prompt="You can take actions in external apps.",
    mcp_servers={
        "composio": {
            "type": "http",
            "url": session.mcp.url,
            "headers": {"x-api-key": os.environ["COMPOSIO_API_KEY"]},
        }
    },
)

async with ClaudeSDKClient(options) as client:
    await client.query("发送 Slack 消息到 #general：你好！")
```

## 认证流程

首次使用应用时：
```
要发送邮件，我需要 Gmail 访问权限。
请在此授权：https://...
完成后说"已连接"。
```

之后连接会保持。

## 框架支持

| 框架 | 安装 |
|-----------|---------|
| Claude Agent SDK | `pip install composio claude-agent-sdk` |
| OpenAI Agents | `pip install composio openai-agents` |
| Vercel AI | `npm install @composio/core @composio/vercel` |
| LangChain | `pip install composio-langchain` |
| 任何 MCP 客户端 | 使用 `session.mcp.url` |

## 故障排除

- **需要认证** → 点击链接，授权后说"已连接"
- **操作失败** → 检查目标应用中的权限
- **找不到工具** → 要具体："Slack #general" 而非 "发送消息"

---

<p align="center">
  <b>加入 20,000+ 开发者，构建可交付的智能体</b>
</p>

<p align="center">
  <a href="https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills">
    <img src="https://img.shields.io/badge/Get_Started_Free-4F46E5?style=for-the-badge" alt="Get Started"/>
  </a>
</p>
