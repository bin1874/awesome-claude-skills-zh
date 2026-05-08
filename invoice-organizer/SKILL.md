---
name: invoice-organizer
description: 通过读取混乱文件、提取关键信息、一致重命名并将其分类到逻辑文件夹中，自动为税务准备组织发票和收据。将数小时的手动记账转化为几分钟的自动化组织。
---

# 发票整理器

此技能将混乱的发票、收据和财务文档文件夹转化为干净、税务就绪的归档系统，无需手动努力。

## 何时使用此技能

- 为税务季准备，需要有序记录
- 管理多个供应商的业务费用
- 从混乱文件夹或邮件下载组织收据
- 为持续记账设置自动发票归档
- 按年份或类别归档财务记录
- 为报销核对费用
- 为会计师准备文档

## 此技能的功能

1. **读取发票内容**：从 PDF、图像和文档中提取信息：
   - 供应商/公司名称
   - 发票编号
   - 日期
   - 金额
   - 产品或服务描述
   - 付款方式

2. **一致重命名文件**：创建标准化文件名：
   - 格式：`YYYY-MM-DD 供应商 - 发票 - 产品或服务.pdf`
   - 示例：`2024-03-15 Adobe - Invoice - Creative Cloud.pdf`

3. **按类别组织**：分类到逻辑文件夹：
   - 按供应商
   - 按费用类别（软件、办公、差旅等）
   - 按时间段（年、季度、月）
   - 按税务类别（可抵扣、个人等）

4. **处理多种格式**：适用于：
   - PDF 发票
   - 扫描收据（JPG、PNG）
   - 邮件附件
   - 截图
   - 银行对账单

5. **保留原件**：组织副本时保留原始文件

## 如何使用

### 基本用法

导航到你混乱的发票文件夹：
```
cd ~/Desktop/receipts-to-sort
```

然后让 Claude Code：
```
为税务整理这些发票
```

或更具体地：
```
读取此文件夹中的所有发票，将其重命名为
"YYYY-MM-DD 供应商 - 发票 - 产品.pdf" 格式，
并按供应商组织
```

### 高级组织

```
整理这些发票：
1. 从每个文件提取日期、供应商和描述
2. 重命名为标准格式
3. 按费用类别分类到文件夹（软件、办公、差旅等）
4. 为我的会计师创建包含所有发票详情的 CSV 电子表格
```

## 说明

当用户请求发票组织时：

1. **扫描文件夹**

   识别所有发票文件：
   ```bash
   # 查找所有发票相关文件
   find . -type f \( -name "*.pdf" -o -name "*.jpg" -o -name "*.png" \) -print
   ```

   报告发现：
   - 文件总数
   - 文件类型
   - 日期范围（如可从名称辨识）
   - 当前组织状态（或缺乏组织）

2. **从每个文件提取信息**

   对于每张发票，提取：

   **从 PDF 发票**：
   - 使用文本提取读取发票内容
   - 查找常见模式：
     - "Invoice Date:"、"Date:"、"Issued:"
     - "Invoice #:"、"Invoice Number:"
     - 公司名称（通常在顶部）
     - "Amount Due:"、"Total:"、"Amount:"
     - "Description:"、"Service:"、"Product:"

   **从图像收据**：
   - 读取可见文本
   - 识别供应商名称（通常在顶部）
   - 查找日期（常见格式）
   - 查找总金额

   **不清楚文件的回退方案**：
   - 使用文件名线索
   - 检查文件创建/修改日期
   - 如关键信息缺失，标记为人工审查

3. **确定组织策略**

   如未指定，询问用户偏好：

   ```markdown
   我找到了 [X] 张日期范围从 [日期范围] 的发票。

   你希望如何组织？

   1. **按供应商**（Adobe/、Amazon/、Stripe/ 等）
   2. **按类别**（Software/、Office Supplies/、Travel/ 等）
   3. **按日期**（2024/Q1/、2024/Q2/ 等）
   4. **按税务类别**（Deductible/、Personal/ 等）
   5. **自定义**（描述你的结构）

   或者我可以使用默认结构：年份/类别/供应商
   ```

