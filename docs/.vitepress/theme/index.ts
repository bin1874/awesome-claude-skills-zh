import type { Theme } from "vitepress"
import DefaultTheme from "vitepress/theme"
import SkillExplorer from "./components/SkillExplorer.vue"
import "./style.css"

const theme: Theme = {
  ...DefaultTheme,
  enhanceApp(ctx) {
    DefaultTheme.enhanceApp?.(ctx)
    ctx.app.component("SkillExplorer", SkillExplorer)
  },
}

export default theme
