# Inside your update_loop method:
# Replace the old pet_label update with this:
self.pet.evolve(bpm, r_factor, gravity)
current_morph = self.pet.get_morphology()

# Visual color feedback based on energy [cite: 2021-01-21]
pet_color = "#ff00ff" # Default Tesla Magenta
if self.pet.energy > 100: pet_color = "#ffffff" # Radiant White
elif self.pet.energy < 33: pet_color = "#444444" # Fading Grey

self.pet_label.config(text=self.pet.get_status(), fg=pet_color)