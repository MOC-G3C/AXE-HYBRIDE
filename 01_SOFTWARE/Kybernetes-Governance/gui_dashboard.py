import museum_mode

# In AxeHybrideGUI.__init__, add:
self.museum_btn = ttk.Button(self.tab1, text="ACTIVATE MUSEUM MODE (🖼️)", command=self.open_museum)
self.museum_btn.pack(pady=5)

# Add the method:
def open_museum(self):
    if museum_mode.generate_gallery_view():
        self.add_log("🖼️ MUSEUM: Gallery updated on Desktop.")
        os.system("open ~/Desktop/AXE_HYBRIDE_GALLERY.html")