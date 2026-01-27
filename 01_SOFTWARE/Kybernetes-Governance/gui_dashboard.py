import tkinter as tk
from tkinter import ttk
import os, time

# Automatic paths fix
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class CyberDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("AXE HYBRIDE - CYBER INTERFACE")
        self.root.geometry("400x300")
        self.root.configure(bg="#0a0a0a")

        # Title
        self.label_title = tk.Label(root, text="SYSTEM RESONANCE", fg="#00ffff", bg="#0a0a0a", font=("Courier", 16, "bold"))
        self.label_title.pack(pady=10)

        # BPM Gauge
        self.bpm_var = tk.DoubleVar(value=0)
        self.label_bpm = tk.Label(root, text="BPM: --", fg="#00ffff", bg="#0a0a0a", font=("Courier", 30))
        self.label_bpm.pack()
        
        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=20)

        # Status
        self.label_status = tk.Label(root, text="INITIATING...", fg="#00ffff", bg="#0a0a0a", font=("Courier", 10))
        self.label_status.pack(side="bottom", pady=10)

        self.update_gui()

    def update_gui(self):
        try:
            # Read current CPU load (same logic as neural bridge)
            load = os.getloadavg()[0]
            bpm = min(max(70 + (load * 15), 60), 180)
            
            # Update Gauge
            self.bpm_var.set(bpm)
            self.progress['value'] = (bpm - 60) / 1.2 # Scale to 100%
            self.label_bpm.config(text=f"{bpm:.1f} BPM")

            # Tesla Harmonic Sync Check (3-6-9 logic)
            if int(bpm) % 3 == 0:
                self.root.configure(bg="#4b0082") # Indigo/Magenta pulse
                self.label_bpm.config(fg="#ff00ff")
                self.label_status.config(text="⚡ TESLA SYNC ACTIVE ⚡", fg="#ff00ff")
                os.system('afplay /System/Library/Sounds/Glass.aiff &')
            else:
                self.root.configure(bg="#0a0a0a")
                self.label_bpm.config(fg="#00ffff")
                self.label_status.config(text="SYSTEM RESONANCE STABLE", fg="#00ffff")

        except Exception as e:
            self.label_status.config(text=f"ERROR: {e}")

        self.root.after(800, self.update_gui)

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberDashboard(root)
    root.mainloop()