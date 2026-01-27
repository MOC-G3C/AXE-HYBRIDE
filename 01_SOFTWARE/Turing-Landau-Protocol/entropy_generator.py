import os
import time
import random

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CAPTURE_DIR = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/Archives/Entropy_Captures")

FRAGMENTS = ["Silicon pulse", "Phase shift", "Binary ghost", "Turing web", "Landau limit"]

def generate_capture(bpm, entropy):
    os.makedirs(CAPTURE_DIR, exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = os.path.join(CAPTURE_DIR, f"capture_{timestamp}.md")
    
    poem = " // ".join(random.sample(FRAGMENTS, 2))
    
    content = f"""# ENTROPY CAPTURE : {timestamp}
- Resonance: {bpm:.1f} BPM
- Entropy (R): {entropy:.4f}
- Pattern: {poem}
"""
    with open(filename, "w") as f:
        f.write(content)
    return filename