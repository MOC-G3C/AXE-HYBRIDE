import pandas as pd
import os
from datetime import datetime, timedelta

# Path setup
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV_PATH = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/pulse_history.csv")
ARCHIVE_DIR = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/Archives")

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

    # Analysis
    df = pd.read_csv(CSV_PATH, names=["Timestamp", "BPM", "Density"])
    avg_bpm = df['BPM'].mean()
    
    # TESLA COUNTER: Counts entries where BPM is a multiple of 3
    tesla_syncs = len(df[df['BPM'].astype(int) % 3 == 0])
    
    prev_avg = get_previous_avg()
    trend = f"Trend: {avg_bpm - prev_avg:+.2f} BPM" if prev_avg else "Trend: N/A"

    report = f"""--- AXE HYBRIDE : DAILY ENERGY REPORT ({today}) ---

- Average Machine Pulse: {avg_bpm:.2f} BPM
- {trend}
- Tesla Harmonic Syncs: {tesla_syncs} times today ⚡
- System Status: {"STABLE" if avg_bpm < 100 else "HIGH ACTIVITY"}
--------------------------------------------------
"""
    with open(report_file, "w") as f:
        f.write(report)
    
    # Native notification
    os.system(f'osascript -e \'display notification "{tesla_syncs} Tesla syncs detected today." with title "Axe Hybride"\'')
    return report

if __name__ == "__main__":
    generate_daily_report()