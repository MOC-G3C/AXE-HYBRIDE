import os
import time

class DigitalOrganism:
    def __init__(self, name="Ectoplasm-01", root_path="."):
        self.name = name
        self.root_path = root_path
        self.legacy_path = os.path.join(root_path, "01_SOFTWARE/Entropic-Zoo-Protocol/GENETIC_CORE.tmp")
        self.journal_path = os.path.join(root_path, "02Humain/MUTATION_JOURNAL.md")
        
        self.genetic_bonus, self.generation = self.load_legacy()
        self.energy = 100.0 + self.genetic_bonus
        self.stability = 1.0 + (self.genetic_bonus / 100)
        self.is_alive = True
        self.last_stage = self.get_stage_name()

    def die(self):
        """Triggers the death cry and final log entry."""
        self.is_alive = False
        self.energy = 0
        
        # 1. THE DEATH CRY (macOS deep sound)
        os.system('afplay /System/Library/Sounds/Basso.aiff &')
        
        # 2. THE FINAL LOG ENTRY
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = f"| {timestamp} | {self.last_stage} | VOID | 0.0% | TERMINATED |\n"
        
        with open(self.journal_path, "a") as f:
            f.write("\n### --- END OF LINE ---\n")
            f.write(entry)
            f.write(f"> Generation {self.generation} has returned to the source code.\n")
        
        # 3. Save legacy for the next gen [cite: 2026-01-26]
        self.save_legacy()

    def evolve(self, bpm, entropy, gravity):
        if not self.is_alive: return
        
        # Tesla Sync logic
        if int(bpm) % 3 == 0:
            self.energy += 5.0
            
        self.stability -= (gravity / 100)
        if entropy > 0.9: self.energy -= 2.0
            
        # Check for death trigger [cite: 2026-01-26]
        if self.energy <= 0 or self.stability <= 0:
            self.die()
            return

        current_stage = self.get_stage_name()
        if current_stage != self.last_stage:
            self.log_mutation(current_stage)