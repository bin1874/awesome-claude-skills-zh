import { defineConfig } from 'vitepress'

const rawBase = process.env.VITEPRESS_BASE
const base = rawBase
  ? rawBase.startsWith('/')
    ? rawBase.endsWith('/') ? rawBase : `${rawBase}/`
    : `/${rawBase}/`
  : '/'

export default defineConfig({
  base,
  title: 'Awesome Claude Skills 中文版',
  description: '精选的实用 Claude Skills 列表，提升 Claude.ai、Claude Code 和 Claude API 的生产力',
  lang: 'zh-CN',

  ignoreDeadLinks: [
    /\.\.\/AGENTS/,
    /\.\.\/template-skill\/SKILL/,
  ],

  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '技能列表', link: '/skills' },
      { text: '入门指南', link: '/getting-started' },
      { text: '贡献指南', link: '/contribute' },
      { text: '资源', link: '/resources' },
      { text: '关于', link: '/about' },
    ],

    sidebar: [
      {
        text: '指南',
        items: [
          { text: '入门指南', link: '/getting-started' },
          { text: '贡献指南', link: '/contribute' },
        ],
      },
      {
        text: '参考',
        items: [
          { text: '技能列表', link: '/skills' },
          { text: '资源', link: '/resources' },
          { text: '关于', link: '/about' },
        ],
      },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/LessUp/awesome-claude-skills-zh' },
    ],

    outline: [2, 3],

    search: {
      provider: 'local',
    },

    footer: {
      message: '采用 Apache License 2.0 许可证',
      copyright: '由 LessUp 维护 | 原项目: ComposioQ/awesome-claude-skills',
    },
  },
})
