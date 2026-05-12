#!/usr/bin/env node

import { existsSync, mkdirSync, readFileSync, readdirSync, writeFileSync } from "node:fs"
import path from "node:path"
import { fileURLToPath } from "node:url"

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

const docsRoot = path.resolve(__dirname, "..")
const repoRoot = path.resolve(docsRoot, "..")

const readmePath = path.join(repoRoot, "README.md")
const categoryConfigPath = path.join(repoRoot, "scripts", "skill_categories.json")
const outputPath = path.join(docsRoot, ".vitepress", "data", "skills.json")
const composioDirPath = path.join(repoRoot, "composio-skills")

const sectionAliasMap = {
  "通过 Composio 的应用自动化": "应用自动化 (Composio)",
}

const categoryMetaMap = {
  文档处理: { id: "documents", emoji: "📄" },
  开发与代码工具: { id: "development", emoji: "💻" },
  数据与分析: { id: "data-analysis", emoji: "📊" },
  商业与营销: { id: "business-marketing", emoji: "📈" },
  沟通与写作: { id: "communication-writing", emoji: "💬" },
  创意与媒体: { id: "creative-media", emoji: "🎨" },
  生产力与组织: { id: "productivity", emoji: "⚡" },
  协作与项目管理: { id: "collaboration", emoji: "🤝" },
  安全与系统: { id: "security", emoji: "🔒" },
  辅助技术: { id: "assistive-tech", emoji: "🧩" },
  "应用自动化 (Composio)": { id: "automation-composio", emoji: "🔌" },
}

const knownLinkOverrides = {
  "software-architecture": "https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/ddd",
  "root-cause-tracing": "https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/root-cause-tracing.md",
  "computer-forensics": "https://github.com/AlabamaMike/forensic-skills",
  "file-deletion": "https://github.com/ljagiello/ctf-skills/tree/main/ctf-forensics",
  "metadata-extraction": "https://github.com/mukul975/Anthropic-Cybersecurity-Skills/tree/main/skills/analyzing-disk-image-with-autopsy",
  "threat-hunting-with-sigma-rules": "https://github.com/AgentSecOps/SecOpsAgentKit/tree/main/skills/incident-response/detection-sigma",
  tapestry: "https://github.com/michalparkola/tapestry-skills/tree/main",
}

const localPathMap = {
  "changelog generator": "changelog-generator",
  "skill creator": "skill-creator",
  "langsmith fetch": "langsmith-fetch",
  "developer growth analysis": "developer-growth-analysis",
  "brand guidelines": "brand-guidelines",
  "competitive ads extractor": "competitive-ads-extractor",
  "domain name brainstormer": "domain-name-brainstormer",
  "internal comms": "internal-comms",
  "lead research assistant": "lead-research-assistant",
  "content research writer": "content-research-writer",
  "meeting insights analyzer": "meeting-insights-analyzer",
  "twitter algorithm optimizer": "twitter-algorithm-optimizer",
  "canvas design": "canvas-design",
  "image enhancer": "image-enhancer",
  "slack gif creator": "slack-gif-creator",
  "theme factory": "theme-factory",
  "video downloader": "video-downloader",
  "file organizer": "file-organizer",
  "invoice organizer": "invoice-organizer",
  "raffle winner picker": "raffle-winner-picker",
  "tailored resume generator": "tailored-resume-generator",
  "skill share": "skill-share",
  "document skills": "document-skills",
  "mcp builder": "mcp-builder",
  "webapp testing": "webapp-testing",
}

function normalizeCategory(rawCategory) {
  return sectionAliasMap[rawCategory] || rawCategory
}

function normalizeLocalPath(rawLink) {
  return rawLink
    .replace(/^\.\//, "")
    .replace(/\/+$/, "")
}

function normalizeSkillKey(rawName) {
  return rawName.trim().toLowerCase()
}

function unique(values) {
  return [...new Set(values)]
}

function trimTrailingSlash(url) {
  return url.replace(/\/+$/, "")
}

function slugifyCategory(value) {
  return value
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
}

function cleanDescription(rawDescription) {
  const authorPattern = /\s*\*作者\s+\[@[^\]]+\]\([^)]+\)\*\s*$/u
  return rawDescription
    .replace(authorPattern, "")
    .trim()
}

function extractAuthor(rawDescription) {
  const matched = rawDescription.match(/\*作者\s+\[@([^\]]+)\]\([^)]+\)\*/u)
  if (!matched) {
    return undefined
  }

  return `@${matched[1]}`
}

function stripWrappingQuotes(rawValue) {
  const value = rawValue.trim()
  if (
    (value.startsWith('"') && value.endsWith('"'))
    || (value.startsWith("'") && value.endsWith("'"))
  ) {
    return value.slice(1, -1).trim()
  }
  return value
}

