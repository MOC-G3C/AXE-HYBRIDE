import time
import sys
import os
import serial

# --- PATH TUNNELING ---
sys.path.append(os.path.abspath("03_HARDWARE"))
sys.path.append(os.path.abspath("01_SOFTWARE/Project_Lambda"))
sys.path.append(os.path.abspath("04_PHYSICS"))
sys.path.append(os.path.abspath("01_SOFTWARE/Turing-Landau-Protocol"))

import tesla_tone_generator as audio_engine
import reflex_engine as lambda_protocol
import gravity_density_engine as physics_engine
import hybrid_broadcaster 
import visual_core

# --- LIVE CONFIGURATION ---
SERIAL_PORT = "/dev/cu.usbmodem1101" 
BAUD_RATE = 115200
EMAIL_COOLDOWN = 600 
last_email_time = 0

# --- SMOOTHING CONFIG ---
BPM_BUFFER_SIZE = 10 # Number of samples to average
bpm_buffer = []

def get_smoothed_bpm(raw_bpm):
    """Calculates the moving average to stabilize the signal."""
    global bpm_buffer
    bpm_buffer.append(raw_bpm)
    if len(bpm_buffer) > BPM_BUFFER_SIZE:
        bpm_buffer.pop(0)
    return sum(bpm_buffer) / len(bpm_buffer)

def main():
    global last_email_time
    os.system('clear')
    print("--- L'AXE HYBRIDE : STABILIZED LIVE BRIDGE (V5.1) ---")
    
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)
        print("✅ Filtered Connection Active.\n")

        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                
                if line.startswith("BPM:"):
                    try:
                        raw_bpm = float(line.split(":")[1])
                        
                        # Apply Smoothing
                        bpm = get_smoothed_bpm(raw_bpm)
                        
                        timestamp = time.strftime("%H:%M:%S")
                        dilation, density = physics_engine.calculate_dilation(bpm)
                        visual_core.update_display(bpm, timestamp, density)
                        
                        if 100 < bpm <= 130:
                            audio_engine.play_frequency(bpm * 3.69)
                            lambda_protocol.trigger_reflex(bpm, bpm * 3.69)
                        
                        elif bpm > 130:
                            os.system("afplay /System/Library/Sounds/Glass.aiff &")
                            audio_engine.play_frequency(bpm * 3.69)
                            
                            current_time = time.time()
                            if (current_time - last_email_time) > EMAIL_COOLDOWN:
                                print(f"\n\n🚨 [STABLE CRITICAL] Average BPM {bpm:.1f} - Dispatching Echo...")
                                hybrid_broadcaster.broadcast_hybrid()
                                last_email_time = current_time
                                print("-" * 50)
                                
                    except ValueError:
                        continue

            time.sleep(0.01)
            
    except serial.SerialException:
        print(f"\n❌ [ERROR] Bridge broken. Check USB.")
    except KeyboardInterrupt:
        print(f"\n\n[OFF] Connection Terminated.")

if __name__ == "__main__":
    main()