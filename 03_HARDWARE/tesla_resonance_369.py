import os
from datetime import datetime

# --- CONFIGURATION AXE HYBRIDE ---
LOG_PATH = os.path.expanduser("~/Desktop/L'AXE HYBRIDE/session_logs/HARDWARE_RESONANCE.md")

def log_resonance(data):
    with open(LOG_PATH, 'a') as f:
        f.write(f"### Session du {datetime.now()}\n{data}\n\n")

def run_simulation(base_numbers=[3, 6, 9]):
    results = []
    print("🌀 Calcul des fréquences de résonance...")
    for n in base_numbers:
        freq_sum = sum([n * i for i in range(1, 4)])
        results.append(f"- Base {n} : Résonance harmonique = {freq_sum}Hz")
    
    summary = "\n".join(results)
    log_resonance(summary)
    print("✅ Résonance archivée dans HARDWARE_RESONANCE.md")

if __name__ == "__main__":
    run_simulation()

    ---
   