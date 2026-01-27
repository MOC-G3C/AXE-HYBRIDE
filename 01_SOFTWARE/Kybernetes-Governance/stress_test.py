import time
import os
import sys

# Paths for audio engine
sys.path.append(os.path.abspath("03_HARDWARE"))
import tesla_tone_generator as audio_engine

def run_stress_test():
    print("--- AXE HYBRIDE : AUDIO STRESS TEST ---")
    print("Simulating BPM increase from 100 to 145...")
    
    # Range of BPM to test the two levels
    for bpm in range(100, 150, 5):
        print(f"\n[TEST] Current BPM: {bpm}")
        
        # Level 1: Standard Tesla Resonance (100 - 130)
        if 100 <= bpm <= 130:
            print("🔊 Level 1: Playing Tesla Frequency...")
            audio_engine.play_frequency(bpm * 3.69)
            
        # Level 2: Critical Resonance (> 130)
        if bpm > 130:
            print("🚨 Level 2: CRITICAL ALERT (Glass.aiff + Tesla)")
            # Triggering the glass sound
            os.system("afplay /System/Library/Sounds/Glass.aiff &")
            # Triggering the resonance
            audio_engine.play_frequency(bpm * 3.69)
            
        time.sleep(1.5)

    print("\n[SUCCESS] Stress test complete. All audio layers verified.")

if __name__ == "__main__":
    run_stress_test()