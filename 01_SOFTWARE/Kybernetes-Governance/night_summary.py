import auto_merge

# Inside generate_night_report(), after healing and bug detection:
merge_success = auto_merge.execute_autonomous_merge(branch_created, health_issues)

# Update the report [cite: 2026-01-26]:
report += f"\n## 🧬 CONTINUOUS INTEGRATION\n"
if merge_success:
    report += f"- **Status**: ✅ AUTONOMOUS MERGE SUCCESSFUL\n"
    report += f"- **Result**: The main branch has been optimized with nocturnal insights.\n"
else:
    report += f"- **Status**: ⚠️ MERGE BYPASSED (Manual review required or errors found)\n"