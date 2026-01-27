import strategic_foresight

# Inside generate_night_report(), using the score from wisdom_evaluator:
daily_directive = strategic_foresight.determine_daily_priority(score)

report += f"\n## 🎯 STRATEGIC FORESIGHT\n"
report += f"- **Daily Directive**: {daily_directive}\n"
report += f"- **Objective #1 Alignment**: Optimal.\n"