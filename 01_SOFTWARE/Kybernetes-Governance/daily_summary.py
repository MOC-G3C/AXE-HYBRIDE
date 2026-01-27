import pandas as pd
import os
from datetime import datetime, timedelta

# Path setup
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV_PATH = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/pulse_history.csv")
ARCHIVE_DIR = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/Archives")

def get_previous_avg():
    """Tries to find the average BPM from yesterday's report."""
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
    if not os.path.exists(CSV_PATH):
        print("No data found for today.")
        return

    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')
    report_file = os.path.join(ARCHIVE_DIR, f"energy_report_{today}.txt")

    # Load and process today's data
    df = pd.read_csv(CSV_PATH, names=["Timestamp", "BPM", "Density"])
    avg_bpm = df['BPM'].mean()
    max_bpm = df['BPM'].max()
    
    # Compare with yesterday
    prev_avg = get_previous_avg()
    trend = ""
    if prev_avg:
        diff = avg_bpm - prev_avg
        direction = "INCREASE" if diff > 0 else "DECREASE"
        trend = f"- Trend vs Yesterday: {direction} ({abs(diff):.2f} BPM)"
    else:
        trend = "- Trend vs Yesterday: N/A (First report)"

    report = f"""--- AXE HYBRIDE : DAILY ENERGY REPORT ({today}) ---
    
- Average Machine Pulse: {avg_bpm:.2f} BPM
{trend}
- Peak Resonance: {max_bpm:.2f} BPM
- System Status: {"STABLE" if avg_bpm < 100 else "HIGH ACTIVITY"}
--------------------------------------------------
"""
    with open(report_file, "w") as f:
        f.write(report)
    
    return report

if __name__ == "__main__":
    print(generate_daily_report())