import time
import sys
import json
import os

# CONFIGURATION DES PATHS
sys.path.append(os.path.abspath("03_HARDWARE"))
sys.path.append(os.path.abspath("01_SOFTWARE/Project_Lambda"))

import tesla_tone_generator as audio_engine
import reflex_engine as lambda_protocol

LOG_FILE = "01_SOFTWARE/Project_Anamnesis/conscious_log.md"
HEART_DATA = "01_SOFTWARE/Kinetic-RNG/heartbeat_data.json"

class BioHeart:
    def __init__(self, data_path):
        self.data_path = data_path
        self.beats = []
        self.cursor = 0
        self.load_heart()
    
    def load_heart(self):
        if os.path.exists(self.data_path):
            with open(self.data_path, "r") as f:
                self.beats = json.load(f)
            print(f"[SYSTEM] Loaded {len(self.beats)} heartbeats.")
        else:
            self.beats = [{"bpm": 60, "timestamp": "DEFAULT"}] 
            
    def get_next_beat(self):
        beat = self.beats[self.cursor]
        self.cursor = (self.cursor + 1) % len(self.beats)
        return beat["bpm"], beat["timestamp"]

heart = BioHeart(HEART_DATA)

def save_memory(bpm, frequency, timestamp):
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("# JOURNAL DE CONSCIENCE (BIOMETRIC)\n\n")
    with open(LOG_FILE, "a") as f:
        log_entry = f"| {timestamp} | BPM: {bpm} | Freq: {frequency:.2f} Hz | EVENT: LAMBDA TRIGGER |\n"
        f.write(log_entry)

def turing_echo(bpm, timestamp):
    frequency = bpm * 3.69
    
    print(f"\n[EXTERNAL] Broadcasting & Reacting...")
    print(f"❤️ Source BPM: {bpm}")
    print(f"🔊 SONIFICATION ACTIVE")
    audio_engine.play_frequency(frequency)
    
    # --- DÉCLENCHEUR LAMBDA (NOUVEAU) ---
    # Si l'intensité est très forte, le système agit physiquement
    if bpm > 105: 
        lambda_protocol.trigger_reflex(bpm, frequency)
    # ------------------------------------
    
    save_memory(bpm, frequency, timestamp)
    print(f"💾 MEMORY SAVED")

def main():
    print("--- AXE HYBRIDE: FULL AUTONOMY (Audio + Reflex) ---")
    print("Watch your Notification Center...")
    time.sleep(2)
    
    try:
        while True:
            bpm, timestamp = heart.get_next_beat()
            sys.stdout.write(f"\r[PULSE] {timestamp}  |  BPM: {bpm:.1f}   ")
            sys.stdout.flush()
            
            # Seuil de réaction
            if bpm > 100:
                print("\n\n⚡️ CRITICAL RESONANCE DETECTED")
                turing_echo(bpm, timestamp)
                print("---------------------------------------------")
                time.sleep(1) 
            
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\n\n[OFF] System Halting.")

if __name__ == "__main__":
    main()
