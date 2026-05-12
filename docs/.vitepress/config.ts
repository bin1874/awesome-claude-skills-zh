import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'
import llmstxt from 'vitepress-plugin-llms'

const rawBase = process.env.VITEPRESS_BASE
const base = rawBase
  ? rawBase.startsWith('/')
    ? rawBase.endsWith('/') ? rawBase : `${rawBase}/`
    : `/${rawBase}/`
  : '/'

export default withMermaid(defineConfig({
  base,
  title: 'Awesome Claude Skills 中文版',
  description: '中文 Claude Skills 高质量索引、实战场景与落地指南',

  ignoreDeadLinks: [
    /\.\.\/AGENTS/,
  ],

  locales: {
    zh: {
      label: '简体中文',
      lang: 'zh-CN',
      link: '/zh/',
      title: 'Awesome Claude Skills 中文版',
      description: '中文 Claude Skills 高质量索引、实战场景与落地指南',
      themeConfig: {
        nav: [
          { text: '指南', link: '/zh/guides/getting-started', activeMatch: '/zh/guides/' },
          { text: '技能索引', link: '/zh/skills/', activeMatch: '/zh/skills/' },
          { text: '实战手册', link: '/zh/playbooks/', activeMatch: '/zh/playbooks/' },
          { text: '资源导航', link: '/zh/resources', activeMatch: '/zh/resources' },
          { text: '贡献', link: '/zh/contribute', activeMatch: '/zh/contribute' },
          { text: '关于', link: '/zh/about', activeMatch: '/zh/about' },
        ],
        sidebar: {
          '/zh/guides/': [
            {
              text: '指南',
              items: [
                { text: '入门指南', link: '/zh/guides/getting-started' },
              ],
            },
          ],
          '/zh/skills/': [
            {
              text: '技能',
              items: [
                { text: '技能索引', link: '/zh/skills/' },
              ],
            },
          ],
          '/zh/playbooks/': [
            {
              text: '实战手册',
              items: [
                { text: '概览', link: '/zh/playbooks/' },
              ],
            },
          ],
        },
      },
    },
  },

  themeConfig: {
    outline: [2, 3],
    search: { provider: 'local' },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/LessUp/awesome-claude-skills-zh' },
    ],
    footer: {
      message: '文档内容遵循 Apache License 2.0',
      copyright: 'Maintained by LessUp · Based on ComposioQ/awesome-claude-skills',
    },
  },

  vite: {
    plugins: [llmstxt()],
  },
}))
