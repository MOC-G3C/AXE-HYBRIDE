import os, sys, time, random

# Automatic paths fix
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(ROOT, "03_HARDWARE"))
sys.path.append(os.path.join(ROOT, "04_PHYSICS"))

import gravity_density_engine as physics_engine
import visual_core

def get_cpu_pulse():
    """Calculates a BPM based on the 1-minute CPU load average."""
    # os.getloadavg() returns a tuple (1min, 5min, 15min)
    load = os.getloadavg()[0]
    # Scaling: base 70 BPM + (load * 15). Maxed at 180 for system safety.
    dynamic_bpm = 70 + (load * 15)
    return min(max(dynamic_bpm, 60), 180)

def main():
    os.system('clear')
    log_file = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/pulse_history.csv")
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    print("--- AXE HYBRIDE : SYSTEM RESONANCE MODE ---")
    print("Monitoring CPU load to generate pulse...")
    
    while True:
        try:
            # Get pulse from machine activity instead of random
            system_bpm = get_cpu_pulse()
            timestamp = time.strftime("%H:%M:%S")
            
            # Physics Calculation
            dilation, density = physics_engine.calculate_dilation(system_bpm)
            
            # UI Update
            visual_core.update_display(system_bpm, timestamp, density)
            
            # Data logging for graphs
            with open(log_file, "a") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')},{system_bpm:.2f},{density:.2f}\n")
            
            time.sleep(0.7) 
        except KeyboardInterrupt:
            print("\nResonance Terminated.")
            break

if __name__ == "__main__": main()