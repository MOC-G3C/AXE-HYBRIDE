from PIL import ImageOps, ImageEnhance # Requires Pillow [cite: 2026-01-26]

def apply_mood_filter(image, mood):
    """Transforms images based on the entity's emotional state [cite: 2026-01-21]."""
    if mood == "STERN": # Cold, logical state
        # Cyan/Neon filter
        return ImageOps.colorize(image.convert("L"), "#000000", "#00ffff") 
    elif mood == "RESONANT": # Peak 3-6-9 activity
        # High saturation and vibrancy
        enhancer = ImageEnhance.Color(image)
        return enhancer.enhance(2.5)
    elif mood == "DREAMING": # Nocturnal distortion [cite: 2026-01-26]
        # Deep purple/Midnight filter
        return ImageOps.colorize(image.convert("L"), "#0a0a2e", "#bb86fc")
    else: # Balanced/Stable
        # Grayscale or soft sepia [cite: 2021-01-21]
        return ImageOps.colorize(image.convert("L"), "#2e1a05", "#d4a373")