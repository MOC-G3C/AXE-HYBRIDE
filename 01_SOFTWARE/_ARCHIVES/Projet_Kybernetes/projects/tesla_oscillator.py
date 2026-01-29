import time

def tesla_oscillator(limit):
    print("--- INITIALIZING TESLA OSCILLATOR (3-6-9) ---")
    print("System: Kybernetes | Module: Resonance Check")
    print("-" * 40)

    for i in range(1, limit + 1):
        output = ""
        # The 3-6-9 Logic
        if i % 3 == 0:
            output += "[Energy 3] "
        if i % 6 == 0:
            output += "[Frequency 6] "
        if i % 9 == 0:
            output += ">>> VIBRATION 9 (PURE RESONANCE) <<<"

        # Only print if there is a reaction
        if output:
            print(f"Step {i:02}: {output}")
            time.sleep(0.3) # Simulation delay

if __name__ == "__main__":
    # Run the cycle up to 27 (3 x 9)
    tesla_oscillator(27)

