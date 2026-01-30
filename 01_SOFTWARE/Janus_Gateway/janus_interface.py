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
RESET = '\033[0m'
BOLD = '\033[1m'

class JanusGateway:
    def __init__(self):
        self.processes = []
        # GPS: We are in "01_SOFTWARE/Janus Gateway"
        # Root software is one level up
        self.root_software = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    def clear_screen(self):
        os.system('clear')

    def draw_banner(self):
        print(f"{BOLD}{CYAN}")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║          ⛩️  JANUS GATEWAY // HYBRID INTERFACE           ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print(f"{RESET}")

    def launch_module(self, path, name):
        full_path = os.path.join(self.root_software, path)
        
        # FIX: Path resilience (Space/Underscore/Hyphen)
        if not os.path.exists(full_path):
            alternative = full_path.replace("-", "_")
            if os.path.exists(alternative):
                full_path = alternative
        
        if not os.path.exists(full_path):
            print(f"{RED}[ERROR] Module path not found: {full_path}{RESET}")
            return

        print(f"{GREEN}[*] INITIALIZING {name}...{RESET}")
        time.sleep(0.5)
        
        # MacOS Launch Command
        cmd = f"""osascript -e 'tell application "Terminal" to do script "python3 \\"{full_path}\\""'"""
        os.system(cmd)

    def run_oracle(self):
        """Runs the Oracle directly in the Gateway window"""
        print(f"\n{BOLD}>> SUMMONING THE COUNCIL...{RESET}")
        time.sleep(1)
        oracle_path = os.path.join(self.root_software, "Kybernetes-Governance/oracle_law.py")
        
        if not os.path.exists(oracle_path):
             oracle_path = oracle_path.replace("-", "_") # Try underscore if hyphen fails
             
        os.system(f"python3 \"{oracle_path}\"")
        input(f"\n{PURPLE}[PRESS ENTER TO DISMISS THE COUNCIL]{RESET}")

    def main_menu(self):
        while True:
            self.clear_screen()
            self.draw_banner()
            print("  [1] 🟢 ACTIVATE SYSTEM (Heart + Brain + Zoo)")
            print("  [2] 👁️  CHECK VITALITY (Lambda Sentinel)")
            print(f"  [3] ⚖️  {PURPLE}CONSULT ORACLE (Kybernetes Law){RESET}")
            print("  [4] 💀 KILL SWITCH (Stop All)")
            print("  [5] 🚪 EXIT GATEWAY")
            print("\n" + "-"*60)
            
            choice = input(f"{YELLOW}>> AWAITING COMMAND: {RESET}")

            if choice == '1':
                print(f"\n{BOLD}>> INITIATING HYBRID SYNCHRONIZATION...{RESET}")
                self.launch_module("Kinetic-RNG/kinetic_pulse.py", "KINETIC HEART")
                time.sleep(1)
                self.launch_module("Entropic-Zoo-Protocol/evolution_engine.py", "ENTROPIC ZOO")
                input(f"\n{CYAN}[PRESS ENTER TO RETURN TO MENU]{RESET}")

            elif choice == '2':
                print(f"\n{BOLD}>> SCANNING MEMORY BANKS...{RESET}")
                sentinel_path = os.path.join(self.root_software, "Project_Lambda/decay_sentinel.py")
                # Path fix logic
                if not os.path.exists(sentinel_path): sentinel_path = sentinel_path.replace("-", "_")
                os.system(f"python3 \"{sentinel_path}\"")
                input(f"\n{CYAN}[PRESS ENTER TO RETURN TO MENU]{RESET}")

            elif choice == '3':
                self.run_oracle()

            elif choice == '4':
                print(f"\n{RED}>> SHUTTING DOWN NEURAL LINKS...{RESET}")
                os.system("pkill -f kinetic_pulse.py")
                os.system("pkill -f evolution_engine.py")
                print(f"{RED}>> SILENCE RESTORED.{RESET}")
                time.sleep(1)

            elif choice == '5':
                print(">> DISCONNECTING.")
                break

if __name__ == "__main__":
    gateway = JanusGateway()
    gateway.main_menu()