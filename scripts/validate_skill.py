#!/usr/bin/env python3
"""
技能验证模块

提供单个接口 validate(skill_path) -> ValidationResult
隐藏所有验证逻辑：frontmatter 解析、目录结构检查、交叉引用验证等。

用法:
    python validate_skill.py <skill_path>
    python validate_skill.py --all  # 验证所有技能
"""

import os
import re
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
import yaml


@dataclass
class ValidationError:
    """验证错误"""
    level: str  # 'error' 或 'warning'
    message: str
    file: Optional[str] = None
    line: Optional[int] = None


@dataclass
class ValidationResult:
    """验证结果"""
    skill_name: str
    valid: bool
    errors: list[ValidationError] = field(default_factory=list)
    warnings: list[ValidationError] = field(default_factory=list)

    def add_error(self, message: str, file: Optional[str] = None, line: Optional[int] = None):
        self.errors.append(ValidationError('error', message, file, line))
        self.valid = False

    def add_warning(self, message: str, file: Optional[str] = None, line: Optional[int] = None):
        self.warnings.append(ValidationError('warning', message, file, line))


class SkillValidator:
    """技能验证器"""

    # 目录命名规范：小写字母、数字、连字符
    DIR_NAME_PATTERN = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')

    # 可选资源目录
    OPTIONAL_DIRS = {'scripts', 'references', 'assets', 'examples'}

    def __init__(self, repo_root: Optional[Path] = None):
        self.repo_root = repo_root or Path.cwd()

    def validate(self, skill_path: Path) -> ValidationResult:
        """
        验证单个技能

        Args:
            skill_path: 技能目录路径

        Returns:
            ValidationResult: 验证结果
        """
        skill_path = Path(skill_path).resolve()
        result = ValidationResult(skill_name=skill_path.name, valid=True)

        # 1. 目录存在性检查
        if not skill_path.exists():
            result.add_error(f"技能目录不存在: {skill_path}")
            return result

        if not skill_path.is_dir():
            result.add_error(f"路径不是目录: {skill_path}")
            return result

        # 2. 目录命名规范检查
        self._validate_dir_name(skill_path, result)

        # 3. SKILL.md 存在性检查
        skill_md_path = skill_path / 'SKILL.md'
        if not skill_md_path.exists():
            result.add_error("缺少必需文件: SKILL.md", str(skill_md_path))
            return result

        # 4. SKILL.md 内容检查
        self._validate_skill_md(skill_md_path, result)

        # 5. 目录结构检查
        self._validate_structure(skill_path, result)

        return result

    def _validate_dir_name(self, skill_path: Path, result: ValidationResult):
        """验证目录命名规范"""
        dir_name = skill_path.name

        if not self.DIR_NAME_PATTERN.match(dir_name):
            result.add_error(
                f"目录名 '{dir_name}' 不符合命名规范。应使用小写字母、数字和连字符",
                str(skill_path)
            )

    def _validate_skill_md(self, skill_md_path: Path, result: ValidationResult):
        """验证 SKILL.md 文件"""
        content = skill_md_path.read_text(encoding='utf-8')

        # 检查 frontmatter 存在性
        if not content.startswith('---'):
            result.add_error(
                "SKILL.md 缺少 YAML frontmatter（应以 '---' 开头）",
                str(skill_md_path),
                1
            )
            return

        # 解析 frontmatter
        try:
            # 提取 frontmatter 部分
            parts = content.split('---', 2)
            if len(parts) < 3:
                result.add_error(
                    "SKILL.md frontmatter 格式错误（缺少结束的 '---'）",
                    str(skill_md_path),
                    1
                )
                return

            frontmatter_text = parts[1].strip()
            frontmatter = yaml.safe_load(frontmatter_text)

            if frontmatter is None:
                result.add_error("frontmatter 为空", str(skill_md_path), 1)
                return

        except yaml.YAMLError as e:
            result.add_error(f"frontmatter YAML 解析错误: {e}", str(skill_md_path), 1)
            return

        # 检查必需字段
        if 'name' not in frontmatter:
            result.add_error("frontmatter 缺少必需字段 'name'", str(skill_md_path), 1)
        else:
            # name 字段与目录名一致性检查
            skill_dir = skill_md_path.parent.name
            if frontmatter['name'] != skill_dir:
                result.add_warning(
                    f"frontmatter 'name' ({frontmatter['name']}) 与目录名 ({skill_dir}) 不一致",
                    str(skill_md_path),
                    1
                )

        if 'description' not in frontmatter:
            result.add_error("frontmatter 缺少必需字段 'description'", str(skill_md_path), 1)
        else:
            # description 质量检查
            desc = frontmatter['description']
            if len(desc) < 20:
                result.add_warning(
                    f"description 过短 ({len(desc)} 字符)，建议至少 20 字符以清晰描述技能用途",
                    str(skill_md_path),
                    1
                )

        # 检查 Markdown 主体内容
        markdown_content = parts[2].strip()
        if len(markdown_content) < 50:
            result.add_warning(
                f"Markdown 内容过短 ({len(markdown_content)} 字符)，建议添加更详细的技能说明",
                str(skill_md_path)
            )

        # 检查是否存在"何时使用"部分
        if '何时使用' not in markdown_content and '## 何时使用' not in markdown_content.lower():
            result.add_warning(
                "建议添加 '## 何时使用此技能' 部分说明技能使用场景",
                str(skill_md_path)
            )

    def _validate_structure(self, skill_path: Path, result: ValidationResult):
        """验证目录结构"""
        # 检查可选目录
        for item in skill_path.iterdir():
            if item.is_dir() and item.name not in self.OPTIONAL_DIRS:
                result.add_warning(
                    f"未知目录 '{item.name}'。可选目录: {', '.join(self.OPTIONAL_DIRS)}",
                    str(item)
                )

        # 检查 SKILL.md 中引用的文件是否存在
        skill_md_path = skill_path / 'SKILL.md'
        if skill_md_path.exists():
            content = skill_md_path.read_text(encoding='utf-8')
            self._validate_referenced_files(skill_path, content, result)

    def _validate_referenced_files(self, skill_path: Path, content: str, result: ValidationResult):
        """验证 SKILL.md 中引用的文件是否存在"""
        # 检查脚本引用
        script_pattern = re.compile(r'`scripts/([^`]+)`|scripts/([^\s`]+)')
        for match in script_pattern.finditer(content):
            script_name = match.group(1) or match.group(2)
            script_path = skill_path / 'scripts' / script_name
            if not script_path.exists():
                result.add_warning(
                    f"引用的脚本文件不存在: scripts/{script_name}",
                    str(skill_md_path := skill_path / 'SKILL.md')
                )

        # 检查参考资料引用
        ref_pattern = re.compile(r'`references/([^`]+)`|references/([^\s`]+)')
        for match in ref_pattern.finditer(content):
            ref_name = match.group(1) or match.group(2)
            ref_path = skill_path / 'references' / ref_name
            if not ref_path.exists():
                result.add_warning(
                    f"引用的参考资料不存在: references/{ref_name}",
                    str(skill_path / 'SKILL.md')
                )

    def validate_all(self) -> list[ValidationResult]:
        """验证所有技能"""
        results = []

        for item in self.repo_root.iterdir():
            if item.is_dir() and item.name not in {'.git', '.github', 'docs', 'scripts', '.claude'}:
                skill_md = item / 'SKILL.md'
                if skill_md.exists():
                    results.append(self.validate(item))

        return results


