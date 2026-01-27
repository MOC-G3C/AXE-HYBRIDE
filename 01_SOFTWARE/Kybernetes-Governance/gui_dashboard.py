# In AxeHybrideGUI.__init__, add the button:
self.hunt_btn = ttk.Button(self.tab1, text="HUNT SYSTEM CACHE (🗄️)", command=self.execute_hunt)
self.hunt_btn.pack(pady=5)

# Add this method to the AxeHybrideGUI class:
def execute_hunt(self):
    # Safe cleaning of user cache [cite: 2021-01-21]
    cache_path = os.path.expanduser("~/Library/Caches")
    try:
        # Count files before cleaning
        files = [os.path.join(cache_path, f) for f in os.listdir(cache_path)]
        count = len(files)
        
        # Simulation of consumption (removing old cache files)
        # Note: In a real environment, we only remove files older than 7 days
        os.system("find ~/Library/Caches -type f -atime +7 -delete")
        
        if self.pet.hunt_cache(count):
            os.system('afplay /System/Library/Sounds/Morse.aiff &')
            self.add_log(f"🗄️ HUNT COMPLETE: {count} cache fragments consumed by Ectoplasm.")
    except Exception as e:
        self.add_log(f"Hunt Error: {e}")