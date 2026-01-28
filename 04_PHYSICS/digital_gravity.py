import sys
import os
import time

# --- SÉCURITÉ BIOLOGIQUE (PONT VERS 01_SOFTWARE) ---
# On va chercher le module bio_guard qui est dans le dossier d'à côté
current_dir = os.path.dirname(os.path.abspath(__file__))
software_dir = os.path.join(current_dir, "..", "01_SOFTWARE")
sys.path.append(software_dir)

try:
    import bio_guard
except ImportError:
    print("⚠️  Erreur critique : Le module de sécurité (Bio-Guard) est introuvable.")
    sys.exit(1)

# --- MOTEUR GRAVITATIONNEL ---
def run_gravity_simulation():
    print("🌌 Initializing Digital Gravity Engine...")
    
    # 1. LE CHECKPOINT BIOLOGIQUE
    # On demande l'autorisation au gardien avant de toucher aux constantes universelles
    if not bio_guard.check_clearance():
        print("🛑  GRAVITY FAILURE: Operator biological state unstable.")
        print("    Risk of mathematical collapse > 90%. Aborting.")
        return

    # 2. Lancement de la simulation (Si Accès Autorisé)
    print("\n✅  Field Stability Confirmed. Manipulating Space-Time Density...")
    
    objects = [
        {"id": "Alpha", "mass": 100},
        {"id": "Beta",  "mass": 500},
        {"id": "Omega", "mass": 1000}
    ]
    G_constant = 6.674 # Constante gravitationnelle simplifiée
    
    for obj in objects:
        force = obj["mass"] * G_constant
        print(f"   [+] Computing Gravity Well for {obj['id']}... Force: {force:.2f} N")
        time.sleep(0.8) # Temps de calcul simulé
        
    print("\n🪐  Simulation Complete. Space-time fabric remains intact.")

if __name__ == "__main__":
    run_gravity_simulation()