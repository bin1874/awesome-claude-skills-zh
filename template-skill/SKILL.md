---
name: template-skill
description: 技能模板文件，用于创建新的 Claude Skill。复制此目录并修改 SKILL.md 开始创建新技能。
---

# 技能模板

这是创建新 Claude Skill 的模板文件。

## 使用方法

1. 复制整个 `template-skill` 目录：
   ```bash
   cp -r template-skill my-new-skill
   ```

2. 重命名目录为你的技能名称（小写，连字符分隔）

3. 编辑 `SKILL.md` 文件：
   - 修改 frontmatter 中的 `name` 和 `description`
   - 添加技能说明、使用时机、详细步骤

## SKILL.md 结构

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

## 说明

Claude 如何执行此技能的详细说明。

## 示例

展示技能实际应用的示例。
```

## 可选目录

| 目录 | 用途 |
|------|------|
| `scripts/` | 辅助脚本（Python/Bash） |
| `reference/` | 参考文档 |
| `assets/` | 资源文件（模板、图片） |
| `examples/` | 示例文件 |
