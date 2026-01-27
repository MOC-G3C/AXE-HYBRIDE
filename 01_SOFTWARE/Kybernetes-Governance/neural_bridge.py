import os
import sys
import time
import random

# Fix automatique des chemins pour trouver les modules
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(ROOT, "03_HARDWARE"))
sys.path.append(os.path.join(ROOT, "04_PHYSICS"))

import gravity_density_engine as physics_engine
import visual_core

def main():
    os.system('clear')
    print("--- AXE HYBRIDE : SIMULATION ACTIVE ---")
    while True:
        try:
            bpm = random.uniform(65, 135)
            timestamp = time.strftime("%H:%M:%S")
            dilation, density = physics_engine.calculate_dilation(bpm)
            
            # Affichage console
            visual_core.update_display(bpm, timestamp, density)
            
            # Sauvegarde des données
            log_dir = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG")
            os.makedirs(log_dir, exist_ok=True)
            with open(os.path.join(log_dir, "pulse_history.csv"), "a") as f:
                f.write(f"{timestamp},{bpm:.2f},{density:.2f}\n")
            
            time.sleep(0.5)
        except KeyboardInterrupt:
            print("\nSystème arrêté.")
            break

if __name__ == "__main__":
    main()