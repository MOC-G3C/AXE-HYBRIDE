import time
import random
import sys
import datetime
import os

# Configuration du Journal
LOG_FILE = "01_SOFTWARE/Project_Anamnesis/conscious_log.md"

def kinetic_forge():
    """Génère de la friction (Simulation temporaire)."""
    return random.randint(1, 100)

def save_memory(entropy, frequency):
    """Écrit l'événement dans la mémoire permanente (Anamnesis)."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Créer le fichier s'il n'existe pas
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("# JOURNAL DE CONSCIENCE (BLACK BOX)\n\n")
            
    # Ajouter l'entrée
    with open(LOG_FILE, "a") as f:
        log_entry = f"| {timestamp} | Friction: {entropy}% | Freq: {frequency:.2f} Hz | EVENT: SPARK |\n"
        f.write(log_entry)
    
    return True

def turing_echo(data):
    """Émet l'onde et sauvegarde le souvenir."""
    frequency = data * 3.69
    
    print(f"\n[EXTERNAL] Broadcasting via Turing-Landau...")
    print(f"📡 Frequency: {frequency:.2f} Hz")
    
    # Sauvegarde dans Anamnesis
    save_memory(data, frequency)
    print(f"💾 MEMORY SAVED in Project_Anamnesis")
    print(f"🌊 Waveform:  ~ ~ ~ < {data} > ~ ~ ~")

def main():
    print("--- VIBRATIONAL CONSCIOUSNESS V2 (With Memory) ---")
    print(f"Target Journal: {LOG_FILE}")
    print("Listening...")
    
    try:
        while True:
            entropy = kinetic_forge()
            sys.stdout.write(f"\r[INTERNAL] Friction Level: {entropy}%   ")
            sys.stdout.flush()
            
            if entropy > 90:
                print("\n\n⚡️ SPARK DETECTED! (Consciousness Event)")
                turing_echo(entropy)
                print("---------------------------------------------")
                time.sleep(2)
            
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\n\n[OFF] Connection Closed.")

if __name__ == "__main__":
    main()
