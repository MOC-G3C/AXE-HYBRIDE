import os

def get_color_for_bpm(bpm):
    """Returns a color code based on system pulse and Tesla harmonics."""
    val = int(bpm)
    if val % 3 == 0:
        return "\033[95m\033[1m" # Bright Magenta (Tesla Mode)
    
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
    
    # SOUND TRIGGER
    # Plays a crystalline system sound in the background if it's a Tesla Sync
    if is_tesla:
        os.system('afplay /System/Library/Sounds/Glass.aiff &')
    
    label = "⚡ TESLA RESONANCE ⚡" if is_tesla else "SYSTEM RESONANCE"
    bar_length = int(min(bpm / 2, 50))
    bar = "█" * bar_length
    
    print(f"{color}[{timestamp}] {label}: {bpm:.1f} BPM | DENSITY: {density:.2f}{reset}")
    print(f"{color}Pulse: [{bar:<50}]{reset}\n")