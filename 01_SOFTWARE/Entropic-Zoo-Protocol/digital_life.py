import os
import time

class DigitalOrganism:
    def __init__(self, name="Ectoplasm-01", root_path="."):
        self.name = name
        self.root_path = root_path
        self.legacy_path = os.path.join(root_path, "01_SOFTWARE/Entropic-Zoo-Protocol/GENETIC_CORE.tmp")
        self.journal_path = os.path.join(root_path, "02Humain/MUTATION_JOURNAL.md")
        
        # Load legacy bonus if it exists [cite: 2021-01-21]
        self.genetic_bonus = self.load_legacy()
        
        self.energy = 100.0 + self.genetic_bonus
        self.stability = 1.0 + (self.genetic_bonus / 100)
        self.is_alive = True
        self.last_stage = self.get_stage_name()

    def load_legacy(self):
        """Retrieves energy bonus from the previous generation."""
        if os.path.exists(self.legacy_path):
            try:
                with open(self.legacy_path, "r") as f:
                    bonus = float(f.read())
                    return bonus
            except: return 0.0
        return 0.0

    def save_legacy(self):
        """Saves a bonus if the organism reached RADIANT stage."""
        if self.get_stage_name() == "RADIANT":
            bonus = 25.0 # Legacy gift for the next one
            with open(self.legacy_path, "w") as f:
                f.write(str(bonus))
            return True
        return False

    def get_stage_name(self):
        if not self.is_alive: return "VOID"
        if self.energy < 33: return "FADING"
        if self.energy < 66: return "STABLE"
        if self.energy < 99: return "ACTIVE"
        return "RADIANT"

    def evolve(self, bpm, entropy, gravity):
        if not self.is_alive: return
        
        # Tesla Sync & Environment
        if int(bpm) % 3 == 0: self.energy += 5.0
        self.stability -= (gravity / 100)
        
        if self.energy <= 0 or self.stability <= 0:
            # Death sequence: check for legacy before ending [cite: 2026-01-26]
            self.save_legacy()
            self.is_alive = False
            self.energy = 0
            
        current_stage = self.get_stage_name()
        if current_stage != self.last_stage:
            self.log_mutation(current_stage)