import os

# MOC-G3C: Recovery Protocol v1.0
# Objective: Restore hidden layers (00 & 02) from the vault.

def execute_recovery(key):
    # This is your "Analog Recovery Key"
    SECRET_KEY = "369" 
    
    if key != SECRET_KEY:
        print("❌ ACCESS DENIED: Invalid Recovery Key.")
        return

    print("="*50)
    print("🔓 RECOVERY SEQUENCE INITIATED")
    print("="*50)
    
    targets = ["00_Admin", "02_HUMAIN"]
    
    for target in targets:
        vault = f".vault_{target}"
        if os.path.exists(vault):
            os.rename(vault, target)
            print(f"  [✓] {target} has been RESTORED.")
        else:
            print(f"  [?] No vault found for {target}.")

    print("\n[✓] SYSTEM RECONSTITUTED. All layers are now visible.")

if __name__ == "__main__":
    print("--- MOC-G3C ANALOG RECOVERY ---")
    user_key = input("Enter Recovery Key: ")
    execute_recovery(user_key)