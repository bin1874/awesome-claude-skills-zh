# Awesome Claude Skills 中文版 - 项目指南

本文件面向 AI 编程助手，提供项目结构、开发规范和工作流程的完整说明。

## 项目概述

本项目是 [awesome-claude-skills](https://github.com/ComposioQ/awesome-claude-skills) 的中文翻译版本，维护一个精选的 Claude Skills 合集仓库。Claude Skills 是可定制的工作流程，用于扩展 Claude（AI 助手）的能力，让它能够在 Claude.ai、Claude Code 和 Claude API 平台上执行特定任务。

**项目定位**：这是一个**文档和模板项目**，而非传统意义上的软件工程代码库。核心内容是技能定义文件（Markdown 格式）和相关的 GitHub Pages 文档站点。

**语言**：中文（zh-CN）

## 仓库结构

```
awesome-claude-skills-zh/
├── README.md                    # 项目主文档，技能总览
├── CONTRIBUTING.md              # 贡献指南
├── AGENTS.md                    # 本文件
├── .github/workflows/           # GitHub Actions
│   └── pages.yml               # GitHub Pages 自动部署
│
├── docs/                        # Jekyll 文档站点
│   ├── _config.yml             # Jekyll 配置
│   ├── Gemfile                 # Ruby 依赖
│   ├── _sass/                  # 自定义样式
│   ├── assets/                 # 静态资源
│   ├── index.md                # 首页
│   ├── skills.md               # 技能列表页
│   ├── getting-started.md      # 入门指南
│   ├── contribute.md           # 贡献说明
│   ├── about.md                # 关于页面
│   └── resources.md            # 资源页面
│
└── [skill-name]/                # 各个技能目录（30+ 个）
    ├── SKILL.md                # 技能定义（必需）
    ├── scripts/                # 辅助脚本（可选）
    ├── reference/              # 参考资料（可选）
    ├── assets/                 # 资源文件（可选）
    └── examples/               # 示例文件（可选）
```

## 技术栈

### 核心
- **Markdown** - 技能定义和文档的主要格式
- **YAML** - 技能元数据 frontmatter

### 文档站点
- **Jekyll** - 静态站点生成器
- **GitHub Pages** - 托管和部署
- **just-the-docs** - Jekyll 主题
- **Ruby/Gem** - 依赖管理

### 工具链
- **Git** - 版本控制
- **GitHub Actions** - CI/CD（仅用于文档部署）

## 技能结构规范

每个技能是一个独立的目录，遵循严格的结构约定：

### 必需文件

**SKILL.md** - 技能的核心定义文件，必须包含 YAML frontmatter：

```markdown
---
name: skill-name                    # 技能标识符（小写，连字符）
description: 技能用途的清晰描述    # 描述性文字，说明何时使用此技能
license: 完整条款见 LICENSE.txt    # 可选：许可证说明
---

# 技能名称

## 何时使用此技能

- 用例 1
- 用例 2

## 说明

Claude 执行此技能的详细指导...

## 示例

展示技能实际应用的例子...
```

### 命名规范

- **目录名**：小写字母，连字符分隔（`skill-name`，非 `skill_name` 或 `SkillName`）
- **SKILL.md**：必须全大写
- **name 字段**：与目录名一致，小写连字符

### 可选目录

| 目录 | 用途 | 示例 |
|------|------|------|
| `scripts/` | 可执行脚本（Python/Bash） | `scripts/rotate_pdf.py` |
| `reference/` | 参考资料文档 | `references/api_docs.md` |
| `assets/` | 资源文件（模板、字体、图片） | `assets/logo.png` |
| `examples/` | 示例文件 | `examples/sample-output.md` |

### 写作风格

- 使用**祈使/不定式形式**（动词优先的说明），而非第二人称
- 客观、指导性语言（"要完成 X，执行 Y" 而非 "你应该做 X"）
- 技能说明面向 Claude（AI），而非最终用户
- 保持简洁，避免冗长解释

## 文档站点（Jekyll）

### 本地开发

```bash
# 进入文档目录
cd docs

# 安装依赖
bundle install

# 启动本地服务器
bundle exec jekyll serve

# 访问 http://localhost:4000
```

### 文件组织

- `_config.yml` - 站点配置、导航、主题设置
- `Gemfile` - Ruby gem 依赖
- `_sass/` - SCSS 样式覆盖
- `assets/` - 图片、CSS、字体等静态资源
- Markdown 页面使用 YAML frontmatter 定义布局

### 自动部署

GitHub Actions 工作流 (`.github/workflows/pages.yml`)：
- **触发条件**：`docs/**` 目录或工作流文件变更时
- **构建**：使用 Jekyll 构建静态站点
- **部署**：自动部署到 GitHub Pages

无需手动干预部署流程。

## 贡献工作流

### 添加新技能

1. **检查重复**：搜索现有技能
2. **创建目录**：使用小写连字符命名
3. **编写 SKILL.md**：遵循模板和写作规范
4. **添加可选资源**：脚本、参考资料、资产文件
5. **更新 README.md**：在合适分类中添加技能链接
6. **提交 PR**：遵循 PR 模板

### 更新现有技能

- 保持向后兼容（如果可能）
- 更新技能目录中的 SKILL.md
- 必要时同步更新 README.md 中的描述

### PR 规范

- **标题**："Add [Skill Name] skill" 或 "Update [Skill Name] skill"
- **描述**：包含真实用例、解决的问题、灵感来源
- **检查清单**：
  - [ ] 技能基于真实用例
  - [ ] 无重复技能
  - [ ] 遵循技能结构模板
  - [ ] SKILL.md 包含 frontmatter
  - [ ] README.md 已更新

## 许可证

- **项目整体**：Apache License 2.0
- **个别技能**：可能有不同许可证，查看技能目录中的 LICENSE.txt

## 关键注意事项

### AI 助手应知

1. **这不是代码项目**：主要是 Markdown 文档，无传统构建/测试流程
2. **技能质量优先**：每个技能必须是真实可用的，基于实际用例
3. **中文内容**：所有 SKILL.md 和文档使用中文
4. **渐进式披露**：技能通过三级加载系统工作（元数据 → SKILL.md → 捆绑资源）
5. **空目录正常**：`scripts/`、`reference/` 等可选目录可能为空

### 常见操作

**创建新技能**：
```bash
# 使用 skill-creator 脚本初始化
# 或手动创建目录和 SKILL.md
mkdir my-new-skill
cat > my-new-skill/SKILL.md << 'EOF'
---
name: my-new-skill
description: 清晰描述此技能的功能和使用时机。
---

# My New Skill

技能详细说明...
EOF
```

**更新文档站点**：
```bash
cd docs
# 编辑 .md 文件
bundle exec jekyll serve  # 本地预览
# 推送到 main 分支自动部署
```

**同步上游变更**（来自原英文项目）：
- 对比上游仓库变更
- 翻译新增内容
- 保持中文表达自然准确

## 相关链接

- 原项目：https://github.com/ComposioQ/awesome-claude-skills
- GitHub Pages：https://lessup.github.io/awesome-claude-skills-zh
- 维护者：LessUp (https://github.com/LessUp)

---

*本文件应随项目演进保持更新。如有重大结构变更，请同步更新此文档。*
