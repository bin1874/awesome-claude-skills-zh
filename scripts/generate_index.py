#!/usr/bin/env python3
"""
技能索引生成模块

从技能目录自动生成索引 Markdown，避免手动维护导致的不同步问题。

提供接口:
    generate_index() -> str          # 生成 Markdown 索引
    update_readme(dry_run=False)     # 更新 README.md

用法:
    python generate_index.py                 # 生成并打印索引
    python generate_index.py --update        # 更新 README.md
    python generate_index.py --update --dry-run  # 预览更新
"""

import json
import re
import sys
from pathlib import Path
from typing import Optional
import yaml


class SkillIndexGenerator:
    """技能索引生成器"""

    def __init__(self, repo_root: Optional[Path] = None):
        self.repo_root = Path(repo_root) if repo_root else Path.cwd()
        self.categories_file = self.repo_root / 'scripts' / 'skill_categories.json'
        self.categories = self._load_categories()

    def _load_categories(self) -> dict:
        """加载分类配置"""
        if self.categories_file.exists():
            return json.loads(self.categories_file.read_text(encoding='utf-8'))
        return {'categories': {}, 'external_skills': {}}

    def _extract_skill_metadata(self, skill_path: Path) -> Optional[dict]:
        """从 SKILL.md 提取元数据"""
        skill_md = skill_path / 'SKILL.md'
        if not skill_md.exists():
            return None

        content = skill_md.read_text(encoding='utf-8')

        # 解析 frontmatter
        if not content.startswith('---'):
            return None

        parts = content.split('---', 2)
        if len(parts) < 3:
            return None

        try:
            frontmatter = yaml.safe_load(parts[1].strip())
        except yaml.YAMLError:
            return None

        return {
            'name': frontmatter.get('name', skill_path.name),
            'description': frontmatter.get('description', ''),
            'path': f"./{skill_path.name}/"
        }

    def _scan_local_skills(self) -> dict[str, list[dict]]:
        """扫描本地技能并按分类组织"""
        skills_by_category = {cat: [] for cat in self.categories['categories']}

        # 建立技能到分类的映射
        skill_to_category = {}
        for cat, data in self.categories['categories'].items():
            for skill_name in data.get('skills', []):
                skill_to_category[skill_name] = cat

        # 扫描所有技能目录
        for item in self.repo_root.iterdir():
            if item.is_dir() and item.name not in {'.git', '.github', 'docs', 'scripts', '.claude'}:
                skill_md = item / 'SKILL.md'
                if skill_md.exists():
                    metadata = self._extract_skill_metadata(item)
                    if metadata:
                        cat = skill_to_category.get(item.name)
                        if cat:
                            skills_by_category[cat].append(metadata)
                        # 如果没有分类，跳过（可能是不需要展示的技能）

        return skills_by_category

    def generate_index(self) -> str:
        """生成技能列表 Markdown"""
        lines = []

        # 扫描本地技能
        local_skills = self._scan_local_skills()

        # 生成各分类的技能列表
        for category, cat_data in self.categories['categories'].items():
            local = local_skills.get(category, [])
            external = self.categories.get('external_skills', {}).get(category, [])

            if not local and not external:
                continue

            lines.append(f"\n### {category}\n")

            # 本地技能
            for skill in local:
                lines.append(f"- [{skill['name']}]({skill['path']}) — {skill['description']}")

            # 外部技能
            for skill in external:
                author = f" *作者 {skill['author']}*" if 'author' in skill else ""
                lines.append(f"- [{skill['name']}]({skill['url']}) — {skill['description']}{author}")

        return '\n'.join(lines)

    def update_readme(self, dry_run: bool = False) -> bool:
        """更新 README.md 中的技能列表"""
        readme_path = self.repo_root / 'README.md'
        if not readme_path.exists():
            print("错误: README.md 不存在")
            return False

        content = readme_path.read_text(encoding='utf-8')

        # 查找技能列表部分
        # 开始标记: "## 技能列表" 或 "> 精选"
        # 结束标记: "## 入门指南" 或下一个二级标题

        pattern = r'(## 技能列表\s*\n\s*> 精选[^[]+\[[^\]]+\][^\n]*\n)(.*?)(\n## 入门指南)'
        match = re.search(pattern, content, re.DOTALL)

        if not match:
            print("错误: 无法找到技能列表部分")
            return False

        # 生成新索引
        new_index = self.generate_index()

        # 构建新内容
        new_content = (
            match.group(1) +  # 标题和简介
            new_index +
            match.group(3)   # 入门指南标题
        )

        updated = content[:match.start()] + new_content + content[match.end():]

        if dry_run:
            print("=== 更新预览 ===")
            print(new_index)
            print("\n=== 使用 --update 执行实际更新 ===")
            return True

        # 备份原文件
        backup_path = readme_path.with_suffix('.md.bak')
        backup_path.write_text(content, encoding='utf-8')

        # 写入新内容
        readme_path.write_text(updated, encoding='utf-8')

        print(f"✅ README.md 已更新")
        print(f"📦 备份保存到: {backup_path}")

        return True

    def list_local_skills(self) -> list[dict]:
        """列出所有本地技能"""
        skills = []

        for item in self.repo_root.iterdir():
            if item.is_dir() and item.name not in {'.git', '.github', 'docs', 'scripts', '.claude'}:
                metadata = self._extract_skill_metadata(item)
                if metadata:
                    skills.append(metadata)

        return sorted(skills, key=lambda x: x['name'])

    def find_unclassified_skills(self) -> list[str]:
        """找出未分类的本地技能"""
        classified = set()
        for cat_data in self.categories['categories'].values():
            classified.update(cat_data.get('skills', []))

        unclassified = []
        for item in self.repo_root.iterdir():
            if item.is_dir() and item.name not in {'.git', '.github', 'docs', 'scripts', '.claude'}:
                if (item / 'SKILL.md').exists() and item.name not in classified:
                    unclassified.append(item.name)

        return sorted(unclassified)


def main():
    """命令行入口"""
    import argparse

    parser = argparse.ArgumentParser(description='生成技能索引')
    parser.add_argument('--update', action='store_true', help='更新 README.md')
    parser.add_argument('--dry-run', action='store_true', help='预览更新，不实际修改')
    parser.add_argument('--list', action='store_true', help='列出所有本地技能')
    parser.add_argument('--unclassified', action='store_true', help='查找未分类技能')

    args = parser.parse_args()

    generator = SkillIndexGenerator()

    if args.list:
        print("=== 本地技能列表 ===")
        for skill in generator.list_local_skills():
            print(f"  {skill['name']}: {skill['description'][:50]}...")
        return

    if args.unclassified:
        unclassified = generator.find_unclassified_skills()
        if unclassified:
            print("=== 未分类技能 ===")
            for name in unclassified:
                print(f"  {name}")
            print(f"\n请在 scripts/skill_categories.json 中添加这些技能的分类")
        else:
            print("✅ 所有技能都已分类")
        return

    if args.update:
        generator.update_readme(dry_run=args.dry_run)
    else:
        print(generator.generate_index())


if __name__ == '__main__':
    main()
