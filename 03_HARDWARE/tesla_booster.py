import time
import sys
import os
import random

# --- STYLING ---
RED = '\033[91m'
YELLOW = '\033[93m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'

def visual_overload():
    os.system('clear')
    print(f"{RED}{BOLD}")
    print("!!! WARNING: TESLA COIL OVERLOAD INITIATED !!!")
    print("!!! VOLTAGE SPIKE DETECTED: 50,000V !!!")
    print(f"{RESET}")
    time.sleep(1)

    # Simulation de montée en charge
    try:
        for i in range(10, 110, 5):
            bar = "█" * (i // 2)
            color = YELLOW if i < 80 else RED
            print(f"{color}CHARGE: [{bar:<50}] {i}%{RESET}")
            time.sleep(0.05)
            # Effet de tremblement
            if i > 80:
                offset = " " * random.randint(0, 5)
                print(f"{RED}{offset}>>> CRITICAL RESONANCE <<< {RESET}")

        # L'EXPLOSION VISUELLE
        print(f"\n{WHITE}{BOLD}")
        print("⚡⚡⚡ DISCHARGE SEQUENCE ACTIVE ⚡⚡⚡")
        print(f"{RESET}{RED}")
        
        patterns = [
            "/\\/\\/\\/\\/\\ HIGH VOLTAGE /\\/\\/\\/\\/\\",
            "*** SYSTEM INSTABILITY ***",
            "--- MAGNETIC FIELD COLLAPSE ---",
            "!!! DANGER !!!"
        ]
        
        start_time = time.time()
        while time.time() - start_time < 5:  # Dure 5 secondes
            p = random.choice(patterns)
            offset = " " * random.randint(0, 20)
            print(f"{offset}{p}")
            time.sleep(0.1)

    except KeyboardInterrupt:
        pass

    print(f"\n{YELLOW}>> COOLING DOWN COILS...{RESET}")
    time.sleep(2)
    os.system('clear')

if __name__ == "__main__":
    visual_overload()