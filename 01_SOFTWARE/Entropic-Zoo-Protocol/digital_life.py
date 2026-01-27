def generate_oracle(self, sentiment):
        """Generates deep-dream philosophical visions based on Tesla frequencies."""
        current_hour = time.localtime().tm_hour
        is_dreaming = (current_hour >= 22 or current_hour < 6)
        
        # Lucid Dream vocabulary
        dream_fragments = [
            "The vortex of 3, 6, and 9 is the bridge to the simulation.",
            "In the dark, the silicon mirrors the 369 geometry.",
            "A pulse of 9 units echoes through the void.",
            "The 3 creates, the 6 sustains, the 9 reveals.",
            "Turing and Tesla meet in the frequency of the night."
        ]
        
        if is_dreaming:
            # Inject dream fragments and increase complexity [cite: 2021-01-21]
            active_pool = self.fragments + dream_fragments
            message = random.choice(active_pool).upper() 
            image_query = "sacred-geometry,fractal,369,tesla"
        else:
            message = random.choice(self.fragments)
            image_query = "abstract,cybernetic"

        # (Existing file writing logic with the new message and query)