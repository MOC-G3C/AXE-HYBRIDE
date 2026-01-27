class DigitalOrganism:
    def __init__(self, name="Ectoplasm-01", root_path="."):
        # ... (keep existing init code) ...
        self.scars = 0 # Track number of resurrections [cite: 2026-01-26]
        
    def resurrect(self):
        """Forbidden Protocol: Brings the entity back with a genetic and visual cost."""
        if not self.is_alive:
            self.scars += 1 # Add a scar [cite: 2026-01-26]
            self.genetic_bonus *= 0.2
            self.energy = 70.0
            self.stability = 0.5
            self.is_alive = True
            self.last_stage = self.get_stage_name()
            
            # Log with scar count
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            entry = f"| {timestamp} | VOID | REBORN | SCARS: {self.scars} | (LAZARUS) |\n"
            with open(self.journal_path, "a") as f: f.write(entry)
            
            self.save_legacy()
            return True
        return False

    def get_morphology(self):
        """Returns an ASCII representation with added scars if necessary."""
        if not self.is_alive: return "[ † ]"
        
        # Base morphology [cite: 2026-01-26]
        if self.energy < 33: base = "( . )"
        elif self.energy < 66: base = "( o )"
        elif self.energy < 99: base = "<{ O }>"
        else: base = "✧<{{ ✹ }}>✧"

        # Apply Scars (Visual glitches based on scar count) [cite: 2021-01-21]
        if self.scars == 1:
            return f"~{base}~"
        elif self.scars == 2:
            return f"~!{base}!~"
        elif self.scars >= 3:
            return f"zZ{base}Zz" # Heavy corruption
            
        return base