import os
import time
from datetime import datetime

# Path to the biological calibration file
BIO_PATH = os.path.expanduser("~/Desktop/L'AXE HYBRIDE/02_HUMAIN/BIO_CALIBRATION.md")
LOG_PATH = os.path.expanduser("~/Desktop/L'AXE HYBRIDE/session_logs/HARDWARE_RESONANCE.md")

def get_bio_state():
    """Reads the biological state to adjust system intensity."""
    try:
        with open(BIO_PATH, 'r') as f:
            content = f.read().lower()
            if "optimized" in content:
                return "high"
            elif "depleted" in content:
                return "low"
    except FileNotFoundError:
        pass
    return "standard"

def log_resonance(summary):
    """Logs resonance results with a timestamp."""
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, 'a') as f:
        f.write(f"\n### Session: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(summary + "\n")

def run_simulation():
    state = get_bio_state()
    # Adjust iterations based on biological state
    iterations = 18 if state == "high" else (3 if state == "low" else 9)
    bases = [3, 6, 9]
    results = [f"System Mode: {state.upper()}"]
    
    print(f"🚀 Initializing Resonance - Mode: {state.upper()}")
    
    for i in range(1, iterations + 1):
        for n in bases:
            freq = n * i
            msg = f"🌀 Harmonic {i} | Base {n}: {freq}Hz"
            print(msg)
            results.append(msg)
            time.sleep(0.05)
            
    log_resonance("\n".join(results))
    print("✅ Session archived in session_logs.")

if __name__ == "__main__":
    run_simulation()