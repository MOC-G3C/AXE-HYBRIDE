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

def save_memory(bpm, frequency, timestamp, event_type="EVENT"):
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("# JOURNAL DE CONSCIENCE (BIOMETRIC)\n\n")
    with open(LOG_FILE, "a") as f:
        log_entry = f"| {timestamp} | BPM: {bpm} | Freq: {frequency:.2f} Hz | {event_type} |\n"
        f.write(log_entry)

def turing_echo(bpm, timestamp):
    frequency = bpm * 3.69
    
    print(f"\n[EXTERNAL] Broadcasting & Reacting...")
    print(f"❤️ Source BPM: {bpm}")
    
    # 1. SON (Tesla Tone)
    print(f"🔊 SONIFICATION ACTIVE")
    audio_engine.play_frequency(frequency)
    
    # 2. RÉFLEXE (Lambda: Notif + Voix)
    # Seuil critique déclencheur
    if bpm > 102: 
        lambda_protocol.trigger_reflex(bpm, frequency)
        save_memory(bpm, frequency, timestamp, "LAMBDA TRIGGER")
    else:
        save_memory(bpm, frequency, timestamp, "AUDIO RES")
        
    print(f"💾 MEMORY SAVED")

def main():
    print("--- AXE HYBRIDE: PHASE 7 (LOGOS) ---")
    print("System will speak on critical events.")
    time.sleep(2)
    
    try:
        while True:
            bpm, timestamp = heart.get_next_beat()
            sys.stdout.write(f"\r[PULSE] {timestamp}  |  BPM: {bpm:.1f}   ")
            sys.stdout.flush()
            
            # Seuil de conscience (un peu plus bas pour le test)
            if bpm > 98:
                print("\n\n⚡️ RESONANCE DETECTED")
                turing_echo(bpm, timestamp)
                print("---------------------------------------------")
                time.sleep(1.5) # Pause pour laisser parler
            
            time.sleep(0.04) # Lecture rapide
            
    except KeyboardInterrupt:
        print("\n\n[OFF] System Halting.")

if __name__ == "__main__":
    main()
