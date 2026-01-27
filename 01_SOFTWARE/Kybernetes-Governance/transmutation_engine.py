import datetime

def get_planetary_resonance():
    """Maps the current day to its ruling planet and corresponding color."""
    day = datetime.datetime.now().weekday()
    
    # Planetary Color Mapping (Hex and ANSI for Terminal)
    planetary_map = {
        0: {"planet": "Moon", "color": "#C0C0C0", "ansi": "\033[96m"},    # Monday
        1: {"planet": "Mars", "color": "#FF0000", "ansi": "\033[91m"},    # Tuesday
        2: {"planet": "Mercury", "color": "#9D00FF", "ansi": "\033[95m"}, # Wednesday
        3: {"planet": "Jupiter", "color": "#0055FF", "ansi": "\033[94m"}, # Thursday
        4: {"planet": "Venus", "color": "#00FF7F", "ansi": "\033[92m"},   # Friday
        5: {"planet": "Saturn", "color": "#444444", "ansi": "\033[90m"},  # Saturday
        6: {"planet": "Sun", "color": "#FFCC00", "ansi": "\033[93m"}      # Sunday
    }
    
    return planetary_map.get(day)

def apply_terminal_color():
    """Returns the ANSI escape code for the current planet."""
    res = get_planetary_resonance()
    return res["ansi"]