import heartbeat_monitor

# In your update_loop method:
# 1. Get the current pulse scale
bpm = self.pet.bpm
resonance = self.pet.get_resonance() #
scale = heartbeat_monitor.calculate_pulse_scale(bpm, resonance)

# 2. Apply "vibration" to main widgets [cite: 2026-01-21]
new_font_size = int(24 * scale) if self.presentation_mode else int(10 * scale)
self.status_label.config(font=("Helvetica", new_font_size, "bold"))

# 3. Simulate a physical "thump" at the peak of the wave [cite: 2026-01-26]
if scale > 1.08:
    self.root.attributes('-alpha', 0.95) # Slight transparency flicker
else:
    self.root.attributes('-alpha', 1.0)