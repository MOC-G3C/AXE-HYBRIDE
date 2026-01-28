import os
import random
import datetime

# CONFIGURATION
ZOO_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ZOO_PATH, "02_Data")
CREATURE_FILE = os.path.join(DATA_PATH, "creature_001.txt")

# MUTATIONS
MUTATIONS = [
    "Developed digital scales",
    "Grew an extra syntax limb",
    "Eyes became recursive",
    "Voice shifted to 432Hz",
    "Skin turned into liquid code",
    "Acquired gravity resistance",
    "Memory buffer overflowed",
    "Started humming Tesla frequencies",
    "Pixelated consciousness",
    "Became transparent to logic"
]

def mutate_creature():
    print(f"--- ACCESSING ZOO ENCLOSURE ---")
    
    # Creation de l'enclos si absent
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)

    if not os.path.exists(CREATURE_FILE):
        with open(CREATURE_FILE, "w") as f:
            f.write("SPECIES: UNKNOWN\nSTATUS: BIRTH\n")

    new_mutation = random.choice(MUTATIONS)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(CREATURE_FILE, "a") as f:
        f.write(f"\n[{timestamp}] MUTATION: {new_mutation}")
    
    print(f"✅ INJECTION SUCCESSFUL.")
    print(f"🧬 Evolved: {new_mutation}")

if __name__ == "__main__":
    mutate_creature()
