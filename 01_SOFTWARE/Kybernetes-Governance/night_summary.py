import self_healing

# Inside your generate_night_report function, after running the bug detector:
if health_issues:
    restored_files = self_healing.heal_detected_issues(health_issues)
    
    # Append to the report string [cite: 2026-01-26]
    report += "\n## 🩹 SELF-HEALING LOG\n"
    if restored_files:
        for f in restored_files:
            report += f"- ✅ Restored stable version for: `{f}`\n"
    else:
        report += "- No automated restoration was necessary or possible.\n"