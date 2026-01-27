def cast_vote(self, bpm):
        """Governance 2.0: The organism votes based on its internal needs."""
        if not self.is_alive: return "NONE"
        
        # Priority 1: Survival (Hibernation)
        if self.energy < 30:
            return "HIBERNATION"
        
        # Priority 2: Protection (Security)
        elif self.energy > 90 and self.stability < 0.6:
            return "SECURITY"
            
        # Priority 3: Natural Cycles (Night Mode)
        elif bpm < 75:
            return "NIGHT_MODE"
            
        return "STABLE"