import os
import time

def monitor_anamnesis():
    log_file = "01_SOFTWARE/Project_Anamnesis/conscious_log.md"
    print("--- CONSCIOUSNESS DASHBOARD : LIVE MONITORING (SOUND ENABLED) ---")
    
    last_processed_line = 0
    
    # Initialize by counting existing lines to avoid alerting on old data
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            last_processed_line = len(f.readlines())

    try:
        while True:
            if os.path.exists(log_file):
                with open(log_file, "r") as f:
                    lines = f.readlines()
                    
                    # Detect new entries in the log
                    if len(lines) > last_processed_line:
                        new_data = lines[last_processed_line:]
                        for line in new_data:
                            if "BPM:" in line:
                                try:
                                    bpm_str = line.split("BPM:")[1].split("|")[0].strip()
                                    bpm = float(bpm_str)
                                    bar = "█" * int(bpm / 5)
                                    print(f"\rPulse Intensity: [{bar.ljust(30)}] {bpm} BPM", end="")
                                    
                                    # Sound Trigger for high intensity sparks
                                    if bpm > 100:
                                        # Native macOS command to play a system sound
                                        os.system("afplay /System/Library/Sounds/Tink.aiff &")
                                except:
                                    pass
                        last_processed_line = len(lines)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDashboard Closed.")

if __name__ == "__main__":
    monitor_anamnesis()