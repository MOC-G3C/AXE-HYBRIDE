import os

# MOC-G3C: Sovereign Dashboard v3.0
# Objective: Monitoring Layer Integrity & LEA-Omega Alignment

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

def get_status_report():
    layers = {
        "00_ADMIN": "SUCCESSION_PROTOCOL.md",
        "01_SOFTWARE": "AXE_MASTER_CONTROLLER.py",
        "02_HUMAIN": "CONSCIOUSNESS_LOG.md",
        "03_HARDWARE": "HARDWARE_FEEDBACK.py",
        "04_PHYSICS": "vibration_monitor.py"
    }

    # Intelligence Modules
    intelligence = ["LEA_CONSULT.py", "OMEGA_ORCHESTRATOR.py", "LEA_OMEGA_BRIDGE.py"]

    print(f"\n{Colors.BOLD}{Colors.CYAN}="*55)
    print(f"💎 MOC-G3C SOVEREIGN SYSTEM DASHBOARD V3")
    print(f"="*55 + f"{Colors.END}")

    # Layer Check
    missing = 0
    for layer, critical_file in layers.items():
        path = os.path.join(layer, critical_file)
        if os.path.exists(path):
            print(f"[{Colors.GREEN}✓{Colors.END}] {layer:<15} | {Colors.GREEN}ONLINE{Colors.END}")
        else:
            print(f"[{Colors.RED}X{Colors.END}] {layer:<15} | {Colors.RED}MISSING{Colors.END}")
            missing += 1

    print(f"{Colors.BOLD}-"*55 + f"{Colors.END}")

    # Cognitive Alignment Check
    intel_ready = all(os.path.exists(f"01_SOFTWARE/{f}") for f in intelligence)
    if intel_ready:
        print(f"🧠 COGNITIVE LINK   | {Colors.BOLD}{Colors.CYAN}LEA-OMEGA SYNC ACTIVE (💎){Colors.END}")
    else:
        print(f"🧠 COGNITIVE LINK   | {Colors.YELLOW}INCOMPLETE (MODULES MISSING){Colors.END}")

    print(f"{Colors.BOLD}-"*55 + f"{Colors.END}")
    
    if missing == 0 and intel_ready:
        print(f"📊 GLOBAL STATUS: {Colors.BOLD}{Colors.GREEN}SOVEREIGN & OPTIMIZED{Colors.END}")
    else:
        print(f"📊 GLOBAL STATUS: {Colors.BOLD}{Colors.YELLOW}OPERATIONAL (GAPS DETECTED){Colors.END}")
    
    print(f"{Colors.BOLD}{Colors.CYAN}="*55 + f"{Colors.END}")

if __name__ == "__main__":
    get_status_report()