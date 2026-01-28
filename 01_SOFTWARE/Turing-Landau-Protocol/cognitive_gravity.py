import math
import random
import sys

# --- CONSTANTS ---
PI = math.pi
# Simulation of the "Debye Length" (Cognitive Reach)
LAMBDA_D = 2.5 
# Simulation of "Plasma Frequency" (Core Processing Speed)
OMEGA_P = 100.0 

class LandauDamping:
    def __init__(self, operator_status="OPTIMIZED"):
        self.status = operator_status
        print(f"[*] LANDAU CORE INITIALIZED // OPERATOR: {self.status}")

    def calculate_gamma(self, k_wave_number):
        """
        Calculates the Landau Damping rate (Gamma).
        Equation: Gamma = - sqrt(pi/8) * (Omega / |k|^3 * Lambda^3) * exp(...)
        
        k_wave_number: Represents 'Information Density' (Input Chaos)
        """
        if k_wave_number == 0:
            return 0.0

        # Term 1: The geometric constant
        term1 = -1 * math.sqrt(PI / 8)
        
        # Term 2: The frequency/wavelength ratio
        denominator = (abs(k_wave_number)**3) * (LAMBDA_D**3)
        term2 = OMEGA_P / denominator
        
        # Term 3: The exponential decay (The Damping)
        exponent = -1 / (2 * (k_wave_number**2) * (LAMBDA_D**2)) - 1.5
        term3 = math.exp(exponent)
        
        gamma = term1 * term2 * term3
        return gamma

    def stabilize_thought(self, input_entropy):
        """
        Takes raw entropy (0-10) and attempts to damp it.
        """
        # We map entropy to wave number (Higher entropy = smaller wavelengths = higher k)
        k = input_entropy * 0.5
        
        gamma = self.calculate_gamma(k)
        
        print(f"   > INPUT ENTROPY: {input_entropy} | WAVE(k): {k:.2f}")
        print(f"   > LANDAU GAMMA:  {gamma:.6f}")
        
        if gamma < -0.01:
            return f"✅ STABLE (Damped by {gamma:.4f})"
        elif gamma < 0:
             return f"⚠️ MARGINAL (Low Damping)"
        else:
            return f"❌ UNSTABLE (Divergence Detected)"

def main():
    print("--- COGNITIVE GRAVITY ENGINE (LANDAU V1) ---")
    
    # 1. Initialize
    engine = LandauDamping()
    
    # 2. Test Loop with random "thoughts"
    test_data = [1.2, 4.5, 8.9, 0.5, 9.8] # Abstract entropy values
    
    for thought in test_data:
        print("\n[Injecting Data Packet...]")
        result = engine.stabilize_thought(thought)
        print(f"   > STATUS: {result}")

if __name__ == "__main__":
    main()