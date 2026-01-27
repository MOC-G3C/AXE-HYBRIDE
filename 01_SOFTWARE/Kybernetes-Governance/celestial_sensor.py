import datetime

def get_lunar_influence():
    """Calculates a gravity modifier based on the current lunar cycle."""
    # Simplified lunar cycle calculation (29.5 days)
    diff = datetime.datetime.now() - datetime.datetime(2026, 1, 14) # New Moon reference
    days = diff.days + (diff.seconds / 86400)
    lunation = (days % 29.53059) / 29.53059
    
    # Influence: 0.5 (New Moon) to 1.5 (Full Moon)
    # Full moon provides stability, New moon increases entropy [cite: 2026-01-26]
    influence = 1.0 + 0.5 * (1 - 2 * abs(lunation - 0.5))
    return round(influence, 2)