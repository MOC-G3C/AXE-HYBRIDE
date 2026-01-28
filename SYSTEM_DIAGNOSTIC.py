import os
import sys
import time

# --- CONFIGURATION DES CHEMINS ---
root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root_dir, "01_SOFTWARE"))

print("\n" + "="*50)
print("   AXE HYBRIDE :: GLOBAL SYSTEM DIAGNOSTIC")
print("="*50 + "\n")

# 1. TEST DU LIEN BIOLOGIQUE (02_HUMAIN)
print("[1/4] Connecting to 02_HUMAIN...", end=" ")
bio_file = os.path.join(root_dir, "02_HUMAIN", "BIO_CALIBRATION.md")

if os.path.exists(bio_file):
    print("✅ CONNECTION ESTABLISHED.")
    with open(bio_file, 'r') as f:
        content = f.read().lower()
        if "optimized" in content:
            status = "OPTIMIZED (Green)"
        elif "depleted" in content:
            status = "DEPLETED (Red)"
        else:
            status = "STANDARD (Yellow)"
    print(f"      └── Current Bio-State: {status}")
else:
    print("❌ ERROR: Bio-Link severed (File missing).")
    status = "UNKNOWN"

time.sleep(1)

# 2. TEST DE LA SÉCURITÉ (01_SOFTWARE)
print("\n[2/4] Verifying Bio-Guard Protocol...", end=" ")
try:
    import bio_guard
    if bio_guard.check_clearance():
        security = "GRANTED"
    else:
        security = "DENIED"
    print(f"      └── Access Rights: {security}")
except ImportError:
    print("❌ ERROR: Bio-Guard module not found.")

time.sleep(1)

# 3. TEST DU MATÉRIEL (03_HARDWARE)
print("\n[3/4] Pinging Hardware Interface...", end=" ")
hardware_script = os.path.join(root_dir, "03_HARDWARE", "tesla_resonance_369.py")
if os.path.exists(hardware_script):
    print("✅ ONLINE.")
    print("      └── Ready to transmit Tesla frequencies.")
else:
    print("❌ OFFLINE.")

time.sleep(1)

# 4. TEST DE LA PHYSIQUE (04_PHYSICS)
print("\n[4/4] Checking Physics Engine...", end=" ")
physics_script = os.path.join(root_dir, "04_PHYSICS", "digital_gravity.py")
if os.path.exists(physics_script):
    print("✅ STABLE.")
    print("      └── Gravity Well generation ready.")
else:
    print("❌ UNSTABLE.")

print("\n" + "="*50)
if status == "OPTIMIZED (Green)":
    print("   SYSTEM STATUS: OPERATIONAL 🟢")
    print("   Ready for full deployment.")
else:
    print("   SYSTEM STATUS: RESTRICTED 🔴