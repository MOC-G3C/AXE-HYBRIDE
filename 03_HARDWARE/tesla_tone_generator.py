import os
import math
import struct
import wave

# CONFIGURATION AUDIO
SAMPLE_RATE = 44100

def generate_sine_wave(frequency, duration=0.8):
    """
    Génère un fichier audio .wav pur (Sine Wave).
    Version corrigée pour compatibilité Python 3.
    """
    num_samples = int(SAMPLE_RATE * duration)
    amplitude = 16000 
    file_name = "03_HARDWARE/temp_pulse.wav"
    
    # Génération des frames audio
    audio_frames = []
    for i in range(num_samples):
        value = int(amplitude * math.sin(2 * math.pi * frequency * i / SAMPLE_RATE))
        data = struct.pack('<h', value)
        audio_frames.append(data)
    
    # Écriture du fichier .wav (Correction ici: utilisation directe de wave.open)
    try:
        with wave.open(file_name, 'w') as wav_file:
            wav_file.setnchannels(1)      # Mono
            wav_file.setsampwidth(2)      # 2 octets (16 bits)
            wav_file.setframerate(SAMPLE_RATE)
            wav_file.writeframes(b''.join(audio_frames))
        return file_name
    except Exception as e:
        print(f"[GENERATOR ERROR] {e}")
        return None

def play_frequency(hz):
    """Joue la fréquence."""
    try:
        wav_file = generate_sine_wave(hz)
        if wav_file:
            # Le '&' permet de jouer sans bloquer le script
            # Utilisation de afplay (macOS native)
            os.system(f"afplay {wav_file} &")
    except Exception as e:
        print(f"[AUDIO ERROR] {e}")

if __name__ == "__main__":
    print("Test Audio 432Hz...")
    play_frequency(432)
