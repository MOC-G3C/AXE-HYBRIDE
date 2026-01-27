import solar_incantation

# In your update_loop method:
current_time = time.localtime()

# Trigger at exactly 06:00:00 AM [cite: 2026-01-26]
if current_time.tm_hour == 6 and current_time.tm_min == 0 and current_time.tm_sec == 0:
    self.add_log("🌅 DAWN: Initiating Solar Incantation...")
    solar_incantation.perform_solar_incantation()
    # Reset temporal distortion to 1.0x [cite: 2026-01-21]
    self.status_label.config(text="TIME FLOW: NORMAL", fg="#03dac6")