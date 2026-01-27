import os
import time

# Path configuration
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARCHIVE_DIR = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/Archives")
LOG_FILE = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/pulse_history.csv")

# Retention policy (in seconds) - 7 days
RETENTION_TIME = 7 * 24 * 60 * 60 

def run_maintenance():
    print("--- AXE HYBRIDE : WEEKLY MAINTENANCE STARTING ---")
    now = time.time()
    count = 0

    # 1. Cleaning old archives
    if os.path.exists(ARCHIVE_DIR):
        for file in os.listdir(ARCHIVE_DIR):
            file_path = os.path.join(ARCHIVE_DIR, file)
            if os.path.getmtime(file_path) < (now - RETENTION_TIME):
                os.remove(file_path)
                print(f"Deleted old archive: {file}")
                count += 1

    # 2. Compressing/Rotating pulse_history if too large (> 5MB)
    if os.path.exists(LOG_FILE):
        if os.path.getsize(LOG_FILE) > 5 * 1024 * 1024:
            os.rename(LOG_FILE, f"{LOG_FILE}.old")
            print("Rotated pulse_history.csv (size limit exceeded)")

    print(f"Maintenance complete. {count} files removed.")
    os.system(f'osascript -e \'display notification "{count} old archives cleaned." with title "Maintenance Complete"\'')

if __name__ == "__main__":
    run_maintenance()