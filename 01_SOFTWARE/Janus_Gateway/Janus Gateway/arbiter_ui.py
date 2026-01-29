import sys
import os
try:
    from sync_memory import MemoryGovernor
except ImportError:
    print("[ERROR] sync_memory.py not found. Please ensure both files are in the same folder.")
    sys.exit(1)

# ==========================================
# MOC-G3C ARBITER CONTROL PANEL [ms]
# Arbiter: Marc-Olivier Corbin
# Protocol: Turing-Landau v1.2
# ==========================================

def main():
    try:
        gov = MemoryGovernor()
        print("\n" + "="*45)
        print("   MOC-G3C ARBITER CONTROL PANEL [ms]")
        print(f"   Location: {gov.memory['system_integrity']['location_anchor']}")
        print(f"   Status: SOUVEREIGNTY ACTIVE")
        print("="*45)
        
        print("\n[1] Etch a New Memory Scar (ms)")
        print("[2] Run 3-6-9 Tesla Audit (ms)")
        print("[3] View Identity Scars")
        print("[4] Exit")
        
        choice = input("\nSelect action: ")
        
        if choice == "1":
            print("\n--- NEW STABLE TRUTH [ms] ---")
            concept = input("Concept name: ")
            definition = input("Simple definition: ")
            gov.add_scar(concept, definition)
            gov.save()
            print(f"\n[SUCCESS] '{concept}' etched permanently.")
            
        elif choice == "2":
            print("\n--- 3-6-9 TESLA AUDIT [ms] ---")
            try:
                e3 = float(input("Energy (3) [1-9]: "))
                f6 = float(input("Frequency (6) [1-9]: "))
                v9 = float(input("Vibration (9) [1-9]: "))
                gov.update_tesla_audit(e3, f6, v9)
                gov.save()
                score = gov.memory['tesla_constants']['last_audit_score']
                status = "VALIDATED" if score >= 6.0 else "REJECTED"
                print(f"\n[AUDIT] Score: {score} | Status: {status}")
            except ValueError:
                print("\n[ERROR] Numbers only for the audit.")
                
        elif choice == "3":
            print("\n--- IDENTITY SCARS ---")
            scars = gov.memory.get("identity_scars", [])
            if not scars:
                print("No scars found.")
            for scar in scars:
                print(f"- {scar['concept']}: {scar['definition']}")
                
        else:
            sys.exit()

    except Exception as e:
        print(f"\n[CRITICAL ERROR] {e}")

if __name__ == "__main__":
    main()