function readSkillFrontmatter(skillFilePath) {
  if (!existsSync(skillFilePath)) {
    return {}
  }

  const content = readFileSync(skillFilePath, "utf-8")
  const match = content.match(/^---\n([\s\S]*?)\n---/)
  if (!match) {
    return {}
  }

  const frontmatterBlock = match[1]
  const metadata = {}

  for (const rawLine of frontmatterBlock.split("\n")) {
    const line = rawLine.trim()
    if (!line || line.startsWith("#")) {
      continue
    }

    const lineMatch = line.match(/^([a-zA-Z0-9_-]+):\s*(.+)$/)
    if (!lineMatch) {
      continue
    }

    const key = lineMatch[1]
    const value = stripWrappingQuotes(lineMatch[2])
    metadata[key] = value
  }

  return metadata
}

function prettifySkillName(rawValue) {
  const value = rawValue.trim()
  if (!value.includes("-")) {
    return value
  }

  return value
    .split("-")
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(" ")
}

function parseReadmeIndex(readmeContent) {
  const sectionMatch = readmeContent.match(/## 技能列表\s*([\s\S]*?)\n## 入门指南/u)
  if (!sectionMatch) {
    throw new Error("无法在 README.md 中找到“技能列表”章节。")
  }

  const sectionText = sectionMatch[1]
  const lines = sectionText.split("\n")

  const local = new Map()
  const external = new Map()

  for (const rawLine of lines) {
    const line = rawLine.trim()
    if (!line.startsWith("- [")) {
      continue
    }

    const itemMatch = line.match(/^- \[([^\]]+)\]\(([^)]+)\)\s*-\s*(.+)$/u)
    if (!itemMatch) {
      continue
    }

    const name = itemMatch[1].trim()
    const rawLink = itemMatch[2].trim()
    const rawDescription = itemMatch[3].trim()
    const info = {
      name,
      description: cleanDescription(rawDescription),
      author: extractAuthor(rawDescription),
    }

    if (rawLink.startsWith("./")) {
      const key = normalizeLocalPath(rawLink)
      local.set(key, info)
      continue
    }

    if (rawLink.startsWith("http://") || rawLink.startsWith("https://")) {
      external.set(rawLink, info)
      external.set(trimTrailingSlash(rawLink), info)
    }
  }

  return { local, external }
}

function loadCategoryConfig() {
  if (!existsSync(categoryConfigPath)) {
    throw new Error(`分类配置文件不存在: ${categoryConfigPath}`)
  }
  const configText = readFileSync(categoryConfigPath, "utf-8")
  try {
    return JSON.parse(configText)
  } catch (parseError) {
    throw new Error(`分类配置文件 JSON 格式错误: ${parseError.message}`)
  }
}

function getCategoryMeta(categoryName) {
  return categoryMetaMap[categoryName] || {
    id: slugifyCategory(categoryName),
    emoji: "📁",
  }
}

function resolveLocalSkillPath(candidatePath) {
  const rootSkillFile = path.join(repoRoot, candidatePath, "SKILL.md")
  if (existsSync(rootSkillFile)) {
    return candidatePath
  }

  const composioCandidate = path.join("composio-skills", candidatePath)
  const composioSkillFile = path.join(repoRoot, composioCandidate, "SKILL.md")
  if (existsSync(composioSkillFile)) {
    return composioCandidate
  }

  return undefined
}

function countComposioSkills() {
  if (!existsSync(composioDirPath)) {
    return 0
  }

  const entries = readdirSafe(composioDirPath)
  let total = 0
  for (const entry of entries) {
    const skillPath = path.join(composioDirPath, entry)
    const skillFile = path.join(skillPath, "SKILL.md")
    if (existsSync(skillFile)) {
      total += 1
    }
  }

  return total
}

function readdirSafe(dirPath) {
  try {
    return readdirSync(dirPath, { withFileTypes: false })
  } catch {
    return []
  }
}

function dedupeSkills(skills) {
  const seen = new Set()
  const output = []
  for (const skill of skills) {
    const key = `${skill.source}:${skill.name.toLowerCase()}`
    if (seen.has(key)) {
      continue
    }
    seen.add(key)
    output.push(skill)
  }
  return output
}

