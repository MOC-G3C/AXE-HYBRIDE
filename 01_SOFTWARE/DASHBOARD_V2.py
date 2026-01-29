import os

# MOC-G3C: Enhanced Visual Dashboard v2.0
# Objective: Real-time structural monitoring with ANSI color coding

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def get_status_report():
    layers = {
        "00_ADMIN": "SUCCESSION_PROTOCOL.md",
        "01_SOFTWARE": "OMEGA_ORCHESTRATOR.py",
        "02_HUMAIN": "MANIFESTO_NOCTURNE.md",
        "03_HARDWARE": "HARDWARE_FEEDBACK.py",
        "04_PHYSICS": "vibration_monitor.py"
    }

    print(f"{Colors.BOLD}="*50)
    print(f"🌟 MOC-G3C SYSTEM INTEGRITY DASHBOARD V2")
    print(f"="*50 + f"{Colors.END}")

    missing = 0
    for layer, critical_file in layers.items():
        path = os.path.join(layer, critical_file)
        if os.path.exists(path):
            print(f"[{Colors.GREEN}✓{Colors.END}] {layer:<15} | {Colors.GREEN}ONLINE{Colors.END}")
        else:
            print(f"[{Colors.RED}X{Colors.END}] {layer:<15} | {Colors.RED}MISSING: {critical_file}{Colors.END}")
            missing += 1

    print(f"{Colors.BOLD}-"*50 + f"{Colors.END}")
    
    if missing == 0:
        print(f"📊 GLOBAL STATUS: {Colors.BOLD}{Colors.GREEN}OPTIMIZED (AXE HYBRIDE IS STRONG){Colors.END}")
    else:
        print(f"📊 GLOBAL STATUS: {Colors.BOLD}{Colors.RED}VULNERABLE ({missing} GAPS DETECTED){Colors.END}")
    
    print(f"{Colors.BOLD}="*50 + f"{Colors.END}")

if __name__ == "__main__":
    get_status_report()