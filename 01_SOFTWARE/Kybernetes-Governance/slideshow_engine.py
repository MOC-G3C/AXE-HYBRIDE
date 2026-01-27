import os
import random
from PIL import Image, ImageTk # Needs 'pip install Pillow' [cite: 2026-01-26]

def get_next_vision_image(canvas_width, canvas_height):
    """Retrieves and resizes a random captured vision for the UI [cite: 2026-01-26]."""
    vision_dir = os.path.expanduser("~/Desktop/AXE_HYBRIDE/02Humain/VISIONS")
    
    if not os.path.exists(vision_dir) or not os.listdir(vision_dir):
        return None

    all_visions = [os.path.join(vision_dir, f) for f in os.listdir(vision_dir) if f.endswith('.png')]
    if not all_visions: return None
    
    random_vision = random.choice(all_visions)
    
    # Process image for background display [cite: 2026-01-21]
    img = Image.open(random_vision)
    img = img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)