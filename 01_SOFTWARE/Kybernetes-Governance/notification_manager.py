import os

def send_mac_notification(title, message):
    """Triggers a native macOS notification via AppleScript."""
    script = f'display notification "{message}" with title "{title}" sound name "Glass"'
    os.system(f"osascript -e '{script}'")

def alert_vision(pet_name, vision_text):
    send_mac_notification(f"🔮 {pet_name} HAS A VISION", vision_text)

def alert_emergency(pet_name, reason):
    send_mac_notification(f"⚠️ {pet_name} CRITICAL", reason)