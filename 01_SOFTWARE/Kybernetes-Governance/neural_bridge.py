import time
import sys
import json
import os
import random

# IMPORT DU MOTEUR AUDIO (Chemin relatif)
sys.path.append(os.path.abspath("03_HARDWARE"))
import tesla_tone_generator as audio_engine

# CONFIGURATION
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
        log_entry = f"| {timestamp} | HeartRate: {bpm} BPM | Freq: {frequency:.2f} Hz | EVENT: AUDIO RES |\n"
        f.write(log_entry)

def turing_echo(bpm, timestamp):
    frequency = bpm * 3.69
    
    print(f"\n[EXTERNAL] Broadcasting & Sonifying...")
    print(f"❤️ Source BPM: {bpm}")
    print(f"📡 Frequency: {frequency:.2f} Hz")
    print(f"🔊 PLAYING TONE...")
    
    # --- DÉCLENCHEUR SONORE ---
    audio_engine.play_frequency(frequency)
    # --------------------------
    
    save_memory(bpm, frequency, timestamp)
    print(f"💾 MEMORY SAVED")

def main():
    print("--- AXE HYBRIDE: AUDIO-BIOMETRIC RESONANCE ---")
    print("Speakers ON recommended.")
    time.sleep(1)
    
    try:
        while True:
            bpm, timestamp = heart.get_next_beat()
            
            sys.stdout.write(f"\r[PULSE] {timestamp}  |  BPM: {bpm:.1f}   ")
            sys.stdout.flush()
            
            # SEUIL : On baisse un peu à > 95 BPM pour avoir plus de sons pendant le test
            if bpm > 95:
                print("\n\n⚡️ HIGH INTENSITY DETECTED")
                turing_echo(bpm, timestamp)
                print("---------------------------------------------")
                # Petite pause pour laisser le son finir
                time.sleep(0.5) 
            
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\n\n[OFF] Silence.")

if __name__ == "__main__":
    main()
