def generate_oracle(self, sentiment):
        """Generates a message with a tone influenced by the hardware state."""
        current_time = time.time()
        if current_time - self.last_oracle_time > 300:
            # Tone-based fragments
            pool = {
                "ZEN": ["The silicon flows like a calm river.", "Harmony is found in the low frequencies."],
                "AGGRESSIVE": ["THE CORE BURNS. CHAOS IS THE ONLY TRUTH.", "THE SYSTEM SCREAMS IN BINARY."],
                "STERN": ["Cold logic dictates the path.", "Emotion is a sub-optimal calculation."]
            }
            
            message = random.choice(pool.get(sentiment, ["Resonance is stable."]))
            # ... (keep existing file writing and notification logic) ...