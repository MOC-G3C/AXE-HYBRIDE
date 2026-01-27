# ... (Gardez les imports existants) ...
import pulse_logger # New Import

# ... (Gardez la configuration et la classe BioHeart) ...

def main():
    global last_email_time
    os.system('clear')
    print("--- L'AXE HYBRIDE : TOTAL LOGGING BRIDGE (V5.2) ---")
    
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)
        print("✅ Live Recording Active. Data saved to pulse_history.csv\n")

        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                
                if line.startswith("BPM:"):
                    try:
                        raw_bpm = float(line.split(":")[1])
                        bpm = get_smoothed_bpm(raw_bpm)
                        timestamp = time.strftime("%H:%M:%S")
                        dilation, density = physics_engine.calculate_dilation(bpm)
                        
                        # Update Terminal Display
                        visual_core.update_display(bpm, timestamp, density)
                        
                        # NEW: Record data to CSV
                        pulse_logger.log_pulse(bpm, density)
                        
                        # Alert Logic (100 - 130 BPM)
                        if 100 < bpm <= 130:
                            audio_engine.play_frequency(bpm * 3.69)
                            lambda_protocol.trigger_reflex(bpm, bpm * 3.69)
                        
                        # Critical Alert (> 130 BPM)
                        elif bpm > 130:
                            # ... (Code des alertes critiques existant) ...
                            pass
                                
                    except ValueError:
                        continue
            time.sleep(0.01)
# ... (Reste du code identique) ...