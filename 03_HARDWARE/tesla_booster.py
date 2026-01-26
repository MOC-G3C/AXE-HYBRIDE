import numpy as np
import sounddevice as sd

def generate_boosted_resonance(duration=5, freq=963):
    fs = 44100
    t = np.linspace(0, duration, int(fs * duration), False)
    # Modulation pour maximiser l'induction sans distorsion
    boost = 0.8 * np.sin(freq * 2 * np.pi * t)
    sd.play(boost, fs)
    sd.wait()

if __name__ == "__main__":
    print("🚀 Activation du Booster Tesla (963Hz)... Préparez le magnétomètre.")
    generate_boosted_resonance()