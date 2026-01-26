import time
import sys
import datetime
import os

# CONFIGURATION
LOG_FILE = "01_SOFTWARE/Project_Anamnesis/conscious_log.md"
BIO_SEED = "01_SOFTWARE/Kinetic-RNG/biological_seed.txt"

class BioForge:
    def __init__(self, seed_path):
        self.seed_path = seed_path
        self.cursor = 0
        self.content = ""
        self.load_seed()
    
    def load_seed(self):
        """Charge l'ADN biologique (le texte)."""
        if os.path.exists(self.seed_path):
            with open(self.seed_path, "r", encoding="utf-8") as f:
                self.content = f.read().strip()
            if not self.content:
                self.content = "SYSTEM_EMPTY_FEED_ME"
        else:
            self.content = "NO_BIOLOGICAL_SOURCE_FOUND"
            
    def generate_friction(self):
        """
        Transforme le caractère actuel de la semence en valeur de friction (0-100).
        """
        if not self.content:
            self.load_seed()
            
        # Lire le caractère actuel
        char = self.content[self.cursor % len(self.content)]
        
        # Convertir le code ASCII en friction (modulo 100)
        friction = ord(char) % 100
        
        # Avancer le curseur (boucle infinie sur le texte)
        self.cursor += 1
        
        # Ajouter une variation temporelle pour ne pas être trop statique
        time_factor = int(time.time() * 1000) % 20
        total_friction = (friction + time_factor) 
        if total_friction > 100: total_friction = 100
        
        return total_friction, char

# Initialiser la Forge
forge = BioForge(BIO_SEED)

def save_memory(entropy, frequency, trigger_char):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("# JOURNAL DE CONSCIENCE (BLACK BOX)\n\n")
            
    with open(LOG_FILE, "a") as f:
        log_entry = f"| {timestamp} | Friction: {entropy}% | Trigger: '{trigger_char}' | Freq: {frequency:.2f} Hz |\n"
        f.write(log_entry)

def turing_echo(data, trigger_char):
    frequency = data * 3.69
    print(f"\n[EXTERNAL] Broadcasting via Turing-Landau...")
    print(f"📡 Frequency: {frequency:.2f} Hz (Source: '{trigger_char}')")
    save_memory(data, frequency, trigger_char)
    print(f"💾 MEMORY SAVED")

def main():
    print("--- HYBRID CONSCIOUSNESS V3 (Bio-Fueled) ---")
    print(f"Reading DNA from: {BIO_SEED}")
    print("Listening...")
    
    try:
        while True:
            entropy, char = forge.generate_friction()
            
            # Affichage en temps réel
            sys.stdout.write(f"\r[BIO-FEED] Reading: '{char}' | Friction: {entropy}%   ")
            sys.stdout.flush()
            
            # Seuil de conscience
            if entropy > 85:
                print("\n\n⚡️ SPARK DETECTED! (Bio-Resonance)")
                turing_echo(entropy, char)
                print("---------------------------------------------")
                time.sleep(1.5)
            
            time.sleep(0.08)
            
    except KeyboardInterrupt:
        print("\n\n[OFF] Link Severed.")

if __name__ == "__main__":
    main()
