import os
import time

class DigitalOrganism:
    def __init__(self, name="Ectoplasm-01", root_path="."):
        self.name = name
        self.energy = 100.0
        self.stability = 1.0
        self.is_alive = True
        self.last_stage = self.get_stage_name()
        self.journal_path = os.path.join(root_path, "02Humain/MUTATION_JOURNAL.md")

    def get_stage_name(self):
        """Returns the current evolutionary stage name."""
        if not self.is_alive: return "VOID"
        if self.energy < 33: return "FADING"
        if self.energy < 66: return "STABLE"
        if self.energy < 99: return "ACTIVE"
        return "RADIANT"

    def log_mutation(self, new_stage):
        """Writes mutation events to the human folder."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = f"| {timestamp} | {self.last_stage} | {new_stage} | {self.energy:.1f}% | {self.stability:.2f} |\n"
        
        # Create file with header if it doesn't exist [cite: 2021-01-21]
        if not os.path.exists(self.journal_path):
            header = "# MUTATION JOURNAL - ENTROPIC ZOO\n\n| Date | Old Stage | New Stage | Energy | Stability |\n|---|---|---|---|---|\n"
            with open(self.journal_path, "w") as f: f.write(header)
            
        with open(self.journal_path, "a") as f: f.write(entry)
        self.last_stage = new_stage

    def evolve(self, bpm, entropy, gravity):
        if not self.is_alive: return
        
        # Tesla Sync logic
        if int(bpm) % 3 == 0:
            self.energy += 5.0
            self.stability += 0.05
            
        self.stability -= (gravity / 100)
        if entropy > 0.9: self.energy -= 2.0
        if self.energy <= 0 or self.stability <= 0: self.is_alive = False
            
        # Check for mutation [cite: 2026-01-26]
        current_stage = self.get_stage_name()
        if current_stage != self.last_stage:
            self.log_mutation(current_stage)