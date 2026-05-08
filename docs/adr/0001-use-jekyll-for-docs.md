# ADR-0001: 使用 Jekyll 和 GitHub Pages 构建文档站点

## 状态

已接受

## 背景

本项目需要一个文档站点来展示技能列表、使用指南和贡献说明。文档站点需要：

1. 易于维护 - 内容以 Markdown 为主
2. 自动部署 - 减少手动操作
3. 免费托管 - 降低项目成本
4. 中文支持 - 本地化需求
5. 良好的搜索和导航功能

## 决策

使用 **Jekyll** 作为静态站点生成器，部署到 **GitHub Pages**，使用 **just-the-docs** 主题。

## 理由

### 选择 Jekyll

1. **GitHub Pages 原生支持** - 无需额外 CI/CD 配置
2. **Markdown 优先** - 技能本身就是 Markdown 格式，无缝衔接
3. **成熟生态** - 丰富的主题和插件
4. **简单配置** - 一个 `_config.yml` 即可完成大部分配置

### 选择 GitHub Pages

1. **免费托管** - 公开仓库免费使用
2. **自动部署** - 推送代码后自动构建和部署
3. **自定义域名支持** - 可配置自定义域名
4. **与 GitHub 深度集成** - 与项目仓库紧密关联

### 选择 just-the-docs 主题

1. **文档导向设计** - 专为文档站点设计
2. **内置搜索** - 前端全文搜索，无需后端
3. **灵活导航** - 支持多级导航和外部链接
4. **响应式设计** - 移动端友好
5. **可定制性强** - 支持自定义颜色方案和布局

## 后果

### 正面

- 文档更新只需编辑 Markdown 文件
- 推送到 main 分支自动部署，无需手动干预
- 无服务器成本
- 良好的用户体验（搜索、导航、响应式）

### 负面

- GitHub Pages 限制 Jekyll 插件（仅支持白名单插件）
- 构建时间随内容增长可能变长
- 自定义主题需要使用 `remote_theme` 配置

### 风险缓解

- 对于复杂功能需求，评估是否可通过前端实现
- 监控构建时间，必要时优化内容结构
- 保持 `remote_theme` 版本固定，避免意外更新

## 替代方案

### Docusaurus

- 优点：React 生态，功能强大，版本化文档支持
- 缺点：需要 Node.js 构建环境，配置复杂度高
- 放弃原因：对于纯文档项目过于复杂

### VuePress

- 优点：Vue 生态，性能好
- 缺点：需要 Node.js 构建环境
- 放弃原因：团队更熟悉 Ruby/Jekyll 生态

### MkDocs

- 优点：Python 生态，简单易用
- 缺点：GitHub Pages 支持不如 Jekyll 原生
- 放弃原因：需要额外的 CI/CD 配置

## 参考

- [Jekyll 官方文档](https://jekyllrb.com/)
- [GitHub Pages 文档](https://docs.github.com/en/pages)
- [just-the-docs 主题](https://just-the-docs.github.io/)