function buildSkillsData(config, readmeIndex) {
  const categories = []
  const skippedMissingLocal = []
  const composioCount = countComposioSkills()

  for (const [rawCategoryName, categoryConfig] of Object.entries(config.categories || {})) {
    const categoryName = normalizeCategory(rawCategoryName)
    const meta = getCategoryMeta(categoryName)
    const categorySkills = []

    const localSkillKeys = categoryConfig?.skills || []
    for (const rawSkillKey of localSkillKeys) {
      const rawKey = String(rawSkillKey)
      const normalizedKey = normalizeSkillKey(rawKey)
      const mappedKey = localPathMap[normalizedKey] || rawKey
      const localPath = normalizeLocalPath(mappedKey)

      if (localPath === "composio-skills") {
        if (composioCount > 0) {
          categorySkills.push({
            name: "Composio Skills Catalog",
            description: `自动化技能全集（当前收录 ${composioCount} 个应用技能目录）`,
            source: "external",
            url: "https://github.com/LessUp/awesome-claude-skills-zh/tree/master/composio-skills",
          })
        }
        continue
      }

      const resolvedPath = resolveLocalSkillPath(localPath)
      if (!resolvedPath) {
        skippedMissingLocal.push(`${categoryName}/${localPath}`)
        continue
      }

      const readmeInfo = readmeIndex.local.get(localPath) || readmeIndex.local.get(resolvedPath)
      const skillFilePath = path.join(repoRoot, resolvedPath, "SKILL.md")
      const frontmatter = readSkillFrontmatter(skillFilePath)

      const name = readmeInfo?.name
        || frontmatter.name
        || prettifySkillName(localPath)
      const description = readmeInfo?.description
        || frontmatter.description
        || `${name} 技能`

      categorySkills.push({
        name,
        description,
        source: "local",
        path: resolvedPath,
        ...(readmeInfo?.author ? { author: readmeInfo.author } : {}),
      })
    }

    const externalConfigured = config.external_skills?.[rawCategoryName]
      || config.external_skills?.[categoryName]
      || []

    for (const externalItem of externalConfigured) {
      const itemName = (externalItem?.name || "").trim()
      const normalizedName = normalizeSkillKey(itemName)
      const resolvedUrl = knownLinkOverrides[normalizedName] || externalItem?.url
      if (!resolvedUrl) {
        continue
      }

      const readmeInfo = readmeIndex.external.get(resolvedUrl)
        || readmeIndex.external.get(trimTrailingSlash(resolvedUrl))

      const name = itemName || readmeInfo?.name || "Unnamed Skill"
      const description = externalItem?.description
        || readmeInfo?.description
        || `${name} 技能`

      categorySkills.push({
        name,
        description,
        source: "external",
        url: resolvedUrl,
        ...(externalItem?.author ? { author: externalItem.author } : {}),
        ...(!externalItem?.author && readmeInfo?.author ? { author: readmeInfo.author } : {}),
      })
    }

    const curatedSkills = dedupeSkills(categorySkills)
    if (curatedSkills.length === 0) {
      continue
    }

    categories.push({
      id: meta.id,
      emoji: meta.emoji,
      name: categoryName,
      skills: curatedSkills,
    })
  }

  const totalSkills = categories.reduce((sum, category) => sum + category.skills.length, 0)
  const localSkills = categories
    .flatMap((category) => category.skills)
    .filter((skill) => skill.source === "local").length

  return {
    output: {
      meta: {
        repo: "LessUp/awesome-claude-skills-zh",
        repoBranch: process.env.SKILLS_REPO_BRANCH || "master",
        strategy: "curated-from-category-config",
        generatedFrom: {
          readme: "README.md",
          categoryConfig: "scripts/skill_categories.json",
        },
      },
      categories,
    },
    stats: {
      categories: categories.length,
      totalSkills,
      localSkills,
      externalSkills: totalSkills - localSkills,
      skippedMissingLocal: skippedMissingLocal.length,
      composioSkills: composioCount,
    },
  }
}

function main() {
  try {
    const config = loadCategoryConfig()
    const readmeText = readFileSync(readmePath, "utf-8")
    const readmeIndex = parseReadmeIndex(readmeText)
    const { output, stats } = buildSkillsData(config, readmeIndex)

    // 确保输出目录存在
    const outputDir = path.dirname(outputPath)
    if (!existsSync(outputDir)) {
      mkdirSync(outputDir, { recursive: true })
    }

    writeFileSync(outputPath, `${JSON.stringify(output, null, 2)}\n`, "utf-8")

    console.log("=== 技能数据生成完成 ===")
    console.log(`输出文件：${path.relative(repoRoot, outputPath)}`)
    console.log(`策略：${output.meta.strategy}`)
    console.log(`分类：${stats.categories}`)
    console.log(`技能：${stats.totalSkills}（本地 ${stats.localSkills} / 外部 ${stats.externalSkills}）`)
    console.log(`跳过（本地目录缺失）：${stats.skippedMissingLocal}`)
    console.log(`Composio 自动化目录：${stats.composioSkills}`)
  } catch (error) {
    console.error(`❌ 技能数据生成失败: ${error.message}`)
    process.exit(1)
  }
}

main()
