import time
import uuid
import json
import os
import random
from datetime import datetime

# Configuration
PIPELINE_FILE = "../../shared_entropy.json"
HISTORY_FILE = "CHRONICLES_OF_THE_ZOO.md" # Le livre d'histoire

class Genome:
    def __init__(self, metabolism=5, resistance=1.0):
        self.metabolism = metabolism       
        self.resistance = resistance       

    def mutate(self):
        new_meta = self.metabolism * random.uniform(0.9, 1.1)
        new_res = self.resistance * random.uniform(0.9, 1.1)
        return Genome(new_meta, new_res)

class EntropicAgent:
    def __init__(self, generation, parent_genome=None):
        self.id = str(uuid.uuid4())[:4]
        self.generation = generation
        self.name = f"Gen{generation}_{self.id}"
        
        if parent_genome:
            self.genome = parent_genome.mutate()
            self.mutation_type = "🧬 MUTATION"
        else:
            self.genome = Genome()
            self.mutation_type = "✨ ORIGINE"

        self.energy = 100
        self.heat = 0
        self.age = 0
        self.alive = True
        self.cause_of_death = "Inconnue"

    def live(self, chaos_input):
        if not self.alive: return

        real_stress = chaos_input / self.genome.resistance
        consumption = self.genome.metabolism * (1 + real_stress)
        
        self.energy -= consumption
        self.heat += consumption * 2
        self.age += 1
        
        self.heat = max(0, self.heat - 10)
        
        if self.energy <= 0:
            self.alive = False
            self.cause_of_death = "Épuisement"
        elif self.heat >= 1000:
            self.alive = False
            self.cause_of_death = "Surchauffe"

    def status_line(self):
        return (f"[{self.name}] Age:{self.age} | "
                f"Gènes({self.genome.metabolism:.2f}/{self.genome.resistance:.2f}) | "
                f"NRJ:{int(self.energy)}")

# --- L'HISTORIEN ---
def write_to_chronicles(text):
    """Écrit les événements majeurs dans le fichier Markdown"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    with open(HISTORY_FILE, "a") as f:
        f.write(f"- **{timestamp}** : {text}\n")

def init_chronicles():
    """Initialise le fichier si besoin"""
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as f:
            f.write(f"# 📖 CHRONIQUES DU ZOO ENTROPIQUE\n")
            f.write(f"Début de la simulation : {datetime.now().strftime('%Y-%m-%d')}\n\n")

def read_entropy():
    try:
        if os.path.exists(PIPELINE_FILE):
            with open(PIPELINE_FILE, "r") as f:
                return json.load(f).get("entropy_level", 0.1)
    except:
        return 0.1
    return 0.1

def run_evolution():
    init_chronicles()
    print(f"--- PROTOCOLE DARWIN + ANAMNESIS ---")
    write_to_chronicles("🔄 **Démarrage du Système** (Nouvelle Session)")
    
    generation = 1
    last_best_genome = None 
    
    while True:
        agent = EntropicAgent(generation, last_best_genome)
        
        # Log de naissance
        birth_msg = f"{agent.mutation_type} : **{agent.name}** né avec Métabolisme {agent.genome.metabolism:.2f}"
        print(f"\n{birth_msg}")
        write_to_chronicles(birth_msg)
        
        while agent.alive:
            chaos = read_entropy()
            agent.live(chaos)
            print(f"{agent.status_line()} | Chaos: {chaos}", end="\r")
            time.sleep(1)
        
        # Log de mort
        death_msg = f"💀 Décès de {agent.name} (Age: {agent.age}) - Cause: {agent.cause_of_death}"
        print(f"\n{death_msg}")
        
        if agent.age > 10:
            print("✅ Gènes VIABLES.")
            write_to_chronicles(f"{death_msg} -> **Gènes Sauvegardés** ✅")
            last_best_genome = agent.genome
        else:
            print("❌ Gènes FAIBLES.")
            write_to_chronicles(f"{death_msg} -> *Extinction de la branche* ❌")
            # On garde quand même le génome pour réessayer
            last_best_genome = agent.genome 

        time.sleep(2)
        generation += 1

if __name__ == "__main__":
    try:
        run_evolution()
    except KeyboardInterrupt:
        write_to_chronicles("🛑 **Arrêt de la simulation**")
        print("\n🛑 ARRÊT")