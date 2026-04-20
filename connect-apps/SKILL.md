---
name: connect-apps
description: 将 Claude 连接到 Gmail、Slack、GitHub 等外部应用。当用户想要发送邮件、创建 Issue、发布消息或在外部服务中执行操作时使用此技能。
---

# 连接应用

将 Claude 连接到 1000+ 应用。真正发送邮件、创建 Issue、发布消息——而不仅仅是生成相关文本。

## 快速开始

### 步骤 1：安装插件

```
/plugin install composio-toolrouter
```

### 步骤 2：运行设置

```
/composio-toolrouter:setup
```

这将：
- 请求你的免费 API 密钥（在 [platform.composio.dev](https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills) 获取）
- 配置 Claude 与 1000+ 应用的连接
- 大约需要 60 秒

### 步骤 3：试用！

设置完成后，重启 Claude Code 并尝试：

```
给我发一封测试邮件到 YOUR_EMAIL@example.com
```

如果成功，说明连接已建立！

## 你可以做什么

| 让 Claude... | 会发生什么 |
|--------------|------------|
| "给 sarah@acme.com 发送关于发布的邮件" | 实际发送邮件 |
| "创建 GitHub Issue：修复登录 Bug" | 创建 Issue |
| "发布到 Slack #general：部署完成" | 发布消息 |
| "将会议笔记添加到 Notion" | 添加到 Notion |

## 支持的应用

**邮件：** Gmail、Outlook、SendGrid
**聊天：** Slack、Discord、Teams、Telegram
**开发：** GitHub、GitLab、Jira、Linear
**文档：** Notion、Google Docs、Confluence
**数据：** Sheets、Airtable、PostgreSQL
**以及 1000+ 更多...**

## 工作原理

1. 你让 Claude 做某事
2. Composio Tool Router 找到合适的工具
3. 第一次？你需要通过 OAuth 授权（一次性）
4. 操作执行并返回结果

## 故障排除

- **"未找到插件"** → 确保你运行了 `/plugin install composio-toolrouter`
- **"需要授权"** → 点击 Claude 提供的 OAuth 链接，然后说"完成"
- **操作失败** → 检查你在目标应用中是否有权限

---

<p align="center">
  <b>加入 20,000+ 构建可交付智能体的开发者</b>
</p>

<p align="center">
  <a href="https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills">
    <img src="https://img.shields.io/badge/Get_Started_Free-4F46E5?style=for-the-badge" alt="Get Started"/>
  </a>
</p>
