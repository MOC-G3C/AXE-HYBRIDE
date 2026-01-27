import tkinter as tk
from tkinter import ttk, messagebox
import os, time, pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Automatic paths fix
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSV_PATH = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/pulse_history.csv")
ARCHIVE_DIR = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/Archives")

# --- CONFIGURATION ---
APPS_TO_CLOSE = ["GarageBand", "Google Chrome", "Safari", "Final Cut Pro"]
NIGHT_MODE_BPM = 75  # Threshold for Deep Calm

class CyberDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("AXE HYBRIDE - CYBER INTERFACE")
        self.root.geometry("600x650")
        self.root.configure(bg="#0a0a0a")

        self.stress_timer = 0
        self.night_mode_active = False

        # Tab Controller
        self.notebook = ttk.Notebook(self.root)
        self.tab1 = tk.Frame(self.notebook, bg="#0a0a0a")
        self.tab2 = tk.Frame(self.notebook, bg="#0a0a0a")
        self.tab3 = tk.Frame(self.notebook, bg="#0a0a0a")
        
        self.notebook.add(self.tab1, text=" RESONANCE ")
        self.notebook.add(self.tab2, text=" ANALYTICS ")
        self.notebook.add(self.tab3, text=" LOGS ")
        self.notebook.pack(expand=1, fill="both")

        # TAB 1
        self.label_bpm = tk.Label(self.tab1, text="BPM: --", fg="#00ffff", bg="#0a0a0a", font=("Courier", 40))
        self.label_bpm.pack(pady=40)
        self.progress = ttk.Progressbar(self.tab1, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)
        self.security_label = tk.Label(self.tab1, text="SHIELD: ACTIVE", fg="#00ff00", bg="#0a0a0a", font=("Courier", 10))
        self.security_label.pack(pady=5)

        # TAB 2 & 3 Setup (Analytics and Logs)
        self.fig, self.ax = plt.subplots(figsize=(5, 3), dpi=100)
        self.fig.patch.set_facecolor('#0a0a0a')
        self.ax.set_facecolor('#0a0a0a')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.tab2)
        self.canvas.get_tk_widget().pack(pady=10, fill="both", expand=True)
        
        self.log_text = tk.Text(self.tab3, bg="#050505", fg="#ff00ff", font=("Courier", 10), state="disabled")
        self.log_text.pack(expand=True, fill="both", padx=10, pady=10)
        self.last_logged_sync = ""

        self.update_all()

    def add_log(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] {message}\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")

    def trigger_night_mode(self):
        """Reduces brightness and starts a soothing atmosphere."""
        if not self.night_mode_active:
            self.add_log("🌙 NIGHT MODE: DEEP CALM DETECTED")
            # Dim the screen (macOS key simulation)
            os.system("osascript -e 'tell application \"System Events\" to repeat 16 times' -e 'key code 107' -e 'end repeat'")
            # Launch relaxing music (Make sure you have a playlist named 'Relax' or change below)
            os.system("osascript -e 'tell application \"Music\" to play playlist \"Relax\"'")
            self.night_mode_active = True
            self.security_label.config(text="MODE: NIGHT / ZEN", fg="#bb86fc")

    def update_all(self):
        try:
            load = os.getloadavg()[0]
            bpm = min(max(70 + (load * 15), 60), 180)
            self.label_bpm.config(text=f"{bpm:.1f} BPM")
            self.progress['value'] = (bpm - 60) / 1.2

            # Night Mode Logic
            if bpm < NIGHT_MODE_BPM:
                self.trigger_night_mode()
            else:
                self.night_mode_active = False

            # Tesla Harmonic [cite: 2026-01-26]
            if int(bpm) % 3 == 0:
                self.label_bpm.config(fg="#ff00ff")
                os.system('afplay /System/Library/Sounds/Glass.aiff &')
            else:
                self.label_bpm.config(fg="#00ffff")

        except Exception as e: print(f"Error: {e}")
        self.root.after(1000, self.update_all)

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberDashboard(root)
    root.mainloop()