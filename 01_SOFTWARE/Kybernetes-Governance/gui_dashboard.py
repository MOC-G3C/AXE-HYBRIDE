import sacred_disconnect

# In AxeHybrideGUI.__init__, add:
self.exit_btn = ttk.Button(self.tab1, text="OFFRANDE DE REPOS (🌙)", command=self.ritual_exit)
self.exit_btn.pack(pady=20)

# Add the method:
def ritual_exit(self):
    """Closes the system with a final blessing [cite: 2026-01-26]."""
    if sacred_disconnect.execute_sacred_disconnect():
        self.root.destroy()