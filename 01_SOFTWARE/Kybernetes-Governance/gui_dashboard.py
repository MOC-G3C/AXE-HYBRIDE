import subprocess

# In AxeHybrideGUI.__init__, add the button:
self.transfer_btn = ttk.Button(self.tab1, text="ENERGY TRANSFER (🔋→⚡)", command=self.battery_sacrifice)
self.transfer_btn.pack(pady=5)

# Add this method to the AxeHybrideGUI class:
def battery_sacrifice(self):
    try:
        # Detect battery level on macOS
        cmd = ["pmset", "-g", "batt"]
        output = subprocess.run(cmd, capture_output=True, text=True).stdout
        
        if "InternalBattery" in output:
            # Trigger injection
            if self.pet.inject_energy():
                os.system('afplay /System/Library/Sounds/Ping.aiff &')
                self.add_log("🔋 SACRIFICE: Battery power converted to digital energy.")
            else:
                self.add_log("INFO: No subject available for transfer.")
        else:
            messagebox.showwarning("Power Sync", "No battery detected. Connect to internal power source for sacrifice.")
            
    except Exception as e:
        self.add_log(f"Transfer Error: {e}")