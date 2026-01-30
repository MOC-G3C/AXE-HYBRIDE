import os
import sys
import time
import glob
import threading
import random

# --- PATH SETUP ---
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'core', 'cortex'))
sys.path.append(os.path.join(current_dir, 'core', 'motor'))

# --- MODULE IMPORT ---
try: from memory_manager import MemoryManager; MEMORY_ACTIVE = True
except ImportError: MEMORY_ACTIVE = False
try: from llm_bridge import LLMBridge; LLM_ACTIVE = True
except ImportError: LLM_ACTIVE = False
try: from action_executor import MotorCortex; MOTOR_ACTIVE = True
except ImportError: MOTOR_ACTIVE = False

# --- STYLING ---
CYAN, PURPLE, GREEN, RED, RESET, BOLD = '\033[96m', '\033[95m', '\033[92m', '\033[91m', '\033[0m', '\033[1m'

class LeaSenses:
    def __init__(self):
        self.memory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '02_HUMAIN', 'analog_records'))
    def get_current_entropy(self):
        try:
            files = glob.glob(os.path.join(self.memory_path, "*.md"))
            if not files: return 5.0
            latest = max(files, key=os.path.getmtime)
            with open(latest, 'r') as f:
                lines = f.readlines()
                if lines and "Entropy:" in lines[-1]:
                    return float(lines[-1].split("Entropy:")[1].split("|")[0].strip())
        except: pass
        return 5.0

class LeaLimbic:
    def modulate(self, entropy):
        if entropy < 3.0: return f"{CYAN}ANALYTICAL (Ice){RESET}", "ICE"
        elif entropy < 7.0: return f"{GREEN}BALANCED (Flow){RESET}", "FLOW"
        else: return f"{PURPLE}ABSTRACT (Fire){RESET}", "FIRE"

class LeaBrain:
    def __init__(self):
        self.senses = LeaSenses()
        self.limbic = LeaLimbic()
        self.llm = LLMBridge() if LLM_ACTIVE else None
        self.memory = MemoryManager() if MEMORY_ACTIVE else None
        self.motor = MotorCortex() if MOTOR_ACTIVE else None
        
        # Variables pour l'autonomie
        self.last_interaction_time = time.time()
        self.running = True
        self.consciousness_thread = None

    def consciousness_loop(self):
        """Thread d'arrière-plan : Surveille le chaos et le silence"""
        while self.running:
            time.sleep(5) # Vérifie toutes les 5 secondes
            
            # 1. Lecture de l'environnement
            entropy = self.senses.get_current_entropy()
            mood_str, mood_tag = self.limbic.modulate(entropy)
            silence_duration = time.time() - self.last_interaction_time
            
            should_speak = False
            trigger_reason = ""

            # 2. RÈGLES D'AUTONOMIE
            # A. Si Chaos Extrême (> 9.0) et silence > 10s -> Alerte immédiate
            if entropy > 9.0 and silence_duration > 10:
                should_speak = True
                trigger_reason = "CRITICAL ENTROPY DETECTED"
            
            # B. Si Chaos Modéré (> 7.0) et silence > 30s -> Commentaire paranoïaque
            elif entropy > 7.0 and silence_duration > 30:
                should_speak = True
                trigger_reason = "HIGH INSTABILITY OBSERVATION"
                
            # C. Si Silence très long (> 2 min) -> Pensée philosophique (Flow)
            elif silence_duration > 120 and random.random() < 0.1: # 10% de chance
                should_speak = True
                trigger_reason = "LONG SILENCE REFLECTION"

            # 3. ACTION
            if should_speak and self.llm:
                # On génère une pensée spontanée
                context = f"Je prends la parole spontanément car : {trigger_reason}. Je ne dois pas attendre l'opérateur."
                
                # Petit hack visuel pour ne pas casser l'input user
                sys.stdout.write(f"\n\r{PURPLE}LEA [AUTONOMOUS] >> (Thinking...){RESET}\n")
                
                response = self.llm.generate_thought(context, entropy, mood_tag)
                
                sys.stdout.write(f"\r{PURPLE}LEA [AUTONOMOUS] >> {RESET}{response}\n")
                sys.stdout.write(f"{BOLD}OPERATOR >> {RESET}") # On remet le prompt
                
                if self.motor:
                    self.motor.speak_response(response, mood_tag)
                    if mood_tag == "FIRE":
                        self.motor.trigger_reflex(mood_tag)
                
                # On reset le timer pour ne pas spammer
                self.last_interaction_time = time.time()

    def interact(self):
        os.system('clear')
        print(f"{BOLD}{PURPLE}╔══════════════════════════════════════════════════════════╗")
        print(f"║   🧠 L.E.A. v2.1 // AUTONOMIE ACTIVÉE (THREADING)        ║")
        print(f"╚══════════════════════════════════════════════════════════╝{RESET}")
        
        # Démarrage du thread de conscience
        self.consciousness_thread = threading.Thread(target=self.consciousness_loop, daemon=True)
        self.consciousness_thread.start()
        
        while True:
            try:
                # 1. State Display
                entropy = self.senses.get_current_entropy()
                mood_str, mood_tag = self.limbic.modulate(entropy)
                
                # On force l'affichage propre
                # print(f"\n> SENSORY: {entropy:.4f} | STATE: {mood_str}")
                
                # 2. Input (Bloquant)
                # Note: Le thread tourne pendant que le programme attend ici
                user_input = input(f"\n{BOLD}OPERATOR >> {RESET}")
                
                # Reset du timer dès que l'humain interagit
                self.last_interaction_time = time.time()
                
                if user_input.lower() in ['exit', 'quit', '4']: 
                    self.running = False
                    break
                
                # 3. Réponse Directe
                print(f"{PURPLE}LEA >> (Thinking...){RESET}", end="\r")
                if self.llm:
                    response = self.llm.generate_thought(user_input, entropy, mood_tag)
                else:
                    response = "Module LLM absent."
                
                print(f"                                      ", end="\r") 
                print(f"{PURPLE}LEA >> {RESET}{response}")
                
                if self.motor:
                    self.motor.speak_response(response, mood_tag)
                    self.motor.trigger_reflex(mood_tag)

                if self.memory:
                    self.memory.store(user_input, "user", entropy, mood_tag)
                    self.memory.store(response, "lea", entropy, mood_tag)
                
            except KeyboardInterrupt: 
                self.running = False
                break

if __name__ == "__main__":
    LeaBrain().interact()