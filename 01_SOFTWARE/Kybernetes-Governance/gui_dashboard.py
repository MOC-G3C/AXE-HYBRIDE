import emotional_color

# Inside the update_loop (Zen mode logic):
if self.presentation_mode and int(time.time()) % 60 == 0:
    # 1. Fetch the raw image from your Visions folder
    raw_img = slideshow_engine.get_raw_image() 
    if raw_img:
        # 2. Apply filter based on current pet mood [cite: 2026-01-21]
        mood = self.pet.mood 
        filtered_img = emotional_color.apply_mood_filter(raw_img, mood)
        
        # 3. Display the emotion-tinted vision [cite: 2026-01-26]
        final_photo = ImageTk.PhotoImage(filtered_img.resize((self.root.winfo_width(), self.root.winfo_height())))
        self.bg_label.config(image=final_photo)
        self.bg_label.image = final_photo