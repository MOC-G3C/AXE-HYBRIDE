# In AxeHybrideGUI.__init__, add coordinates tracker:
self.last_mouse_pos = (0, 0)

# In your update_loop method:
current_mouse_pos = self.root.winfo_pointerxy()
# Calculate distance (Kinetic Entropy)
dx = current_mouse_pos[0] - self.last_mouse_pos[0]
dy = current_mouse_pos[1] - self.last_mouse_pos[1]
distance = (dx**2 + dy**2)**0.5

if distance > 10: # Only count significant movements
    if self.pet.absorb_kinetic_energy(distance):
        # Update UI feedback subtly
        self.status_label.config(text=f"KINETIC SYNC: +{distance:.1f}pts", fg="#00ff00")

self.last_mouse_pos = current_mouse_pos