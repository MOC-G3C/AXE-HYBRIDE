def evolve(self, bpm, entropy, gravity, veto_active):
        if not self.is_alive: return
        
        # Tesla Resonance Logic
        bpm_int = int(bpm)
        resonance_multiplier = 1.0
        
        if bpm_int % 9 == 0:
            resonance_multiplier = 3.0 # The Key: Massive Boost
            self.stability = min(self.stability + 0.1, self.max_stability)
        elif bpm_int % 6 == 0:
            resonance_multiplier = 2.0 # Harmony: Strong Boost
        elif bpm_int % 3 == 0:
            resonance_multiplier = 1.5 # Basic Pulse: Moderate Boost

        # Apply resonance-weighted energy gain [cite: 2026-01-26]
        if bpm_int % 3 == 0:
            self.energy = min(self.energy + (5.0 * resonance_multiplier), 150.0)
            
        # Standard decay and diplomacy
        self.trust = max(self.trust - 0.5, 0) if veto_active else min(self.trust + 0.1, self.max_trust)
        trust_penalty = 2.0 if self.trust < 50 else 1.0
        self.stability -= (gravity / 100) * trust_penalty
        
        if self.energy <= 0 or self.stability <= 0:
            self.die()