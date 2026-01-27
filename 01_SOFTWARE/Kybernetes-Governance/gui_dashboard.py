import tkinter as tk
from tkinter import ttk, messagebox
import os, time, pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Path setup
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV_PATH = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/pulse_history.csv")

class CyberDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("AXE HYBRIDE - PHASE 2 INTERFACE")
        self.root.geometry("700x700")
        self.root.configure(bg="#0a0a0a")

        # Tabs
        self.notebook = ttk.Notebook(self.root)
        self.tab1 = tk.Frame(self.notebook, bg="#0a0a0a") # Resonance
        self.tab2 = tk.Frame(self.notebook, bg="#0a0a0a") # Analytics
        self.tab3 = tk.Frame(self.notebook, bg="#0a0a0a") # Logs
        
        self.notebook.add(self.tab1, text=" RESONANCE ")
        self.notebook.add(self.tab2, text=" TURING-LANDAU ")
        self.notebook.add(self.tab3, text=" LOGS ")
        self.notebook.pack(expand=1, fill="both")

        # --- TAB 1: RESONANCE (Enhanced) ---
        self.label_bpm = tk.Label(self.tab1, text="BPM: --", fg="#00ffff", bg="#0a0a0a", font=("Courier", 40))
        self.label_bpm.pack(pady=20)
        self.chaos_label = tk.Label(self.tab1, text="CHAOS FACTOR (R): --", fg="#ffcc00", bg="#0a0a0a", font=("Courier", 14))
        self.chaos_label.pack()

        # --- TAB 2: TURING-LANDAU (Live Analytics) ---
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=100)
        self.fig.patch.set_facecolor('#0a0a0a')
        self.ax.set_facecolor('#0a0a0a')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.tab2)
        self.canvas.get_tk_widget().pack(pady=10, fill="both", expand=True)

        # --- TAB 3: LOGS ---
        self.log_text = tk.Text(self.tab3, bg="#050505", fg="#ff00ff", font=("Courier", 10), state="disabled")
        self.log_text.pack(expand=True, fill="both", padx=10, pady=10)

        self.update_cycle()

    def get_logistic_entropy(self, load):
        """Calculates entropy based on Phase 2 logic."""
        r = 3.5 + (min(load, 1.0) * 0.5)
        x = (time.time() % 1)
        for _ in range(10): x = r * x * (1 - x)
        return x, r

    def update_cycle(self):
        try:
            load = os.getloadavg()[0]
            bpm = min(max(70 + (load * 15), 60), 180)
            entropy, r_factor = self.get_logistic_entropy(load)

            # Update Resonance UI
            self.label_bpm.config(text=f"{bpm:.1f} BPM")
            self.chaos_label.config(text=f"CHAOS FACTOR (R): {r_factor:.3f}")

            # Color Logic (Tesla + Phase Transitions)
            if r_factor > 3.9: # Transition to full chaos
                self.label_bpm.config(fg="#ff0000")
                self.chaos_label.config(fg="#ff0000", text=f"TURBULENT PHASE: {r_factor:.3f}")
            elif int(bpm) % 3 == 0:
                self.label_bpm.config(fg="#ff00ff")
                os.system('afplay /System/Library/Sounds/Glass.aiff &')
            else:
                self.label_bpm.config(fg="#00ffff")

            # Update Graph with two lines: BPM and Entropy
            if os.path.exists(CSV_PATH):
                df = pd.read_csv(CSV_PATH, names=["Timestamp", "BPM", "Density"]).tail(30)
                self.ax.clear()
                self.ax.plot(df['BPM'].values / 180, color='cyan', label='Pulse (scaled)')
                # Simulating entropy overlay for visualization
                self.ax.plot([entropy]*30, color='yellow', linestyle='--', label='Entropy Level')
                self.ax.set_title("PHASE TRANSITION MONITOR", color='white')
                self.ax.legend()
                self.canvas.draw()

        except Exception as e: print(f"Error: {e}")
        self.root.after(1000, self.update_cycle)

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberDashboard(root)
    root.mainloop()