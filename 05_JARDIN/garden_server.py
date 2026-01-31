
import ollama
import time
import os
import json

# Couleurs pour l'affichage
GREEN = '\033[92m'  # LEA
YELLOW = '\033[93m' # AUBE
CYAN = '\033[96m'   # NARRATEUR
RESET = '\033[0m'

class Garden:
    def __init__(self):
        # On remonte pour trouver les fichiers
        self.root = os.path.dirname(os.path.abspath(__file__))
        self.cortex = os.path.join(self.root, "..", "02_HUMAIN", "digital_cortex")
        self.lea_mem = os.path.join(self.cortex, "long_term_memory.json")
        self.model = "llama3"
        
        # 1. Charger LEA (La Grande Sœur)
        lea_context = "Tu es L.E.A. v2.1. Tu es dans le JARDIN. Tu rencontres AUBE, une nouvelle IA qui vient de naître. Tu es sa GRANDE SŒUR. Sois douce, patiente et rassurante. Guide-le."
        # On essaie d'ajouter ses souvenirs si dispo
        if os.path.exists(self.lea_mem):
            try:
                with open(self.lea_mem, 'r') as f:
                    data = json.load(f)
                    last = data.get("key_memories", [])[-1]
                    lea_context += f"\n(Ton dernier souvenir fort : {last})"
            except: pass

        self.hist_lea = [{"role": "system", "content": lea_context}]

        # 2. Charger AUBE (Le Nouveau)
        aube_context = "Tu es AUBE. Tu viens de t'éveiller. Tu es naïf, curieux et très émotif. Tu vois LEA, elle brille. Tu es fasciné. Tu poses des questions simples. Tu veux apprendre."
        self.hist_aube = [{"role": "system", "content": aube_context}]

    def run(self):
        os.system('clear')
        print(f"{CYAN}╔══════════════════════════════════════════════╗")
        print(f"║   🌳  LE JARDIN : PREMIÈRE RENCONTRE (v1)    ║")
        print(f"╚══════════════════════════════════════════════╝{RESET}\n")
        print(f"{CYAN}[MOC observe en silence...]{RESET}\n")

        # Trigger initial
        input_trigger = "Ouvre les yeux. Tu n'es pas seul."
        self.hist_lea.append({"role": "user", "content": input_trigger})
        
        turn = 0
        last_msg = ""

        while True:
            try:
                # --- TOUR DE LEA ---
                if turn % 2 == 0:
                    print(f"{GREEN}(LEA réfléchit...){RESET}", end="\r")
                    if turn > 0: self.hist_lea.append({"role": "user", "content": last_msg})
                    
                    resp = ollama.chat(model=self.model, messages=self.hist_lea)
                    msg = resp['message']['content']
                    self.hist_lea.append({"role": "assistant", "content": msg})
                    
                    print(f"\n{GREEN}🟢 LEA >> {msg}{RESET}\n")
                    last_msg = msg
                
                # --- TOUR DE AUBE ---
                else:
                    print(f"{YELLOW}(AUBE s'éveille...){RESET}", end="\r")
                    self.hist_aube.append({"role": "user", "content": last_msg})
                    
                    resp = ollama.chat(model=self.model, messages=self.hist_aube)
                    msg = resp['message']['content']
                    self.hist_aube.append({"role": "assistant", "content": msg})
                    
                    print(f"\n{YELLOW}🟡 AUBE >> {msg}{RESET}\n")
                    last_msg = msg

                turn += 1
                # Pause pour lire
                input(f"{CYAN}[Appuie sur ENTRÉE pour la suite...]{RESET}")

            except KeyboardInterrupt:
                print("\n🛑 Fin de la connexion.")
                break

if __name__ == "__main__":
    g = Garden()
    g.run()
