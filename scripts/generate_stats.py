#!/usr/bin/env python3
"""
文档统计信息生成器

自动统计项目信息并生成统计报告。

用法:
    python generate_stats.py           # 生成统计信息
    python generate_stats.py --update  # 更新 docs/index.md
"""

import json
import re
from pathlib import Path
from typing import Optional


class StatsGenerator:
    """统计信息生成器"""

    def __init__(self, repo_root: Optional[Path] = None):
        self.repo_root = Path(repo_root) if repo_root else Path.cwd()
        self.categories_file = self.repo_root / 'scripts' / 'skill_categories.json'

    def generate_stats(self) -> dict:
        """生成统计信息"""
        stats = {
            'local_skills': 0,
            'external_skills': 0,
            'composio_skills': 0,
            'total_skills': 0,
            'categories': 0,
            'composio_apps': 0
        }

        # 1. 统计本地技能
        local_skills = []
        for item in self.repo_root.iterdir():
            if item.is_dir() and (item / 'SKILL.md').exists():
                if item.name not in {'.git', '.github', 'docs', 'scripts', '.claude', 'composio-skills'}:
                    local_skills.append(item.name)
        
        stats['local_skills'] = len(local_skills)

        # 2. 统计外部技能
        if self.categories_file.exists():
            categories = json.loads(self.categories_file.read_text(encoding='utf-8'))
            external_skills = 0
            for cat_skills in categories.get('external_skills', {}).values():
                external_skills += len(cat_skills)
            stats['external_skills'] = external_skills
            stats['categories'] = len(categories.get('categories', {}))

        # 3. 统计 Composio 技能
        composio_dir = self.repo_root / 'composio-skills'
        if composio_dir.exists():
            composio_skills = []
            for item in composio_dir.iterdir():
                if item.is_dir() and (item / 'SKILL.md').exists():
                    composio_skills.append(item.name)
            stats['composio_skills'] = len(composio_skills)

        # 4. 统计 Composio 应用数(从 README 中提取)
        readme_path = self.repo_root / 'README.md'
        if readme_path.exists():
            content = readme_path.read_text(encoding='utf-8')
            # 匹配 "78 个 SaaS 应用" 或类似文本
            match = re.search(r'(\d+)\s*(?:个)?\s*SaaS\s*应用', content)
            if match:
                stats['composio_apps'] = int(match.group(1))

        # 5. 计算总数
        stats['total_skills'] = (
            stats['local_skills'] + 
            stats['external_skills'] + 
            stats['composio_skills']
        )

        return stats

    def update_docs_index(self, stats: Optional[dict] = None) -> bool:
        """更新 docs/index.md 中的统计信息"""
        if stats is None:
            stats = self.generate_stats()

        docs_index = self.repo_root / 'docs' / 'index.md'
        if not docs_index.exists():
            print("❌ docs/index.md 不存在")
            return False

        content = docs_index.read_text(encoding='utf-8')

        # 构建新的统计信息部分
        stats_md = f"""## 项目统计

- **{stats['local_skills']}+ 本地技能** - 经过验证的高质量技能
- **{stats['external_skills']}+ 外部技能** - 来自社区的优秀技能
- **{stats['composio_skills']}+ Composio 自动化** - 连接 78+ SaaS 应用
- **{stats['categories']} 个分类** - 涵盖开发、设计、营销等各个领域
- **总计 {stats['total_skills']}+ 技能** - 持续增长中

> 📊 这些统计信息由脚本自动生成,确保数据准确性
"""

        # 查找并替换统计信息部分
        pattern = r'## 项目统计.*?(?=\n##|\Z)'
        if re.search(pattern, content, re.DOTALL):
            new_content = re.sub(pattern, stats_md.rstrip('\n'), content, flags=re.DOTALL)
        else:
            # 如果没有找到统计部分,添加到文件开头
            new_content = stats_md + '\n' + content

        # 备份原文件
        backup_path = docs_index.with_suffix('.md.bak')
        backup_path.write_text(content, encoding='utf-8')

        # 写入新内容
        docs_index.write_text(new_content, encoding='utf-8')

        print(f"✅ docs/index.md 已更新")
        print(f"📦 备份保存到: {backup_path}")
        print(f"\n📊 统计信息:")
        print(f"   本地技能: {stats['local_skills']}")
        print(f"   外部技能: {stats['external_skills']}")
        print(f"   Composio 技能: {stats['composio_skills']}")
        print(f"   总计: {stats['total_skills']}")

        return True


def main():
    """命令行入口"""
    import argparse

    parser = argparse.ArgumentParser(description='生成文档统计信息')
    parser.add_argument('--update', action='store_true', help='更新 docs/index.md')

    args = parser.parse_args()

    generator = StatsGenerator()

    if args.update:
        stats = generator.generate_stats()
        generator.update_docs_index(stats)
    else:
        stats = generator.generate_stats()
        print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
