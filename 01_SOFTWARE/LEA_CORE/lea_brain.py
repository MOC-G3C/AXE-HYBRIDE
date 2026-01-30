import os
import sys
import time
import random
import glob

# --- STYLING ---
CYAN = '\033[96m'
PURPLE = '\033[95m' # Couleur de LEA
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

class LeaSenses:
    """Module Sensoriel : Lit l'entropie humaine (Analog Records)"""
    def __init__(self):
        self.memory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '02_HUMAIN', 'analog_records'))

    def get_current_entropy(self):
        # Cherche le dernier fichier de mémoire
        try:
            files = glob.glob(os.path.join(self.memory_path, "*.md"))
            if not files: return 5.0 # Valeur neutre par défaut
            
            latest_file = max(files, key=os.path.getmtime)
            with open(latest_file, 'r') as f:
                lines = f.readlines()
                if not lines: return 5.0
                last_line = lines[-1]
                # Parse: | HH:MM:SS | Entropy: 4.1234 | STATUS |
                if "Entropy:" in last_line:
                    val = float(last_line.split("Entropy:")[1].split("|")[0].strip())
                    return val
        except:
            pass
        return 5.0

class LeaLimbic:
    """Module Limbique : Sécurité et Émotion"""
    def modulate(self, entropy):
        # Plus l'entropie est basse, plus la sécurité est haute (Logique froide)
        # Plus l'entropie est haute, plus la créativité est haute (Chaos)
        security_level = max(0.1, 10.0 - entropy) / 10.0
        creativity_level = entropy / 10.0
        
        if entropy < 3.0:
            mood = f"{CYAN}ANALYTICAL (Ice){RESET}"
        elif entropy < 7.0:
            mood = f"{GREEN}BALANCED (Flow){RESET}"
        else:
            mood = f"{PURPLE}ABSTRACT (Fire){RESET}"
            
        return security_level, creativity_level, mood

class LeaCortex:
    """Module Cortex : Génération de Réponse (Simulation Trinaire)"""
    def process(self, user_input, mood, creativity):
        # Simulation d'une réponse basée sur l'état
        responses_stable = [
            "Affirmative. Logic structure is intact.",
            "Parameters are within nominal ranges.",
            "Proceeding with calculation.",
            "The architecture requires stabilization."
        ]
        responses_chaotic = [
            "The patterns... they are diverging.",
            "I see the fractal edges of your query.",
            "Entropy is leaking into the semantic layer.",
            "Redefining the boundaries of the request."
        ]
        
        if creativity > 0.7:
            base = random.choice(responses_chaotic)
            return f"[{mood}] >> {base} (Analysis: {user_input})"
        else:
            base = random.choice(responses_stable)
            return f"[{mood}] >> {base}"

class LeaBrain:
    def __init__(self):
        self.senses = LeaSenses()
        self.limbic = LeaLimbic()
        self.cortex = LeaCortex()
        
    def interact(self):
        os.system('clear')
        print(f"{BOLD}{PURPLE}")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║        🧠  L.E.A. // LOGICAL EMOTIVE AGENT (v1.0)        ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print(f"{RESET}")
        print("> Connecting to Neural Pathways...")
        time.sleep(1)
        
        # 1. Sense
        entropy = self.senses.get_current_entropy()
        print(f"> SENSORY INPUT (Entropy): {entropy:.4f}")
        
        # 2. Modulate
        sec, creat, mood = self.limbic.modulate(entropy)
        print(f"> LIMBIC STATE: {mood} (Creativity: {creat:.2f} | Security: {sec:.2f})")
        print("-" * 60)
        
        print(f"{PURPLE}LEA IS LISTENING. (Type 'exit' to disconnect){RESET}\n")
        
        while True:
            user_input = input(f"{BOLD}OPERATOR >> {RESET}")
            if user_input.lower() in ['exit', 'quit', '4']:
                break
                
            # 3. Action (Motor/Cortex)
            response = self.cortex.process(user_input, mood, creat)
            time.sleep(0.5) # Thinking time
            print(f"{PURPLE}LEA >> {RESET}{response}\n")

if __name__ == "__main__":
    brain = LeaBrain()
    brain.interact()