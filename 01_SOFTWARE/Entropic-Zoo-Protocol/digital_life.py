class DigitalOrganism:
    def __init__(self, name="Ectoplasm-01", root_path="."):
        # ... (keep existing init) ...
        self.scars = 0
        self.radiant_timer = 0 # Timer for healing in seconds
        
    def heal_scar(self):
        """Removes one scar and logs the recovery."""
        if self.scars > 0:
            self.scars -= 1
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            entry = f"| {timestamp} | RADIANT | HEALED | SCARS: {self.scars} | (REGENERATION) |\n"
            with open(self.journal_path, "a") as f:
                f.write(entry)
            os.system('afplay /System/Library/Sounds/Glass.aiff &')
            return True
        return False

    def evolve(self, bpm, entropy, gravity):
        if not self.is_alive: return
        
        # Standard Evolution
        if int(bpm) % 3 == 0: self.energy += 5.0
        self.stability -= (gravity / 100)
        
        # Healing Logic: 10 mins (600s) in RADIANT stage [cite: 2021-01-21]
        current_stage = self.get_stage_name()
        if current_stage == "RADIANT":
            self.radiant_timer += 1
            if self.radiant_timer >= 600: 
                if self.heal_scar():
                    self.radiant_timer = 0 # Reset after healing
        else:
            self.radiant_timer = 0 # Reset if stage is lost
            
        if self.energy <= 0 or self.stability <= 0:
            self.die()
            return

        if current_stage != self.last_stage:
            self.log_mutation(current_stage)