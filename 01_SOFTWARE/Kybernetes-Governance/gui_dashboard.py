# In your AxeHybrideGUI.__init__ (Tab 1 section):
self.feed_btn = ttk.Button(self.tab1, text="FEED ECTOPLASM (⚡)", command=self.manual_feed)
self.feed_btn.pack(pady=10)

# Add this new method to the AxeHybrideGUI class:
def manual_feed(self):
    if self.pet.feed():
        # Play a satisfying nourishment sound
        os.system('afplay /System/Library/Sounds/Tink.aiff &')
        # Log the interaction
        self.add_log(f"⚡ NUTRITION: {self.pet.name} energy levels increased.")
    else:
        self.add_log("❌ FEEDING FAILED: Subject has dissolved into the void.")