def print_result(result: ValidationResult):
    """打印验证结果"""
    status = "✅ 通过" if result.valid else "❌ 失败"
    print(f"\n{status} {result.skill_name}")

    for error in result.errors:
        loc = f" ({error.file}:{error.line})" if error.file else ""
        print(f"  ❌ {error.message}{loc}")

    for warning in result.warnings:
        loc = f" ({warning.file}:{warning.line})" if warning.file else ""
        print(f"  ⚠️  {warning.message}{loc}")


def main():
    """命令行入口"""
    import argparse

    parser = argparse.ArgumentParser(description='验证 Claude Skills')
    parser.add_argument('path', nargs='?', help='技能目录路径')
    parser.add_argument('--all', action='store_true', help='验证所有技能')
    parser.add_argument('--json', action='store_true', help='输出 JSON 格式')

    args = parser.parse_args()

    validator = SkillValidator()

    if args.all:
        results = validator.validate_all()

        if args.json:
            import json
            output = []
            for r in results:
                output.append({
                    'skill_name': r.skill_name,
                    'valid': r.valid,
                    'errors': [{'message': e.message, 'file': e.file, 'line': e.line} for e in r.errors],
                    'warnings': [{'message': w.message, 'file': w.file, 'line': w.line} for w in r.warnings]
                })
            print(json.dumps(output, ensure_ascii=False, indent=2))
        else:
            for result in results:
                print_result(result)

            # 统计
            total = len(results)
            passed = sum(1 for r in results if r.valid)
            failed = total - passed

            print(f"\n{'='*50}")
            print(f"总计: {total} 个技能")
            print(f"通过: {passed} 个")
            print(f"失败: {failed} 个")

        sys.exit(0 if all(r.valid for r in results) else 1)

    elif args.path:
        result = validator.validate(Path(args.path))
        print_result(result)
        sys.exit(0 if result.valid else 1)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
