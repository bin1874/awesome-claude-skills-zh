---
name: preview
description: 启动本地 VitePress 服务器，在 http://localhost:5173 预览文档站点
---

# 预览 VitePress 站点

启动本地 VitePress 开发服务器以预览文档站点。

## 步骤

1. 进入 docs 目录：
   ```bash
   cd docs
   ```

2. 确保依赖已安装：
   ```bash
   npm install
   ```

3. 启动 VitePress 开发服务器：
   ```bash
   npm run dev
   ```

4. 在浏览器中打开 http://localhost:5173 查看站点。

5. 完成后按 Ctrl+C 停止服务器。

## 注意

- 文件变更时站点自动热更新。
- 推送到 main/master 分支后自动部署到 GitHub Pages。
