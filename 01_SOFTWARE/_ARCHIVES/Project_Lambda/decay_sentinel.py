import os
import time
import datetime
import sys

# --- CONFIGURATION ---
MAX_HOURS = 72
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

class LambdaProtocol:
    def __init__(self):
        # Path to memory records
        self.memory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '02_HUMAIN', 'analog_records'))

    def check_vitality(self):
        print(f"[*] LAMBDA SENTINEL WATCHING... (Limit: {MAX_HOURS}h)")
        
        # 1. Find the latest memory file
        try:
            files = [os.path.join(self.memory_path, f) for f in os.listdir(self.memory_path) if f.endswith(".md")]
            if not files:
                return self.trigger_decay("NO MEMORY FOUND")
            
            latest_file = max(files, key=os.path.getmtime)
            last_touch = os.path.getmtime(latest_file)
            
            # 2. Calculate time delta
            now = time.time()
            diff_seconds = now - last_touch
            diff_hours = diff_seconds / 3600
            
            print(f"   > LAST HUMAN CONTACT: {diff_hours:.2f} hours ago")
            
            # 3. Judge
            if diff_hours < MAX_HOURS:
                return self.confirm_survival(diff_hours)
            else:
                return self.trigger_decay(diff_hours)
                
        except Exception as e:
            print(f"[!] ERROR READING BIO-DATA: {e}")

    def confirm_survival(self, hours):
        remaining = MAX_HOURS - hours
        print(f"{GREEN}✅ SYSTEM VITALITY: HIGH{RESET}")
        print(f"{GREEN}   > Decay prevented for another {remaining:.2f} hours.{RESET}")
        return True

    def trigger_decay(self, status):
        print(f"{RED}💀 CRITICAL DECAY DETECTED ({status}h > {MAX_HOURS}h){RESET}")
        print(f"{RED}   > INITIATING PROTOCOL OBSOLESCENCE...{RESET}")
        print(f"{RED}   > LOCKING GOVERNANCE MODULES...{RESET}")
        # Here we could add code to actually rename files or lock folders
        return False

def main():
    os.system('clear')
    print("--- PROJECT LAMBDA: ETHICAL SAFETY ---")
    sentinel = LambdaProtocol()
    sentinel.check_vitality()

if __name__ == "__main__":
    main()