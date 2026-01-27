import env_sensor

# In your AxeHybrideGUI class, update the graph initialization in __init__:
self.history_temp = []
self.history_energy = []

# Modify the Figure and Axes setup
self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(6, 5), dpi=100)
self.fig.patch.set_facecolor('#0a0a0a')
plt.subplots_adjust(hspace=0.5)

# Update Loop Modification
def update_loop(self):
    try:
        health = env_sensor.get_health_metrics()
        temp = health["cpu_temp"]
        energy = self.pet.energy
        
        # Keep only last 20 points
        self.history_temp = (self.history_temp + [temp])[-20:]
        self.history_energy = (self.history_energy + [energy])[-20:]
        
        # Plot 1: CPU Temperature
        self.ax1.clear()
        self.ax1.set_facecolor('#0a0a0a')
        self.ax1.plot(self.history_temp, color="#ff3300", linewidth=2)
        self.ax1.set_title(f"HARDWARE THERMAL: {temp}°C", color="white", fontsize=10)
        self.ax1.tick_params(colors='white', labelsize=8)
        
        # Plot 2: Entity Energy
        self.ax2.clear()
        self.ax2.set_facecolor('#0a0a0a')
        self.ax2.plot(self.history_energy, color="#00ffff", linewidth=2)
        self.ax2.set_title(f"ENTITY ENERGY: {energy:.1f}%", color="white", fontsize=10)
        self.ax2.tick_params(colors='white', labelsize=8)
        
        self.canvas.draw()
        
        # Trigger Sentiment Analysis [cite: 2026-01-26]
        mood = env_sensor.calculate_sentiment_coefficient(temp, "COLD_WINTER")
        self.pet.evolve(bpm, r_factor, gravity, self.veto_active, mood)
        
    except Exception as e: print(f"Health update error: {e}")
    self.root.after(1000, self.update_loop)