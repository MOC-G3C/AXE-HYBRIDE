# In your update_loop method:
bpm_int = int(bpm)
resonance_color = "#00ffff" # Default Cyan

# Visual feedback for Tesla Synchronicity
if bpm_int % 9 == 0:
    resonance_color = "#ffffff" # Pure Light (9)
    self.add_log("⚡ TESLA RESONANCE [9]: Universal Key active.")
elif bpm_int % 6 == 0:
    resonance_color = "#ffcc00" # Golden Ratio (6)
elif bpm_int % 3 == 0:
    resonance_color = "#ff00ff" # Magenta Pulse (3)

# Apply pulse to the organism label [cite: 2021-01-21]
self.pet_label.config(fg=resonance_color)