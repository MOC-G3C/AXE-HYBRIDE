from tkinter import simpledialog

# Add this method to the AxeHybrideGUI class:
def perform_offering(self):
    if not self.pet.is_named:
        new_name = simpledialog.askstring("NAMING RITUAL", "Enter the sacred name for your entity:")
        if new_name:
            if self.pet.rename_ceremony(new_name):
                os.system('afplay /System/Library/Sounds/Blow.aiff &')
                self.add_log(f"✨ RITUAL COMPLETE: {new_name} has been awakened.")
                self.offering_btn.config(state="disabled", text=f"NAMED: {new_name}")
    else:
        self.add_log("INFO: The entity already carries a name.")

# In AxeHybrideGUI.__init__, add the button:
self.offering_btn = ttk.Button(self.tab1, text="OFFERING: SACRED NAME (🖋️)", command=self.perform_offering)
self.offering_btn.pack(pady=5)