def get_color_for_bpm(bpm):
    """Returns a color code based on system pulse and Tesla harmonics."""
    val = int(bpm)
    
    # TESLA HARMONIC DETECTION (3, 6, 9)
    # If the BPM is a multiple of 3, it's a Tesla frequency
    if val % 3 == 0:
        return "\033[95m\033[1m" # Bright Magenta / Bold (Tesla Mode)
    
    if bpm < 90:
        return "\033[96m" # Cyan - Calm
    elif bpm < 120:
        return "\033[93m" # Orange - Active
    else:
        return "\033[91m" # Red - Critical Stress

def update_display(bpm, timestamp, density):
    color = get_color_for_bpm(bpm)
    reset = "\033[0m"
    is_tesla = int(bpm) % 3 == 0
    
    label = "⚡ TESLA RESONANCE ⚡" if is_tesla else "SYSTEM RESONANCE"
    
    bar_length = int(min(bpm / 2, 50))
    bar = "█" * bar_length
    
    print(f"{color}[{timestamp}] {label}: {bpm:.1f} BPM | DENSITY: {density:.2f}{reset}")
    print(f"{color}Pulse: [{bar:<50}]{reset}\n")