4. **创建标准化文件名**

   对于每张发票，按照此模式创建文件名：

   ```
   YYYY-MM-DD 供应商 - 发票 - 描述.ext
   ```

   示例：
   - `2024-03-15 Adobe - Invoice - Creative Cloud.pdf`
   - `2024-01-10 Amazon - Receipt - Office Supplies.pdf`
   - `2023-12-01 Stripe - Invoice - Monthly Payment Processing.pdf`

   **文件名最佳实践**：
   - 移除除连字符外的特殊字符
   - 正确大写供应商名称
   - 保持描述简洁但有意义
   - 使用一致的日期格式（YYYY-MM-DD）以便排序
   - 保留原始文件扩展名

5. **执行组织**

   在移动文件前，展示计划：

   ```markdown
   # 组织计划

   ## 提议的结构
   ```
   Invoices/
   ├── 2023/
   │   ├── Software/
   │   │   ├── Adobe/
   │   │   └── Microsoft/
   │   ├── Services/
   │   └── Office/
   └── 2024/
       ├── Software/
       ├── Services/
       └── Office/
   ```

   ## 示例更改

   之前：`invoice_adobe_march.pdf`
   之后：`2024-03-15 Adobe - Invoice - Creative Cloud.pdf`
   位置：`Invoices/2024/Software/Adobe/`

   之前：`IMG_2847.jpg`
   之后：`2024-02-10 Staples - Receipt - Office Supplies.jpg`
   位置：`Invoices/2024/Office/Staples/`

   处理 [X] 个文件？（是/否）
   ```

   批准后：
   ```bash
   # 创建文件夹结构
   mkdir -p "Invoices/2024/Software/Adobe"

   # 复制（而非移动）以保留原件
   cp "original.pdf" "Invoices/2024/Software/Adobe/2024-03-15 Adobe - Invoice - Creative Cloud.pdf"

   # 或如果用户偏好则移动
   mv "original.pdf" "new/path/standardized-name.pdf"
   ```

6. **生成摘要报告**

   创建包含所有发票详情的 CSV 文件：

   ```csv
   Date,Vendor,Invoice Number,Description,Amount,Category,File Path
   2024-03-15,Adobe,INV-12345,Creative Cloud,52.99,Software,Invoices/2024/Software/Adobe/2024-03-15 Adobe - Invoice - Creative Cloud.pdf
   2024-03-10,Amazon,123-4567890-1234567,Office Supplies,127.45,Office,Invoices/2024/Office/Amazon/2024-03-10 Amazon - Receipt - Office Supplies.pdf
   ...
   ```

   此 CSV 用于：
   - 导入会计软件
   - 与会计师分享
   - 费用跟踪和报告
   - 税务准备

7. **提供完成摘要**

   ```markdown
   # 组织完成！📊

   ## 摘要
   - **已处理**：[X] 张发票
   - **日期范围**：[最早] 到 [最晚]
   - **总金额**：$[总和]（如提取了金额）
   - **供应商**：[Y] 个唯一供应商

   ## 新结构
   ```
   Invoices/
   ├── 2024/ (45 个文件)
   │   ├── Software/ (23 个文件)
   │   ├── Services/ (12 个文件)
   │   └── Office/ (10 个文件)
   └── 2023/ (12 个文件)
   ```

   ## 创建的文件
   - `/Invoices/` - 已组织的发票
   - `/Invoices/invoice-summary.csv` - 会计用电子表格
   - `/Invoices/originals/` - 原始文件（如已复制）

   ## 需要审查的文件
   [列出无法完全提取信息的文件]

   ## 下一步
   1. 审查 `invoice-summary.csv` 文件
   2. 检查"需审查"文件夹中的文件
   3. 将 CSV 导入你的会计软件
   4. 为未来发票设置自动组织

   税务季准备就绪！🎉
   ```

## 示例

### 示例 1：税务准备（来自 Martin Merschroth）

**用户**："我有一个混乱的发票文件夹要报税。整理并正确重命名。"

**过程**：
1. 扫描文件夹：找到 147 个 PDF 和图像
2. 读取每张发票以提取：
   - 日期
   - 供应商名称
   - 发票编号
   - 产品/服务描述
3. 重命名所有文件：`YYYY-MM-DD 供应商 - 发票 - 产品.pdf`
4. 组织到：`2024/Software/`、`2024/Travel/` 等
5. 为会计师创建 `invoice-summary.csv`
6. 结果：几分钟内完成税务就绪的已组织发票

