import tkinter as tk
from tkinter import ttk
import os, sys, time, pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Environment Setup
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(ROOT, "01_SOFTWARE/Turing-Landau-Protocol"))
sys.path.append(os.path.join(ROOT, "04_PHYSICS"))

import entropy_generator
import digital_gravity

CSV_PATH = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/pulse_history.csv")

class AxeHybrideGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AXE HYBRIDE - CORE INTERFACE")
        self.root.geometry("800x600")
        self.root.configure(bg="#0a0a0a")

        # Tabs
        self.notebook = ttk.Notebook(self.root)
        self.tab1 = tk.Frame(self.notebook, bg="#0a0a0a") # Resonance
        self.tab2 = tk.Frame(self.notebook, bg="#0a0a0a") # Logs
        self.notebook.add(self.tab1, text=" RESONANCE ")
        self.notebook.add(self.tab2, text=" ACTIVITY LOGS ")
        self.notebook.pack(expand=1, fill="both")

        # Display Elements
        self.label_bpm = tk.Label(self.tab1, text="BPM: --", fg="#00ffff", bg="#0a0a0a", font=("Courier", 50, "bold"))
        self.label_bpm.pack(pady=20)
        
        self.status_label = tk.Label(self.tab1, text="SYSTEM STABLE", fg="#00ff00", bg="#0a0a0a", font=("Courier", 12))
        self.status_label.pack()

        # Graph
        self.fig, self.ax = plt.subplots(figsize=(6, 3), dpi=100)
        self.fig.patch.set_facecolor('#0a0a0a')
        self.ax.set_facecolor('#0a0a0a')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.tab1)
        self.canvas.get_tk_widget().pack(pady=10)

        # Logs
        self.log_text = tk.Text(self.tab2, bg="#050505", fg="#ff00ff", font=("Courier", 10), state="disabled")
        self.log_text.pack(expand=True, fill="both", padx=10, pady=10)

        self.update_loop()

    def update_loop(self):
        try:
            load = os.getloadavg()[0]
            bpm = 70 + (load * 20)
            
            # Entropy & Gravity Logic [cite: 2026-01-26]
            r_factor = 3.5 + (min(load, 1.0) * 0.5)
            gravity = digital_gravity.calculate_gravity(bpm, load)
            
            self.label_bpm.config(text=f"{bpm:.1f} BPM")
            
            # Tesla Harmonic Sync (3-6-9)
            if int(bpm) % 3 == 0:
                self.label_bpm.config(fg="#ff00ff")
                os.system('afplay /System/Library/Sounds/Glass.aiff &')
                # Trigger Poetic Capture if high entropy
                if r_factor > 3.8:
                    entropy_generator.generate_capture(bpm, r_factor)
            else:
                self.label_bpm.config(fg="#00ffff")

            # Update Graph
            self.ax.clear()
            self.ax.plot([bpm]*10, color="cyan") # Simplified for rebuild
            self.ax.set_title(f"GRAVITY: {gravity} | CHAOS: {r_factor:.2f}", color="white")
            self.canvas.draw()

        except Exception as e: print(f"Update error: {e}")
        self.root.after(1000, self.update_loop)

if __name__ == "__main__":
    root = tk.Tk()
    app = AxeHybrideGUI(root)
    root.mainloop()