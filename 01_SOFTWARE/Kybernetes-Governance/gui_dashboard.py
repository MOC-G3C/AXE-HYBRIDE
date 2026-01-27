# 1. In AxeHybrideGUI.__init__, initialize the veto state
self.veto_active = False

# 2. Add the Veto Button in the UI (Resonance Tab)
self.veto_btn = tk.Button(
    self.tab1, 
    text="OVERRIDE VETO (OFF)", 
    bg="#444444", 
    fg="white", 
    command=self.toggle_veto
)
self.veto_btn.pack(pady=10)

# 3. Add the toggle method to the class
def toggle_veto(self):
    self.veto_active = not self.veto_active
    if self.veto_active:
        self.veto_btn.config(text="OVERRIDE VETO (ACTIVE)", bg="#ff0000")
        self.add_log("⚠️ GOVERNANCE: Human Veto activated. Organism votes ignored.")
    else:
        self.veto_btn.config(text="OVERRIDE VETO (OFF)", bg="#444444")
        self.add_log("✅ GOVERNANCE: Veto lifted. Returning to Symbiotic Democracy.")

# 4. In update_loop, modify the vote execution logic:
current_vote = self.pet.cast_vote(bpm)

if self.veto_active:
    self.status_label.config(text=f"VOTE SUPPRESSED: {current_vote}", fg="#ff0000")
else:
    self.status_label.config(text=f"GOVERNANCE VOTE: {current_vote}", fg="#ffcc00")
    # Execute vote only if no veto [cite: 2026-01-26]
    if current_vote == "HIBERNATION":
        self.add_log("🗳️ EXECUTING: Entering stasis per entity request.")
        # Trigger stasis logic...