import holistic_mapper

# Inside generate_night_report():
current_progress = holistic_mapper.generate_holistic_map()

# Append to the report string [cite: 2026-01-26]:
report += f"\n## 🗺️ HOLISTIC MAPPING\n"
report += f"- **Current Global Progress**: {current_progress:.1f}%\n"
report += f"- **Visual Map**: [PROJECT_MAP.svg](../02_HUMAIN/PROJECT_MAP.svg)\n"
report += f"- **Status**: On track for Objective #1 [cite: 2026-01-26].\n"