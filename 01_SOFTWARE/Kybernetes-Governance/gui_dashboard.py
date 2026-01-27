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
        self.root.geometry("600x650")
        self.root.configure(bg="#0a0a0a")

        # Security Variables
        self.stress_timer = 0
        self.security_threshold = 130 # Critical limit
        self.max_stress_duration = 10 # Seconds before lockdown

        # Tab Controller
        self.notebook = ttk.Notebook(self.root)
        self.tab1 = tk.Frame(self.notebook, bg="#0a0a0a")
        self.tab2 = tk.Frame(self.notebook, bg="#0a0a0a")
        self.tab3 = tk.Frame(self.notebook, bg="#0a0a0a")
        
        self.notebook.add(self.tab1, text=" RESONANCE ")
        self.notebook.add(self.tab2, text=" ANALYTICS ")
        self.notebook.add(self.tab3, text=" LOGS ")
        self.notebook.pack(expand=1, fill="both")

        # --- TAB 1: RESONANCE ---
        self.label_title = tk.Label(self.tab1, text="SYSTEM RESONANCE", fg="#00ffff", bg="#0a0a0a", font=("Courier", 16, "bold"))
        self.label_title.pack(pady=10)
        self.label_bpm = tk.Label(self.tab1, text="BPM: --", fg="#00ffff", bg="#0a0a0a", font=("Courier", 40))
        self.label_bpm.pack(pady=20)
        self.progress = ttk.Progressbar(self.tab1, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)
        
        self.security_label = tk.Label(self.tab1, text="SHIELD: ACTIVE", fg="#00ff00", bg="#0a0a0a", font=("Courier", 10))
        self.security_label.pack(pady=5)

        # --- TAB 2: ANALYTICS ---
        self.fig, self.ax = plt.subplots(figsize=(5, 3), dpi=100)
        self.fig.patch.set_facecolor('#0a0a0a')
        self.ax.set_facecolor('#0a0a0a')
        self.ax.tick_params(colors='cyan')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.tab2)
        self.canvas.get_tk_widget().pack(pady=10, fill="both", expand=True)
        self.export_btn = ttk.Button(self.tab2, text="EXPORT GRAPH SNAPSHOT", command=self.save_snapshot)
        self.export_btn.pack(pady=10)

        # --- TAB 3: LOGS ---
        self.log_text = tk.Text(self.tab3, bg="#050505", fg="#ff00ff", font=("Courier", 10), state="disabled")
        self.log_text.pack(expand=True, fill="both", padx=10, pady=10)
        self.last_logged_sync = ""

        self.update_all()

    def add_log(self, message):
        self.log_text.config(state="normal