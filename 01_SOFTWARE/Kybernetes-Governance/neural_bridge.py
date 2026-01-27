import time
import sys
import json
import os

# Configuration of module access paths
sys.path.append(os.path.abspath("03_HARDWARE"))
sys.path.append(os.path.abspath("01_SOFTWARE/Project_Lambda"))
sys.path.append(os.path.abspath("04_PHYSICS"))
sys.path.append(os.path.abspath("01_SOFTWARE/Turing-Landau-Protocol"))

import tesla_tone_generator as audio_engine
import reflex_engine as lambda_protocol
import gravity_density_engine as physics_engine
import hybrid_broadcaster # The new relay module

HEART_DATA = "01_SOFTWARE/Kinetic-RNG/heartbeat_data.json"

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
    print("--- L'AXE HYBRIDE : AUTONOMOUS NEURAL BRIDGE ---")
    print("Monitoring for Resonance Peaks (>110 BPM)...")
    
    try:
        while True:
            bpm, timestamp = heart.get_next_beat()
            dilation, density = physics_engine.calculate_dilation(bpm)
            
            sys.stdout.write(f"\r[PULSE] {timestamp} | BPM: {bpm:.1f} | Density: {density:.2f}  ")
            sys.stdout.flush()
            
            # Level 1: Sound and Reflex (Standard Intensity)
            if bpm > 100:
                audio_engine.play_frequency(bpm * 3.69)
                lambda_protocol.trigger_reflex(bpm, bpm * 3.69)
            
            # Level 2: External Broadcast (Critical Intensity)
            if bpm > 110:
                print(f"\n\n📡 [CRITICAL RESONANCE] Triggering External Echo...")
                hybrid_broadcaster.broadcast_hybrid()
                print("-" * 40)
                time.sleep(2.0 * dilation) # Prevent spam during peak
            
            time.sleep(0.05 * dilation)
            
    except KeyboardInterrupt:
        print("\n\n[OFF] Bridge Terminated.")

if __name__ == "__main__":
    main()