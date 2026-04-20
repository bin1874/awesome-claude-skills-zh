# 连接应用插件

让 Claude 在 500+ 应用中执行真实操作。使用 Composio 在底层处理认证和连接。

## 安装

```bash
claude --plugin-dir ./connect-apps-plugin
```

然后运行设置：
```
/connect-apps:setup
```

## 你获得什么

安装后，Claude 可以：
- **发送邮件** 通过 Gmail、Outlook
- **创建 Issue** 在 GitHub、GitLab、Jira、Linear
- **发布消息** 到 Slack、Discord、Teams
- **更新文档** 在 Notion、Google Docs
- **管理数据** 在 Sheets、Airtable、数据库
- **以及 500+ 更多操作**

## 工作原理

1. 从 [platform.composio.dev](https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills) 获取免费 API 密钥
2. 运行 `/connect-apps:setup` 并粘贴你的密钥
3. 重启 Claude Code
4. 第一次使用应用时，你将通过 OAuth 授权
5. 就是这样——Claude 现在可以执行真实操作了

## 试用

设置后，问 Claude：
```
给我发一封测试邮件到 myemail@example.com
```

---

<p align="center">
  <a href="https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills">
    <img src="https://img.shields.io/badge/Get_API_Key-4F46E5?style=for-the-badge" alt="Get API Key"/>
  </a>
</p>
