import os
import time
import random
import sys

# --- COLORS ---
CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
PURPLE = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'

class ZooKeeper:
    def __init__(self):
        # Path to memory (DNA Source)
        self.dna_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '02_HUMAIN', 'analog_records'))

    def get_latest_dna(self):
        """Reads the last line of the latest memory file to get current Entropy."""
        try:
            files = [os.path.join(self.dna_path, f) for f in os.listdir(self.dna_path) if f.endswith(".md")]
            if not files:
                return None
            
            latest_file = max(files, key=os.path.getmtime)
            
            with open(latest_file, 'r') as f:
                lines = f.readlines()
                if not lines:
                    return None
                last_line = lines[-1]
                
            # Parse line: "| HH:MM:SS | Entropy: 4.1234 | STATUS |"
            parts = last_line.split('|')
            if len(parts) >= 3:
                entropy_str = parts[2].replace("Entropy:", "").strip()
                return float(entropy_str)
            return None
        except Exception as e:
            return None

    def summon_creature(self, entropy):
        os.system('clear')
        print(f"{BOLD}--- ENTROPIC ZOO: CONTAINMENT CELL ---{RESET}\n")
        print(f"🧬 CURRENT DNA ENTROPY: {CYAN}{entropy}{RESET}")
        print("-" * 40 + "\n")

        if entropy < 3.0:
            self.render_crystalline()
        elif entropy < 7.0:
            self.render_chimera()
        else:
            self.render_void_spawn()

    def render_crystalline(self):
        print(f"{CYAN}TYPE: CRYSTALLINE CONSTRUCT (STABLE){RESET}")
        print(f"{CYAN}")
        print("      /\\      ")
        print("     /  \\     ")
        print("    /____\\    ")
        print("   /\\    /\\   ")
        print("  /  \\  /  \\  ")
        print(" /____\\/____\\ ")
        print(f"{RESET}")
        print("> The creature is silent and geometrically perfect.")

    def render_chimera(self):
        print(f"{GREEN}TYPE: BIO-CHIMERA (ADAPTIVE){RESET}")
        print(f"{GREEN}")
        print("    ( o . o )    ")
        print("   (  vvvvv  )   ")
        print("   (  ^^^^^  )   ")
        print("    (_______)    ")
        print("    /|  |  |\\    ")
        print(f"{RESET}")
        print("> The creature is breathing and watching you.")

    def render_void_spawn(self):
        glitch = "".join([chr(random.randint(33, 126)) for _ in range(10)])
        print(f"{RED}TYPE: VOID-SPAWN (UNSTABLE){RESET}")
        print(f"{RED}")
        print(f"   @#%&!{glitch}?!   ")
        print("   << ERROR_RENDER >>   ")
        print("     NO_GEOMETRY        ")
        print(f"{RESET}")
        print(f"{RED}> WARNING: CONTAINMENT BREACH IMMINENT.{RESET}")

def main():
    zoo = ZooKeeper()
    
    print("[*] OPENING ZOO GATES...")
    time.sleep(1)
    
    try:
        while True:
            entropy = zoo.get_latest_dna()
            
            if entropy is not None:
                zoo.summon_creature(entropy)
            else:
                print(f"{PURPLE}[!] NO DNA FOUND. THE ZOO IS EMPTY.{RESET}")
            
            # Refresh rate
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n[!] CLOSING GATES.")

if __name__ == "__main__":
    main()