class DigitalOrganism:
    def __init__(self, name="Ectoplasm-01", root_path="."):
        # ... (keep existing init) ...
        self.name = name
        self.max_trust = 100.0 # Standard ceiling
        self.trust = 100.0
        self.is_named = False

    def rename_ceremony(self, new_name):
        """Naming ritual: increases the capacity for trust and resonance."""
        if not self.is_named and new_name.strip():
            self.name = new_name
            self.is_named = True
            # Sacred Bonus: Max Trust is elevated by 50%
            self.max_trust = 150.0 
            self.trust = self.max_trust
            
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            entry = f"| {timestamp} | RITUAL | NAMING | Entity identified as: {self.name} | Max Trust: {self.max_trust}% |\n"
            with open(self.journal_path, "a") as f: f.write(entry)
            
            # Save identity in genetic core for next generations
            self.save_legacy()
            return True
        return False