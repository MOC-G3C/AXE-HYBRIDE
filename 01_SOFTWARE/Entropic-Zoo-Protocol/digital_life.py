def inject_energy(self):
        """Sacrificial Protocol: Injects 50% energy from external source."""
        if self.is_alive:
            # Boosting energy (can exceed 100% up to 150%)
            self.energy = min(self.energy + 50.0, 150.0)
            # Stability gains a small boost from the raw power
            self.stability = min(self.stability + 0.1, self.max_stability)
            
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            entry = f"| {timestamp} | {self.get_stage_name()} | POWER INJECTION | +50% ENERGY |\n"
            with open(self.journal_path, "a") as f:
                f.write(entry)
            return True
        return False