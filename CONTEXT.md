# 上下文

本项目是 [awesome-claude-skills](https://github.com/ComposioQ/awesome-claude-skills) 的中文翻译版本。这是一个**文档和模板项目**，维护一个精选的 Claude Skills 合集。

## 核心概念

### Skill（技能）

**定义**：模块化、自包含的包，通过提供专业知识、工作流和工具来扩展 Claude 的能力。技能将 Claude 从通用智能体转变为配备程序性知识的专用智能体。

**能力**：
- 专用工作流 - 特定领域的多步骤流程
- 工具集成 - 处理特定文件格式或 API 的说明
- 领域专业知识 - 公司特定知识、模式、业务逻辑
- 捆绑资源 - 用于复杂和重复任务的脚本、参考资料和资产

**结构**：
```
skill-name/
├── SKILL.md        # 必需：技能定义文件
├── scripts/        # 可选：可执行代码
├── references/     # 可选：参考文档
└── assets/         # 可选：资源文件
```

### SKILL.md

**定义**：技能的核心定义文件，必须包含 YAML frontmatter 和 Markdown 说明。

**组成部分**：
1. **Frontmatter**（必需）：YAML 元数据，包含 `name` 和 `description`
2. **Markdown 主体**（必需）：技能说明、使用时机、详细步骤

**命名规范**：
- 文件名必须全大写：`SKILL.md`
- 目录名使用小写连字符：`skill-name`
- Frontmatter 中的 `name` 与目录名一致

### Frontmatter

**定义**：SKILL.md 文件开头的 YAML 元数据块。

**必需字段**：
- `name`：技能标识符（小写，连字符分隔）
- `description`：描述性文字，说明何时使用此技能

**可选字段**：
- `license`：许可证说明

**质量要求**：
- Description 决定 Claude 何时使用技能
- 使用第三人称（"此技能应在...时使用"）
- 要具体说明功能和使用时机

### 渐进式披露

**定义**：技能使用三级加载系统高效管理上下文。

**级别**：
1. **元数据** - 始终在上下文中（约 100 词）
2. **SKILL.md 主体** - 技能触发时加载（<5k 词）
3. **捆绑资源** - Claude 按需加载（无限制）

### 捆绑资源

**定义**：技能的可选辅助文件，用于增强技能能力。

**类型**：
- **scripts/**：可执行代码（Python/Bash 等）
- **references/**：参考文档，按需加载到上下文
- **assets/**：输出中使用的资源文件（模板、图片、字体等）

## 项目定位

### 文档和模板项目

本项目不是传统意义上的软件工程代码库。核心内容是：
- Markdown 格式的技能定义文件
- GitHub Pages 文档站点
- 中文翻译内容

### 技术栈

**核心**：
- Markdown - 技能定义和文档的主要格式
- YAML - 技能元数据 frontmatter

**文档站点**：
- VitePress - 静态站点生成器（Vue.js 生态）
- GitHub Pages - 托管和部署
- vitepress-plugin-mermaid - Mermaid 图表支持
- vitepress-plugin-llms - AI 索引生成（llms.txt）

### VitePress 主题定制

主题样式采用 **CSS 变量覆盖** 模式：

```
docs/.vitepress/theme/
├── index.ts          # 主题入口，注册自定义组件
├── style.css         # 自定义样式（品牌色、字体、布局）
└── components/       # 自定义 Vue 组件
```

**修改品牌色**：编辑 `style.css` 中的 CSS 变量（如 `--vp-c-brand-1`）。

## 工作流程

### 创建技能

1. 通过具体示例理解技能需求
2. 规划可复用技能内容（脚本、参考资料、资产）
3. 初始化技能目录
4. 编辑 SKILL.md 和捆绑资源
5. 打包验证
6. 迭代改进

### 贡献流程

1. 检查重复技能
2. 创建目录和 SKILL.md
3. 添加可选资源
4. 更新 README.md
5. 提交 PR

## 写作规范

### 语言

- 所有技能和文档使用中文（zh-CN）
- 代码注释使用中文
- 保持翻译表达自然准确

### 技能写作风格

- 使用**祈使/不定式形式**（动词优先的说明）
- 客观、指导性语言（"要完成 X，执行 Y" 而非 "你应该做 X"）
- 面向 Claude（AI）而非最终用户
- 保持简洁，避免冗长解释

## 许可证

- 项目整体：Apache License 2.0
- 个别技能：可能有不同许可证，查看技能目录中的 LICENSE.txt

## 相关资源

- 原项目：https://github.com/ComposioQ/awesome-claude-skills
- GitHub Pages：https://lessup.github.io/awesome-claude-skills-zh
- 维护者：LessUp (https://github.com/LessUp)
