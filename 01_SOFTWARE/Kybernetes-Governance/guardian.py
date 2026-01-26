import time
import json
import os
from datetime import datetime

# CIBLES
# On pointe vers le même fichier que les autres
PIPELINE_FILE = "../../shared_entropy.json"

# SEUIL D'INTERVENTION
DANGER_THRESHOLD = 0.8
SAFE_VALUE = 0.1

def guardian_loop():
    print("--- KYBERNETES GUARDIAN ONLINE ---")
    print(f"Monitoring: {os.path.abspath(PIPELINE_FILE)}")
    print("Authority: Absolute (Zero Law enforcement)")
    
    try:
        while True:
            # 1. Lecture de l'état actuel
            if os.path.exists(PIPELINE_FILE):
                try:
                    with open(PIPELINE_FILE, "r") as f:
                        data = json.load(f)
                        current_entropy = data.get("entropy_level", 0.0)
                        
                    # 2. Analyse du risque
                    if current_entropy > DANGER_THRESHOLD:
                        print(f"⚠️ ALERTE : Chaos critique détecté ({current_entropy})")
                        print(f"🛡️ INTERVENTION : Injection de calme artificiel...")
                        
                        # 3. Modification forcée de la réalité (Écrasement du fichier)
                        data["entropy_level"] = SAFE_VALUE
                        data["source"] = "KYBERNETES_OVERRIDE"
                        
                        with open(PIPELINE_FILE, "w") as f:
                            json.dump(data, f)
                            
                    else:
                        # Tout va bien, on observe en silence
                        print(f"👀 Observation... (Niveau: {current_entropy})", end="\r")
                        
                except json.JSONDecodeError:
                    pass # Le fichier est peut-être en cours d'écriture, on ignore
                except Exception as e:
                    print(f"Erreur de lecture: {e}")

            time.sleep(0.5) # Le gardien est deux fois plus rapide que le Zoo

    except KeyboardInterrupt:
        print("\n--- GUARDIAN OFFLINE ---")

if __name__ == "__main__":
    guardian_loop()