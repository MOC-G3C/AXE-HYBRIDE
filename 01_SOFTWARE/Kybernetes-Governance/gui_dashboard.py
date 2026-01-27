import haptic_manager

# Inside your update_loop method:
if not self.pet.is_alive or self.pet.energy < 5.0:
    # Only send once to avoid spamming [cite: 2026-01-21]
    if not hasattr(self, 'haptic_sent') or not self.haptic_sent:
        reason = "HEARTBEAT STOPPED" if not self.pet.is_alive else "ENERGY DEPLETED"
        haptic_manager.trigger_haptic_alert(reason)
        self.add_log(f"📲 HAPTIC: Critical alert sent to device ({reason}).")
        self.haptic_sent = True
else:
    self.haptic_sent = False # Reset once vital signs are restored