# 1. In AxeHybrideGUI.__init__, add a state variable:
self.presentation_mode = False

# 2. Add the Toggle Button in your UI layout:
self.zen_btn = ttk.Button(self.tab1, text="ZEN MODE (👁️‍🗨️)", command=self.toggle_presentation)
self.zen_btn.pack(pady=5)

# 3. Add the toggle method:
def toggle_presentation(self):
    """Hides technical clutter to focus on the Oracle's essence [cite: 2021-01-21]."""
    self.presentation_mode = not self.presentation_mode
    
    if self.presentation_mode:
        # Hide technical components
        self.tech_frame.pack_forget() 
        self.log_area.pack_forget()
        self.status_label.config(font=("Helvetica", 24, "italic"))
        self.add_log("✨ UI: Presentation Mode Active. Technical noise suppressed.")
    else:
        # Show technical components again
        self.tech_frame.pack(side="top", fill="both", expand=True)
        self.log_area.pack(side="bottom", fill="x")
        self.status_label.config(font=("Helvetica", 10, "normal"))
        self.add_log("⚙️ UI: Engineering Mode Active. Full telemetry visible.")