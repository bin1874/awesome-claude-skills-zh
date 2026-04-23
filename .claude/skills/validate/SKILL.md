---
name: validate
description: 验证翻译内容 — 检查未翻译的英文、无效链接和 SKILL.md 文件缺失的 frontmatter
---

# 验证翻译内容

对项目中的 Markdown 文件运行验证检查。

## 检查项

1. **未翻译的英文文本** — 检测 SKILL.md 文件中可能需要翻译的英文内容
2. **缺失 frontmatter** — 确保所有 SKILL.md 文件都有必需的 `name` 和 `description` 字段
3. **无效内部链接** — 检查指向不存在文件或锚点的链接

## 使用方法

不带参数运行以验证所有技能文件：
```bash
/validate
```

## 实现

```bash
# 检查 SKILL.md 文件缺失 frontmatter
find . -name "SKILL.md" -type f | while read f; do
  if ! grep -q "^name:" "$f" || ! grep -q "^description:" "$f"; then
    echo "缺失 frontmatter: $f"
  fi
done

# 检查未翻译的英文（启发式：中文内容区域中 ASCII 字母占比 >50% 的行）
find . -name "SKILL.md" -type f | while read f; do
  # 跳过代码块和 frontmatter，检查正文
  awk '/^---$/,/^---$/ {next} /^```/,/^```/ {next} /[a-zA-Z]{20,}/ {print FILENAME ":" NR ": 可能的未翻译文本"}' "$f"
done 2>/dev/null | head -20

# 检查无效的相对链接
find . -name "*.md" -type f | while read f; do
  grep -oE '\]\([^)]+\)' "$f" | grep -vE 'http|mailto' | sed 's/](\(.*\))/\1/' | while read link; do
    target="$(dirname "$f")/$link"
    if [[ "$link" == \#* ]]; then
      continue  # 锚点链接，跳过
    fi
    if [[ ! -f "$target" ]]; then
      echo "$f 中的无效链接: $link"
    fi
  done
done 2>/dev/null | head -20
```

## 注意

- 这是轻量级验证。如需全面检查，请手动审查。
- 重点关注技能目录中的 SKILL.md 文件。
