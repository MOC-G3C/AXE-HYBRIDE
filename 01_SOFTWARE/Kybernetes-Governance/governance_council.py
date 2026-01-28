import sys
import os
import time

# --- PONT VERS LE BIO-GUARD ---
# On remonte de deux niveaux pour trouver bio_guard.py dans 01_SOFTWARE
current_dir = os.path.dirname(os.path.abspath(__file__))
software_root = os.path.join(current_dir, "..")
sys.path.append(software_root)

try:
    import bio_guard
except ImportError:
    print("⚠️  CRITICAL: Bio-Guard module missing. Governance suspended.")
    sys.exit(1)

# --- LE CONSEIL DE GOUVERNANCE ---
def open_council_session():
    print("🏛️  Kybernetes Council: Session Opening...")
    print("    Verifying Supreme Leader's Biological Integrity...")

    # 1. VÉRIFICATION BIOLOGIQUE
    if not bio_guard.check_clearance():
        print("\n⚖️  VETO AUTOMATIQUE :")
        print("    L'état biologique 'DEPLETED' interdit toute réforme.")
        print("    Le système passe en mode : CONSERVATION (Read-Only).")
        return

    # 2. Si l'accès est autorisé (Optimized)
    print("\n✅  Quorum Reached. The Council is listening.")
    print("    Mode: CONSTITUTIONAL AMENDMENT (Write Access)")
    
    decisions = [
        "Protocol 7: Expand Neural Network",
        "Protocol 12: Allocate more CPU to Creativity",
        "Protocol 99: Merge Organic & Digital Memories"
    ]
    
    for decision in decisions:
        print(f"    [Vote] Ratifying {decision}... APPROVED")
        time.sleep(1)
        
    print("\n📜  Session Adjourned. New laws are active.")

if __name__ == "__main__":
    open_council_session()