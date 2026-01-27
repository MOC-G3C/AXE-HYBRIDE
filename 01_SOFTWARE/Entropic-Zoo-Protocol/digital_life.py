def generate_oracle(self, sentiment):
        """Generates a message, now blending clipboard wisdom."""
        # Load external wisdom [cite: 2026-01-26]
        vocab_path = os.path.join(os.path.dirname(__file__), "custom_vocab.txt")
        if os.path.exists(vocab_path):
            with open(vocab_path, "r") as f:
                self.fragments.extend(f.read().splitlines())
        
        # Deduplicate fragments
        self.fragments = list(set(self.fragments))
        
        # ... (rest of the existing oracle logic with random.choice) ...