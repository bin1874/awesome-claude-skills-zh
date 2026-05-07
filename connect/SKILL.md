---
name: connect
description: 将 Claude 连接到任何应用。发送邮件、创建 Issue、发布消息、更新数据库 - 在 Gmail、Slack、GitHub、Notion 和 1000+ 服务中执行真实操作。
---

# Connect

将 Claude 连接到任何应用。停止生成关于你可以做什么的文本 - 实际去做。

## 何时使用此技能

当你需要 Claude 时使用此技能：

- **发送那封邮件**而不是起草它
- **创建那个 Issue**而不是描述它
- **发布那条消息**而不是建议它
- **更新那个数据库**而不是解释如何做

## 有什么变化

| 没有 Connect | 有 Connect |
|-----------------|--------------|
| "这是一个邮件草稿..." | 发送邮件 |
| "你应该创建一个 issue..." | 创建 issue |
| "把这个发布到 Slack..." | 发布它 |
| "把这个添加到 Notion..." | 添加它 |

## 支持的应用

**1000+ 集成**包括：

- **邮件**：Gmail、Outlook、SendGrid
- **聊天**：Slack、Discord、Teams、Telegram
- **开发**：GitHub、GitLab、Jira、Linear
- **文档**：Notion、Google Docs、Confluence
- **数据**：Sheets、Airtable、PostgreSQL
- **CRM**：HubSpot、Salesforce、Pipedrive
- **存储**：Drive、Dropbox、S3
- **社交**：Twitter、LinkedIn、Reddit

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
发送邮件到 sarah@acme.com - 主题："已发布！" 正文："v2.0 已上线，如有问题请告诉我"
```

### 创建 GitHub Issue
```
在 my-org/repo 创建 issue："移动端超时 bug" 标签：bug
```

### 发布到 Slack
```
发布到 #engineering："部署完成 - v2.4.0 已上线"
```

### 链式操作
```
查找本周标记为"bug"的 GitHub issues，总结，发布到 Slack 的 #bugs 频道
```

## 工作原理

使用 Composio 工具路由器：

1. **你要求**Claude 做某事
2. **工具路由器找到**正确的工具（1000+ 选项）
3. **OAuth 自动**处理
4. **操作执行**并返回结果

### 代码

```python
from composio import Composio
from claude_agent_sdk.client import ClaudeSDKClient
from claude_agent_sdk.types import ClaudeAgentOptions
import os

composio = Composio(api_key=os.environ["COMPOSIO_API_KEY"])
session = composio.create(user_id="user_123")

options = ClaudeAgentOptions(
    system_prompt="你可以在外部应用中执行操作。",
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

首次使用应用：
```
要发送邮件，我需要 Gmail 访问权限。
在此授权：https://...
完成后说"已连接"。
```

之后连接持续有效。

## 框架支持

| 框架 | 安装 |
|-----------|---------|
| Claude Agent SDK | `pip install composio claude-agent-sdk` |
| OpenAI Agents | `pip install composio openai-agents` |
| Vercel AI | `npm install @composio/core @composio/vercel` |
| LangChain | `pip install composio-langchain` |
| 任何 MCP 客户端 | 使用 `session.mcp.url` |

## 故障排除

- **需要认证** → 点击链接、授权、说"已连接"
- **操作失败** → 检查目标应用中的权限
- **工具未找到** → 要具体："Slack #general"而不是"发送消息"

---

<p align="center">
  <b>加入 20,000+ 构建可交付智能体的开发者</b>
</p>

<p align="center">
  <a href="https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills">
    <img src="https://img.shields.io/badge/Get_Started_Free-4F46E5?style=for-the-badge" alt="Get Started"/>
  </a>
</p>
