import csv
import os
import time

# Store the log in the data folder
LOG_FILE = "01_SOFTWARE/Kinetic-RNG/pulse_history.csv"

def init_log():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(LOG_FILE):
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "BPM_Smoothed", "Density"])

def log_pulse(bpm, density):
    """Appends a new record to the pulse history."""
    init_log()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, f"{bpm:.2f}", f"{density:.2f}"])