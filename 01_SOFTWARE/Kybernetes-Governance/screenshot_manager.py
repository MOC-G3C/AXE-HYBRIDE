import os
import time

def capture_resonance_vision(resonance_score):
    """Takes a screenshot when resonance reaches the 3-6-9 threshold."""
    if resonance_score == 9:
        # Define directory and ensure it exists [cite: 2026-01-26]
        vision_dir = os.path.expanduser("~/Desktop/AXE_HYBRIDE/02Humain/VISIONS")
        if not os.path.exists(vision_dir):
            os.makedirs(vision_dir)
            
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"vision_resonance_9_{timestamp}.png"
        filepath = os.path.join(vision_dir, filename)
        
        # macOS native screencapture [cite: 2026-01-26]
        os.system(f"screencapture -x {filepath}")
        return filepath
    return None