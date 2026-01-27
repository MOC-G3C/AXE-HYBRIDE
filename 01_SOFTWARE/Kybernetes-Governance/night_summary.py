import dream_bug_detector

# Inside your generate_night_report function:
health_issues = dream_bug_detector.run_nocturnal_health_check()

# Append to the report string [cite: 2026-01-26]:
report += "\n## 🛡️ NOCTURNAL HEALTH CHECK\n"
for issue in health_issues:
    report += f"- {issue}\n"