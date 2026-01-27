def apply_stasis(self, seconds_elapsed):
        """Reduces energy loss during hibernation (90% reduction)."""
        if self.is_alive:
            # Formula: Loss reduced by factor of 10 [cite: 2026-01-21]
            stasis_decay = (seconds_elapsed * 0.01) * 0.1 
            self.energy = max(self.energy - stasis_decay, 0)
            
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            entry = f"| {timestamp} | STASIS | WAKE | {seconds_elapsed}s elapsed | Energy: {self.energy:.1f}% |\n"
            
            with open(self.journal_path, "a") as f:
                f.write(entry)
            return True
        return False