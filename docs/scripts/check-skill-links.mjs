#!/usr/bin/env node

import { readFile } from "node:fs/promises"
import path from "node:path"
import { fileURLToPath } from "node:url"

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)
const docsRoot = path.resolve(__dirname, "..")
const repoRoot = path.resolve(docsRoot, "..")
const skillsDataPath = path.join(docsRoot, ".vitepress", "data", "skills.json")

const shouldSkipExternal = process.argv.includes("--skip-external")
const timeoutMs = Number(process.env.SKILLS_LINK_CHECK_TIMEOUT_MS || 12000)
const maxConcurrent = Number(process.env.SKILLS_LINK_CHECK_CONCURRENCY || 8)

const failures = []
const warnings = []

function fail(message) {
  failures.push(message)
}

function warn(message) {
  warnings.push(message)
}

function unique(values) {
  return [...new Set(values)]
}

function extractAnchorsFromMarkdown(markdownText) {
  const anchors = new Set()

  for (const match of markdownText.matchAll(/\{#([a-z0-9-]+)\}/gi)) {
    anchors.add(match[1].toLowerCase())
  }

  return anchors
}

function extractHashLinks(markdownText, routePrefix) {
  const escapedPrefix = routePrefix.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
  const regexp = new RegExp(`${escapedPrefix}#([a-z0-9-]+)`, "gi")
  const ids = []

  for (const match of markdownText.matchAll(regexp)) {
    ids.push(match[1].toLowerCase())
  }

  return ids
}

async function readJson(filePath) {
  const content = await readFile(filePath, "utf-8")
  return JSON.parse(content)
}

function validateDataSchema(skillsData) {
  if (!skillsData?.meta?.repo || !skillsData?.meta?.repoBranch) {
    fail("skills.json 缺少 meta.repo 或 meta.repoBranch。")
  }

  if (!Array.isArray(skillsData?.categories) || skillsData.categories.length === 0) {
    fail("skills.json 缺少 categories，或 categories 为空。")
    return
  }

  const categoryIds = skillsData.categories.map((category) => category.id)
  const uniqueIds = unique(categoryIds)

  if (categoryIds.length !== uniqueIds.length) {
    fail("skills.json 存在重复分类 id。")
  }

  for (const category of skillsData.categories) {
    if (!category.id || !category.name || !Array.isArray(category.skills)) {
      fail(`分类数据不完整：${JSON.stringify(category)}`)
      continue
    }

    for (const skill of category.skills) {
      if (!skill.name || !skill.description || !skill.source) {
        fail(`技能数据不完整：${category.name} / ${JSON.stringify(skill)}`)
      }

      if (skill.source === "local" && !skill.path) {
        fail(`本地技能缺少 path：${category.name} / ${skill.name}`)
      }

      if (skill.source === "external" && !skill.url) {
        fail(`外部技能缺少 url：${category.name} / ${skill.name}`)
      }
    }
  }
}

async function checkLocalSkillFiles(skillsData) {
  for (const category of skillsData.categories) {
    for (const skill of category.skills) {
      if (skill.source !== "local") {
        continue
      }

      const skillFilePath = path.join(repoRoot, skill.path, "SKILL.md")

      try {
        await readFile(skillFilePath, "utf-8")
      } catch {
        fail(`本地技能链接失效：${category.name} / ${skill.name} -> ${skillFilePath}`)
      }
    }
  }
}

async function checkHttpLink(url) {
  const controller = new AbortController()
  const timer = setTimeout(() => controller.abort(), timeoutMs)

  const headers = {
    "user-agent": "awesome-claude-skills-zh-link-checker/1.0",
  }

  try {
    let response = await fetch(url, {
      method: "HEAD",
      redirect: "follow",
      headers,
      signal: controller.signal,
    })

    if (response.status === 405 || response.status === 403) {
      response = await fetch(url, {
        method: "GET",
        redirect: "follow",
        headers,
        signal: controller.signal,
      })
    }

    return { ok: response.status >= 200 && response.status < 400, error: null }
  } catch (error) {
    const errorMessage = error.name === "AbortError" ? "请求超时" : error.message
    return { ok: false, error: errorMessage }
  } finally {
    clearTimeout(timer)
  }
}

async function checkHttpLinkWithRetry(url, retries = 1) {
  const firstAttempt = await checkHttpLink(url)
  if (firstAttempt.ok) {
    return { ok: true, error: null }
  }

  let lastError = firstAttempt.error
  for (let i = 0; i < retries; i += 1) {
    const retried = await checkHttpLink(url)
    if (retried.ok) {
      return { ok: true, error: null }
    }
    lastError = retried.error
  }

  return { ok: false, error: lastError }
}

async function checkExternalSkillLinks(skillsData) {
  const externalLinks = unique(
    skillsData.categories
      .flatMap((category) =>
        category.skills
          .filter((skill) => skill.source === "external")
          .map((skill) => skill.url),
      )
      .filter(Boolean),
  )

  const invalidLinks = []
  const queue = [...externalLinks]

  async function worker() {
    while (queue.length > 0) {
      const url = queue.shift()
      if (!url) {
        continue
      }

      const result = await checkHttpLinkWithRetry(url, 1)
      if (!result.ok) {
        invalidLinks.push({ url, error: result.error })
      }
    }
  }

  await Promise.all(Array.from({ length: Math.max(1, maxConcurrent) }, () => worker()))

  if (invalidLinks.length > 0) {
    for (const { url, error } of invalidLinks) {
      const errorDetail = error ? ` (${error})` : ""
      fail(`外部技能链接不可达：${url}${errorDetail}`)
    }
  }
}

async function validateAssociatedAnchorLinks(skillsData) {
  const categoryIds = new Set(skillsData.categories.map((category) => category.id.toLowerCase()))

  const indexText = await readFile(path.join(docsRoot, "index.md"), "utf-8")
  const playbooksText = await readFile(path.join(docsRoot, "playbooks.md"), "utf-8")

  const skillsHashLinks = [
    ...extractHashLinks(indexText, "/skills"),
    ...extractHashLinks(playbooksText, "/skills"),
  ]

  for (const hashId of skillsHashLinks) {
    if (!categoryIds.has(hashId)) {
      fail(`/skills#${hashId} 未在 skills.json 分类中找到对应 id。`)
    }
  }

  const playbookAnchors = extractAnchorsFromMarkdown(playbooksText)
  const playbookHashLinks = extractHashLinks(indexText, "/playbooks")

  for (const hashId of playbookHashLinks) {
    if (!playbookAnchors.has(hashId)) {
      fail(`/playbooks#${hashId} 在 playbooks.md 中不存在对应锚点。`)
    }
  }
}

async function main() {
  const skillsData = await readJson(skillsDataPath)

  validateDataSchema(skillsData)
  await checkLocalSkillFiles(skillsData)
  await validateAssociatedAnchorLinks(skillsData)

  if (shouldSkipExternal) {
    warn("已跳过外部链接检查（--skip-external）。")
  } else {
    await checkExternalSkillLinks(skillsData)
  }

  const totalSkills = skillsData.categories.reduce((sum, category) => sum + category.skills.length, 0)
  const localSkills = skillsData.categories
    .flatMap((category) => category.skills)
    .filter((skill) => skill.source === "local").length
  const externalSkills = totalSkills - localSkills

  console.log("=== 技能链接校验报告 ===")
  console.log(`分类：${skillsData.categories.length}`)
  console.log(`技能：${totalSkills}（本地 ${localSkills} / 外部 ${externalSkills}）`)
  console.log(`分支：${skillsData.meta.repoBranch}`)

  if (warnings.length > 0) {
    for (const message of warnings) {
      console.log(`⚠️  ${message}`)
    }
  }

  if (failures.length > 0) {
    for (const message of failures) {
      console.error(`❌ ${message}`)
    }

    process.exit(1)
  }

  console.log("✅ 所有技能卡片链接和关联锚点校验通过。")
}

main().catch((error) => {
  console.error("❌ 校验脚本执行失败：", error)
  process.exit(1)
})
