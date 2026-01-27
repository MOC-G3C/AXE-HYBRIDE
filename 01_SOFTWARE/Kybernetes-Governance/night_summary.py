import self_code_refactor

# Inside your generate_night_report function, before writing the file:
branch_created = self_code_refactor.prepare_ectoplasm_branch()

# Append this to the report string:
report += f"\n## 🛠️ AUTONOMOUS REFACTORING\n"
report += f"- **Git Branch Created**: `{branch_created}`\n"
report += f"- **Action Required**: Run `git checkout {branch_created}` to review proposals.\n"