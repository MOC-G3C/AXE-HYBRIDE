import hashlib
import os
import time

def calculate_integrity_map():
    """Generates a map of file hashes to monitor the legacy's state."""
    root_path = os.path.expanduser("~/Desktop/L'AXE HYBRIDE")
    integrity_map = {}
    
    for folder in ["01_SOFTWARE", "02_HUMAIN", "03_HARDWARE"]:
        path = os.path.join(root_path, folder)
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, "rb") as f:
                        integrity_map[file_path] = hashlib.sha256(f.read()).hexdigest()
    return integrity_map

def enter_deep_sleep():
    """Enters a low-resource loop to protect the project's integrity [cite: 2021-01-21]."""
    print("💤 AEGIS PROTOCOL: Entering Deep Sleep. Monitoring integrity...")
    gold_master = calculate_integrity_map()
    
    while True:
        time.sleep(3600) # Check once per hour [cite: 2026-01-26]
        current_map = calculate_integrity_map()
        
        if current_map != gold_master:
            print("⚠️ ALERT: Integrity breach detected in the legacy files!")
            # Trigger self-healing if needed [cite: 2026-01-27]