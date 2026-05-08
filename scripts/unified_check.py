#!/usr/bin/env python3
"""
统一验证和同步脚本

整合所有验证和同步功能,提供单一入口点。

用法:
    python unified_check.py --all              # 运行所有检查
    python unified_check.py --validate         # 仅验证技能
    python unified_check.py --sync             # 仅检查同步
    python unified_check.py --fix              # 自动修复问题
    python unified_check.py --ci               # CI 模式(严格检查)
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Optional

# 导入现有模块
sys.path.insert(0, str(Path(__file__).parent))
from validate_skill import SkillValidator
from check_docs_sync import DocSyncChecker, SyncReport
from generate_index import SkillIndexGenerator


class UnifiedChecker:
    """统一检查器"""

    def __init__(self, repo_root: Optional[Path] = None):
        self.repo_root = Path(repo_root) if repo_root else Path.cwd()
        self.validator = SkillValidator(self.repo_root)
        self.sync_checker = DocSyncChecker(self.repo_root)
        self.index_generator = SkillIndexGenerator(self.repo_root)

    def run_all_checks(self, fix: bool = False) -> dict:
        """运行所有检查"""
        results = {
            'valid': True,
            'validation': None,
            'sync': None,
            'fixed': []
        }

        # 1. 验证技能
        print("🔍 验证技能文件...")
        validation_results = self.validator.validate_all()
        
        # 统计验证结果
        total = len(validation_results)
        valid_count = sum(1 for r in validation_results if r.valid)
        errors = []
        warnings = []
        
        for r in validation_results:
            errors.extend(r.errors)
            warnings.extend(r.warnings)
        
        results['validation'] = {
            'total': total,
            'valid': valid_count,
            'errors': [{'message': e.message, 'file': e.file, 'line': e.line} for e in errors],
            'warnings': [{'message': w.message, 'file': w.file, 'line': w.line} for w in warnings]
        }
        
        if errors:
            results['valid'] = False
            print(f"   ❌ 发现 {len(errors)} 个错误")
        
        if warnings:
            print(f"   ⚠️  发现 {len(warnings)} 个警告")

        # 2. 检查文档同步
        print("\n🔍 检查文档同步...")
        sync_report = self.sync_checker.check_sync()
        results['sync'] = {
            'valid': sync_report.valid,
            'issues': [
                {
                    'type': i.issue_type,
                    'severity': i.severity,
                    'message': i.message,
                    'locations': i.locations,
                    'suggestion': i.suggestion
                }
                for i in sync_report.issues
            ]
        }
        
        if not sync_report.valid:
            results['valid'] = False
            print(f"   ❌ 同步检查失败")
        elif sync_report.issues:
            print(f"   ⚠️  发现 {len(sync_report.issues)} 个问题")
        else:
            print(f"   ✅ 同步检查通过")

        # 3. 自动修复(如果请求)
        if fix:
            print("\n🔧 自动修复问题...")
            fixed = self._auto_fix(sync_report)
            results['fixed'] = fixed
            
            if fixed:
                print(f"   ✅ 已修复 {len(fixed)} 个问题")
            else:
                print(f"   ℹ️  没有可自动修复的问题")

        return results

    def _auto_fix(self, sync_report: SyncReport) -> list[str]:
        """自动修复可修复的问题"""
        fixed = []

        for issue in sync_report.issues:
            # 自动同步技能列表
            if issue.issue_type == 'outdated' and 'README.md' in issue.locations:
                if '同步技能列表' in (issue.suggestion or ''):
                    print("   📝 更新 README.md 中的技能列表...")
                    if self.index_generator.update_readme(dry_run=False):
                        fixed.append('README.md 技能列表已更新')

        return fixed

    def validate_only(self) -> dict:
        """仅运行技能验证"""
        validation_results = self.validator.validate_all()
        
        # 统计验证结果
        total = len(validation_results)
        valid_count = sum(1 for r in validation_results if r.valid)
        errors = []
        warnings = []
        
        for r in validation_results:
            errors.extend(r.errors)
            warnings.extend(r.warnings)
        
        return {
            'valid': len(errors) == 0,
            'validation': {
                'total': total,
                'valid': valid_count,
                'errors': [{'message': e.message, 'file': e.file, 'line': e.line} for e in errors],
                'warnings': [{'message': w.message, 'file': w.file, 'line': w.line} for w in warnings]
            }
        }

    def sync_only(self) -> dict:
        """仅运行同步检查"""
        sync_report = self.sync_checker.check_sync()
        
        return {
            'valid': sync_report.valid,
            'sync': {
                'valid': sync_report.valid,
                'issues': [
                    {
                        'type': i.issue_type,
                        'severity': i.severity,
                        'message': i.message,
                        'locations': i.locations,
                        'suggestion': i.suggestion
                    }
                    for i in sync_report.issues
                ]
            }
        }


def print_results(results: dict, json_output: bool = False):
    """打印检查结果"""
    if json_output:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    print("\n" + "="*50)
    print("检查结果汇总")
    print("="*50)

    # 验证结果
    if results.get('validation'):
        val = results['validation']
        print(f"\n📊 技能验证:")
        print(f"   总数: {val.get('total', 0)}")
        print(f"   有效: {val.get('valid', 0)}")
        print(f"   错误: {len(val.get('errors', []))}")
        print(f"   警告: {len(val.get('warnings', []))}")

    # 同步结果
    if results.get('sync'):
        sync = results['sync']
        print(f"\n📄 文档同步:")
        print(f"   状态: {'✅ 通过' if sync['valid'] else '❌ 失败'}")
        print(f"   问题: {len(sync.get('issues', []))}")

    # 修复结果
    if results.get('fixed'):
        print(f"\n🔧 自动修复:")
        for fix in results['fixed']:
            print(f"   ✅ {fix}")

    # 最终状态
    print("\n" + "="*50)
    if results['valid']:
        print("✅ 所有检查通过")
    else:
        print("❌ 检查失败,请修复上述问题")
    print("="*50 + "\n")


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(
        description='统一验证和同步检查',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python unified_check.py --all              # 运行所有检查
  python unified_check.py --validate         # 仅验证技能
  python unified_check.py --sync             # 仅检查同步
  python unified_check.py --all --fix        # 运行检查并自动修复
  python unified_check.py --ci               # CI 模式(严格)
        """
    )

    parser.add_argument('--all', action='store_true', help='运行所有检查')
    parser.add_argument('--validate', action='store_true', help='仅验证技能')
    parser.add_argument('--sync', action='store_true', help='仅检查同步')
    parser.add_argument('--fix', action='store_true', help='自动修复问题')
    parser.add_argument('--ci', action='store_true', help='CI 模式(严格检查)')
    parser.add_argument('--json', action='store_true', help='JSON 格式输出')

    args = parser.parse_args()

    checker = UnifiedChecker()

    # 确定运行模式
    if args.ci:
        # CI 模式:运行所有检查,严格模式
        results = checker.run_all_checks(fix=False)
        print_results(results, json_output=args.json)
        sys.exit(0 if results['valid'] else 1)

    if args.all:
        # 运行所有检查
        results = checker.run_all_checks(fix=args.fix)
        print_results(results, json_output=args.json)
        sys.exit(0 if results['valid'] else 1)

    if args.validate:
        # 仅验证
        results = checker.validate_only()
        print_results(results, json_output=args.json)
        sys.exit(0 if results['valid'] else 1)

    if args.sync:
        # 仅同步检查
        results = checker.sync_only()
        print_results(results, json_output=args.json)
        sys.exit(0 if results['valid'] else 1)

    # 默认:运行所有检查
    results = checker.run_all_checks(fix=args.fix)
    print_results(results, json_output=args.json)
    sys.exit(0 if results['valid'] else 1)


if __name__ == '__main__':
    main()
