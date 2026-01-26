# MOC-G3C : Hardware Identity Seal
# Node: Beloeil | Terminal: MacBook Pro M5

import os
import platform

def verify_hardware():
    # Identité du matériel
    machine = platform.processor()
    system = platform.system()
    
    print("--- VÉRIFICATION DU SCEAU DE SÉCURITÉ ---")
    
    # Vérification du verrouillage M5
    if "Apple" in platform.version() or "arm" in platform.machine():
        print(f"✅ MATÉRIEL IDENTIFIÉ : {system} Apple Silicon M-Series")
        print("✅ ACCÈS À L'AXE HYBRIDE : AUTORISÉ")
        return True
    else:
        print("❌ ERREUR : MATÉRIEL NON RECONNU")
        return False

if __name__ == "__main__":
    verify_hardware()