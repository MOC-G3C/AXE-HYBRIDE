import os
import sys

# MOC-G3C System Health Monitor v1.0
# Objective: Structural Integrity Verification

def check_structure():
    layers = {
        "00_Admin": ["CORE_ARCHITECTURE.md", "ROADMAP_2026.md", "SUCCESSION_PROTOCOL.md"],
        "01_SOFTWARE": ["SYSTEM_STATUS.py", "Janus_Gateway/TESTS_PHASE_2.md"],
        "02_HUMAIN": ["00_Meta_Protocol/SUCCESSION_PROTOCOL.md"],
        "03_HARDWARE": [],
        "04_PHYSICS": []
    }
    
    print("="*40)
    print("🌟 MOC-G3C SYSTEM HEALTH REPORT")
    print("="*40)
    
    total_files = 0
    missing_files = 0

    for layer, files in layers.items():
        print(f"\n📂 Layer: {layer}")
        if os.path.exists(layer):
            print("  [✓] Directory exists")
            for f in files:
                f_path = os.path.join(layer, f)
                if os.path.exists(f_path):
                    print(f"  [✓] File: {f}")
                    total_files += 1
                else:
                    print(f"  [X] Missing: {f}")
                    missing_files += 1
        else:
            print(f"  [X] Directory {layer} NOT FOUND")

    print("\n" + "="*40)
    print(f"📊 SUMMARY:")
    print(f"   Files Verified: {total_files}")
    print(f"   Critical Gaps: {missing_files}")
    if missing_files == 0:
        print("   STATUS: OPTIMIZED (Axe Hybride is Strong)")
    else:
        print("   STATUS: VULNERABLE (Check missing protocols)")
    print("="*40)

if __name__ == "__main__":
    check_structure()