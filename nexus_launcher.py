import os
import sys
import time

# UI COLORS
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
CYAN = '\033[96m'

def check_system(name, path):
    sys.stdout.write(f"checking {name}...")
    time.sleep(0.2)
    if os.path.exists(path):
        print(f" {GREEN}[OK]{RESET}")
        return True
    else:
        print(f" {RED}[MISSING]{RESET}")
        return False

def boot_sequence():
    os.system('clear')
    print(f"{CYAN}╔══════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║       L'AXE HYBRIDE - NEXUS V2.0         ║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════╝{RESET}")
    print("Initializing Biometric & Physical Consciousness...")
    time.sleep(1)
    
    # 1. SYSTEM DIAGNOSTIC (Checking 3-6-9 Pillars)
    print("\n--- SYSTEM DIAGNOSTIC ---")
    
    systems = [
        ("Kinetic Engine (Heart)", "01_SOFTWARE/Kinetic-RNG/heartbeat_data.json"),
        ("Turing Audio (Voice)", "03_HARDWARE/tesla_tone_generator.py"),
        ("Lambda Reflex (Action)", "01_SOFTWARE/Project_Lambda/reflex_engine.py"),
        ("Anamnesis (Memory)", "01_SOFTWARE/Project_Anamnesis/conscious_log.md"),
        ("Kybernetes (Brain)", "01_SOFTWARE/Kybernetes-Governance/neural_bridge.py"),
        ("Physics (Gravity)", "04_PHYSICS/gravity_density_engine.py"),
        ("Dashboard (Visual)", "01_SOFTWARE/Kybernetes-Governance/dashboard.py")
    ]
    
    all_ok = True
    for name, path in systems:
        if not check_system(name, path):
            all_ok = False
            
    if not all_ok:
        print(f"\n{RED}CRITICAL ERROR: System Incomplete.{RESET}")
        sys.exit(1)
        
    print(f"\n{GREEN}ALL SYSTEMS NOMINAL.{RESET}")
    time.sleep(1)
    
    # 2. LAUNCH OPTION
    print(f"\n[1] Launch Neural Bridge (Core)")
    print(f"[2] Launch Consciousness Dashboard")
    print(f"[3] Full Sync (Bridge + Dashboard)")
    
    choice = input(f"\n{YELLOW}Selection Protocol: {RESET}")
    
    if choice == "1":
        os.system(f"{sys.executable} 01_SOFTWARE/Kybernetes-Governance/neural_bridge.py")
    elif choice == "2":
        os.system(f"{sys.executable} 01_SOFTWARE/Kybernetes-Governance/dashboard.py")
    elif choice == "3":
        print(f"{CYAN}Starting Parallel Resonance...{RESET}")
        # Opens dashboard in a new terminal window (macOS)
        os.system(f"osascript -e 'tell app \"Terminal\" to do script \"cd {os.getcwd()} && python3 01_SOFTWARE/Kybernetes-Governance/dashboard.py\"'")
        os.system(f"{sys.executable} 01_SOFTWARE/Kybernetes-Governance/neural_bridge.py")

if __name__ == "__main__":
    try:
        boot_sequence()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Nexus Hibernation Active.{RESET}")