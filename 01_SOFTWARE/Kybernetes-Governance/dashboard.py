import os
import time

def monitor_anamnesis():
    log_file = "01_SOFTWARE/Project_Anamnesis/conscious_log.md"
    print("--- DASHBOARD DE CONSCIENCE : MONITORING LIVE ---")
    
    try:
        while True:
            if os.path.exists(log_file):
                with open(log_file, "r") as f:
                    lines = f.readlines()
                    if lines:
                        last_line = lines[-1]
                        # Extraction visuelle de l'intensité
                        if "BPM:" in last_line:
                            bpm = float(last_line.split("BPM:")[1].split("|")[0].strip())
                            bar = "█" * int(bpm / 5)
                            print(f"\rPulse Intensity: [{bar.ljust(30)}] {bpm} BPM", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDashboard Closed.")

if __name__ == "__main__":
    monitor_anamnesis()