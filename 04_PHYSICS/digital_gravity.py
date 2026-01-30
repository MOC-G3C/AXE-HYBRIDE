import time
import math
import os
import glob
import statistics
import sys

# --- CONFIGURATION ---
# Path to Human Memory (The source of Political Law)
MEMORY_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '02_HUMAIN', 'analog_records'))

# --- STYLING ---
CYAN = '\033[96m'
PURPLE = '\033[95m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'
BOLD = '\033[1m'

class GravityEngine:
    def __init__(self):
        print(f"{BOLD}[*] INITIALIZING DIGITAL GRAVITY ENGINE...{RESET}")
        self.base_gravity = 9.81
    
    def get_political_gravity(self):
        """
        Reads the history of the Operator to determine the Laws of Physics.
        """
        all_entropy = []
        files = glob.glob(os.path.join(MEMORY_PATH, "*.md"))
        
        if not files:
            return 9.81, "NEUTRAL (No History)"

        for file_path in files:
            try:
                with open(file_path, 'r') as f:
                    for line in f:
                        if "Entropy:" in line:
                            parts = line.split("Entropy:")
                            if len(parts) > 1:
                                val = float(parts[1].split("|")[0].strip())
                                all_entropy.append(val)
            except:
                continue

        if not all_entropy:
            return 9.81, "NEUTRAL (Empty Data)"

        avg_entropy = statistics.mean(all_entropy)

        # --- THE LAW APPLIED TO MATTER ---
        if avg_entropy < 3.0:
            # PAX TECHNOLOGICA: Lightness, flight is easy.
            return 1.62, f"{GREEN}MOON GRAVITY (Pax Technologica){RESET}"
        elif avg_entropy < 7.0:
            # VIGILANT REPUBLIC: Earth standard.
            return 9.81, f"{CYAN}EARTH GRAVITY (Vigilant Republic){RESET}"
        else:
            # MARTIAL LAW: Heavy, oppressive, movement is difficult.
            return 24.79, f"{RED}JUPITER GRAVITY (Martial Law){RESET}"

    def apply_tesla_modifier(self, gravity, phase):
        """
        Applies Nikola Tesla's 3-6-9 Keys to bend gravity locally.
        """
        status = "SOLID"
        modifier = 1.0
        
        if phase in [3, 6]:
            # Flux State: Magnetic partial levitation
            modifier = 0.5
            status = f"{PURPLE}FLUX (3-6){RESET}"
        elif phase == 9:
            # Zero Point: Total Singularity
            modifier = 0.0
            status = f"{BOLD}ZERO POINT (9){RESET}"
        
        final_g = gravity * modifier
        return final_g, status

    def run_simulation(self):
        print("--- SYNCING PHYSICS WITH POLITICS ---")
        
        # Séquence Tesla
        cycle_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        object_mass = 75 # kg (Operator Weight)
        
        try:
            while True:
                # 1. Update Political Laws (Real-time check)
                base_g, law_name = self.get_political_gravity()
                
                print(f"\n{BOLD}>> CURRENT LAW: {law_name} (Base G: {base_g:.2f}){RESET}")
                
                # 2. Cycle through Energy Phases
                for phase in cycle_sequence:
                    final_g, tesla_state = self.apply_tesla_modifier(base_g, phase)
                    weight = object_mass * final_g
                    
                    # Visual Bar
                    bar_len = int(weight / 50)
                    visual = "█" * bar_len
                    
                    print(f"   [PHASE {phase}] G: {final_g:.2f} m/s² | Weight: {weight:.1f} N | {tesla_state} {visual}")
                    time.sleep(0.4)
                
                print("-" * 40)
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n[!] GRAVITY DECOUPLED.")

if __name__ == "__main__":
    engine = GravityEngine()
    engine.run_simulation()