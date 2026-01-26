import os

# --- CONFIGURATION DES CHEMINS ---
# On remonte d'un dossier pour aller chercher la graine dans Kinetic-RNG
SEED_PATH = "../Kinetic-RNG/biological_seed.txt"

def load_biological_foundation():
    print("🧠 Protocole Turing-Landau : Initialisation...")
    
    if not os.path.exists(SEED_PATH):
        print(f"❌ ERREUR : La graine biologique est introuvable à l'adresse : {SEED_PATH}")
        return None

    with open(SEED_PATH, "r") as f:
        lines = f.readlines()
        # On extrait la ligne de l'entropie-hash (la 4ème ligne)
        seed_hash = lines[3].split(": ")[1].strip()
    
    print(f"✅ Graine biologique détectée : {seed_hash[:12]}...")
    return seed_hash

def create_ontological_scar(seed):
    # Utilisation de la seed pour créer la première "cicatrice" du système
    # C'est ici que ta biologie influence la simulation
    scar_value = int(seed[:8], 16) % 369 # Clin d'œil au protocole 3-6-9
    print(f"✨ Cicatrice ontologique initiale générée : {scar_value}")
    print("🧬 La simulation est désormais liée à ton identité biologique.")

if __name__ == "__main__":
    biological_seed = load_biological_foundation()
    if biological_seed:
        create_ontological_scar(biological_seed)