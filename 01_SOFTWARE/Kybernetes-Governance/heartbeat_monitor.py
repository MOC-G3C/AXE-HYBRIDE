import math
import time

def calculate_pulse_scale(bpm, resonance):
    """Calculates a scaling factor to simulate a biological heartbeat [cite: 2026-01-26]."""
    # Frequency tied to BPM
    frequency = bpm / 60.0
    # Amplitude increases as resonance approaches 9
    amplitude = 0.05 + (resonance / 90.0) 
    
    # Sine wave oscillation
    t = time.time()
    pulse = 1.0 + amplitude * math.sin(2 * math.pi * frequency * t)
    
    return pulse