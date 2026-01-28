import os
import time

# System paths
BIO_PATH = os.path.expanduser("~/Desktop/L'AXE HYBRIDE/02_HUMAIN/BIO_CALIBRATION.md")

def get_biological_input():
    """Extracts recovery status from the human layer."""
    try:
        with open(BIO_PATH, 'r') as f:
            status = f.read().lower()
            if "optimized" in status: return "DYNAMIC"
            if "depleted" in status: return "SOFT"
    except FileNotFoundError:
        pass
    return "BALANCED"

def apply_visual_filter():
    mode = get_biological_input()
    print(f"🖥️ Visual Core Initialization...")
    
    # Logic: Adjust brightness/color based on biological stress levels
    settings = {
        "DYNAMIC": {"brightness": 100, "temp": "6500K", "desc": "High productivity mode active."},
        "BALANCED": {"brightness": 70, "temp": "5000K", "desc": "Standard operation mode."},
        "SOFT": {"brightness": 30, "temp": "2700K", "desc": "Recovery mode - Reducing neural load."}
    }
    
    current = settings[mode]
    print(f"Status: {mode}")
    print(f"Setting: {current['brightness']}% Brightness | {current['temp']}")
    print(f"Note: {current['desc']}")

if __name__ == "__main__":
    apply_visual_filter()