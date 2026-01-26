import os
import sys
import time

# Add paths for internal modules
sys.path.append(os.path.abspath("01_SOFTWARE/Entropic-Zoo-Protocol"))

# Import the Analyzer
try:
    import zoo_analyzer
except ImportError:
    zoo_analyzer = None

# UI COLORS
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
CYAN = '\033[96m'

def boot_sequence():
    os.system('clear')
    print(f"{CYAN}╔══════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║       L'AXE HYBRIDE - NEXUS V3.0         ║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════╝{RESET}")
    
    # 1. BIOMETRIC REFLECTION (The "Self-Aware" step)
    print(f"\n{YELLOW}--- BIOMETRIC REFLECTION ---{RESET}")
    if zoo_analyzer:
        zoo_analyzer.analyze_zoo()
    else:
        print(f"{RED}[ERROR] Zoo Analyzer unreachable.{RESET}")
    
    time.sleep(2)
    
    # 2. SYSTEM DIAGNOSTIC
    print(f"\n{YELLOW}--- READINESS CHECK ---{RESET}")
    # (Checking core files)
    all_ok = True
    for path in ["01_SOFTWARE/Kybernetes-Governance/neural_bridge.py", "01_SOFTWARE/Project_Anamnesis/conscious_log.md"]:
        if os.path.exists(path):
            print(f"Checking {path}... {GREEN}[OK]{RESET}")
        else:
            print(f"Checking {path}... {RED}[MISSING]{RESET}")
            all_ok = False
            
    if not all_ok:
        sys.exit(1)

    # 3. LAUNCH
    print(f"\n{GREEN}INITIALIZATION COMPLETE. READY FOR RESONANCE.{RESET}")
    input(f"\nPress Enter to bridge the Biometric Gap...")
    
    os.system(f"{sys.executable} 01_SOFTWARE/Kybernetes-Governance/neural_bridge.py")

if __name__ == "__main__":
    try:
        boot_sequence()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Nexus Hibernation Active.{RESET}")