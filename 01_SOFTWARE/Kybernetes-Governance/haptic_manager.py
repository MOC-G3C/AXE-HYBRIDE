import requests # Requires 'pip install requests' [cite: 2026-01-22]

def trigger_haptic_alert(reason):
    """Sends a critical vibration alert to the smartphone via ntfy.sh."""
    topic = "axe_hybride_marko_alert" # Unique topic for your ntfy app
    message = f"🚨 AXE_HYBRIDE CRITICAL: {reason}"
    
    try:
        requests.post(f"https://ntfy.sh/{topic}",
            data=message.encode('utf-8'),
            headers={
                "Title": "AXE_HYBRIDE | VITAL ALERT",
                "Priority": "5", # Critical: triggers vibration/sound bypass [cite: 2026-01-26]
                "Tags": "warning,skull"
            })
        return True
    except Exception as e:
        return False