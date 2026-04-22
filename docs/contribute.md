---
layout: default
title: 贡献指南
nav_order: 4
---

# 贡献指南

我们欢迎所有形式的贡献！无论是提交新技能、修复翻译错误，还是改进文档。

---

## 快速贡献步骤

1. **Fork 本仓库**

   点击 GitHub 页面的 "Fork" 按钮创建你的副本。

2. **克隆到你的本地**

   ```bash
   git clone https://github.com/YOUR_USERNAME/awesome-claude-skills-zh.git
   cd awesome-claude-skills-zh
   ```

3. **创建新分支**

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **进行你的修改**

5. **提交更改**

   ```bash
   git add .
   git commit -m "添加：你的修改描述"
   git push origin feature/your-feature-name
   ```

6. **提交 Pull Request**

   在 GitHub 上创建 Pull Request，描述你的修改内容。

---

## 提交新技能

### 技能质量标准

提交的技能应满足以下标准：

- ✅ **基于真实用例** - 解决实际问题，而非示例代码
- ✅ **无重复** - 检查现有技能列表，避免功能重复
- ✅ **遵循结构模板** - 使用标准的 SKILL.md 格式
- ✅ **跨平台测试** - 在 Claude.ai、Claude Code 上测试通过
- ✅ **清晰文档** - 包含详细说明和使用示例

### 技能结构

每个技能是一个包含 `SKILL.md` 文件的文件夹：

```
skill-name/
├── SKILL.md          # 必需：技能说明和元数据
├── scripts/          # 可选：辅助脚本
├── templates/        # 可选：文档模板
└── resources/        # 可选：参考文件
```

### SKILL.md 格式

```markdown
---
name: my-skill-name
description: 清晰描述此技能的功能和使用时机
license: 许可证信息（可选）
---

# My Skill Name

技能用途和能力的详细描述。

## 何时使用此技能

- 用例 1
- 用例 2
- 用例 3

## 说明

Claude 如何执行此技能的详细说明

## 示例

展示技能实际应用的示例

## 注意事项

- 前置条件
- 依赖说明
- 错误处理建议
```

### 技能最佳实践

- **聚焦特定任务** - 一个技能专注于一个明确的、可重复的任务
- **使用清晰示例** - 展示预期输入和输出
- **处理边缘情况** - 说明边界条件和限制
- **为 Claude 编写** - 说明要指导 Claude 如何执行任务
- **文档化依赖** - 明确所需的外部工具或 API

---

## 改进翻译

如果发现有翻译错误或不准确的地方，欢迎提交修复。

### 翻译原则

1. **准确性** - 保留原意，不曲解
2. **可读性** - 中文表达通顺自然
3. **一致性** - 统一术语翻译（如 skill → 技能）
4. **上下文** - 根据语境选择合适译法

### 术语对照表

| 英文 | 中文翻译 | 说明 |
|:---|:---|:---|
| Skill | 技能 | |
| Artifact | Artifact | 保留原名 |
| Prompt | 提示词 | |
| Agent | 智能体 | |
| MCP (Model Context Protocol) | MCP | 保留缩写 |
| Workflow | 工作流 | |
| Tool | 工具 | |
| Integration | 集成 | |

---

## 改进文档

### 可改进的内容

- 首页介绍文字
- 技能分类和描述
- 使用教程和示例
- 页面样式和布局

### 提交文档修改

文档文件位于 `docs/` 目录：

```
docs/
├── _config.yml         # Jekyll 配置
├── index.md            # 首页
├── skills.md           # 技能列表
├── getting-started.md  # 入门指南
├── contribute.md       # 本文件
└── ...
```

---

## 代码规范

### Markdown 规范

- 使用中文字符和标点
- 代码块标注语言类型
- 表格对齐，增强可读性
- 适当使用强调和引用

### 文件命名

- 使用小写字母
- 单词间用连字符 `-` 分隔
- 保持简洁、有意义

### Git 提交信息

提交信息格式：

```
类型: 简短描述

详细说明（可选）
```

类型包括：
- `添加:` - 新增功能或内容
- `修复:` - 修复错误
- `改进:` - 改进现有内容
- `文档:` - 文档更新
- `样式:` - 样式调整

---

## 行为准则

参与本项目即表示你同意遵守以下行为准则：

- 以专业和尊重的态度对待他人
- 接受建设性批评
- 关注对社区最有利的事情
- 对其他社区成员表示同理心

不当行为包括：
- 使用冒犯性的评论或语言
- 骚扰、歧视或不当行为
- 发布他人私人信息
- 其他不专业行为

---

## 获取帮助

如果你有任何问题或需要帮助：

- 在 GitHub 上 [提交 Issue](https://github.com/LessUp/awesome-claude-skills-zh/issues)
- 发送邮件至: [项目维护者邮箱]

---

感谢你的贡献！🙏
