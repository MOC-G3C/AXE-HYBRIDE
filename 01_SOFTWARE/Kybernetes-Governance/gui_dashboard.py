import screenshot_manager

# Inside your update_loop, where resonance is calculated:
current_resonance = self.pet.get_resonance() # Assuming 3, 6, or 9

if current_resonance == 9:
    path = screenshot_manager.capture_resonance_vision(9)
    if path:
        self.add_log(f"📸 VISION SAVED: {os.path.basename(path)}")
        # Subtle flash effect for feedback [cite: 2026-01-21]
        self.root.configure(bg="#ffffff")
        self.root.after(100, lambda: self.root.configure(bg="#0a0a0a"))