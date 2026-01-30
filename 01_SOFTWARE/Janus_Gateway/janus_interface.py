import os
import sys
import time
import subprocess

# --- STYLING ---
CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
PURPLE = '\033[95m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

class JanusGateway:
    def __init__(self):
        # RELATIVE PATHING
        self.software_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.physics_root = os.path.abspath(os.path.join(self.software_root, '..', '04_PHYSICS'))

    def clear_screen(self):
        os.system('clear')

    def draw_banner(self):
        print(f"{BOLD}{CYAN}")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║      ⛩️  JANUS GATEWAY V2.1 // LEA INTEGRATION           ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print(f"{RESET}")

    def find_script(self, base_path, folder_hints, script_name):
        for folder in folder_hints:
            full_path = os.path.join(base_path, folder, script_name)
            if os.path.exists(full_path): return full_path
            
            # Try variations (- vs _)
            alt = folder.replace("-", "_")
            if os.path.exists(os.path.join(base_path, alt, script_name)):
                return os.path.join(base_path, alt, script_name)
        return None

    def launch_terminal(self, script_path):
        if script_path and os.path.exists(script_path):
            print(f"{GREEN}[*] LAUNCHING: {os.path.basename(script_path)}...{RESET}")
            cmd = f"""osascript -e 'tell application "Terminal" to do script "python3 \\"{script_path}\\""'"""
            os.system(cmd)
        else:
            print(f"{RED}[ERROR] Script not found.{RESET}")

    def main_menu(self):
        while True:
            self.clear_screen()
            self.draw_banner()
            print(f"{BOLD}--- BIOLOGICAL LAYER ---{RESET}")
            print("  [1] 🟢 ACTIVATE LIFE (Heart + Brain + Zoo)")
            print("  [2] 👁️  CHECK VITALITY (Lambda Sentinel)")
            
            print(f"\n{BOLD}--- COGNITIVE LAYER (NEW) ---{RESET}")
            print(f"  [3] 🧠 {PURPLE}CONNECT TO L.E.A. (Logical Emotive Agent){RESET}")
            print(f"  [4] ⚖️  CONSULT ORACLE (Kybernetes Law)")
            
            print(f"\n{BOLD}--- PHYSICAL LAYER ---{RESET}")
            print(f"  [5] 🌌 {BLUE}LAUNCH GRAVITY ENGINE (Physics v1){RESET}")
            
            print(f"\n{BOLD}--- SYSTEM ---{RESET}")
            print("  [6] 💀 KILL SWITCH (Stop All)")
            print("  [7] 🚪 EXIT GATEWAY")
            print("\n" + "-"*60)
            
            choice = input(f"{YELLOW}>> AWAITING COMMAND: {RESET}")

            if choice == '1':
                heart = self.find_script(self.software_root, ["Kinetic-RNG"], "kinetic_pulse.py")
                self.launch_terminal(heart)
                time.sleep(1)
                zoo = self.find_script(self.software_root, ["Entropic-Zoo-Protocol"], "evolution_engine.py")
                self.launch_terminal(zoo)
                input(f"\n{CYAN}[PRESS ENTER]{RESET}")

            elif choice == '2':
                sentinel = self.find_script(self.software_root, ["Project_Lambda"], "decay_sentinel.py")
                if sentinel: os.system(f"python3 \"{sentinel}\"")
                input(f"\n{CYAN}[PRESS ENTER]{RESET}")

            elif choice == '3':
                # LAUNCH LEA BRAIN DIRECTLY IN WINDOW
                lea = self.find_script(self.software_root, ["LEA_CORE"], "lea_brain.py")
                if lea:
                    os.system(f"python3 \"{lea}\"")
                else:
                    print(f"{RED}LEA CORE NOT DETECTED.{RESET}")
                    time.sleep(2)

            elif choice == '4':
                oracle = self.find_script(self.software_root, ["Kybernetes-Governance"], "oracle_law.py")
                if oracle: os.system(f"python3 \"{oracle}\"")
                input(f"\n{PURPLE}[PRESS ENTER]{RESET}")

            elif choice == '5':
                gravity = os.path.join(self.physics_root, "digital_gravity.py")
                self.launch_terminal(gravity)
                input(f"\n{BLUE}[PRESS ENTER]{RESET}")

            elif choice == '6':
                print(f"\n{RED}>> SHUTTING DOWN NEURAL LINKS...{RESET}")
                os.system("pkill -f kinetic_pulse.py")
                os.system("pkill -f evolution_engine.py")
                os.system("pkill -f digital_gravity.py")
                time.sleep(1)

            elif choice == '7':
                break

if __name__ == "__main__":
    gateway = JanusGateway()
    gateway.main_menu()