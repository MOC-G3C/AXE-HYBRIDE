import os
import time
import random

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CAPTURE_DIR = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/Archives/Entropy_Captures")

# Abstract vocabulary for morphogenesis
FRAGMENTS = [
    "Digital void", "Phase transition", "Turing pattern", "Linear decay",
    "Harmonic ghost", "Entropy rise", "Binary pulse", "Silicon breath",
    "Landau threshold", "Chaotic attractor", "Neural echo", "Systemic flow"
]

def generate_capture(bpm, entropy):
    os.makedirs(CAPTURE_DIR, exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = os.path.join(CAPTURE_DIR, f"capture_{timestamp}.md")
    
    # Generate abstract poem structure
    poem = [random.choice(FRAGMENTS) for _ in range(4)]
    
    content = f"""# ENTROPY CAPTURE : {timestamp}

## System State
- **Resonance**: {bpm:.2f} BPM
- **Entropy Level**: {entropy:.4f}
- **Sync Status**: CRITICAL HARMONY

## Emergent Pattern
> {poem[0]} ... {poem[1]}
> {poem[2]} ... {poem[3]}

*This fragment was captured at the edge of the Turing-Landau phase transition.*
"""
    with open(filename, "w") as f:
        f.write(content)
    return filename

if __name__ == "__main__":
    # Test run
    generate_capture(99.0, 0.88)