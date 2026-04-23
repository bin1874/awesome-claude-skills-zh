---
name: preview
description: 启动本地 Jekyll 服务器，在 http://localhost:4000 预览文档站点
---

# 预览 Jekyll 站点

启动本地 Jekyll 开发服务器以预览文档站点。

## 步骤

1. 进入 docs 目录：
   ```bash
   cd docs
   ```

2. 确保依赖已安装：
   ```bash
   bundle install
   ```

3. 启动 Jekyll 服务器：
   ```bash
   bundle exec jekyll serve
   ```

4. 在浏览器中打开 http://localhost:4000 查看站点。

5. 完成后按 Ctrl+C 停止服务器。

## 注意

- 文件变更时站点自动重新生成。
- 推送到 main/master 分支后自动部署到 GitHub Pages。
