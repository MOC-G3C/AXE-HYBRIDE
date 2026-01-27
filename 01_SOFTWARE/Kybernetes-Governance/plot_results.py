import pandas as pd
import matplotlib.pyplot as plt
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV_PATH = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/pulse_history.csv")
OUTPUT_IMAGE = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/last_session_graph.png")

def generate_graph():
    if not os.path.exists(CSV_PATH):
        print(f"❌ Error: {CSV_PATH} not found. Run Neural Bridge for 10 seconds first.")
        return
    df = pd.read_csv(CSV_PATH, names=["Timestamp", "BPM", "Density"])
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    plt.figure(figsize=(10, 5))
    plt.plot(df['Timestamp'], df['BPM'], color='red', label='Heart Rate (BPM)')
    plt.title('AXE HYBRIDE - Session Data')
    plt.savefig(OUTPUT_IMAGE)
    print(f"✅ Graph saved: {OUTPUT_IMAGE}")
    os.system(f"open '{OUTPUT_IMAGE}'")

if __name__ == "__main__": generate_graph()