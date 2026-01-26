import time
import json
import os
import sys

# CONNECTION AU FLUX (On remonte de 2 dossiers pour trouver le fichier racine)
PIPELINE_FILE = "../../shared_entropy.json"

# FRÉQUENCES SACRÉES (TESLA 3-6-9)
HARM_3 = 396.0     # Libération (Calme)
HARM_6 = 639.0     # Connexion (Actif)
HARM_9 = 963.0     # Transcendance (Danger/Critique)

def get_tesla_frequency(chaos_level):
    """Convertit le chaos en une fréquence harmonique"""
    if chaos_level < 0.4:
        return HARM_3, "🟢 396 Hz (Harmonie)"
    elif chaos_level < 0.8:
        return HARM_6, "🟡 639 Hz (Action)"
    else:
        return HARM_9, "🔴 963 Hz (ALERTE)"

def visual_oscilloscope(freq, chaos):
    """Affiche une onde sinusoïdale dans le terminal"""
    # Amplitude visuelle basée sur le chaos
    width = 40
    amplitude = int(chaos * width)
    
    # Dessin de l'onde
    wave = "=" * amplitude
    space = " " * (width - amplitude)
    
    if freq == HARM_9:
        print(f"⚡ {wave}| CRITIQUE {chaos}")
    else:
        print(f"~ {wave}| {int(freq)} Hz")

def run_generator():
    print("--- TESLA TONE GENERATOR (RESONANCE) ---")
    print(f"Monitoring: {os.path.abspath(PIPELINE_FILE)}")
    
    try:
        while True:
            if os.path.exists(PIPELINE_FILE):
                try:
                    with open(PIPELINE_FILE, "r") as f:
                        data = json.load(f)
                        chaos = data.get("entropy_level", 0.1)
                        
                    freq, state = get_tesla_frequency(chaos)
                    
                    # 1. Feedback Visuel
                    visual_oscilloscope(freq, chaos)
                    
                    # 2. Feedback Sonore (Seulement en cas d'alerte rouge)
                    # Le caractère \a déclenche le 'Bell' système du Mac
                    if freq == HARM_9:
                        print("\a", end="", flush=True)
                    
                except:
                    pass
            
            # Fréquence de rafraîchissement rapide (10Hz)
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n--- SILENCE ---")

if __name__ == "__main__":
    run_generator()