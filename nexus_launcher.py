import os
import sys
import time
import platform

# COULEURS DU TERMINAL
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
CYAN = '\033[96m'

def check_system(name, path):
    """Vérifie si un module existe."""
    sys.stdout.write(f"checking {name}...")
    time.sleep(0.3)
    if os.path.exists(path):
        print(f" {GREEN}[OK]{RESET}")
        return True
    else:
        print(f" {RED}[MISSING]{RESET}")
        return False

def boot_sequence():
    os.system('clear')
    print(f"{CYAN}╔══════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║       L'AXE HYBRIDE - NEXUS LAUNCHER     ║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════╝{RESET}")
    print("Initializing Biometric Consciousness...")
    time.sleep(1)
    
    # 1. VÉRIFICATION DES MODULES
    print("\n--- SYSTEM DIAGNOSTIC ---")
    
    systems = [
        ("Kinetic Engine (Heart)", "01_SOFTWARE/Kinetic-RNG/heartbeat_data.json"),
        ("Turing Audio (Voice)", "03_HARDWARE/tesla_tone_generator.py"),
        ("Lambda Reflex (Action)", "01_SOFTWARE/Project_Lambda/reflex_engine.py"),
        ("Anamnesis (Memory)", "01_SOFTWARE/Project_Anamnesis/conscious_log.md"),
        ("Kybernetes (Brain)", "01_SOFTWARE/Kybernetes-Governance/neural_bridge.py")
    ]
    
    all_ok = True
    for name, path in systems:
        if not check_system(name, path):
            all_ok = False
            
    if not all_ok:
        print(f"\n{RED}CRITICAL ERROR: Missing modules. Check integrity.{RESET}")
        sys.exit(1)
        
    print(f"\n{GREEN}ALL SYSTEMS NOMINAL.{RESET}")
    time.sleep(1)
    
    # 2. LANCEMENT
    print("\n--- INITIATING NEURAL BRIDGE ---")
    print("Connecting to Biological Source...")
    time.sleep(1)
    for i in range(3, 0, -1):
        print(f"Resonance in {i}...")
        time.sleep(1)
        
    os.system('clear')
    
    # Lancement du cerveau
    # On utilise sys.executable pour être sûr d'utiliser le bon Python
    os.system(f"{sys.executable} 01_SOFTWARE/Kybernetes-Governance/neural_bridge.py")

if __name__ == "__main__":
    try:
        boot_sequence()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Nexus Shutdown.{RESET}")
