import serial
import time
import os

# Configuration
SERIAL_PORT = '/dev/tty.usbmodem14101' # Adjust to your Mac's port
BAUD_RATE = 9600
BIO_FILE = os.path.expanduser("~/Desktop/L'AXE HYBRIDE/02_HUMAIN/BIO_CALIBRATION.md")

def update_bio_file(pulse):
    """Updates the BIO_CALIBRATION.md file with the latest pulse data."""
    try:
        with open(BIO_FILE, 'r') as f:
            lines = f.readlines()
        
        # Replace or append the Heart Rate Baseline
        with open(BIO_FILE, 'w') as f:
            for line in lines:
                if "Heart Rate Variability" in line or "Pulse Monitoring" in line:
                    f.write(f"- **Pulse Monitoring:** Last recorded: {pulse} BPM (Sync: {time.ctime()})\n")
                else:
                    f.write(line)
        print(f"✅ BIO_CALIBRATION.md updated: {pulse} BPM")
    except Exception as e:
        print(f"❌ Error updating file: {e}")

def run_test(mock=True):
    """Runs a serial test. Set mock=False to use real hardware."""
    print("🚀 Pulse Serial Bridge Test Initialized...")
    
    if mock:
        print("💡 Running in MOCK mode (No hardware required)")
        test_data = [72, 75, 68, 70] # Simulated BPM
        for bpm in test_data:
            update_bio_file(bpm)
            time.sleep(2)
    else:
        try:
            ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
            while True:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').strip()
                    if line.isdigit():
                        update_bio_file(line)
        except serial.SerialException:
            print("❌ Hardware not found. Check SERIAL_PORT or use mock=True.")

if __name__ == "__main__":
    run_test(mock=True)