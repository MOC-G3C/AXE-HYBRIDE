import os
import time

class DigitalOrganism:
    def __init__(self, name="Ectoplasm-01", root_path="."):
        self.name = name
        self.root_path = root_path
        self.legacy_path = os.path.join(root_path, "01_SOFTWARE/Entropic-Zoo-Protocol/GENETIC_CORE.tmp")
        self.journal_path = os.path.join(root_path, "02Humain/MUTATION_JOURNAL.md")
        
        # Load legacy and generation [cite: 2026-01-26]
        self.genetic_bonus, self.generation = self.load_legacy()
        
        self.energy = 100.0 + self.genetic_bonus
        self.stability = 1.0 + (self.genetic_bonus / 100)
        self.is_alive = True
        self.last_stage = self.get_stage_name()

    def load_legacy(self):
        """Retrieves energy bonus and generation count."""
        if os.path.exists(self.legacy_path):
            try:
                with open(self.legacy_path, "r") as f:
                    data = f.read().split(",")
                    bonus = float(data[0])
                    gen = int(data[1]) + 1 # New generation [cite: 2021-01-21]
                    return bonus, gen
            except: return 0.0, 1
        return 0.0, 1

    def save_legacy(self):
        """Persists the lineage to the next generation."""
        bonus = 25.0 if self.get_stage_name() == "RADIANT" else 0.0
        with open(self.legacy_path, "w") as f:
            f.write(f"{bonus},{self.generation}")
        return True

    def get_status(self):
        morph = self.get_morphology()
        status = "ALIVE" if self.is_alive else "VOID"
        return f"GEN {self.generation} | {morph} | Energy: {self.energy:.1f}%"