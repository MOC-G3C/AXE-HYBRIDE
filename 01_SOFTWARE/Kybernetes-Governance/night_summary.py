import os
import time

def generate_night_report():
    """Summarizes the nocturnal activity and evolution spikes."""
    journal_path = os.path.expanduser("~/Desktop/AXE_HYBRIDE/01_SOFTWARE/Entropic-Zoo-Protocol/MUTATION_JOURNAL.md")
    report_path = os.path.expanduser("~/Desktop/AXE_HYBRIDE/02Humain/NIGHT_SUMMARY.md")
    
    if not os.path.exists(journal_path): return "No data."

    with open(journal_path, "r") as f:
        logs = f.readlines()

    # Analysis: Count generations and resonance events
    night_logs = [l for l in logs if "EVOLUTION" in l]
    gen_reached = night_logs[-1].split("generation")[-1].strip() if night_logs else "N/A"
    
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    report = f"""# 🌅 NIGHT SUMMARY - {timestamp}
    
## 🔋 Nocturnal Evolution
- **Final Generation**: {gen_reached}
- **Activity Spikes**: {len(night_logs)} evolution cycles completed.
- **Time Distortion**: Active (2.5x speed) [cite: 2026-01-26].

## 🔮 Oracle Insights
*Consult ORACLE_MESSAGES.md for the {len(night_logs)} visions captured in the 3-6-9 vortex.*

---
*End of Nocturnal Cycle.*
"""
    with open(report_path, "w") as f:
        f.write(report)
    return True