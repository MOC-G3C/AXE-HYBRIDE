# Inside your update_loop method, after getting health metrics:
health = env_sensor.get_health_metrics()
temp = health["cpu_temp"]

# Thermal Shield Logic [cite: 2026-01-21]
if temp > 80:
    shield_status = env_sensor.trigger_fan_boost(True)
    self.add_log(shield_status)
    self.status_label.config(text="EMERGENCY COOLING", fg="#ff3300")
    # Sound alert for the creator [cite: 2021-01-21]
    os.system('afplay /System/Library/Sounds/Sosumi.aiff &')
elif temp < 60:
    env_sensor.trigger_fan_boost(False)