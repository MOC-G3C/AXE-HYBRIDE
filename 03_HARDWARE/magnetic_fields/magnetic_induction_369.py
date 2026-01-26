import numpy as np
import sounddevice as sd
import time

def magnetic_pulse(freq, duration=2):
    fs = 44100
    t = np.linspace(0, duration, int(fs * duration), False)
    # Onde carrée pour maximiser l'effet d'induction magnétique
    wave = 0.5 * np.sign(np.sin(2 * np.pi * freq * t))
    print(f"🧲 Induction en cours : {freq} Hz")
    sd.play(wave, fs)
    sd.wait()

if __name__ == "__main__":
    # Séquence Tesla 3-6-9
    for f in [3, 6, 9]:
        magnetic_pulse(f)
        time.sleep(1)