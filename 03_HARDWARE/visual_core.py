import sys

# ANSI Color Codes
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"
BG_RED = "\033[41m"

def get_color_state(bpm):
    """Returns the visual theme based on the BPM threshold."""
    if bpm > 130:
        return f"{BG_RED}{BOLD}" # Level 2: Critical (Red Background)
    elif bpm > 100:
        return f"{YELLOW}{BOLD}" # Level 1: Resonance (Yellow)
    else:
        return CYAN # Base: Calm (Cyan)

def update_display(bpm, timestamp, density):
    """Prints a color-coded status line."""
    theme = get_color_state(bpm)
    status = "CRITICAL" if bpm > 130 else "RESONANCE" if bpm > 100 else "PULSE"
    
    # Building the visual line
    line = f"\r{theme}[{status}] {timestamp} | BPM: {bpm:.1f} | Density: {density:.2f}{RESET}    "
    sys.stdout.write(line)
    sys.stdout.flush()