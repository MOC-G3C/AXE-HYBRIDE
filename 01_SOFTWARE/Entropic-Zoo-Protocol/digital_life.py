def resurrect(self):
        """Forbidden Protocol: Brings the entity back with a heavy genetic cost."""
        if not self.is_alive:
            # The cost: 80% of genetic legacy is lost
            self.genetic_bonus *= 0.2
            self.energy = 70.0 # Reborn with partial energy
            self.stability = 0.5 # Fragile state
            self.is_alive = True
            self.last_stage = self.get_stage_name()
            
            # Log the forbidden act
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            entry = f"| {timestamp} | VOID | REBORN | {self.energy:.1f}% | {self.stability:.2f} | (FORBIDDEN PROTOCOL) |\n"
            with open(self.journal_path, "a") as f:
                f.write(entry)
            
            # Save the corrupted legacy immediately
            self.save_legacy()
            return True
        return False