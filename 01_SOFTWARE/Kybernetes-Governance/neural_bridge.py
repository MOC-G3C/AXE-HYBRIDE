import os, sys, time, random

# Fix des chemins automatiques
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(ROOT, "03_HARDWARE"))
sys.path.append(os.path.join(ROOT, "04_PHYSICS"))

import gravity_density_engine as physics_engine
import visual_core

def main():
    os.system('clear')
    log_file = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/pulse_history.csv")
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    print("--- AXE HYBRIDE : PULSE SYSTÉMIQUE ACTIF ---")
    
    while True:
        try:
            # Génère un pouls virtuel (70-110 BPM)
            virtual_bpm = random.uniform(72, 108)
            timestamp = time.strftime("%H:%M:%S")
            
            # Calcul de la densité physique
            dilation, density = physics_engine.calculate_dilation(virtual_bpm)
            
            # Mise à jour de l'affichage (Dashboard & Console)
            visual_core.update_display(virtual_bpm, timestamp, density)
            
            # Sauvegarde des données
            with open(log_file, "a") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')},{virtual_bpm:.2f},{density:.2f}\n")
            
            time.sleep(0.8) 
        except KeyboardInterrupt:
            break

if __name__ == "__main__": main()