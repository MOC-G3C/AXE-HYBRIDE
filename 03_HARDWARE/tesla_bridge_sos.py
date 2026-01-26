import numpy as np
import sounddevice as sd
import time

def pulse_signal(duration, freq=963): # Utilise le "9" pour la clarté
    fs = 44100
    t = np.linspace(0, duration, int(fs * duration), False)
    wave = 0.5 * np.sin(freq * 2 * np.pi * t)
    sd.play(wave, fs)
    sd.wait()

def send_sos():
    print("🆘 Envoi du signal SOS via Le Pont de Tesla...")
    # S-O-S en Morse ( . . .   --- --- ---   . . . )
    for _ in range(3): pulse_signal(0.2); time.sleep(0.1) # S
    time.sleep(0.3)
    for _ in range(3): pulse_signal(0.6); time.sleep(0.1) # O
    time.sleep(0.3)
    for _ in range(3): pulse_signal(0.2); time.sleep(0.1) # S

if __name__ == "__main__":
    send_sos()