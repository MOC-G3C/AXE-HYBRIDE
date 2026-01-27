import os
import math
import time
import random

def get_system_entropy():
    """Captures non-linear entropy using system load and micro-variations."""
    load = os.getloadavg()[0]
    # Non-linear Logistic Map: x_next = r * x * (1 - x)
    # r is driven by the CPU load (3.5 to 4.0 is the chaotic zone)
    r = 3.5 + (min(load, 1.0) * 0.5)
    
    # Initial seed based on time
    x = (time.time() % 1)
    
    # Iterate to find the attractor
    for _ in range(10):
        x = r * x * (1 - x)
        
    return x, r

def run_turing_landau_loop():
    print("--- TURING-LANDAU PROTOCOL : PHASE 2 ACTIVE ---")
    print("Modeling non-linear phase transitions...")
    
    try:
        while True:
            entropy_value, chaos_factor = get_system_entropy()
            
            # Landau-inspired Phase Transition check
            # Transition happens when chaos factor crosses specific thresholds
            phase = "STABLE" if chaos_factor < 3.7 else "TURBULENT"
            
            print(f"[{time.strftime('%H:%M:%S')}] Entropy: {entropy_value:.4f} | Factor R: {chaos_factor:.2f} | Phase: {phase}")
            
            # Logic for pattern emergence (Turing Morphogenesis)
            if phase == "TURBULENT" and entropy_value > 0.8:
                print("⚡ PATTERN EMERGENCE DETECTED ⚡")
                os.system('afplay /System/Library/Sounds/Morse.aiff &')
                
            time.sleep(1.5)
    except KeyboardInterrupt:
        print("\nProtocol Suspended.")

if __name__ == "__main__":
    run_turing_landau_loop()