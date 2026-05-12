---
title: 实战手册
---

# 实战手册

这页不是“文档搬运”，而是给出可直接执行的 Claude Skills 任务路径。  
建议方式：先选一个明确目标，再套用下面的路径模板执行。

## 任务决策矩阵

| 目标 | 推荐技能链路 | 预计输出 | 成功判定 |
|:---|:---|:---|:---|
| 快速产出一篇可发布内容 | `Content Research Writer` → `article-extractor` → `NotebookLM Integration` | 带结构与引用的初稿 | 30 分钟内产出可审阅版本 |
| 提升开发交付速度 | `MCP Builder` → `Webapp Testing` → `test-driven-development` | 可运行功能 + 自动化测试 | 首次提交即通过关键用例 |
| 做市场/竞品分析 | `Competitive Ads Extractor` → `deep-research` → `Lead Research Assistant` | 竞品洞察报告 + 行动清单 | 明确下一步增长实验 |
| 建立自动化执行流 | `Connect` → `Connect Apps` | 可重复执行的跨应用任务 | 至少 1 条任务无需手工重复 |

## 路径一：30 分钟跑通第一条链路 {#path-quick-start}

<div class="playbook-grid">
  <div class="playbook-card">
    <h3>第 1 步：定义“可验收结果”</h3>
    <p>先写一句验收标准，而不是先选技能。例如：“生成一份包含 5 条风险和对应行动建议的竞品分析简报”。</p>
  </div>
  <div class="playbook-card">
    <h3>第 2 步：在技能索引中选 2-3 个技能</h3>
    <p>去 <a href="/skills">技能索引</a> 按关键词筛选，优先选一个“主技能”加一到两个“补位技能”。</p>
  </div>
  <div class="playbook-card">
    <h3>第 3 步：按平台安装并验证</h3>
    <p>在 <a href="/getting-started">入门指南</a> 选择 Claude.ai、Claude Code 或 API 路径，先跑一个最小示例。</p>
  </div>
  <div class="playbook-card">
    <h3>第 4 步：复盘可复用模板</h3>
    <p>记录“输入模板 + 触发条件 + 输出结构”，下次直接复用，不再从零试错。</p>
  </div>
</div>

推荐提示词骨架：

```text
目标：<一句话结果>
上下文：<数据来源/受众/约束>
输出格式：<列表/表格/JSON/报告>
验收标准：<3 条可检查标准>
优先使用技能：<技能 A, 技能 B>
```

## 路径二：搭建个人技能系统 {#path-build-system}

单次成功不代表可持续。建议把技能按角色放入“个人技能栈”：

<div class="resource-grid">
  <div class="resource-card">
    <h3>输入层（采集）</h3>
    <p>例如：`article-extractor`、`youtube-transcript`、`CSV Data Summarizer`。负责拿到干净输入。</p>
  </div>
  <div class="resource-card">
    <h3>处理层（推理）</h3>
    <p>例如：`deep-research`、`root-cause-tracing`、`Developer Growth Analysis`。负责分析和决策。</p>
  </div>
  <div class="resource-card">
    <h3>输出层（交付）</h3>
    <p>例如：`Content Research Writer`、`Canvas Design`、`Tailored Resume Generator`。负责产出可交付成果。</p>
  </div>
  <div class="resource-card">
    <h3>执行层（自动化）</h3>
    <p>例如：`Connect`、`Connect Apps`、`Skill Share`。负责把结果推送到真实系统和团队流程。</p>
  </div>
</div>

每周维护一次“技能栈健康度”：

1. 删除 30 天内从未使用的技能。
2. 给高频技能补一条失败案例和规避方式。
3. 把可复用的提示词模板放进团队共享文档。

## 路径三：团队协作与共享 {#path-team-collab}

团队场景的关键不是“谁会用”，而是“每个人都能稳定复现”。

建议采用以下协作机制：

| 机制 | 做法 | 价值 |
|:---|:---|:---|
| 技能来源统一 | 统一维护技能清单（本仓库 + 白名单外部技能） | 降低不可信来源风险 |
| 版本与链接校验 | 在 CI 中校验技能链接是否有效 | 避免文档可点但实际 404 |
| 贡献流程标准化 | 通过 [贡献指南](/contribute) 统一 PR 要求 | 减少重复沟通成本 |
| 场景模板沉淀 | 每条业务场景至少沉淀 1 份模板 | 新成员可快速接手 |

## 高频场景模板（开箱即用）

### 发布前质量检查（开发团队）

- 目标：上线前发现风险并形成修复顺序。
- 组合：`Webapp Testing` + `test-driven-development` + `review-implementing`。
- 输出：问题清单（严重级、复现步骤、建议修复）。

### 周报自动草稿（运营团队）

- 目标：把分散数据快速汇总为可读周报。
- 组合：`Connect Apps` + `Content Research Writer` + `Canvas Design`。
- 输出：一页摘要 + 详细版本。

### 竞品策略快报（增长团队）

- 目标：每周稳定输出竞争动态和动作建议。
- 组合：`Competitive Ads Extractor` + `deep-research` + `Lead Research Assistant`。
- 输出：3 条机会点、3 条风险、下周实验计划。

## 继续深入

- 想先解决安装和平台差异：看 [入门指南](/getting-started)
- 想直接筛技能并查看链接：看 [技能索引](/skills)
- 想扩展更多官方与社区资源：看 [资源导航](/resources)
