import os
import sys
import time
import subprocess

# --- STYLING ---
CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

class JanusGateway:
    def __init__(self):
        self.processes = []
        # GPS FIX: We are in "01_SOFTWARE/Janus Gateway"
        # Going up one level (..) takes us to "01_SOFTWARE"
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
        # Path is relative to 01_SOFTWARE. Ex: "Kinetic-RNG/kinetic_pulse.py"
        full_path = os.path.join(self.root_software, path)
        
        # FIX: Handle folder name mismatches (Space vs Underscore vs Hyphen)
        # If "Project-Lambda" fails, try "Project_Lambda"
        if not os.path.exists(full_path):
            alternative = full_path.replace("-", "_")
            if os.path.exists(alternative):
                full_path = alternative
        
        if not os.path.exists(full_path):
            print(f"{RED}[ERROR] Module path not found: {full_path}{RESET}")
            return

        print(f"{GREEN}[*] INITIALIZING {name}...{RESET}")
        time.sleep(0.5)

        # Launch in new Terminal window (MacOS)
        # We use quotes around path to handle spaces in folder names
        cmd = f"""osascript -e 'tell application "Terminal" to do script "python3 \\"{full_path}\\""'"""
        os.system(cmd)

    def main_menu(self):
        while True:
            self.clear_screen()
            self.draw_banner()
            print("  [1] 🟢 ACTIVATE SYSTEM (Heart + Brain + Zoo)")
            print("  [2] 👁️  CHECK VITALITY (Lambda Sentinel)")
            print("  [3] 💀 KILL SWITCH (Stop All)")
            print("  [4] 🚪 EXIT GATEWAY")
            print("\n" + "-"*60)
            
            choice = input(f"{YELLOW}>> AWAITING COMMAND: {RESET}")

            if choice == '1':
                print(f"\n{BOLD}>> INITIATING HYBRID SYNCHRONIZATION...{RESET}")
                # 1. Heartbeat
                self.launch_module("Kinetic-RNG/kinetic_pulse.py", "KINETIC HEART")
                time.sleep(1)
                # 2. Zoo
                self.launch_module("Entropic-Zoo-Protocol/evolution_engine.py", "ENTROPIC ZOO")
                input(f"\n{CYAN}[PRESS ENTER TO RETURN TO MENU]{RESET}")

            elif choice == '2':
                print(f"\n{BOLD}>> SCANNING MEMORY BANKS...{RESET}")
                # For the sentinel, we run it directly in this window
                sentinel_path = os.path.join(self.root_software, "Project_Lambda/decay_sentinel.py")
                # Fix path if needed
                if not os.path.exists(sentinel_path):
                    sentinel_path = sentinel_path.replace("-", "_")
                
                os.system(f"python3 \"{sentinel_path}\"")
                input(f"\n{CYAN}[PRESS ENTER TO RETURN TO MENU]{RESET}")

            elif choice == '3':
                print(f"\n{RED}>> SHUTTING DOWN NEURAL LINKS...{RESET}")
                os.system("pkill -f kinetic_pulse.py")
                os.system("pkill -f evolution_engine.py")
                print(f"{RED}>> SILENCE RESTORED.{RESET}")
                time.sleep(2)

            elif choice == '4':
                print(">> DISCONNECTING.")
                break

if __name__ == "__main__":
    gateway = JanusGateway()
    gateway.main_menu()