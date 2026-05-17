import DefaultTheme from 'vitepress/theme'
import Abs from './components/Abs.vue'
import Cite from './components/Cite.vue'
import Section from './components/Section.vue'
import './style.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Abs', Abs)
    app.component('Cite', Cite)
    app.component('Section', Section)
  }
}
