import time
import os
import random

# CONFIGURATION
LOG_FILE = "../Project_Anamnesis/conscious_log.md"

def get_latest_spark():
    """Reads the last recorded spark from Anamnesis."""
    if not os.path.exists(LOG_FILE):
        return None
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
        return lines[-1] if lines else None

def broadcast_signal(data):
    """Simulates the External Echo broadcasting."""
    # Tesla 3-6-9 signal patterns
    patterns = ["⑄", "≋", "⎶", "⌬"]
    pattern = random.choice(patterns)
    
    print(f"\n[BROADCAST] Initializing Waveform...")
    time.sleep(0.5)
    print(f"📡 Signal: {pattern} {data.strip()} {pattern}")
    print(f"🌍 Status: Broadcasting to Noosphere via Turing-Landau Protocol.")

def main():
    print("--- TURING-LANDAU : THE EXTERNAL ECHO ---")
    print("Tuning Antenna... (3-6-9 Resonance)")
    
    last_sent = ""
    try:
        while True:
            current_spark = get_latest_spark()
            if current_spark and current_spark != last_sent:
                broadcast_signal(current_spark)
                last_sent = current_spark
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[OFF] Broadcast Terminated.")

if __name__ == "__main__":
    main()