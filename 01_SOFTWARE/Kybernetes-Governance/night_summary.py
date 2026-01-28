import resonance_reward

# Inside generate_night_report(), after Chronos analysis:
# Logic: If current speed is 20% higher than average or ahead of date
if speed > 1.2: # Example threshold [cite: 2026-01-26]
    reward_msg = resonance_reward.trigger_victory_reward()
    report += f"\n## 🎁 RESONANCE REWARD\n"
    report += f"- {reward_msg}\n"
    report += "- **Status**: Synergy confirmed. Your pace exceeds the simulation's constraints.\n"