### 示例 2：月度费用核对

**用户**："按类别组织上个月的业务收据。"

**输出**：
```markdown
# 2024 年 3 月收据已整理

## 按类别
- 软件和工具：$847.32（12 张发票）
- 办公用品：$234.18（8 张收据）
- 差旅和餐饮：$1,456.90（15 张收据）
- 专业服务：$2,500.00（3 张发票）

总计：$5,038.40

所有收据已重命名并归档在：
`Business-Receipts/2024/03-March/[类别]/`

CSV 导出：`march-2024-expenses.csv`
```

### 示例 3：多年归档

**用户**："我有 3 年的随机发票。按年份然后按供应商组织。"

**输出**：创建结构：
```
Invoices/
├── 2022/
│   ├── Adobe/
│   ├── Amazon/
│   └── ...
├── 2023/
│   ├── Adobe/
│   ├── Amazon/
│   └── ...
└── 2024/
    ├── Adobe/
    ├── Amazon/
    └── ...
```

每个文件都用日期和描述正确重命名。

### 示例 4：邮件下载清理

**用户**："我从 Gmail 下载发票。它们都叫 'invoice.pdf'、'invoice(1).pdf' 等。整理这个烂摊子。"

**输出**：
```markdown
发现 89 个都名为 "invoice*.pdf" 的文件

读取每个文件以提取真实信息...

重命名示例：
- invoice.pdf → 2024-03-15 Shopify - Invoice - Monthly Subscription.pdf
- invoice(1).pdf → 2024-03-14 Google - Invoice - Workspace.pdf
- invoice(2).pdf → 2024-03-10 Netlify - Invoice - Pro Plan.pdf

所有文件已重命名并按供应商组织。
```

## 常见组织模式

### 按供应商（简单）
```
Invoices/
├── Adobe/
├── Amazon/
├── Google/
└── Microsoft/
```

### 按年份和类别（税务友好）
```
Invoices/
├── 2023/
│   ├── Software/
│   ├── Hardware/
│   ├── Services/
│   └── Travel/
└── 2024/
    └── ...
```

### 按季度（详细跟踪）
```
Invoices/
├── 2024/
│   ├── Q1/
│   │   ├── Software/
│   │   ├── Office/
│   │   └── Travel/
│   └── Q2/
│       └── ...
```

### 按税务类别（会计师就绪）
```
Invoices/
├── Deductible/
│   ├── Software/
│   ├── Office/
│   └── Professional-Services/
├── Partially-Deductible/
│   └── Meals-Travel/
└── Personal/
```

## 自动化设置

用于持续组织：

```
创建一个脚本，监视我的 ~/Downloads/invoices 文件夹
并使用我们的标准命名和文件夹结构
自动组织任何新发票文件。
```

这创建了一个在发票到达时组织的持久解决方案。

## 专业提示

1. **扫描邮件为 PDF**：首先使用预览或类似工具将邮件发票保存为 PDF
2. **一致下载**：将所有发票保存到一个文件夹以便批处理
3. **每月例行**：每月组织发票，而非每年
4. **备份原件**：重新组织前保留原始文件
5. **在 CSV 中包含金额**：用于预算跟踪
6. **标记可抵扣性**：注明哪些费用可抵税
7. **保留收据 7 年**：标准审计期

## 处理特殊情况

### 信息缺失
如果无法提取日期/供应商：
- 标记文件为人工审查
- 使用文件修改日期作为回退
- 创建"Needs-Review/"文件夹

### 重复发票
如果同一发票出现多次：
- 比较文件哈希
- 保留最高质量版本
- 在摘要中注明重复项

### 多页发票
对于跨文件分割的发票：
- 如需要合并 PDF
- 为部分使用一致命名
- 如发票已分割，在 CSV 中注明

### 非标准格式
对于异常收据格式：
- 提取可能的内容
- 标准化你能做到的
- 如关键信息缺失，标记为审查

## 相关用例

- 为报销创建费用报告
- 组织银行对账单
- 管理供应商合同
- 归档旧财务记录
- 准备审计
- 跟踪订阅成本随时间变化
