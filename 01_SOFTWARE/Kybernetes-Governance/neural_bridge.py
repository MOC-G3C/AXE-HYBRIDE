import time
import sys
import json
import os

# Paths
sys.path.append(os.path.abspath("03_HARDWARE"))
sys.path.append(os.path.abspath("01_SOFTWARE/Project_Lambda"))
sys.path.append(os.path.abspath("04_PHYSICS"))
sys.path.append(os.path.abspath("01_SOFTWARE/Turing-Landau-Protocol"))

import tesla_tone_generator as audio_engine
import reflex_engine as lambda_protocol
import gravity_density_engine as physics_engine
import hybrid_broadcaster 

HEART_DATA = "01_SOFTWARE/Kinetic-RNG/heartbeat_data.json"
# --- COOLDOWN CONFIG ---
# Only one email every 300 seconds (5 minutes)
EMAIL_COOLDOWN = 300 
last_email_time = 0

class BioHeart:
    def __init__(self, data_path):
        self.data_path = data_path
        self.beats = []
        self.cursor = 0
        if os.path.exists(self.data_path):
            with open(self.data_path, "r") as f:
                self.beats = json.load(f)
            
    def get_next_beat(self):
        if not self.beats: return 60, "NO_DATA"
        beat = self.beats[self.cursor]
        self.cursor = (self.cursor + 1) % len(self.beats)
        return beat["bpm"], beat["timestamp"]

heart = BioHeart(HEART_DATA)

def main():
    global last_email_time
    print("--- L'AXE HYBRIDE : STABLE NEURAL BRIDGE ---")
    
    try:
        while True:
            bpm, timestamp = heart.get_next_beat()
            dilation, density = physics_engine.calculate_dilation(bpm)
            
            sys.stdout.write(f"\r[PULSE] {timestamp} | BPM: {bpm:.1f} | Density: {density:.2f}  ")
            sys.stdout.flush()
            
            if bpm > 100:
                audio_engine.play_frequency(bpm * 3.69)
                lambda_protocol.trigger_reflex(bpm, bpm * 3.69)
            
            # Broadcast with Cooldown check
            if bpm > 110:
                current_time = time.time()
                if (current_time - last_email_time) > EMAIL_COOLDOWN:
                    print(f"\n\n📡 [PEAK] Broadcasting Resonance Report...")
                    hybrid_broadcaster.broadcast_hybrid()
                    last_email_time = current_time
                    print(f"Next broadcast available in {EMAIL_COOLDOWN/60} minutes.")
                    print("-" * 40)
            
            time.sleep(0.05 * dilation)
            
    except KeyboardInterrupt:
        print("\n\n[OFF] Connection Terminated.")

if __name__ == "__main__":
    main()