class DigitalOrganism:
    def __init__(self, name="Ectoplasm-01"):
        self.name = name
        self.energy = 100.0
        self.stability = 1.0
        self.is_alive = True

    def get_morphology(self):
        """Returns an ASCII representation based on energy tiers."""
        if not self.is_alive:
            return "[ † ]" # Void/Dead
        
        # Energy Tiers
        if self.energy < 33:
            return "( . )" # Fading
        elif self.energy < 66:
            return "( o )" # Stable
        elif self.energy < 99:
            return "<{ O }>" # Active
        else:
            return "✧<{{ ✹ }}>✧" # Radiant / Overcharged

    def feed(self):
        if self.is_alive:
            self.energy = min(self.energy + 15.0, 150.0)
            self.stability = min(self.stability + 0.15, 2.0)
            return True
        return False

    def evolve(self, bpm, entropy, gravity):
        if not self.is_alive: return
        
        # Tesla Harmonic Multiplier
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
        morph = self.get_morphology()
        status = "ALIVE" if self.is_alive else "VOID"
        return f"{morph} | Energy: {self.energy:.1f}% | {status}"