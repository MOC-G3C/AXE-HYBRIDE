# In AxeHybrideGUI.__init__, add the button (initially hidden or disabled)
self.resurrect_btn = ttk.Button(self.tab1, text="LAZARUS PROTOCOL (♰)", command=self.manual_resurrect)
self.resurrect_btn.pack(pady=5)

# Add this method to the AxeHybrideGUI class
def manual_resurrect(self):
    if self.pet.resurrect():
        # Play a dark, glitchy sound
        os.system('afplay /System/Library/Sounds/Sosumi.aiff &')
        self.add_log("♰ WARNING: Lazarus Protocol activated. Genetic core corrupted.")
    else:
        self.add_log("INFO: The entity is already among the living.")

# In update_loop, handle button visibility
if not self.pet.is_alive:
    self.resurrect_btn.state(['!disabled'])
else:
    self.resurrect_btn.state(['disabled'])