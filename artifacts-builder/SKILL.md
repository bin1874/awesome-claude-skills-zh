---
name: artifacts-builder
description: 使用现代前端 Web 技术（React、Tailwind CSS、shadcn/ui）创建复杂多组件 claude.ai HTML artifacts 的工具套件。用于需要状态管理、路由或 shadcn/ui 组件的复杂 artifacts - 不适用于简单的单文件 HTML/JSX artifacts。
license: 完整条款见 LICENSE.txt
---

# Artifacts Builder

要构建强大的前端 claude.ai artifacts，请按以下步骤操作：
1. 使用 `scripts/init-artifact.sh` 初始化前端仓库
2. 通过编辑生成的代码开发你的 artifact
3. 使用 `scripts/bundle-artifact.sh` 将所有代码打包成单个 HTML 文件
4. 向用户展示 artifact
5. （可选）测试 artifact

**技术栈**：React 18 + TypeScript + Vite + Parcel（打包）+ Tailwind CSS + shadcn/ui

## 设计与样式指南

非常重要：为避免所谓的 "AI slop"，避免使用过多的居中布局、紫色渐变、统一的圆角和 Inter 字体。

## 快速开始

### 步骤 1：初始化项目

运行初始化脚本创建新的 React 项目：
```bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
```

这将创建一个完全配置好的项目，包含：
- ✅ React + TypeScript（通过 Vite）
- ✅ Tailwind CSS 3.4.1 与 shadcn/ui 主题系统
- ✅ 路径别名（`@/`）已配置
- ✅ 40+ shadcn/ui 组件预安装
- ✅ 所有 Radix UI 依赖已包含
- ✅ Parcel 已配置用于打包（通过 .parcelrc）
- ✅ Node 18+ 兼容性（自动检测并固定 Vite 版本）

### 步骤 2：开发你的 Artifact

要构建 artifact，编辑生成的文件。参见下方**常见开发任务**获取指导。

### 步骤 3：打包成单个 HTML 文件

要将 React 应用打包成单个 HTML artifact：
```bash
bash scripts/bundle-artifact.sh
```

这将创建 `bundle.html` - 一个包含所有 JavaScript、CSS 和依赖项的独立 artifact。此文件可直接在 Claude 对话中作为 artifact 分享。

**要求**：你的项目根目录必须有 `index.html`。

**脚本执行内容**：
- 安装打包依赖（parcel、@parcel/config-default、parcel-resolver-tspaths、html-inline）
- 创建支持路径别名的 `.parcelrc` 配置
- 使用 Parcel 构建（无源映射）
- 使用 html-inline 将所有资源内联到单个 HTML

### 步骤 4：与用户分享 Artifact

最后，在对话中与用户分享打包后的 HTML 文件，以便他们将其作为 artifact 查看。

### 步骤 5：测试/可视化 Artifact（可选）

注意：这是完全可选的步骤。仅在必要时或被请求时执行。

要测试/可视化 artifact，使用可用工具（包括其他 Skills 或内置工具如 Playwright 或 Puppeteer）。通常，避免预先测试 artifact，因为这会增加从请求到展示完成 artifact 之间的延迟。如果被请求或出现问题，在展示 artifact 后再进行测试。

## 参考

- **shadcn/ui 组件**：https://ui.shadcn.com/docs/components