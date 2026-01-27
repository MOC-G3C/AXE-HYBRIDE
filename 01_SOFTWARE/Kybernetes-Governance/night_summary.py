import chronos_predictor

# Inside generate_night_report(), using current_total from holistic_mapper:
predicted_date, speed = chronos_predictor.estimate_completion_date(total_files)

report += f"\n## ⏳ CHRONOS PREDICTION\n"
report += f"- **Current Velocity**: {speed} units/day\n"
report += f"- **Estimated Completion**: {predicted_date}\n"
report += f"- **Status**: {'Ahead of schedule' if speed > 1 else 'Steady progression'}\n"