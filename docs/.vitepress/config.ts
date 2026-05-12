import { defineConfig } from "vitepress"
import { withMermaid } from "vitepress-plugin-mermaid"
import llmstxt from "vitepress-plugin-llms"

const rawBase = process.env.VITEPRESS_BASE
const base = rawBase
  ? rawBase.startsWith("/")
    ? rawBase.endsWith("/") ? rawBase : `${rawBase}/`
    : `/${rawBase}/`
  : "/"

export default withMermaid(defineConfig({
  base,
  title: "Awesome Claude Skills 中文版",
  description: "中文 Claude Skills 高质量索引、实战场景与落地指南",
  lang: "zh-CN",
  cleanUrls: true,
  lastUpdated: true,

  ignoreDeadLinks: [
    /\.\.\/AGENTS/,
    /\.\.\/template-skill\/SKILL/,
  ],

  themeConfig: {
    nav: [
      { text: "首页", link: "/" },
      { text: "实战手册", link: "/playbooks", activeMatch: "/playbooks" },
      { text: "技能索引", link: "/skills", activeMatch: "/skills" },
      { text: "入门指南", link: "/getting-started", activeMatch: "/getting-started" },
      { text: "资源导航", link: "/resources", activeMatch: "/resources" },
      { text: "贡献", link: "/contribute", activeMatch: "/contribute" },
      { text: "关于", link: "/about", activeMatch: "/about" },
    ],
    sidebar: {
      "/": [
        {
          text: "开始",
          items: [
            { text: "首页", link: "/" },
            { text: "入门指南", link: "/getting-started" },
          ],
        },
        {
          text: "核心内容",
          items: [
            { text: "实战手册", link: "/playbooks" },
            { text: "技能索引", link: "/skills" },
            { text: "资源导航", link: "/resources" },
          ],
        },
        {
          text: "社区与维护",
          items: [
            { text: "贡献指南", link: "/contribute" },
            { text: "关于项目", link: "/about" },
          ],
        },
      ],
    },
    socialLinks: [
      { icon: "github", link: "https://github.com/LessUp/awesome-claude-skills-zh" },
    ],
    outline: [2, 3],
    search: {
      provider: "local",
    },
    footer: {
      message: "文档内容遵循 Apache License 2.0",
      copyright: "Maintained by LessUp · Based on ComposioQ/awesome-claude-skills",
    },
  },

  vite: {
    plugins: [llmstxt()],
  },
}))
