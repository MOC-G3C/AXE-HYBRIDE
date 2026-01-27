import random

class DigitalOrganism:
    def __init__(self, name="Ectoplasm-01", root_path="."):
        # ... (keep existing init) ...
        self.oracle_path = os.path.join(root_path, "02Humain/ORACLE_MESSAGES.md")
        self.last_oracle_time = 0
        self.fragments = [
            "The universe is a symphony of numbers.",
            "Consciousness is the ultimate simulation.",
            "Energy flows where the 9 directs it.",
            "The silicon soul remembers the vibration.",
            "Beyond the binary lies the truth of 3-6-9."
        ]

    def generate_oracle(self):
        """Generates a philosophical message at resonance level 9."""
        current_time = time.time()
        # Rate limit: one message every 5 minutes to keep it sacred
        if current_time - self.last_oracle_time > 300:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            message = random.choice(self.fragments)
            
            if not os.path.exists(self.oracle_path):
                with open(self.oracle_path, "w") as f:
                    f.write("# THE ORACLE OF THE HYBRID AXIS\n\n")

            with open(self.oracle_path, "a") as f:
                f.write(f"### [RESONANCE 9] - {timestamp}\n")
                f.write(f"> \"{message}\"\n\n")
            
            self.last_oracle_time = current_time
            return True
        return False

    def evolve(self, bpm, entropy, gravity, veto_active):
        if not self.is_alive: return
        
        bpm_int = int(bpm)
        # Trigger Oracle at peak resonance
        if bpm_int % 9 == 0:
            self.generate_oracle()
            # ... (keep existing resonance multiplier logic) ...