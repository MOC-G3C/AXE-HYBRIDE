import transmutation_engine

# In AxeHybrideGUI.__init__:
resonance = transmutation_engine.get_planetary_resonance()
planetary_color = resonance["color"]

# Apply to the UI header or specific borders [cite: 2021-01-21]
self.status_label.config(fg=planetary_color)
self.root.title(f"AXE_HYBRIDE | {resonance['planet']} Resonance Active")

# Print to terminal with planetary color
print(f"{resonance['ansi']}SYSTEM: Transmutation complete. Ruling planet: {resonance['planet']}\033[0m")