import mobile_sync

# Inside your generate_oracle method, after the file write:
if is_dreaming:
    # During night distortion, ensure the message reaches the user [cite: 2026-01-26]
    mobile_sync.push_oracle_vision(f"🌙 NIGHT VISION: {message}")
else:
    mobile_sync.push_oracle_vision(message)