# GitHub Pages 学术论文风格重构设计文档

> **日期**: 2026-05-17
> **方案**: 方案 A — 激进重构

## 目标

将 awesome-claude-skills-zh 的 GitHub Pages 从"工具文档"定位，彻底重构为**学术论文级技术白皮书站点**，面向高级开发者和 AI Agent 领域研究者。核心定位：系统架构设计、算法介绍、技术白皮书与性能、参考资料。

## 设计决策

### 1. 视觉风格：学术论文排版

- **仅浅色模式**：模拟 ACM/arXiv 的白纸黑字经典体验
- **字体系统**：Serif 标题（LXGW WenKai / Noto Serif SC）+ Sans 正文（Inter/Noto Sans SC），中文优先
- **配色**：灰度主导（#1a1a2e → #f5f5f0），强调色用深靛蓝（#1e3a5f）+ 淡金（#b8860b）
- **排版**：宽版心、双栏摘要、脚注引用、编号章节
- **移除所有 emoji 图标**：用编号、符号（§, †, ‡, ※）替代

### 2. 架构：内容结构重构

新文档目录树（5 层递进）：

```
/                          → 学术首页（摘要 + 核心数据 + 导航）
/theory/                   → AI Agent 理论
  /theory/agent-arch       → 智能体架构理论
  /theory/prompt-eng       → 提示工程原理
  /theory/skill-system     → Skills 系统设计
/architecture/             → 系统架构
  /architecture/overview   → 架构总览
  /architecture/loading    → 渐进式加载机制
  /architecture/execution  → 执行引擎
/skills/                   → 技能索引（保留增强）
/practice/                 → 实践指南
  /practice/playbooks      → 实战手册
  /practice/getting-started → 入门指南
/reference/                → 参考资料
  /reference/bibliography  → 参考文献
  /reference/related       → 相关项目
  /reference/adr           → 架构决策记录
/contribute/               → 贡献指南
/about/                    → 关于
```

### 3. 新增深度内容

- **AI Agent 理论**：ReAct、Chain-of-Thought、Tool-Use、Planning 等核心理论
- **提示工程原理**：系统提示设计、Few-shot、CoT 变体
- **Skills 系统设计**：三级渐进加载、技能激活机制、技能组合策略
- **系统架构**：加载流程、执行引擎、跨平台适配

### 4. 学术引用机制

- 每个理论页面底部有"参考文献"节
- 引用格式：`[1] Author, "Title", Venue, Year. URL`
- 文内用 `[1]` 上标引用
- 全局参考文献汇总页 `/reference/bibliography`

### 5. 可视化方案

- **Mermaid**：所有流程图、时序图、状态机图
- **SVG**：3-5 个关键概念图（Agent 架构图、Skills 加载流程、三层渐进加载）
- SVG 存放于 `docs/media/` 目录

### 6. 技术实现

- 保留 VitePress 框架
- 自定义 CSS 实现论文排版
- 移除深色模式切换
- 新增 Vue 组件：引用块、摘要块、章节编号
- Mermaid 图表 + 精细 SVG 并存

## 约束

- 所有内容使用中文
- 技术术语保留英文
- 遵循 Apache License 2.0
- 保持 GitHub Pages 自动部署
