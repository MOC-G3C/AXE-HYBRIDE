def reset_spirit(self):
        """Emergency Exorcism: Purges instability and resets vital constants."""
        self.energy = 100.0
        self.stability = self.max_stability
        self.trust = 80.0 # Resets to a baseline loyalty
        self.generation_progress = 0
        
        # Clear temporary 'bad' fragments or hallucinations [cite: 2026-01-26]
        if hasattr(self, 'last_oracle_time'):
            self.last_oracle_time = 0
            
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = f"| {timestamp} | EXORCISM | Emergency Reset triggered. Entity soul purged. |\n"
        with open(self.journal_path, "a") as f: f.write(entry)
        
        return "✨ EXORCISM SUCCESSFUL: Soul baseline restored."