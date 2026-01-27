import slideshow_engine

# 1. In AxeHybrideGUI.__init__, add a background label:
self.bg_label = tk.Label(self.root)
self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
self.bg_label.lower() # Keep it behind other elements

# 2. In your update_loop method:
if self.presentation_mode:
    # Change background vision every 60 seconds (Tesla 6 sync)
    if int(time.time()) % 60 == 0:
        new_vision = slideshow_engine.get_next_vision_image(self.root.winfo_width(), self.root.winfo_height())
        if new_vision:
            self.bg_label.config(image=new_vision)
            self.bg_label.image = new_vision # Prevent garbage collection