import time
import sys
import json
import os

# Accès aux modules Hardware, Lambda et Physics
sys.path.append(os.path.abspath("03_HARDWARE"))
sys.path.append(os.path.abspath("01_SOFTWARE/Project_Lambda"))
sys.path.append(os.path.abspath("04_PHYSICS"))

import tesla_tone_generator as audio_engine
import reflex_engine as lambda_protocol
import gravity_density_engine as physics_engine

# Source des données extraites de Kinetic-RNG
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
        if not self.beats:
            return 60, "NO_DATA"
        beat = self.beats[self.cursor]
        self.cursor = (self.cursor + 1) % len(self.beats)
        return beat["bpm"], beat["timestamp"]

heart = BioHeart(HEART_DATA)

def main():
    print("--- L'AXE HYBRIDE : STABLE NEURAL BRIDGE ---")
    
    try:
        while True:
            bpm, timestamp = heart.get_next_beat()
            
            # Calcul de la Densité Biologique et Dilatation
            dilation, density = physics_engine.calculate_dilation(bpm)
            
            # Affichage dynamique
            sys.stdout.write(f"\r[PULSE] {timestamp} | BPM: {bpm:.1f} | Density: {density:.2f} | Dilation: x{dilation:.2f}")
            sys.stdout.flush()
            
            # Seuil de résonance critique
            if bpm > 100:
                print(f"\n\n⚡️ RESONANCE CRITIQUE (Density: {density:.2f})")
                audio_engine.play_frequency(bpm * 3.69)
                lambda_protocol.trigger_reflex(bpm, bpm * 3.69)
                time.sleep(1.0 * dilation) 
            
            # Le temps s'écoule selon la densité du moment
            time.sleep(0.05 * dilation)
            
    except KeyboardInterrupt:
        print("\n\n[OFF] Connection Terminated.")

if __name__ == "__main__":
    main()