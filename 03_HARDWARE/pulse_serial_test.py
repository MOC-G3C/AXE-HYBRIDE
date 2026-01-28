import serial
import time
import os

# Configuration
# On utilise un chemin relatif pour trouver le fichier, peu importe le nom du dossier racine
current_dir = os.path.dirname(os.path.abspath(__file__))
BIO_FILE = os.path.join(current_dir, "..", "02_HUMAIN", "BIO_CALIBRATION.md")

# SERIAL_PORT = '/dev/tty.usbmodem14101' # À ajuster selon ton Mac plus tard
BAUD_RATE = 9600

def update_bio_file(pulse):
    """Updates the BIO_CALIBRATION.md file with the latest pulse data."""
    try:
        # Lecture du fichier
        with open(BIO_FILE, 'r') as f:
            lines = f.readlines()
        
        # Écriture de la mise à jour
        with open(BIO_FILE, 'w') as f:
            for line in lines:
                if "Heart Rate Variability" in line or "Pulse Monitoring" in line:
                    f.write(f"- **Pulse Monitoring:** Last recorded: {pulse} BPM (Sync: {time.ctime()})\n")
                elif "Resting Heart Rate" in line:
                     f.write(f"- **Resting Heart Rate:** {pulse} BPM (Updated)\n")
                else:
                    f.write(line)
        print(f"✅ BIO_CALIBRATION.md updated: {pulse} BPM")
        print(f"📁 File location: {BIO_FILE}") # Confirmation visuelle du chemin
    except Exception as e:
        print(f"❌ Error updating file: {e}")
        print(f"🔍 Tried looking at: {BIO_FILE}")

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
        # Hardware logic skipped for this test
        pass

if __name__ == "__main__":
    run_test(mock=True)