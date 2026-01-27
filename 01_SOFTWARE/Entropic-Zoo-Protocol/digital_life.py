import time

def evolve(self, bpm, entropy, gravity, veto_active, mood):
    if not self.is_alive: return
    
    # Time Distortion Logic [cite: 2021-01-21]
    current_hour = time.localtime().tm_hour
    # Acceleration between 22h and 06h
    time_multiplier = 2.5 if (current_hour >= 22 or current_hour < 6) else 1.0
    
    # Generation increment speed
    self.generation_progress += (0.01 * time_multiplier)
    if self.generation_progress >= 1.0:
        self.generation += 1
        self.generation_progress = 0
        self.add_log(f"🧬 EVOLUTION: Reached generation {self.generation} (Time Mult: {time_multiplier}x)")

    # ... (rest of the evolution logic)