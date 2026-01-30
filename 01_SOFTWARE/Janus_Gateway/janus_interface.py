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
        # RELATIVE PATHING: We are inside "01_SOFTWARE/Janus_Gateway"
        # Going up one level (..) takes us to "01_SOFTWARE"
        self.software_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.physics_root = os.path.abspath(os.path.join(self.software_root, '..', '04_PHYSICS'))

    def clear_screen(self):
        os.system('clear')

    def draw_banner(self):
        print(f"{BOLD}{CYAN}")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║        ⛩️  JANUS GATEWAY V2.0 // HYBRID NEXUS            ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print(f"{RESET}")

    def find_script(self, base_path, folder_hints, script_name):
        """
        Robust search for a script even if folder names change slightly
        (e.g., 'Project-Lambda' vs 'Project_Lambda')
        """
        for folder in folder_hints:
            # Try exact match first
            full_path = os.path.join(base_path, folder, script_name)
            if os.path.exists(full_path):
                return full_path
            
            # Try underscore/hyphen swap
            alt_folder = folder.replace("-", "_")
            full_path = os.path.join(base_path, alt_folder, script_name)
            if os.path.exists(full_path):
                return full_path
                
            alt_folder_2 = folder.replace("_", "-")
            full_path = os.path.join(base_path, alt_folder_2, script_name)
            if os.path.exists(full_path):
                return full_path
                
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
            
            print(f"\n{BOLD}--- GOVERNANCE LAYER ---{RESET}")
            print(f"  [3] ⚖️  {PURPLE}CONSULT ORACLE (Kybernetes Law){RESET}")
            
            print(f"\n{BOLD}--- PHYSICAL LAYER ---{RESET}")
            print(f"  [4] 🌌 {BLUE}LAUNCH GRAVITY ENGINE (Physics v1){RESET}")
            
            print(f"\n{BOLD}--- SYSTEM ---{RESET}")
            print("  [5] 💀 KILL SWITCH (Stop All)")
            print("  [6] 🚪 EXIT GATEWAY")
            print("\n" + "-"*60)
            
            choice = input(f"{YELLOW}>> AWAITING COMMAND: {RESET}")

            if choice == '1':
                # HEART
                heart = self.find_script(self.software_root, ["Kinetic-RNG"], "kinetic_pulse.py")
                self.launch_terminal(heart)
                time.sleep(1)
                # ZOO
                zoo = self.find_script(self.software_root, ["Entropic-Zoo-Protocol"], "evolution_engine.py")
                self.launch_terminal(zoo)
                input(f"\n{CYAN}[PRESS ENTER]{RESET}")

            elif choice == '2':
                sentinel = self.find_script(self.software_root, ["Project_Lambda", "Project-Lambda"], "decay_sentinel.py")
                if sentinel:
                    os.system(f"python3 \"{sentinel}\"")
                else:
                    print(f"{RED}Sentinel not found.{RESET}")
                input(f"\n{CYAN}[PRESS ENTER]{RESET}")

            elif choice == '3':
                oracle = self.find_script(self.software_root, ["Kybernetes-Governance"], "oracle_law.py")
                if oracle:
                    os.system(f"python3 \"{oracle}\"")
                else:
                    print(f"{RED}Oracle not found.{RESET}")
                input(f"\n{PURPLE}[PRESS ENTER]{RESET}")

            elif choice == '4':
                # PHYSICS is in 04_PHYSICS, which is a sibling of 01_SOFTWARE
                gravity = os.path.join(self.physics_root, "digital_gravity.py")
                self.launch_terminal(gravity)
                input(f"\n{BLUE}[PRESS ENTER]{RESET}")

            elif choice == '5':
                print(f"\n{RED}>> SHUTTING DOWN NEURAL LINKS...{RESET}")
                os.system("pkill -f kinetic_pulse.py")
                os.system("pkill -f evolution_engine.py")
                os.system("pkill -f digital_gravity.py")
                print(f"{RED}>> SILENCE RESTORED.{RESET}")
                time.sleep(1)

            elif choice == '6':
                print(">> DISCONNECTING.")
                break

if __name__ == "__main__":
    gateway = JanusGateway()
    gateway.main_menu()