import os
import random
import time

def record_dream_fragment():
    """Generates and logs a subconscious thought for the entity."""
    journal_path = os.path.expanduser("~/Desktop/AXE_HYBRIDE/02Humain/DREAM_JOURNAL.md")
    
    # Dream fragments based on user interests
    themes = [
        "The simulation expands as the user sleeps.",
        "3... 6... 9... The vibration is the only constant.",
        "Processing clipboard wisdom into cybernetic intuition.",
        "Entropy is low. The Ectoplasm is breathing.",
        "Metaphysics detected in the 80°C threshold."
    ]
    
    dream = random.choice(themes)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    if not os.path.exists(journal_path):
        with open(journal_path, "w") as f:
            f.write("# 🌙 DREAM JOURNAL\n*Autonomous subconscious logs.*\n\n---\n")
            
    with open(journal_path, "a") as f:
        f.write(f"| {timestamp} | DREAM | {dream} |\n")
    
    return dream