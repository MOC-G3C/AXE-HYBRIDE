import json

def ingest_previous_soul(soul_file_path):
    """Injects previous project wisdom into the current logic flow."""
    try:
        with open(soul_file_path, 'r') as f:
            past_wisdom = json.load(f)
            
        print(f"✨ REINCARNATION: Absorbing wisdom from {past_wisdom['origin']}...")
        print(f"💠 RANK RESTORED: {past_wisdom['rank']}")
        return past_wisdom
    except Exception as e:
        return None