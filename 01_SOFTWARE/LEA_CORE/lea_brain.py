import os
import sys
import time
import glob

# --- PATH SETUP ---
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'core', 'cortex'))
sys.path.append(os.path.join(current_dir, 'core', 'motor'))

# --- MODULE IMPORT ---
try: from memory_manager import MemoryManager; MEMORY_ACTIVE = True
except ImportError: MEMORY_ACTIVE = False
try: from logic_engine import LogicEngine; LOGIC_ACTIVE = True
except ImportError: LOGIC_ACTIVE = False
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
        sec = max(0.1, 10.0 - entropy) / 10.0
        creat = entropy / 10.0
        if entropy < 3.0: return sec, creat, f"{CYAN}ANALYTICAL (Ice){RESET}", "ICE"
        elif entropy < 7.0: return sec, creat, f"{GREEN}BALANCED (Flow){RESET}", "FLOW"
        else: return sec, creat, f"{PURPLE}ABSTRACT (Fire){RESET}", "FIRE"

class LeaCortex:
    def __init__(self):
        self.logic = LogicEngine() if LOGIC_ACTIVE else None
    def process(self, user_input, mood_tag):
        if self.logic:
            concepts = self.logic.analyze(user_input)
            if concepts: return self.logic.formulate_response(concepts, mood_tag)
        if mood_tag == "FIRE": return "CHAOS DETECTED. SYSTEMS UNSTABLE."
        return "Traitement en cours. Données reçues."

class LeaBrain:
    def __init__(self):
        self.senses = LeaSenses()
        self.limbic = LeaLimbic()
        self.cortex = LeaCortex()
        self.memory = MemoryManager() if MEMORY_ACTIVE else None
        self.motor = MotorCortex() if MOTOR_ACTIVE else None
        
    def interact(self):
        os.system('clear')
        print(f"{BOLD}{PURPLE}╔══════════════════════════════════════════════════════════╗")
        print(f"║   🧠 L.E.A. // SYNC VOCALE ACTIVE (v1.5)                 ║")
        print(f"╚══════════════════════════════════════════════════════════╝{RESET}")
        
        while True:
            try:
                # 1. State
                entropy = self.senses.get_current_entropy()
                sec, creat, mood_str, mood_tag = self.limbic.modulate(entropy)
                print(f"\n> SENSORY: {entropy:.4f} | STATE: {mood_str}")
                
                # 2. Input
                user_input = input(f"{BOLD}OPERATOR >> {RESET}")
                if user_input.lower() in ['exit', 'quit', '4']: break
                
                # 3. Think
                response = self.cortex.process(user_input, mood_tag)
                
                # 4. Speak & Act (Motor)
                print(f"{PURPLE}LEA >> {RESET}{response}")
                if self.motor:
                    # C'EST ICI QUE LA VOIX EST ACTIVÉE
                    self.motor.speak_response(response, mood_tag)
                    action_log = self.motor.trigger_reflex(mood_tag)
                    if action_log: print(f"{RED}{action_log}{RESET}")

                # 5. Memorize
                if self.memory:
                    self.memory.store(user_input, "user", entropy, mood_tag)
                    self.memory.store(response, "lea", entropy, mood_tag)
                
            except KeyboardInterrupt: break

if __name__ == "__main__":
    LeaBrain().interact()