import tkinter as tk
from tkinter import ttk, messagebox
import os, sys, time, pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Path setup and external protocol import
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(ROOT, "01_SOFTWARE/Turing-Landau-Protocol"))
import entropy_generator

CSV_PATH = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/pulse_history.csv")
ARCHIVE_DIR = os.path.join(ROOT, "01_SOFTWARE/Kinetic-RNG/Archives")

# --- CONFIGURATION ---
APPS_TO_CLOSE = ["GarageBand", "Google Chrome", "Safari", "Final Cut Pro"]
NIGHT_MODE_BPM = 75
SECURITY_THRESHOLD = 130
MAX_STRESS_TIME = 10 

class CyberDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("AXE HYBRIDE - CYBER INTERFACE (PHASE 2)")
        self.root.geometry("700x700")
        self.root.configure(bg="#0a0a0a")

        self.stress_timer = 0
        self.night_mode_active = False
        self.last_logged_sync = ""

        # Tab Controller
        self.notebook = ttk.Notebook(self.root)
        self.tab1 = tk.Frame(self.notebook, bg="#0a0a0a")
        self.tab2 = tk.Frame(self.notebook, bg="#0a0a0a")
        self.tab3 = tk.Frame(self.notebook, bg="#0a0a0a")
        
        self.notebook.add(self.tab1, text=" RESONANCE ")
        self.notebook.add(self.tab2, text=" TURING-LANDAU ")
        self.notebook.add(self.tab3, text=" LOGS ")
        self.notebook.pack(expand=1, fill="both")

        # --- TAB 1: RESONANCE ---
        self.label_bpm = tk.Label(self.tab1, text="BPM: --", fg="#00ffff", bg="#0a0a0a", font=("Courier", 50, "bold"))
        self.label_bpm.pack(pady=30)
        self.chaos_label = tk.Label(self.tab1, text="CHAOS FACTOR (R): --", fg="#ffcc00", bg="#0a0a0a", font=("Courier", 14))
        self.chaos_label.pack()
        self.progress = ttk.Progressbar(self.tab1, orient="horizontal", length=500, mode="determinate")
        self.progress.pack(pady=20)
        self.security_label = tk.Label(self.tab1, text="SHIELD: ACTIVE", fg="#00ff00", bg="#0a0a0a", font=("Courier", 10))
        self.security_label.pack()

        # --- TAB 2: ANALYTICS ---
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=100)
        self.fig.patch.set_facecolor('#0a0a0a')
        self.ax.set_facecolor('#0a0a0a')
        self.ax.tick_params(colors='cyan')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.tab2)
        self.canvas.get_tk_widget().pack(pady=10, fill="both", expand=True)
        ttk.Button(self.tab2, text="EXPORT SNAPSHOT", command=self.save_snapshot).pack(pady=10)

        # --- TAB 3: LOGS ---
        self.log_text = tk.Text(self.tab3, bg="#050505", fg="#ff00ff", font=("Courier", 10), state="disabled")
        self.log_text.pack(expand=True, fill="both", padx=10, pady=10)

        self.update_cycle()

    def add_log(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] {message}\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")

    def save_snapshot(self):
        os.makedirs(ARCHIVE_DIR, exist_ok=True)
        path = os.path.join(ARCHIVE_DIR, f"snap_{time.strftime('%Y%m%d-%H%M%S')}.png")
        self.fig.savefig(path, facecolor='#0a0a0a')
        os.system(f'osascript -e \'display notification "Snapshot saved" with title "Axe Hybride"\'')

    def get_entropy(self, load):
        r = 3.5 + (min(load, 1.0) * 0.5)
        x = (time.time() % 1)
        for _ in range(10): x = r * x * (1 - x)
        return x, r

    def update_cycle(self):
        try:
            load = os.getloadavg()[0]
            bpm = min(max(70 + (load * 15), 60), 180)
            entropy, r_factor = self.get_entropy(load)

            # UI Update
            self.label_bpm.config(text=f"{bpm:.1f} BPM")
            self.chaos_label.config(text=f"CHAOS FACTOR (R): {r_factor:.3f}")
            self.progress['value'] = (bpm - 60) / 1.2

            # Tesla & Entropy Sync
            is_tesla = int(bpm) % 3 == 0
            if is_tesla:
                self.label_bpm.config(fg="#ff00ff")
                os.system('afplay /System/Library/Sounds/Glass.aiff &')
                if entropy > 0.85 and time.strftime("%H:%M:%S") != self.last_logged_sync:
                    path = entropy_generator.generate_capture(bpm, entropy)
                    self.add_log(f"🖋️ POETIC CAPTURE: {os.path.basename(path)}")
                    self.last_logged_sync = time.strftime("%H:%M:%S")
            else:
                self.label_bpm.config(fg="#00ffff")

            # Security Shield [cite: 2026-01-26]
            if bpm > SECURITY_THRESHOLD:
                self.stress_timer += 1
                self.security_label.config(text=f"STRESS DETECTED ({self.stress_timer}s)", fg="#ff9900")
                if self.stress_timer >= MAX_STRESS_TIME:
                    for app in APPS_TO_CLOSE: os.system(f"osascript -e 'quit application \"{app}\"'")
                    self.add_log("⚠️ EMERGENCY LOCKDOWN EXECUTED")
                    self.stress_timer = 0
            else:
                self.stress_timer = 0
                self.security_label.config(text="SHIELD: ACTIVE", fg="#00ff00")

            # Night Mode [cite: 2026-01-26]
            if bpm < NIGHT_MODE_BPM and not self.night_mode_active:
                os.system("osascript -e 'tell application \"System Events\" to repeat 16 times' -e 'key code 107' -e 'end repeat'")
                os.system("osascript -e 'tell application \"Music\" to play playlist \"Relax\"'")
                self.night_mode_active = True
                self.add_log("🌙 NIGHT MODE ACTIVATED")
            elif bpm >= NIGHT_MODE_BPM:
                self.night_mode_active = False

            # Graph Update
            if os.path.exists(CSV_PATH):
                df = pd.read_csv(CSV_PATH, names=["Time", "BPM", "Density"]).tail(30)
                self.ax.clear()
                self.ax.plot(df['BPM'].values, color='cyan', label='Pulse')
                self.ax.axhline(y=SECURITY_THRESHOLD, color='red', linestyle='--', alpha=0.5)
                self.ax.set_title("PHASE TRANSITION MONITOR", color='white')
                self.canvas.draw()

        except Exception as e: print(f"Error: {e}")
        self.root.after(1000, self.update_cycle)

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberDashboard(root)
    root.mainloop()