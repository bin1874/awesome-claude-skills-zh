---
name: before-you-build
description: 在开始构建产品、功能、SaaS、AI 应用、独立开发项目或创业想法之前，先做一次需求、分发、定价和失败模式的现实检查。
---

# Before You Build

Before You Build 是一个面向 AI 编程助手的预构建审查技能。

它不帮用户更快写代码，而是先帮用户判断：这个产品或功能是否值得现在就做，最可能失败在哪里，开始开发前应该先验证什么。

## 何时使用此技能

- 用户说“我想做一个产品 / SaaS / AI 工具 / 独立开发项目”
- 用户问“这个想法值不值得做”
- 用户想让 AI 直接开始写代码，但需求、用户或场景还很模糊
- 用户准备新增功能，想确认是不是应该开发
- 用户说“竞品都有这个功能，我们是不是也要加”
- 用户说“有个用户提了这个需求，我们要不要做”

## 此技能的功能

1. **阻止过早开工**: 在写代码前先检查目标用户、使用场景和真实需求。
2. **识别失败模式**: 关注薄 AI 包装、弱付费意愿、低频使用、分发困难、信任不足等常见风险。
3. **审查新增功能**: 判断功能需求是重复出现的真实需求，还是单个用户的特殊请求。
4. **给出下一步验证动作**: 输出小而具体的验证步骤，而不是直接进入完整实现。

## 如何使用

### 基本用法

```text
Use before-you-build to review this idea before writing code:

I want to build an AI tool that helps indie hackers validate SaaS ideas.
```

### 功能变更审查

```text
Use before-you-build to review this feature request before implementation:

A user asked us to add team accounts and permissions to our small solo-founder tool.
```

## 示例

**用户**: “我想做一个 AI 工具，输入产品想法后自动生成完整 MVP。”

**输出**:

```text
Quick Reality Check

Biggest risk:
- The user may not need more building speed. They may need sharper idea selection before building.

Most likely failure patterns:
- Thin AI wrapper
- Weak willingness to pay
- Tool without workflow

Validate before building:
1. Find 10 recent examples where indie builders abandoned an AI-generated MVP.
2. Interview 5 builders about what actually stopped their last project.
3. Test whether users want a risk review before code, not another code generator.

Recommendation:
Validate first.
```

## 提示

- 不要把它当成 PRD 生成器。
- 不要让它推荐技术栈或架构。
- 最适合在“准备让 AI 开始写代码”之前使用。
- 如果想法太宽，先用一句话补全：这个工具是为谁、在哪个场景下、解决什么问题。

## 常见用例

- 独立开发者在开工前审查产品想法
- SaaS 团队在新增功能前审查需求
- AI 编程代理在生成代码前先做产品风险检查
- 创业者在写 MVP 前识别最可能失败的假设

**灵感来源:** Before You Build Skill 项目。源码和完整版本见 https://github.com/bin1874/before-you-build-skill
