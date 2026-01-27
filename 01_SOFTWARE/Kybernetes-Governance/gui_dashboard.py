# 1. Add this at the top with other imports
sys.path.append(os.path.join(ROOT, "01_SOFTWARE/Entropic-Zoo-Protocol"))
from digital_life import DigitalOrganism

# 2. In __init__, initialize the organism
self.pet = DigitalOrganism("ECTO-01")
self.pet_label = tk.Label(self.tab1, text="", fg="#ff00ff", bg="#0a0a0a", font=("Courier", 12))
self.pet_label.pack(pady=10)

# 3. In update_loop, after gravity calculation
self.pet.evolve(bpm, r_factor, gravity)
self.pet_label.config(text=self.pet.get_status())