import os
import sys
from datetime import datetime

# --- CONFIGURATION DU SYSTÈME ---
SYSTEM_NAME = "MOC-G3C / AXE HYBRIDE"
VERSION = "2.0 (Protocol Era)"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Nouveaux Chemins des Protocoles
PROTOCOLS = {
    "GOVERNANCE": os.path.join(ROOT_DIR, "01_SOFTWARE", "Kybernetes-Governance"),
    "CHAOS_ZOO":  os.path.join(ROOT_DIR, "01_SOFTWARE", "Entropic-Zoo-Protocol"),
    "ENGINE":     os.path.join(ROOT_DIR, "01_SOFTWARE", "Turing-Landau-Protocol"),
    "PHYSICS":    os.path.join(ROOT_DIR, "04_PHYSICS"),
    "HARDWARE":   os.path.join(ROOT_DIR, "03_HARDWARE"),
    "HUMAN":      os.path.join(ROOT_DIR, "02_HUMAIN")
}

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def check_integrity():
    print(f"\n--- INITIALIZING {SYSTEM_NAME} DIAGNOSTIC ---\n")
    all_systems_go = True
    
    for name, path in PROTOCOLS.items():
        if os.path.exists(path):
            # Compte les fichiers dans le module
            file_count = sum([len(files) for r, d, files in os.walk(path)])
            log(f"✅ MODULE [{name}] DETECTED. Files: {file_count}")
        else:
            log(f"❌ MODULE [{name}] MISSING at {path}")
            all_systems_go = False
            
    print("\n-------------------------------------------------")
    if all_systems_go:
        log("SYSTEM STATUS: NOMINAL. READY FOR EVOLUTION.")
    else:
        log("SYSTEM STATUS: CRITICAL. ARCHITECTURE MISMATCH.")
    print("-------------------------------------------------\n")

if __name__ == "__main__":
    check_integrity()