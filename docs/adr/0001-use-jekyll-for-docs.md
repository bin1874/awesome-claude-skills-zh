# ADR-0001: 使用 VitePress 构建文档站点

## 状态

已接受（替代原有的 Jekyll 方案）

## 背景

本项目需要一个文档站点来展示技能列表、使用指南和贡献说明。文档站点需要：

1. 易于维护 - 内容以 Markdown 为主
2. 自动部署 - 减少手动操作
3. 免费托管 - 降低项目成本
4. 中文支持 - 本地化需求
5. 良好的搜索和导航功能
6. 现代化的开发体验 - 快速的热更新

## 决策

使用 **VitePress** 作为静态站点生成器，部署到 **GitHub Pages**，使用默认主题加自定义样式。

## 理由

### 选择 VitePress

1. **Vue.js 生态** - 基于 Vite 构建，开发体验极佳
2. **快速热更新** - 开发时即时预览更改
3. **内置本地搜索** - 无需额外配置
4. **TypeScript 支持** - 配置文件可类型检查
5. **Mermaid 图表** - 支持 Mermaid 流程图和图表
6. **llms.txt 支持** - 生成 AI 友好的文档索引

### 选择 GitHub Pages

1. **免费托管** - 公开仓库免费使用
2. **自动部署** - 通过 GitHub Actions 自动构建和部署
3. **自定义域名支持** - 可配置自定义域名
4. **与 GitHub 深度集成** - 与项目仓库紧密关联

### 品牌定制

- 使用琥珀色作为品牌色（#d97706）
- 自定义组件样式（skill-card、stats 等）

## 后果

### 正面

- 文档更新只需编辑 Markdown 文件
- 推送到 main 分支自动部署，无需手动干预
- 无服务器成本
- 良好的用户体验（搜索、导航、响应式）
- 极快的开发体验（热更新）
- 支持 Mermaid 图表
- 生成 llms.txt 便于 AI 索引

### 负面

- 需要 Node.js 构建环境
- 构建产物需要 `.nojekyll` 文件防止 Jekyll 处理

## 迁移历史

### 原方案（已废弃）

最初使用 Jekyll + just-the-docs 主题，但由于：
- 开发体验较慢
- 插件受 GitHub Pages 白名单限制
- 缺乏现代化工具链支持

于 2025 年迁移至 VitePress。

## 参考

- [VitePress 官方文档](https://vitepress.dev/)
- [GitHub Pages 文档](https://docs.github.com/en/pages)
- [vitepress-plugin-mermaid](https://github.com/emersonbottero/vitepress-plugin-mermaid)
- [vitepress-plugin-llms](https://github.com/okineadev/vitepress-plugin-llms)
