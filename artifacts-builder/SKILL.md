---
name: artifacts-builder
description: 用于创建复杂的、多组件的 claude.ai HTML artifacts 的工具套件，使用现代前端 Web 技术（React、Tailwind CSS、shadcn/ui）。适用于需要状态管理、路由或 shadcn/ui 组件的复杂 artifacts，不适用于简单的单文件 HTML/JSX artifacts。
license: 完整条款见 LICENSE.txt
---

# Artifacts Builder

要构建强大的前端 claude.ai artifacts，请按以下步骤操作：
1. 使用 `scripts/init-artifact.sh` 初始化前端项目
2. 通过编辑生成的代码来开发你的 artifact
3. 使用 `scripts/bundle-artifact.sh` 将所有代码打包成单个 HTML 文件
4. 向用户展示 artifact
5. （可选）测试 artifact

**技术栈**：React 18 + TypeScript + Vite + Parcel（打包）+ Tailwind CSS + shadcn/ui

## 设计与风格指南

非常重要：为避免所谓的"AI 风格"，避免使用过度居中的布局、紫色渐变、统一的圆角和 Inter 字体。

## 快速开始

### 步骤 1：初始化项目

运行初始化脚本创建新的 React 项目：
```bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
```

这将创建一个完全配置的项目，包含：
- ✅ React + TypeScript（通过 Vite）
- ✅ Tailwind CSS 3.4.1 与 shadcn/ui 主题系统
- ✅ 路径别名（`@/`）已配置
- ✅ 预装 40+ shadcn/ui 组件
- ✅ 包含所有 Radix UI 依赖
- ✅ 已配置 Parcel 用于打包（通过 .parcelrc）
- ✅ Node 18+ 兼容（自动检测并固定 Vite 版本）

### 步骤 2：开发你的 Artifact

要构建 artifact，请编辑生成的文件。参见下方的**常见开发任务**。

### 步骤 3：打包成单个 HTML 文件

要将 React 应用打包成单个 HTML artifact：
```bash
bash scripts/bundle-artifact.sh
```

这将创建 `bundle.html` - 一个自包含的 artifact，所有 JavaScript、CSS 和依赖都已内联。此文件可以直接在 Claude 对话中作为 artifact 分享。

**要求**：你的项目必须在根目录有 `index.html`。

**脚本做了什么**：
- 安装打包依赖（parcel、@parcel/config-default、parcel-resolver-tspaths、html-inline）
- 创建带路径别名支持的 `.parcelrc` 配置
- 使用 Parcel 构建（无 source maps）
- 使用 html-inline 将所有资源内联成单个 HTML

### 步骤 4：与用户分享 Artifact

最后，在对话中分享打包好的 HTML 文件，让用户可以将其作为 artifact 查看。

### 步骤 5：测试/可视化 Artifact（可选）

注意：这是完全可选的步骤。仅在必要或用户请求时执行。

要测试/可视化 artifact，使用可用工具（包括其他 Skills 或 Playwright、Puppeteer 等内置工具）。一般来说，避免在初始阶段测试 artifact，因为它会在请求和完成的 artifact 之间增加延迟。在展示 artifact 之后，如果请求或出现问题时再进行测试。

## 参考

- **shadcn/ui 组件**：https://ui.shadcn.com/docs/components
