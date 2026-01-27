import random

class DigitalOrganism:
    def __init__(self, name="Ectoplasm-01"):
        self.name = name
        self.energy = 100.0
        self.stability = 1.0
        self.is_alive = True

    def evolve(self, bpm, entropy, gravity):
        """Reacts to the system environment."""
        if not self.is_alive: return

        # Tesla Sync gives energy
        if int(bpm) % 3 == 0:
            self.energy += 5.0
            self.stability += 0.05
        
        # High gravity pulls on stability [cite: 2026-01-26]
        self.stability -= (gravity / 100)
        
        # Entropy fluctuations
        if entropy > 0.9:
            self.energy -= 2.0 # Chaos is taxing
        
        # Death conditions
        if self.energy <= 0 or self.stability <= 0:
            self.is_alive = False
            self.energy = 0

    def get_status(self):
        status = "ALIVE" if self.is_alive else "VOID"
        return f"{self.name} | Energy: {self.energy:.1f}% | Stability: {self.stability:.2f} | [{status}]"