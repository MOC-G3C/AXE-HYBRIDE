import os
import time
import sys
import subprocess

# --- CONFIGURATION ---
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
KINETIC_PATH = os.path.join(ROOT_DIR, "01_SOFTWARE", "Kinetic-RNG", "kinetic_pulse.py")
JANUS_PATH = os.path.join(ROOT_DIR, "01_SOFTWARE", "Janus_Gateway", "janus_interface.py")

# Couleurs
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

def launch_terminal(script_path):
    """Ouvre une fenêtre Terminal via AppleScript (Correction Guillemets)"""
    if not os.path.exists(script_path):
        print(f"{RED}[ERROR] Introuvable: {script_path}{RESET}")
        return False
        
    # CORRECTION ICI: On utilise des apostrophes simples (') autour du chemin
    # Cela évite le conflit avec les guillemets doubles (") d'AppleScript
    cmd = f"python3 '{script_path}'"
    
    apple_script = f'''
    tell application "Terminal"
        do script "{cmd}"
        activate
    end tell
    '''
    
    try:
        # On lance la commande sans attendre de retour complexe
        subprocess.run(["osascript", "-e", apple_script], check=True)
        return True
    except Exception as e:
        print(f"{RED}[FAIL] Erreur AppleScript: {e}{RESET}")
        return False

def main():
    os.system('clear')
    print(f"{BOLD}{GREEN}")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║           🧬  PROJECT GENESIS // INITIALIZATION          ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(f"{RESET}")
    
    print("Initializing Neural Link...")
    time.sleep(1)
    
    # 1. Démarrer le Cœur
    print(f">> Waking up {RED}KINETIC HEART{RESET}...")
    if launch_terminal(KINETIC_PATH):
        print(f"{GREEN}[OK] Heart Started.{RESET}")
    else:
        print(f"{RED}[FAIL] Heart failure.{RESET}")
    
    time.sleep(2) 
    
    # 2. Démarrer le Cerveau
    print(f">> Waking up {GREEN}JANUS GATEWAY{RESET}...")
    if launch_terminal(JANUS_PATH):
        print(f"{GREEN}[OK] Brain Connected.{RESET}")
    else:
        print(f"{RED}[FAIL] Brain failure.{RESET}")
    
    print("\n" + "-"*60)
    print(f"{BOLD}SYSTEM ALIVE.{RESET}")
    print("-"*60 + "\n")

if __name__ == "__main__":
    main()