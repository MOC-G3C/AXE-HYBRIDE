def get_color_for_bpm(bpm):
    """Returns a color code based on the system pulse intensity."""
    if bpm < 90:
        return "\033[96m" # Cyan - Calm
    elif bpm < 120:
        return "\033[93m" # Orange - Active
    else:
        return "\033[91m" # Red - Critical Stress

def update_display(bpm, timestamp, density):
    color = get_color_for_bpm(bpm)
    reset = "\033[0m"
    
    # Building the visual bar
    bar_length = int(min(bpm / 2, 50))
    bar = "█" * bar_length
    
    print(f"{color}[{timestamp}] RESONANCE: {bpm:.1f} BPM | DENSITY: {density:.2f}{reset}")
    print(f"{color}Pulse: [{bar:<50}]{reset}\n")