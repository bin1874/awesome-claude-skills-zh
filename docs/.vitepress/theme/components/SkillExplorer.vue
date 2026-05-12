<script setup lang="ts">
import { computed, ref } from "vue"
import skillsData from "../../data/skills.json"

interface SkillEntry {
  name: string
  description: string
  source: "local" | "external"
  path?: string
  url?: string
  author?: string
}

interface SkillCategory {
  id: string
  emoji: string
  name: string
  skills: SkillEntry[]
}

const categories = skillsData.categories as SkillCategory[]

const query = ref("")
const selectedCategory = ref("all")
const selectedSource = ref("all")

const normalizedQuery = computed(() => query.value.trim().toLowerCase())

const sourceLabel = (source: SkillEntry["source"]) => {
  return source === "local" ? "本仓库" : "外部仓库"
}

const resolveSkillLink = (skill: SkillEntry) => {
  if (skill.source === "local") {
    // GitHub Pages 中本仓库目录统一走当前默认分支 master，避免 main 导致 404。
    return `https://github.com/${skillsData.meta.repo}/tree/${skillsData.meta.repoBranch}/${skill.path}`
  }

  return skill.url || "#"
}

const filteredCategories = computed(() => {
  const matchedByCategory = categories
    .filter((category) => {
      return selectedCategory.value === "all" || category.id === selectedCategory.value
    })
    .map((category) => {
      const skills = category.skills.filter((skill) => {
        const sourceMatch = selectedSource.value === "all" || skill.source === selectedSource.value

        if (!sourceMatch) {
          return false
        }

        if (!normalizedQuery.value) {
          return true
        }

        const haystacks = [skill.name, skill.description, skill.author || "", category.name]
          .join(" ")
          .toLowerCase()

        return haystacks.includes(normalizedQuery.value)
      })

      return { ...category, skills }
    })
    .filter((category) => category.skills.length > 0)

  return matchedByCategory
})

const totalVisible = computed(() => {
  return filteredCategories.value.reduce((sum, category) => sum + category.skills.length, 0)
})

const totalAll = computed(() => {
  return categories.reduce((sum, category) => sum + category.skills.length, 0)
})

const categoryOptions = computed(() => {
  return categories.map((category) => ({
    id: category.id,
    label: `${category.emoji} ${category.name}`,
  }))
})
</script>

<template>
  <div class="skills-shell">
    <p class="skills-intro">
      该页面已升级为数据驱动索引，可按关键词、来源和分类快速筛选，并统一修复了本仓库技能卡片在 GitHub Pages 的跳转分支问题。
    </p>

    <div class="skills-toolbar">
      <input
        v-model="query"
        class="skills-search"
        type="search"
        placeholder="搜索技能名、描述、作者（例如：Playwright / 终端 / 研究）"
        aria-label="搜索技能"
      >
      <select v-model="selectedCategory" class="skills-filter" aria-label="按分类筛选">
        <option value="all">全部分类</option>
        <option
          v-for="item in categoryOptions"
          :key="item.id"
          :value="item.id"
        >
          {{ item.label }}
        </option>
      </select>
      <select v-model="selectedSource" class="skills-filter" aria-label="按来源筛选">
        <option value="all">全部来源</option>
        <option value="local">本仓库</option>
        <option value="external">外部仓库</option>
      </select>
    </div>

    <div class="skills-summary">
      <span>显示 {{ totalVisible }} / {{ totalAll }} 个技能</span>
      <span>分类 {{ filteredCategories.length }} / {{ categories.length }}</span>
      <span>本仓库链接自动指向 {{ skillsData.meta.repoBranch }} 分支</span>
    </div>

    <div class="skills-jump">
      <a
        v-for="category in filteredCategories"
        :key="`jump-${category.id}`"
        class="jump-item"
        :href="`#${category.id}`"
      >
        {{ category.emoji }} {{ category.name }}
      </a>
    </div>

    <template v-if="filteredCategories.length > 0">
      <section
        v-for="category in filteredCategories"
        :id="category.id"
        :key="category.id"
        class="skill-category"
      >
        <div class="skill-category-header">
          <h2>{{ category.emoji }} {{ category.name }}</h2>
          <span class="skill-category-count">{{ category.skills.length }} 个技能</span>
        </div>

        <div class="skill-grid">
          <a
            v-for="skill in category.skills"
            :key="`${category.id}-${skill.name}`"
            class="skill-card"
            :href="resolveSkillLink(skill)"
            target="_blank"
            rel="noopener noreferrer"
          >
            <h3 class="skill-card-title">{{ skill.name }}</h3>
            <p class="skill-card-desc">{{ skill.description }}</p>
            <div class="skill-meta">
              <span
                class="meta-chip"
                :class="skill.source === 'local' ? 'is-local' : 'is-external'"
              >
                {{ sourceLabel(skill.source) }}
              </span>
              <span v-if="skill.author" class="skill-author">{{ skill.author }}</span>
            </div>
          </a>
        </div>
      </section>
    </template>

    <div v-else class="skills-empty">
      未找到匹配技能，请调整筛选条件或搜索关键词。
    </div>
  </div>
</template>
