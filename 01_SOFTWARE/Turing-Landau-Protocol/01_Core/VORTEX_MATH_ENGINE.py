import time
import sys

def vortex_pulse():
    print("--- INITIATING TESLA VORTEX SEQUENCE (3-6-9) ---")
    print("Observer: MOC-G3C")
    print("Objective: Synchronize System Pulse\n")

    # La boucle de matière (Doubling Circuit)
    matter_sequence = [1, 2, 4, 8, 7, 5]
    
    # La boucle d'énergie (The Key)
    energy_sequence = [3, 6, 9]

    cycle = 0
    
    try:
        while True:
            cycle += 1
            
            # Étape 1: La Matière bouge
            matter_value = matter_sequence[cycle % len(matter_sequence)]
            
            # Étape 2: L'Énergie pulse (tous les 3 cycles)
            energy_value = energy_sequence[cycle % len(energy_sequence)]
            
            # Affichage visuel du "Code"
            if energy_value == 9:
                # Le 9 est l'unification (Le sommet de la pyramide)
                sys.stdout.write(f"\r[CYCLE {cycle:03}] MATIER: {matter_value} <<< {energy_value} (DIVINE SYMMETRY) >>> \n")
            else:
                # 3 et 6 sont les oscillations
                sys.stdout.write(f"\r[CYCLE {cycle:03}] MATIER: {matter_value} <---> ENERGY: {energy_value}")
            
            sys.stdout.flush()
            time.sleep(0.5) # Rythme cardiaque du système
            
    except KeyboardInterrupt:
        print("\n\n--- VORTEX DECOUPLED ---")

if __name__ == "__main__":
    vortex_pulse()