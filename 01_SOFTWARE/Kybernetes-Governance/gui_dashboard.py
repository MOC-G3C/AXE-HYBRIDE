import tkinter as tk
from tkinter import ttk, messagebox
import os, time, pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Automatic paths fix
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV_PATH = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/pulse_history.csv")
ARCHIVE_DIR = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/Archives")

class CyberDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("AXE HYBRIDE - CYBER INTERFACE")
        self.root.geometry("600x550") # Slightly taller for the button
        self.root.configure(bg="#0a0a0a")

        # Tab Controller
        self.notebook = ttk.Notebook(self.root)
        self.tab1 = tk.Frame(self.notebook, bg="#0a0a0a")
        self.tab2 = tk.Frame(self.notebook, bg="#0a0a0a")
        
        self.notebook.add(self.tab1, text=" RESONANCE ")
        self.notebook.add(self.tab2, text=" ANALYTICS ")
        self.notebook.pack(expand=1, fill="both")

        # --- TAB 1: RESONANCE ---
        self.label_title = tk.Label(self.tab1, text="SYSTEM RESONANCE", fg="#00ffff", bg="#0a0a0a", font=("Courier", 16, "bold"))
        self.label_title.pack(pady=10)
        self.label_bpm = tk.Label(self.tab1, text="BPM: --", fg="#00ffff", bg="#0a0a0a", font=("Courier", 40))
        self.label_bpm.pack(pady=20)
        self.progress = ttk.Progressbar(self.tab1, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        # --- TAB 2: ANALYTICS ---
        self.fig, self.ax = plt.subplots(figsize=(5, 3), dpi=100)
        self.fig.patch.set_facecolor('#0a0a0a')
        self.ax.set_facecolor('#0a0a0a')
        self.ax.tick_params(colors='cyan')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.tab2)
        self.canvas.get_tk_widget().pack(pady=10, fill="both", expand=True)

        # Export Button
        self.export_btn = ttk.Button(self.tab2, text="EXPORT GRAPH SNAPSHOT", command=self.save_snapshot)
        self.export_btn.pack(pady=10)

        self.update_all()

    def save_snapshot(self):
        """Saves the current plot as a PNG in the Archives folder."""
        try:
            os.makedirs(ARCHIVE_DIR, exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = os.path.join(ARCHIVE_DIR, f"snapshot_{timestamp}.png")
            self.fig.savefig(filename, facecolor='#0a0a0a')
            messagebox.showinfo("Export Success", f"Graph saved to:\n{filename}")
            # Tesla notification [cite: 2026-01-26]
            os.system(f'osascript -e \'display notification "Snapshot saved as {timestamp}.png" with title "Axe Hybride"\'')
        except Exception as e:
            messagebox.showerror("Export Error", str(e))

    def update_all(self):
        try:
            # Update Resonance (Tab 1)
            load = os.getloadavg()[0]
            bpm = min(max(70 + (load * 15), 60), 180)
            self.progress['value'] = (bpm - 60) / 1.2
            self.label_bpm.config(text=f"{bpm:.1f} BPM")

            # Tesla Harmonic Logic [cite: 2026-01-26]
            if int(bpm) % 3 == 0:
                self.label_bpm.config(fg="#ff00ff")
                os.system('afplay /System/Library/Sounds/Glass.aiff &')
            else:
                self.label_bpm.config(fg="#00ffff")

            # Update Plot (Tab 2)
            if os.path.exists(CSV_PATH):
                df = pd.read_csv(CSV_PATH, names=["Timestamp", "BPM", "Density"]).tail(30)
                self.ax.clear()
                self.ax.plot(df['BPM'].values, color='red', linewidth=2)
                self.ax.set_title("LIVE PULSE HISTORY", color='cyan')
                self.canvas.draw()

        except Exception as e:
            print(f"Error: {e}")

        self.root.after(1000, self.update_all)

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use('default')
    style.configure("TNotebook", background="#0a0a0a", borderwidth=0)
    style.configure("TNotebook.Tab", background="#333", foreground="white", padding=[10, 5])
    style.map("TNotebook.Tab", background=[("selected", "#00ffff")], foreground=[("selected", "black")])
    style.configure("TButton", padding=6, relief="flat", background="#333")
    
    app = CyberDashboard(root)
    root.mainloop()