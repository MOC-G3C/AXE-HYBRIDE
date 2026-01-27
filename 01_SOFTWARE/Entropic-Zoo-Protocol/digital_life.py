class DigitalOrganism:
    def __init__(self, name="Ectoplasm-01"):
        self.name = name
        self.energy = 100.0
        self.stability = 1.0
        self.is_alive = True

    def feed(self):
        """Manual feeding: adds a burst of energy and stability."""
        if self.is_alive:
            # Overcharge is possible up to 150%
            self.energy = min(self.energy + 15.0, 150.0) 
            self.stability = min(self.stability + 0.15, 2.0)
            return True
        return False

    def evolve(self, bpm, entropy, gravity):
        if not self.is_alive: return
        if int(bpm) % 3 == 0:
            self.energy += 5.0
            self.stability += 0.05
        self.stability -= (gravity / 100)
        if entropy > 0.9:
            self.energy -= 2.0
        if self.energy <= 0 or self.stability <= 0:
            self.is_alive = False
            self.energy = 0

    def get_status(self):
        status = "ALIVE" if self.is_alive else "VOID"
        return f"{self.name} | Energy: {self.energy:.1f}% | Stability: {self.stability:.2f} | [{status}]"