cat << 'EOF' > "01_SOFTWARE/Entropic-Zoo-Protocol/zoo_analyzer.py"
import os
import re

LOG_FILE = "01_SOFTWARE/Project_Anamnesis/conscious_log.md"

def analyze_zoo():
    print("--- ENTROPIC ZOO : TAXONOMY ANALYSIS ---")
    if not os.path.exists(LOG_FILE):
        print("[ERROR] Anamnesis log not found.")
        return

    stats = {"Pulse (3)": 0, "Surge (6)": 0, "Transcendence (9)": 0}
    total_sparks = 0

    with open(LOG_FILE, "r") as f:
        for line in f:
            if "BPM:" in line or "Friction:" in line:
                total_sparks += 1
                # Recherche de la fréquence dans la ligne
                freq_match = re.search(r"Freq:\s*([\d.]+)", line)
                if freq_match:
                    freq = float(freq_match.group(1))
                    
                    # Classification selon l'échelle Tesla
                    if freq >= 369.0:
                        stats["Transcendence (9)"] += 1
                    elif freq >= 360.0:
                        stats["Surge (6)"] += 1
                    else:
                        stats["Pulse (3)"] += 1

    print(f"\nTotal Sparks Analyzed: {total_sparks}")
    print("-" * 30)
    for species, count in stats.items():
        percentage = (count / total_sparks * 100) if total_sparks > 0 else 0
        bar = "█" * int(percentage / 5)
        print(f"{species.ljust(18)}: [{bar.ljust(20)}] {count} ({percentage:.1f}%)")
    print("-" * 30)

if __name__ == "__main__":
    analyze_zoo()
EOF