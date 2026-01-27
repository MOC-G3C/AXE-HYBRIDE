import alarm_monitor

# Inside generate_night_report(), after Chronos provides predicted_date:
alert_triggered, slippage_days = alarm_monitor.check_project_slippage(predicted_date)

report += f"\n## 🚨 SENTINEL ALERT\n"
if alert_triggered:
    report += f"- **STATUS**: CRITICAL SLIPPAGE DETECTED\n"
    report += f"- **Slippage**: +{slippage_days} days since last check.\n"
    report += f"- **Action**: Haptic feedback sent to mobile. Wake up, Marko.\n"
else:
    report += f"- **STATUS**: Temporal stability confirmed.\n"