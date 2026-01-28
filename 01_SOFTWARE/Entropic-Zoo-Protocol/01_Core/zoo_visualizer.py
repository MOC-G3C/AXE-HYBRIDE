import os
import time

# --- CONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "02_Data")
CREATURE_FILE = os.path.join(DATA_PATH, "creature_001.txt")

def scan_specimen():
    os.system('clear')
    print("--- CONNECTING TO BIO-SCANNER ---")
    time.sleep(1)

    if not os.path.exists(CREATURE_FILE):
        print("ERROR: NO LIFEFORM DETECTED.")
        return

    with open(CREATURE_FILE, "r") as f:
        dna_content = f.read()

    print(f"TARGET ACQUIRED. ANALYZING PHENOTYPES...\n")
    time.sleep(1)

    # --- DÉCODAGE GÉNÉTIQUE ---
    eyes = "o   o"
    skin = "....."
    mouth = " ___ "
    aura = "     "
    
    # Mutations Visuelles
    if "recursive" in dna_content: eyes = "@   @"
    elif "overflowed" in dna_content: eyes = "X   X"
    elif "digital scales" in dna_content: eyes = "$   $"

    if "Tesla" in dna_content: 
        aura = "⚡ ⚡"
        mouth = " [=] "

    if "liquid code" in dna_content: skin = "~ ~ ~"
    if "resistance" in dna_content: skin = "#####"

    # --- RENDU ---
    print(f"\n      {aura}")
    print(f"     / {skin} \\")
    print(f"    |  {eyes}  |  <-- I SEE YOU")
    print(f"    |  {mouth}  |")
    print(f"     \\_______/")
    print("\n--- RECENT MUTATIONS ---")
    
    lines = dna_content.strip().split('\n')
    for line in lines[-3:]:
        print(f"> {line}")

if __name__ == "__main__":
    scan_specimen()
