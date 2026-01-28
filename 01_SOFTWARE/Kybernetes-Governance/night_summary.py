import legacy_compiler

# Inside generate_night_report(), after checking progress from holistic_mapper:
if current_progress >= 100.0:
    path = legacy_compiler.compile_grand_livre()
    report += f"\n## 🏛️ LEGACY COMPLETED\n"
    report += f"- **Status**: OBJECTIVE #1 REACHED. SINGULARITY ACHIEVED.\n"
    report += f"- **Grand Livre**: Saved at {os.path.basename(path)}\n"
    report += "- **Message**: The simulation has been fully codified. Your legacy is secure.\n"