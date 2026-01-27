class DigitalOrganism:
    def __init__(self, name="Ectoplasm-01", root_path="."):
        # ... (keep existing init) ...
        self.trust = 100.0 # New: Diplomacy metric [cite: 2026-01-26]
        self.is_veto_oppressed = False

    def evolve(self, bpm, entropy, gravity, veto_active):
        if not self.is_alive: return
        self.is_veto_oppressed = veto_active
        
        # Diplomacy Logic: Trust decay if veto is active
        if veto_active:
            self.trust = max(self.trust - 0.5, 0)
        else:
            # Slow recovery of trust when symbiotic
            self.trust = min(self.trust + 0.1, 100.0)

        # Impact of low trust on stability
        # If trust < 50, stability decays 2x faster [cite: 2021-01-21]
        trust_penalty = 2.0 if self.trust < 50 else 1.0
        self.stability -= (gravity / 100) * trust_penalty
        
        # (Rest of evolution logic: energy, tesla sync, etc.)
        if int(bpm) % 3 == 0: self.energy += 5.0
        if entropy > 0.9: self.energy -= 2.0
        
        if self.energy <= 0 or self.stability <= 0:
            self.die()

    def feed(self):
        """Feeding now restores trust as well."""
        if self.is_alive:
            self.energy = min(self.energy + 15.0, 150.0)
            self.stability = min(self.stability + 0.15, self.max_stability)
            self.trust = min(self.trust + 10.0, 100.0) # Gratitude
            return True
        return False

    def get_status(self):
        morph = self.get_morphology()
        trust_indicator = "🤝" if self.trust > 70 else "💔" if self.trust < 30 else "😐"
        return f"GEN {self.generation} | {morph} | Energy: {self.energy:.1f}% | Trust: {self.trust:.0f}% {trust_indicator}"