class DigitalOrganism:
    def __init__(self, name="Ectoplasm-01", root_path="."):
        # ... (keep existing init) ...
        self.genetic_bonus, self.generation = self.load_legacy()
        
        # New: Dynamic stability ceiling
        self.max_stability = 1.0 + (self.genetic_bonus / 100)
        self.stability = self.max_stability
        self.energy = 100.0 + self.genetic_bonus
        
        self.scars = 0
        self.radiant_timer = 0
        self.is_alive = True

    def heal_scar(self):
        """Removes a scar and permanently increases Max Stability."""
        if self.scars > 0:
            self.scars -= 1
            # PURITY BONUS: +0.1 to the ceiling [cite: 2026-01-26]
            self.max_stability += 0.1 
            self.stability = self.max_stability
            
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            entry = f"| {timestamp} | RADIANT | PURIFIED | MAX STABILITY: {self.max_stability:.2f} |\n"
            with open(self.journal_path, "a") as f: f.write(entry)
            
            os.system('afplay /System/Library/Sounds/Glass.aiff &')
            return True
        return False

    def evolve(self, bpm, entropy, gravity):
        if not self.is_alive: return
        
        # Environment Impact
        if int(bpm) % 3 == 0: self.energy += 5.0
        self.stability -= (gravity / 100)
        
        # Purity Cap: Stability cannot exceed Max Stability [cite: 2026-01-26]
        self.stability = min(self.stability, self.max_stability)
        
        # (Keep the rest of your healing/death/mutation logic here)