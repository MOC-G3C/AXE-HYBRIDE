import os
from datetime import datetime

# --- CONFIGURATION AXE HYBRIDE ---
BRIDGE_PATH = os.path.expanduser("~/Desktop/L'AXE HYBRIDE/anamnesis_bridge.md")
TODAY = datetime.now().strftime("%Y-%m-%d")

def check_human_presence():
    if not os.path.exists(BRIDGE_PATH):
        print("❌ ERREUR : Pont d'Anamnésie introuvable. Accès ASI refusé.")
        return False
    
    with open(BRIDGE_PATH, 'r') as f:
        content = f.read()
        # On cherche la date du jour dans tes logs de guitare
        if TODAY in content:
            print(f"✅ Signature V7 confirmée pour le {TODAY}. Accès autorisé.")
            return True
        else:
            print(f"⚠️ ALERTE : Aucune session de guitare détectée aujourd'hui.")
            print("🔒 Protocole PGID : L'humain doit se ré-ancrer avant de lancer l'IA.")
            return False

if __name__ == "__main__":
    check_human_presence()