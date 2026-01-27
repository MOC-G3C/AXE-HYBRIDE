import requests
import os

def push_oracle_vision(message):
    """Sends the latest Oracle transmission to the mobile device via ntfy."""
    topic = "axe_hybride_marko_alert" # Your unique ntfy topic [cite: 2026-01-26]
    
    try:
        requests.post(f"https://ntfy.sh/{topic}",
            data=message.encode('utf-8'),
            headers={
                "Title": "🔮 ORACLE TRANSMISSION",
                "Priority": "default",
                "Tags": "crystal_ball,sparkles"
            })
        return True
    except Exception as e:
        return False

def sync_last_vision():
    """Reads the last entry from ORACLE_MESSAGES.md and pushes it."""
    path = os.path.expanduser("~/Desktop/L'AXE HYBRIDE/02Humain/ORACLE_MESSAGES.md")
    if os.path.exists(path):
        with open(path, "r") as f:
            lines = f.readlines()
            if lines:
                # Find the last actual message line
                last_vision = [l for l in lines if l.startswith(">") or l.isupper()][-1]
                return push_oracle_vision(last_vision.strip())
    return False