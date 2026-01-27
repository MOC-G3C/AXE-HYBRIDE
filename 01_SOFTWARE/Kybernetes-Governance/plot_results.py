import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
CSV_PATH = "01_SOFTWARE/Kinetic-RNG/pulse_history.csv"
OUTPUT_IMAGE = "01_SOFTWARE/Kinetic-RNG/last_session_graph.png"

def generate_graph():
    if not os.path.exists(CSV_PATH):
        print(f"❌ Error: {CSV_PATH} not found. Run the neural bridge first.")
        return

    # Loading data
    print("📊 Loading biometric data...")
    df = pd.read_csv(CSV_PATH)
    
    # Converting timestamp to datetime for better display
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Creating the plot
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # BPM Plot (Axis 1)
    color = 'tab:red'
    ax1.set_xlabel('Time')
    ax1.set_ylabel('BPM (Smoothed)', color=color)
    ax1.plot(df['Timestamp'], df['BPM_Smoothed'], color=color, linewidth=2, label='Heart Rate')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True, alpha=0.3)

    # Density Plot (Axis 2)
    ax2 = ax1.twinx()
    color = 'tab:cyan'
    ax2.set_ylabel('Physical Density', color=color)
    ax2.plot(df['Timestamp'], df['Density'], color=color, linestyle='--', alpha=0.7, label='Density')
    ax2.tick_params(axis='y', labelcolor=color)

    # Formatting
    plt.title('AXE HYBRIDE - Session Resonance Analysis')
    fig.tight_layout()
    
    # Saving
    plt.savefig(OUTPUT_IMAGE)
    print(f"✅ Graph saved successfully: {OUTPUT_IMAGE}")
    
    # Optional: Open the image immediately (macOS only)
    os.system(f"open '{OUTPUT_IMAGE}'")

if __name__ == "__main__":
    generate_graph()