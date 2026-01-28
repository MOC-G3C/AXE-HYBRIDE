import os
import sys
import time
import subprocess
import threading

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
        self.root_software = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '01_SOFTWARE'))

    def clear_screen(self):
        os.system('clear')

    def draw_banner(self):
        print(f"{BOLD}{CYAN}")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║          ⛩️  JANUS GATEWAY // HYBRID INTERFACE           ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print(f"{RESET}")

    def launch_module(self, path, name, new_window=True):
        full_path = os.path.join(self.root_software, path)
        
        if not os.path.exists(full_path):
            print(f"{RED}[ERROR] Module not found: {name}{RESET}")
            return

        print(f"{GREEN}[*] INITIALIZING {name}...{RESET}")
        time.sleep(0.5)

        # MacOS specific: launch in new Terminal window
        if new_window:
            cmd = f"""osascript -e 'tell application "Terminal" to do script "python3 \\"{full_path}\\""'"""
            os.system(cmd)
        else:
            # Run in background (silent)
            p = subprocess.Popen(["python3", full_path])
            self.processes.append(p)

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
                # Launch Sequence
                print(f"\n{BOLD}>> INITIATING HYBRID SYNCHRONIZATION...{RESET}")
                # 1. Heartbeat (Kinetic)
                self.launch_module("Kinetic-RNG/kinetic_pulse.py", "KINETIC HEART")
                time.sleep(1)
                # 2. Zoo (Visualization)
                self.launch_module("Entropic-Zoo-Protocol/evolution_engine.py", "ENTROPIC ZOO")
                input(f"\n{CYAN}[PRESS ENTER TO RETURN TO MENU]{RESET}")

            elif choice == '2':
                # Security Check
                print(f"\n{BOLD}>> SCANNING MEMORY BANKS...{RESET}")
                os.system(f"python3 \"{os.path.join(self.root_software, 'Project_Lambda/decay_sentinel.py')}\"")
                input(f"\n{CYAN}[PRESS ENTER TO RETURN TO MENU]{RESET}")

            elif choice == '3':
                print(f"\n{RED}>> SHUTTING DOWN NEURAL LINKS...{RESET}")
                # Kills all python processes (Forceful reset)
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