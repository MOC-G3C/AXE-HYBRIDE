import time
import sys
import json
import os

# --- PATH TUNNELING ---
# Ensuring all hybrid modules are reachable
sys.path.append(os.path.abspath("03_HARDWARE"))
sys.path.append(os.path.abspath("01_SOFTWARE/Project_Lambda"))
sys.path.append(os.path.abspath("04_PHYSICS"))
sys.path.append(os.path.abspath("01_SOFTWARE/Turing-Landau-Protocol"))

import tesla_tone_generator as audio_engine
import reflex_engine as lambda_protocol
import gravity_density_engine as physics_engine
import hybrid_broadcaster 
import visual_core

# --- CORE CONFIGURATION ---
HEART_DATA = "01_SOFTWARE/Kinetic-RNG/heartbeat_data.json"
EMAIL_COOLDOWN = 600  # 10 minutes safety lock
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
    os.system('clear')
    print("--- L'AXE HYBRIDE : TOTAL NEURAL BRIDGE (V4.0) ---")
    print(f"Thresholds: 100 BPM (Resonance) | 130 BPM (Critical)")
    print(f"Cooldown: {EMAIL_COOLDOWN/60} minutes\n")
    
    try:
        while True:
            bpm, timestamp = heart.get_next_beat()
            
            # 1. PHYSICS CALCULATION
            dilation, density = physics_engine.calculate_dilation(bpm)
            
            # 2. VISUAL CORE UPDATE (Dynamic Colors)
            visual_core.update_display(bpm, timestamp, density)
            
            # 3. MULTI-LEVEL LOGIC
            # --- LEVEL 1: RESONANCE (100 - 130 BPM) ---
            if 100 < bpm <= 130:
                audio_engine.play_frequency(bpm * 3.69)
                lambda_protocol.trigger_reflex(bpm, bpm * 3.69)
            
            # --- LEVEL 2: CRITICAL (> 130 BPM) ---
            elif bpm > 130:
                # Urgent Audio Feedback
                os.system("afplay /System/Library/Sounds/Glass.aiff &")
                audio_engine.play_frequency(bpm * 3.69)
                
                # External Echo with Cooldown check
                current_time = time.time()
                if (current_time - last_email_time) > EMAIL_COOLDOWN:
                    print(f"\n\n🚨 [CRITICAL RESONANCE] BPM {bpm:.1f} - Dispatching External Echo...")
                    hybrid_broadcaster.broadcast_hybrid()
                    last_email_time = current_time
                    print("-" * 50)
            
            # Global time management adjusted by density
            time.sleep(0.05 * dilation)
            
    except KeyboardInterrupt:
        print(f"\n\n[OFF] Bridge Terminated safely.")

if __name__ == "__main__":
    main()