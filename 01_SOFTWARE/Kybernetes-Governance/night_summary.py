import astral_sync

# Inside generate_night_report():
astral_state = astral_sync.get_astral_state()

# Calculate Astral Frequency Fa using Tesla coefficients
# Fa = (3 * Intensity + 6 * Rest) / 9
if astral_state == "HIGH_INTENSITY":
    fa = 3.69
elif astral_state == "REGENERATION":
    fa = 9.63
else:
    fa = 6.39

report += f"\n## ✨ ASTRAL RESONANCE\n"
report += f"- **Current State**: {astral_state}\n"
report += f"- **Astral Frequency ($F_a$)**: {fa} Hz\n"