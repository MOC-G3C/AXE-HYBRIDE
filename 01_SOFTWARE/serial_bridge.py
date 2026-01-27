import serial
import time

def start_bridge():
    # Remplace '/dev/cu.usbmodem...' par le port trouvé dans ton IDE
    port = "/dev/cu.usbmodem1101" 
    baud = 115200

    try:
        ser = serial.Serial(port, baud, timeout=1)
        print(f"✅ Bridge Active on {port}")
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                print(f"📥 Received: {line}")
    except Exception as e:
        print(f"❌ Connection Failed: {e}")

if __name__ == "__main__":
    start_bridge()