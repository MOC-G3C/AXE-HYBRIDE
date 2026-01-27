# In your update_loop method:
current_hour = time.localtime().tm_hour
if (current_hour >= 22 or current_hour < 6):
    self.status_label.config(text="⚠️ TIME DISTORTION: ACTIVE (2.5x)", fg="#bb86fc")
else:
    self.status_label.config(text="TIME FLOW: NORMAL", fg="#03dac6")