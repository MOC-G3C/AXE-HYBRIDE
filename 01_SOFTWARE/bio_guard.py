import os
import sys

# Configuration intelligente des chemins (Relatif)
# Permet de remonter vers 02_HUMAIN peu importe le nom du dossier racine
current_dir = os.path.dirname(os.path.abspath(__file__))
BIO_PATH = os.path.join(current_dir, "..", "02_HUMAIN", "BIO_CALIBRATION.md")

def check_clearance():
    """Checks the admin's biological state before authorizing software execution."""
    print("🔒 Bio-Guard: Verifying Admin Vital Signs...")
    
    try:
        with open(BIO_PATH, 'r') as f:
            content = f.read().lower()
            
        if "depleted" in content:
            print("\n" + "="*40)
            print("⛔ ACCESS DENIED / RESTRICTED")
            print("⚠️  Alert: Biological state is DEPLETED.")
            print("   Risk of syntax errors/bugs is > 80%.")
            print("   Action: Go to sleep or switch to 03_HARDWARE tasks.")
            print("="*40 + "\n")
            return False
            
        elif "optimized" in content:
            print("✅ Access Granted: Biological state OPTIMIZED.")
            print("   Cognitive capacity is peak. Good luck.")
            return True
            
        else:
            print("ℹ️  Caution: Biological state is STANDARD.")
            return True
            
    except FileNotFoundError:
        print(f"⚠️ Warning: Could not find Bio-Calibration at {BIO_PATH}")
        return True # On laisse passer par défaut si le fichier manque

if __name__ == "__main__":
    # Test direct du script
    if check_clearance():
        print("🚀 System Launch Sequence Initiated...")
    else:
        sys.exit(1)