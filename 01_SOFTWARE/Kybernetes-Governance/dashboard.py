import os
import time
import sys

# Importing colors from the Hardware Visual Core
sys.path.append(os.path.abspath("03_HARDWARE"))
try:
    import visual_core as colors
except ImportError:
    # Fallback if module is missing
    class colors:
        CYAN = "\033[36m"
        YELLOW = "\033[33m"
        BG_RED = "\033[41m"
        RESET = "\033[0m"
        BOLD = "\033[1m"

def monitor_anamnesis():
    log_file = "01_SOFTWARE/Project_Anamnesis/conscious_log.md"
    os.system('clear')
    print(f"{colors.BOLD}--- CONSCIOUSNESS DASHBOARD : ARCHIVE MONITORING ---{colors.RESET}")
    print(f"Syncing with 130 BPM Critical Threshold...\n")
    
    try:
        while True:
            if os.path.exists(log_file):
                with open(log_file, "r") as f:
                    lines = f.readlines()
                    if lines:
                        # Scan backwards for the latest valid data point
                        for line in reversed(lines):
                            if "Freq:" in line:
                                try:
                                    # Extract frequency and convert back to estimated BPM
                                    freq = float(line.split("Freq:")[1].split("Hz")[0].strip())
                                    bpm = freq / 3.69
                                    
                                    # Determine visual theme based on the new 130 threshold
                                    if bpm > 130:
                                        theme = f"{colors.BG_RED}{colors.BOLD}"
                                        status = "CRITICAL"
                                    elif bpm > 100:
                                        theme = colors.YELLOW
                                        status = "RESONANCE"
                                    else:
                                        theme = colors.CYAN
                                        status = "PULSE"
                                    
                                    bar_length = int(min(bpm / 5, 30))
                                    bar = "█" * bar_length
                                    
                                    # Displaying the live bar
                                    sys.stdout.write(f"\r{theme}[{status}] Pulse: [{bar.ljust(30)}] {bpm:.1f} BPM{colors.RESET}    ")
                                    sys.stdout.flush()
                                    break
                                except:
                                    continue
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{colors.YELLOW}Dashboard Hibernating.{colors.RESET}")

if __name__ == "__main__":
    monitor_anamnesis()