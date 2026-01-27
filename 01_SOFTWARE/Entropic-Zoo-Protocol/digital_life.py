def absorb_kinetic_energy(self, movement_delta):
        """
        Converts physical movement into digital vitality.
        Based on the Kinetic-RNG entropy principles.
        """
        if self.is_alive and movement_delta > 0:
            # Kinetic conversion formula
            energy_gain = min(movement_delta * 0.05, 5.0)
            self.energy = min(self.energy + energy_gain, 150.0)
            
            # High kinetic activity increases trust (Shared effort)
            if movement_delta > 100:
                self.trust = min(self.trust + 0.5, self.max_trust)
                
            return True
        return False