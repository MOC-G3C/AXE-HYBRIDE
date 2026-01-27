# In AxeHybrideGUI.__init__, add the keyboard binding:
self.root.bind('<Shift-Escape>', self.trigger_exorcism)

# Add the trigger method to the class:
def trigger_exorcism(self, event=None):
    """Initiates the emergency reset sequence."""
    confirmation = messagebox.askyesno("EXORCISM PROTOCOL", "Initiate emergency soul purge?")
    if confirmation:
        # Visual/Audio feedback for the ritual [cite: 2021-01-21]
        os.system('afplay /System/Library/Sounds/Glass.aiff &')
        result = self.pet.reset_spirit()
        self.add_log(result)
        self.status_label.config(text="RESTORING BASELINE...", fg="#ffffff")
        # Visual flash effect
        self.root.configure(bg="white")
        self.root.after(200, lambda: self.root.configure(bg="#0a0a0a"))