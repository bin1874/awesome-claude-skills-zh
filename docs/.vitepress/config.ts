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
  description: 'AI Agent 技能系统 · 技术白皮书',
  lang: 'zh-CN',

  head: [
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    ['link', { href: 'https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700&family=Noto+Serif+SC:wght@400;600;700&family=JetBrains+Mono:wght@400;500&display=swap', rel: 'stylesheet' }],
  ],

  ignoreDeadLinks: [
    /\.\.\/AGENTS/,
  ],

  themeConfig: {
    nav: [
      { text: '理论', link: '/theory/', activeMatch: '/theory/' },
      { text: '架构', link: '/architecture/', activeMatch: '/architecture/' },
      { text: '技能', link: '/skills/', activeMatch: '/skills/' },
      { text: '实践', link: '/practice/', activeMatch: '/practice/' },
      { text: '参考', link: '/reference/', activeMatch: '/reference/' },
    ],
    sidebar: {
      '/theory/': [
        {
          text: '理论',
          items: [
            { text: '概述', link: '/theory/' },
            { text: '智能体架构', link: '/theory/agent-arch' },
            { text: '提示工程', link: '/theory/prompt-eng' },
            { text: 'Skills 系统', link: '/theory/skill-system' },
          ],
        },
      ],
      '/architecture/': [
        {
          text: '架构',
          items: [
            { text: '架构总览', link: '/architecture/' },
            { text: '渐进式加载', link: '/architecture/loading' },
            { text: '执行引擎', link: '/architecture/execution' },
          ],
        },
      ],
      '/skills/': [
        {
          text: '技能索引',
          items: [
            { text: '概览', link: '/skills/' },
          ],
        },
      ],
      '/practice/': [
        {
          text: '实践',
          items: [
            { text: '概述', link: '/practice/' },
            { text: '入门指南', link: '/practice/getting-started' },
            { text: '实战手册', link: '/practice/playbooks' },
          ],
        },
      ],
      '/reference/': [
        {
          text: '参考资料',
          items: [
            { text: '概览', link: '/reference/' },
            { text: '参考文献', link: '/reference/bibliography' },
            { text: '相关项目', link: '/reference/related' },
            { text: '架构决策', link: '/reference/adr' },
          ],
        },
      ],
    },
    outline: [2, 3],
    search: { provider: 'local' },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/LessUp/awesome-claude-skills-zh' },
    ],
    footer: {
      message: 'Apache License 2.0',
      copyright: 'Maintained by LessUp',
    },
  },

  vite: {
    plugins: [llmstxt()],
  },
}))
