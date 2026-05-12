#!/usr/bin/env python3
"""
文档同步验证模块

检测文档之间的重复内容、版本一致性、引用完整性问题。

提供接口:
    check_sync() -> SyncReport       # 检查同步状态
    find_duplicates() -> list        # 查找重复内容

用法:
    python check_docs_sync.py              # 检查同步状态
    python check_docs_sync.py --duplicates # 查找重复内容
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
from difflib import SequenceMatcher


@dataclass
class SyncIssue:
    """同步问题"""
    issue_type: str  # 'duplicate', 'outdated', 'missing_ref', 'inconsistent'
    severity: str    # 'error', 'warning', 'info'
    message: str
    locations: list[str] = field(default_factory=list)
    suggestion: Optional[str] = None


@dataclass
class SyncReport:
    """同步检查报告"""
    valid: bool
    issues: list[SyncIssue] = field(default_factory=list)

    def add_issue(self, issue: SyncIssue):
        self.issues.append(issue)
        if issue.severity == 'error':
            self.valid = False


class DocSyncChecker:
    """文档同步检查器"""

    # 需要检查的主要文档
    MAIN_DOCS = ['README.md', 'AGENTS.md', 'CONTRIBUTING.md']

    # docs 目录下的文档
    DOCS_DIR = 'docs'

    # 技能目录
    SKILLS_DIRS = []  # 动态检测

    def __init__(self, repo_root: Optional[Path] = None):
        self.repo_root = Path(repo_root) if repo_root else Path.cwd()
        self.docs_dir = self.repo_root / self.DOCS_DIR

    def check_sync(self) -> SyncReport:
        """执行完整同步检查"""
        report = SyncReport(valid=True)

        # 1. 检查 README.md 与 docs/skills.md 的同步
        self._check_readme_skills_sync(report)

        # 2. 检查技能列表与实际目录的一致性
        self._check_skill_dirs_consistency(report)

        # 3. 检查 AGENTS.md 与实际结构的一致性
        self._check_agents_consistency(report)

        # 4. 检查文档链接有效性
        self._check_doc_links(report)

        return report

    def find_duplicates(self) -> list[SyncIssue]:
        """查找文档间的重复内容"""
        issues = []

        # 收集所有文档内容
        docs_content = {}
        for doc_file in self._get_all_docs():
            if doc_file.exists():
                docs_content[str(doc_file.relative_to(self.repo_root))] = doc_file.read_text(encoding='utf-8')

        # 检查重复的段落
        issues.extend(self._find_duplicate_sections(docs_content))

        # 检查重复的技能描述
        issues.extend(self._find_duplicate_skill_descriptions(docs_content))

        return issues

    def _get_all_docs(self) -> list[Path]:
        """获取所有需要检查的文档"""
        docs = []

        # 主要文档
        for doc_name in self.MAIN_DOCS:
            docs.append(self.repo_root / doc_name)

        # docs 目录下的文档
        if self.docs_dir.exists():
            for doc_file in self.docs_dir.glob('**/*.md'):
                docs.append(doc_file)

        return docs

    def _check_readme_skills_sync(self, report: SyncReport):
        """检查 README.md 与 docs/skills.md 的同步"""
        readme_path = self.repo_root / 'README.md'
        skills_path = self.docs_dir / 'skills.md'

        if not readme_path.exists():
            report.add_issue(SyncIssue(
                issue_type='missing',
                severity='error',
                message='README.md 不存在',
                locations=['README.md']
            ))
            return

        if not skills_path.exists():
            report.add_issue(SyncIssue(
                issue_type='missing',
                severity='warning',
                message='docs/skills.md 不存在',
                locations=['docs/skills.md'],
                suggestion='考虑创建 docs/skills.md 作为技能列表的独立页面'
            ))
            return

        # 比较技能列表（使用专门的提取方法）
        readme_skills = self._extract_skills_from_readme(readme_path.read_text(encoding='utf-8'))
        skills_md_skills = self._extract_skills_from_skills_md(skills_path.read_text(encoding='utf-8'))

        # 检查 README 中有但 skills.md 中没有的技能
        missing_in_skills = readme_skills - skills_md_skills
        if missing_in_skills:
            report.add_issue(SyncIssue(
                issue_type='outdated',
                severity='warning',
                message=f'docs/skills.md 缺少以下技能: {", ".join(missing_in_skills)}',
                locations=['docs/skills.md'],
                suggestion='运行 python scripts/generate_index.py --update 同步技能列表'
            ))

        # 检查 skills.md 中有但 README 中没有的技能
        missing_in_readme = skills_md_skills - readme_skills
        if missing_in_readme:
            report.add_issue(SyncIssue(
                issue_type='outdated',
                severity='warning',
                message=f'README.md 缺少以下技能: {", ".join(missing_in_readme)}',
                locations=['README.md'],
                suggestion='运行 python scripts/generate_index.py --update 同步技能列表'
            ))

    def _check_skill_dirs_consistency(self, report: SyncReport):
        """检查技能列表与实际目录的一致性"""
        readme_path = self.repo_root / 'README.md'

        if not readme_path.exists():
            return

        readme_content = readme_path.read_text(encoding='utf-8')

        # 获取本地技能目录
        local_skills = set()
        for item in self.repo_root.iterdir():
            if item.is_dir() and (item / 'SKILL.md').exists():
                if item.name not in {'.git', '.github', 'docs', 'scripts', '.claude'}:
                    local_skills.add(item.name)

        # 获取 README 中引用的本地技能
        readme_local_skills = set()
        for match in re.finditer(r'\]\(\./([a-z0-9-]+)/\)', readme_content):
            readme_local_skills.add(match.group(1))

        # 检查目录中存在但 README 中没有的技能
        missing_in_readme = local_skills - readme_local_skills
        if missing_in_readme:
            report.add_issue(SyncIssue(
                issue_type='missing_ref',
                severity='info',
                message=f'以下本地技能未在 README.md 中列出: {", ".join(missing_in_readme)}',
                locations=['README.md'],
                suggestion='这些技能可能是模板或不需展示的技能，或需要添加到分类配置'
            ))

    def _check_agents_consistency(self, report: SyncReport):
        """检查 AGENTS.md 与实际结构的一致性"""
        agents_path = self.repo_root / 'AGENTS.md'

        if not agents_path.exists():
            return

        agents_content = agents_path.read_text(encoding='utf-8')

        # 检查是否提到 CONTEXT.md
        if 'CONTEXT.md' in agents_content:
            context_path = self.repo_root / 'CONTEXT.md'
            if not context_path.exists():
                report.add_issue(SyncIssue(
                    issue_type='missing_ref',
                    severity='warning',
                    message='AGENTS.md 引用了 CONTEXT.md 但文件不存在',
                    locations=['AGENTS.md', 'CONTEXT.md'],
                    suggestion='创建 CONTEXT.md 或更新 AGENTS.md 移除引用'
                ))

        # 检查是否提到 docs/adr/
        if 'docs/adr/' in agents_content or 'ADR' in agents_content:
            adr_dir = self.docs_dir / 'adr'
            if not adr_dir.exists():
                report.add_issue(SyncIssue(
                    issue_type='missing_ref',
                    severity='warning',
                    message='AGENTS.md 引用了 docs/adr/ 但目录不存在',
                    locations=['AGENTS.md', 'docs/adr/'],
                    suggestion='创建 docs/adr/ 目录或更新 AGENTS.md 移除引用'
                ))

    def _check_doc_links(self, report: SyncReport):
        """检查文档中的链接有效性"""
        for doc_path in self._get_all_docs():
            if not doc_path.exists():
                continue

            content = doc_path.read_text(encoding='utf-8')

            # 检查本地文件链接
            for match in re.finditer(r'\]\(([^)]+)\)', content):
                link = match.group(1)

                # 跳过外部链接和锚点
                if link.startswith('http') or link.startswith('#'):
                    continue

                # 检查相对路径链接
                if link.startswith('./') or link.startswith('../'):
                    target = doc_path.parent / link
                else:
                    target = doc_path.parent / link

                if not target.exists():
                    report.add_issue(SyncIssue(
                        issue_type='missing_ref',
                        severity='warning',
                        message=f'链接指向不存在的文件: {link}',
                        locations=[str(doc_path.relative_to(self.repo_root))]
                    ))

    def _extract_skill_names(self, content: str) -> set[str]:
        """从内容中提取技能名称（通用方法，已弃用，保留向后兼容）

        注意: 此方法已弃用，请使用 _extract_skills_from_readme 或 _extract_skills_from_skills_md
        """
        # 同时使用两种方法提取
        readme_skills = self._extract_skills_from_readme(content)
        skills_md_skills = self._extract_skills_from_skills_md(content)
        return readme_skills | skills_md_skills

    def _extract_skills_from_readme(self, content: str) -> set[str]:
        """从 README.md 提取技能名称

        README.md 格式:
        - 技能列表在 '## 技能列表' 和 '## 入门指南' 之间
        - 本地技能: [Name](./name/)
        - 外部技能: [Name](https://...)
        - 作者标记: [@username](...) 需要过滤
        """
        skills = set()

        # 提取技能列表区域
        match = re.search(r'## 技能列表.*?(?=## 入门指南)', content, re.DOTALL)
        if not match:
            return skills

        skill_section = match.group(0)

        # 提取技能链接
        # 1. 本地技能: ./skill-name/
        for match in re.finditer(r'\[([^\]]+)\]\(\./([^/]+)/\)', skill_section):
            name = match.group(1)
            # 过滤作者标记
            if not name.startswith('@'):
                skills.add(name.lower())

        # 2. 外部技能: https://...
        for match in re.finditer(r'\[([^\]]+)\]\(https://[^)]+\)', skill_section):
            name = match.group(1)
            # 过滤作者标记
            if not name.startswith('@'):
                skills.add(name.lower())

        return skills

    def _extract_skills_from_skills_md(self, content: str) -> set[str]:
        """从 docs/skills.md 提取技能名称

        docs/skills.md 格式:
        - HTML 技能卡片: <a class="skill-name">Name</a>
        """
        skills = set()

        # 匹配 HTML skill-name 类中的技能名称
        # 支持 class="skill-name" 或 class="xxx skill-name yyy"
        html_pattern = r'<a[^>]*class="[^"]*skill-name[^"]*"[^>]*>([^<]+)</a>'
        for match in re.finditer(html_pattern, content):
            skill_name = match.group(1).strip()
            if len(skill_name) > 2:
                skills.add(skill_name.lower())

        return skills

    def _find_duplicate_sections(self, docs_content: dict[str, str]) -> list[SyncIssue]:
        """查找重复的段落"""
        issues = []

        # 定义要检查的关键段落
        key_sections = [
            ('技能结构', r'```\nskill-name/.*?```'),
            ('SKILL.md 模板', r'```markdown\n---\nname:.*?```'),
            ('使用方法', r'## 使用方法.*?(?=\n##|$)'),
        ]

        for section_name, pattern in key_sections:
            matches = {}
            for doc_path, content in docs_content.items():
                for match in re.finditer(pattern, content, re.DOTALL):
                    text = match.group(0)
                    if len(text) > 50:  # 忽略太短的匹配
                        matches[doc_path] = text[:100] + '...'

            if len(matches) > 1:
                issues.append(SyncIssue(
                    issue_type='duplicate',
                    severity='info',
                    message=f'发现重复的 "{section_name}" 部分',
                    locations=list(matches.keys()),
                    suggestion='考虑将此内容提取到单一来源，其他地方引用'
                ))

        return issues

    def _find_duplicate_skill_descriptions(self, docs_content: dict[str, str]) -> list[SyncIssue]:
        """查找重复的技能描述"""
        issues = []

        # 从各文档中提取技能描述
        skill_descriptions = {}
        for doc_path, content in docs_content.items():
            for match in re.finditer(r'\[([a-z0-9-]+)\]\([^)]*\)\s*[—-]\s*([^\n]+)', content):
                skill_name = match.group(1)
                description = match.group(2).strip()
                if skill_name not in skill_descriptions:
                    skill_descriptions[skill_name] = []
                skill_descriptions[skill_name].append((doc_path, description))

        # 检查描述不一致
        for skill_name, descs in skill_descriptions.items():
            if len(descs) > 1:
                # 比较描述是否相似
                unique_descs = set(d[1] for d in descs)
                if len(unique_descs) > 1:
                    issues.append(SyncIssue(
                        issue_type='inconsistent',
                        severity='info',
                        message=f'技能 "{skill_name}" 在不同文档中的描述不一致',
                        locations=[d[0] for d in descs],
                        suggestion='统一技能描述以确保一致性'
                    ))

        return issues


def print_report(report: SyncReport):
    """打印同步检查报告"""
    print("\n=== 文档同步检查报告 ===\n")

    if not report.issues:
        print("✅ 所有文档同步状态良好")
        return

    # 按严重程度分组
    errors = [i for i in report.issues if i.severity == 'error']
    warnings = [i for i in report.issues if i.severity == 'warning']
    infos = [i for i in report.issues if i.severity == 'info']

    if errors:
        print(f"❌ 错误 ({len(errors)}):")
        for issue in errors:
            print(f"   - {issue.message}")
            if issue.locations:
                print(f"     位置: {', '.join(issue.locations)}")
            if issue.suggestion:
                print(f"     建议: {issue.suggestion}")

    if warnings:
        print(f"\n⚠️  警告 ({len(warnings)}):")
        for issue in warnings:
            print(f"   - {issue.message}")
            if issue.locations:
                print(f"     位置: {', '.join(issue.locations)}")
            if issue.suggestion:
                print(f"     建议: {issue.suggestion}")

    if infos:
        print(f"\nℹ️  信息 ({len(infos)}):")
        for issue in infos:
            print(f"   - {issue.message}")
            if issue.suggestion:
                print(f"     建议: {issue.suggestion}")

    print(f"\n{'='*40}")
    print(f"总计: {len(report.issues)} 个问题")
    print(f"状态: {'❌ 需要修复' if not report.valid else '✅ 可接受'}")


def main():
    """命令行入口"""
    import argparse

    parser = argparse.ArgumentParser(description='检查文档同步状态')
    parser.add_argument('--duplicates', action='store_true', help='查找重复内容')
    parser.add_argument('--json', action='store_true', help='输出 JSON 格式')

    args = parser.parse_args()

    checker = DocSyncChecker()

    if args.duplicates:
        issues = checker.find_duplicates()

        if args.json:
            import json
            output = [{
                'type': i.issue_type,
                'severity': i.severity,
                'message': i.message,
                'locations': i.locations,
                'suggestion': i.suggestion
            } for i in issues]
            print(json.dumps(output, ensure_ascii=False, indent=2))
        else:
            print("\n=== 重复内容检测 ===\n")
            if issues:
                for issue in issues:
                    print(f"📌 {issue.message}")
                    print(f"   位置: {', '.join(issue.locations)}")
                    if issue.suggestion:
                        print(f"   建议: {issue.suggestion}")
                    print()
            else:
                print("✅ 未发现重复内容")

        return

    report = checker.check_sync()

    if args.json:
        import json
        output = {
            'valid': report.valid,
            'issues': [{
                'type': i.issue_type,
                'severity': i.severity,
                'message': i.message,
                'locations': i.locations,
                'suggestion': i.suggestion
            } for i in report.issues]
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        print_report(report)

    sys.exit(0 if report.valid else 1)


if __name__ == '__main__':
    main()
