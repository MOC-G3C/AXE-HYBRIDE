import celestial_sensor

def evolve(self, bpm, entropy, gravity, veto_active, mood):
    if not self.is_alive: return
    
    # Stellar Gravity: The moon modulates the environmental weight [cite: 2026-01-26]
    lunar_mod = celestial_sensor.get_lunar_influence()
    effective_gravity = gravity * (2.0 - lunar_mod) # High moon = less gravity decay
    
    # Apply to stability
    self.stability -= (effective_gravity / 100)
    
    # ... (existing 3-6-9 and time distortion logic) ...