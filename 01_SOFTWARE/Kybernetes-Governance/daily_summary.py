import pandas as pd
import os
from datetime import datetime, timedelta

# Path setup
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV_PATH = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/pulse_history.csv")
ARCHIVE_DIR = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/Archives")

def send_notification(title, message):
    """Sends a native macOS visual notification."""
    cmd = f'display notification "{message}" with title "{title}"'
    os.system(f"osascript -e '{cmd}'")

def get_previous_avg():
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    prev_report = os.path.join(ARCHIVE_DIR, f"energy_report_{yesterday}.txt")
    if os.path.exists(prev_report):
        try:
            with open(prev_report, "r") as f:
                for line in f:
                    if "Average Machine Pulse:" in line:
                        return float(line.split(":")[1].split("BPM")[0].strip())
        except: return None
    return None

def generate_daily_report():
    if not os.path.exists(CSV_PATH): return
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')
    report_file = os.path.join(ARCHIVE_DIR, f"energy_report_{today}.txt")

    df = pd.read_csv(CSV_PATH, names=["Timestamp", "BPM", "Density"])
    avg_bpm = df['BPM'].mean()
    status = "STABLE" if avg_bpm < 100 else "HIGH ACTIVITY"

    # Save report
    report = f"--- AXE HYBRIDE REPORT ({today}) ---\nAvg: {avg_bpm:.2f} BPM | Status: {status}"
    with open(report_file, "w") as f:
        f.write(report)
    
    # Trigger visual notification
    send_notification("Axe Hybride", f"Rapport généré. Statut système : {status}")
    return report

if __name__ == "__main__":
    generate_daily_report()