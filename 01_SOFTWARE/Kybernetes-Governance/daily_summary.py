import pandas as pd
import os
from datetime import datetime

# Path setup
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV_PATH = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/pulse_history.csv")
ARCHIVE_DIR = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/Archives")

def generate_daily_report():
    if not os.path.exists(CSV_PATH):
        print("No data found for today.")
        return

    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')
    report_file = os.path.join(ARCHIVE_DIR, f"energy_report_{today}.txt")

    # Load and process data
    df = pd.read_csv(CSV_PATH, names=["Timestamp", "BPM", "Density"])
    avg_bpm = df['BPM'].mean()
    max_bpm = df['BPM'].max()
    peak_count = len(df[df['BPM'] > 130])

    # Build the report content
    report = f"""--- AXE HYBRIDE : DAILY ENERGY REPORT ({today}) ---
    
- Average Machine Pulse: {avg_bpm:.2f} BPM
- Peak Resonance: {max_bpm:.2f} BPM
- Critical Stress Alerts: {peak_count} instances
- System Status: {"STABLE" if avg_bpm < 100 else "HIGH ACTIVITY"}
--------------------------------------------------
"""
    with open(report_file, "w") as f:
        f.write(report)
    
    print(f"Report generated: {report_file}")
    return report

if __name__ == "__main__":
    print(generate_daily_report())