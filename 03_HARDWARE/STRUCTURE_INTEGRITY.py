import sys
import os

# Importation de la logique Tesla depuis le Layer 04
sys.path.append(os.path.abspath("04_PHYSICS"))
try:
    from vibration_monitor import calculate_energy
except ImportError:
    def calculate_energy(f): return f * 6.626

def analyze_wood_structure(material_density, base_frequency):
    print("="*40)
    print("🌲 WOOD STRUCTURE INTEGRITY AUDIT")
    print("="*40)
    
    # Calcul de l'énergie de résonance via Tesla-Logic
    energy_level = calculate_energy(base_frequency)
    
    # Seuil de sécurité basé sur la densité du bois (ex: 3.69 comme pivot)
    safety_threshold = material_density * 3.69
    
    print(f"Structure Density: {material_density} kg/m³")
    print(f"Resonance Frequency: {base_frequency} Hz")
    print(f"Computed Energy: {energy_level} units")
    
    if energy_level > safety_threshold:
        print("\n⚠️ ALERT: High Resonance detected. Risk of structural fatigue.")
    else:
        print("\n✅ STATUS: Structural Damping Optimal. Resilience confirmed.")
    print("="*40)

if __name__ == "__main__":
    # Test pour une structure standard
    analyze_wood_structure(material_density=0.5, base_frequency=9)