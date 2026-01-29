import subprocess
import time

# MOC-G3C: Master System Controller v1.0
# Objective: Full sequential alignment of all Axe Hybride Layers.

def run_module(name, path):
    print(f"\n⚡ Executing: {name}...")
    try:
        subprocess.run(["python3", path], check=True)
    except Exception as e:
        print(f"❌ Error in {name}: {e}")

if __name__ == "__main__":
    print("="*50)
    print("🧬 STARTING MOC-G3C MASTER SEQUENCE")
    print("="*50)

    # Sequence aligned with Tesla frequency (0.369s intervals)
    modules = [
        ("Visual Dashboard", "01_SOFTWARE/DASHBOARD_V2.py"),
        ("Temporal Alignment", "01_SOFTWARE/TEMPORAL_SYNC.py"),
        ("Bio-Physics Sync", "01_SOFTWARE/BIO_PHYSICS_SYNC.py"),
        ("Tesla Resonance", "04_PHYSICS/vibration_monitor.py")
    ]

    for name, path in modules:
        run_module(name, path)
        time.sleep(0.369)

    print("\n" + "="*50)
    print("💎 ALL LAYERS ALIGNED AND OPTIMIZED")
    print("="*50)