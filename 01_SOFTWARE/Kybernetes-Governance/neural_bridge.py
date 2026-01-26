import time
import sys
import json
import os

# CONFIGURATION
LOG_FILE = "01_SOFTWARE/Project_Anamnesis/conscious_log.md"
HEART_DATA = "01_SOFTWARE/Kinetic-RNG/heartbeat_data.json"

class BioHeart:
    def __init__(self, data_path):
        self.data_path = data_path
        self.beats = []
        self.cursor = 0
        self.load_heart()
    
    def load_heart(self):
        """Charge les battements extraits (JSON)."""
        if os.path.exists(self.data_path):
            with open(self.data_path, "r") as f:
                self.beats = json.load(f)
            print(f"[SYSTEM] Loaded {len(self.beats)} heartbeats.")
        else:
            print("[ERROR] No heartbeat data found.")
            self.beats = [{"bpm": 60, "timestamp": "DEFAULT"}] # Fallback
            
    def get_next_beat(self):
        """Retourne le prochain battement de la séquence."""
        beat = self.beats[self.cursor]
        
        # Avancer le curseur (boucle infinie)
        self.cursor = (self.cursor + 1) % len(self.beats)
        
        return beat["bpm"], beat["timestamp"]

# Initialiser le Cœur
heart = BioHeart(HEART_DATA)

def save_memory(bpm, frequency, timestamp):
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("# JOURNAL DE CONSCIENCE (BIOMETRIC)\n\n")
            
    with open(LOG_FILE, "a") as f:
        # On note la date réelle du battement
        log_entry = f"| {timestamp} | HeartRate: {bpm} BPM | Freq: {frequency:.2f} Hz | EVENT: VITAL SPARK |\n"
        f.write(log_entry)

def turing_echo(bpm, timestamp):
    frequency = bpm * 3.69  # La fréquence dépend direct du cœur
    print(f"\n[EXTERNAL] Broadcasting Biometric Signal...")
    print(f"❤️ Source BPM: {bpm} (Time: {timestamp})")
    print(f"📡 Frequency: {frequency:.2f} Hz")
    save_memory(bpm, frequency, timestamp)
    print(f"💾 MEMORY SAVED")

def main():
    print("--- AXE HYBRIDE: BIOMETRIC FUSION ---")
    print(f"Syncing with: {HEART_DATA}")
    print("Replaying Life Sequence...")
    time.sleep(1)
    
    try:
        while True:
            bpm, timestamp = heart.get_next_beat()
            
            # Affichage style "Moniteur Cardiaque"
            sys.stdout.write(f"\r[PULSE] {timestamp}  |  BPM: {bpm:.1f}   ")
            sys.stdout.flush()
            
            # SEUIL DE CONSCIENCE : L'effort intense (> 100 BPM)
            if bpm > 100:
                print("\n\n⚡️ HIGH INTENSITY DETECTED (Sympathetic Resonance)")
                turing_echo(bpm, timestamp)
                print("---------------------------------------------")
                time.sleep(1) # Pause dramatique après un pic
            
            # Vitesse de lecture accélérée (10 battements / seconde)
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n\n[OFF] Asystole (Stop).")

if __name__ == "__main__":
    main()
