import os
import time
import sys

# --- CONFIGURATION ---
SYSTEM_NAME = "NEXUS LAUNCHER // AXE HYBRIDE"
VERSION = "2.0.1 (God Mode)"

def clear_screen():
    os.system('clear')

def print_banner():
    clear_screen()
    print("==================================================")
    print(f"   {SYSTEM_NAME}")
    print(f"   Version: {VERSION}")
    print("   Operator: MOC-G3C")
    print("==================================================\n")

def main_menu():
    while True:
        print_banner()
        print("SELECT PROTOCOL TO INITIATE:")
        print("1. [DIAGNOSTIC]  Check System Integrity")
        print("2. [ENGINE]      Start Vortex Math (3-6-9)")
        print("3. [PHYSICS]     Activate Gravity Bridge (Zero Point)")
        print("4. [ZOO]         Enter Entropic Zoo (Chaos)")
        print("Q. [QUIT]        Decouple from Simulation")
        
        choice = input("\nCOMMAND > ").upper()
        
        if choice == '1':
            os.system("python3 SYSTEM_DIAGNOSTIC.py")
            input("\nPress Enter to return...")
            
        elif choice == '2':
            print("\n>>> INITIALIZING TURING-LANDAU ENGINE...")
            time.sleep(1)
            path = "01_SOFTWARE/Turing-Landau-Protocol/01_Core/VORTEX_MATH_ENGINE.py"
            os.system(f"python3 {path}")
            
        elif choice == '3':
            print("\n>>> CONNECTING TO GRAVITY FIELD...")
            time.sleep(1)
            path = "04_PHYSICS/digital_gravity.py"
            os.system(f"python3 {path}")
            
        elif choice == '4':
            print("\n>>> WARNING: ENTERING CHAOS ZONE...")
            time.sleep(1)
            print("Listing Active Species in Enclosures...")
            os.system("ls -R 01_SOFTWARE/Entropic-Zoo-Protocol/02_Data")
            input("\nObservation Complete. Press Enter to return...")

        elif choice == 'Q':
            print("\nShutting down Nexus...")
            time.sleep(1)
            clear_screen()
            sys.exit()
        
        else:
            print("\nINVALID COMMAND.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
