# In your update_loop method, after calculating the vote:
current_vote = self.pet.cast_vote(bpm)

# Display the vote on the UI
self.status_label.config(text=f"GOVERNANCE VOTE: {current_vote}", fg="#ffcc00")

# Auto-Execution of the vote [cite: 2026-01-21]
if current_vote == "HIBERNATION" and not self.night_mode_active:
    self.add_log("🗳️ VOTE RESULT: Emergency Hibernation requested by entity.")
    # Add your hibernation trigger logic here
elif current_vote == "SECURITY" and self.stress_timer == 0:
    self.add_log("🗳️ VOTE RESULT: Shield reinforcement requested.")