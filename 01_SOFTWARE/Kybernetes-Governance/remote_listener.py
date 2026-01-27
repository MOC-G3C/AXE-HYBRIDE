import requests
import json
import time

def listen_for_remote_commands(callback_exorcism, callback_mood):
    """Polls the ntfy command topic to execute remote instructions [cite: 2026-01-26]."""
    topic = "axe_hybride_marko_cmd" # Unique topic for incoming commands
    url = f"https://ntfy.sh/{topic}/json"
    
    print(f"📡 REMOTE: Listening on {topic}...")
    
    try:
        # Stream messages from ntfy [cite: 2026-01-21]
        with requests.get(url, stream=True) as r:
            for line in r.iter_lines():
                if line:
                    data = json.loads(line)
                    command = data.get("message", "").upper()
                    
                    if "EXORCISM" in command:
                        callback_exorcism()
                    elif "STERN" in command or "RESONANT" in command:
                        callback_mood(command)
    except Exception as e:
        print(f"❌ REMOTE ERROR: {e}")