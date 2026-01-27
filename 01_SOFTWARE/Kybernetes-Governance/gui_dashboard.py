# In your update_loop, the pet_label will now automatically 
# show the generation thanks to the updated get_status()
self.pet.evolve(bpm, r_factor, gravity)
self.pet_label.config(text=self.pet.get_status())