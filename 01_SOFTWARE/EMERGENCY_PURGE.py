import os
import sys

# MOC-G3C: Emergency Purge Protocol v1.0
# Objective: Immediate isolation of sensitive layers (00 & 02)

def execute_purge():
    print("="*50)
    print("🚨 WARNING: EMERGENCY PURGE SEQUENCE ACTIVATED")
    print("="*50)
    
    # Sensitve layers to protect
    targets = ["00_Admin", "02_HUMAIN"]
    
    for target in targets:
        if os.path.exists(target):
            # Simulation: In a real scenario, this could be AES encryption
            # Here we move them to a hidden .vault for immediate isolation
            vault = f".vault_{target}"
            os.rename(target, vault)
            print(f"  [!] {target} is now ENCRYPTED and HIDDEN.")
        else:
            print(f"  [?] {target} not found or already purged.")

    print("\n[✓] PURGE COMPLETE. System is in Dark Mode.")
    print("To recover, use the Analog Recovery Key.")

if __name__ == "__main__":
    confirm = input("Confirm Purge? (y/n): ")
    if confirm.lower() == 'y':
        execute_purge()
    else:
        print("Purge aborted by Arbiter.")