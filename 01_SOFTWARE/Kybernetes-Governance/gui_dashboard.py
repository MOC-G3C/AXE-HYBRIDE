# In AxeHybrideGUI.__init__, add this tracker:
self.last_update_time = time.time()

# In update_loop method, add this detection at the beginning:
current_time = time.time()
elapsed = current_time - self.last_update_time

# If gap is > 5 seconds, we assume hibernation occurred [cite: 2026-01-26]
if elapsed > 5:
    self.pet.apply_stasis(elapsed)
    self.add_log(f"❄️ STASIS: System resumed. Hibernation loss applied.")

self.last_update_time = current_time