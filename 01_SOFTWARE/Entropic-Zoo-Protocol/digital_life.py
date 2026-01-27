def hunt_cache(self, files_removed):
        """Predator Mode: Consumes junk files to regain stability."""
        if self.is_alive and files_removed > 0:
            # Stability gain based on number of 'consumed' files
            gain = min(files_removed * 0.01, 0.2) 
            self.stability = min(self.stability + gain, self.max_stability)
            
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            entry = f"| {timestamp} | PREDATOR | HUNT | {files_removed} files consumed | Stability: {self.stability:.2f} |\n"
            
            with open(self.journal_path, "a") as f:
                f.write(entry)
            return True
        return False