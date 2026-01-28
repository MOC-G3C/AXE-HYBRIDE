import os
import time
import sys

# --- COLORS & STYLING ---
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def check_path(path, name):
    sys.stdout.write(f"[*] Checking {name} ... ")
    if os.path.exists(path):
        print(f"{GREEN}ONLINE{RESET}")
        return True
    else:
        print(f"{RED}OFFLINE (Missing: {path}){RESET}")
        return False

def get_bio_status():
    path = "02_HUMAIN/BIO_CALIBRATION.md"
    if not os.path.exists(path):
        return "UNKNOWN"
    
    try:
        with open(path, 'r') as f:
            content = f.read().upper()
            if "OPTIMIZED" in content:
                return "OPTIMIZED"
            elif "DEPLETED" in content:
                return "DEPLETED"
            else:
                return "STABLE"
    except:
        return "ERROR"

def main():
    os.system('clear')
    print(f"{BOLD}{CYAN}")
    print("╔══════════════════════════════════════╗")
    print("║   AXE HYBRIDE // SYSTEM DIAGNOSTIC   ║")
    print("╚══════════════════════════════════════╝")
    print(f"{RESET}")
    time.sleep(0.5)

    # 1. ARCHITECTURE SCAN
    print(f"{BOLD}>> SCANNING NEURAL ARCHITECTURE...{RESET}")
    check_path("01_SOFTWARE", "Logic Core")
    check_path("02_HUMAIN", "Biological Anchor")
    check_path("03_HARDWARE", "Physical Interface")
    check_path("04_PHYSICS", "Simulation Engine")
    print("-" * 40)
    time.sleep(0.5)

    # 2. BIO-GUARD PROTOCOL
    print(f"{BOLD}>> INITIATING BIO-GUARD HANDSHAKE...{RESET}")
    status = get_bio_status()
    
    sys.stdout.write("OPERATOR STATUS: ")
    time.sleep(0.5)
    
    if status == "OPTIMIZED":
        print(f"{GREEN}{BOLD}✅ OPTIMIZED{RESET}")
        print(f"{GREEN}>> SYSTEM FULLY UNLOCKED. CREATIVITY MAXIMIZED.{RESET}")
    elif status == "DEPLETED":
        print(f"{RED}{BOLD}⚠️  DEPLETED{RESET}")
        print(f"{RED}>> SAFETY LOCKS ENGAGED. RECOVERY MODE ACTIVE.{RESET}")
    else:
        print(f"{YELLOW}{status}{RESET}")
        print(f"{YELLOW}>> STANDARD OPERATION.{RESET}")

    print("\n" + f"{CYAN}[DIAGNOSTIC COMPLETE]{RESET}")

if __name__ == "__main__":
    main()