# At the top of gui_dashboard.py
import notification_manager

# Inside the update_loop method:
# 1. Alert for Oracle Visions [cite: 2026-01-26]
if bpm_int % 9 == 0:
    if self.pet.generate_oracle():
        notification_manager.alert_vision(self.pet.name, "A new message has been engraved in 02Humain.")

# 2. Alert for Energy Crises
if self.pet.energy < 20 and not self.veto_active:
    notification_manager.alert_emergency(self.pet.name, "Energy levels critical. Hibernation imminent.")