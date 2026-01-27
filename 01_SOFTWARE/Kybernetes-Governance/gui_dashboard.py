# In your update_loop method:
# Pass self.veto_active to the evolve function
self.pet.evolve(bpm, r_factor, gravity, self.veto_active)

# The pet_label will automatically show the trust levels 
# via the updated get_status() method.
self.pet_label.config(text=self.pet.get_status())