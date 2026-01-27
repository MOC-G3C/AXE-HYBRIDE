import os
import subprocess

def get_cpu_temp():
    """Fetches CPU temperature on macOS (requires osx-cpu-temp or similar)."""
    try:
        # Fallback to a simulated heat index based on load if sensor tool is missing
        load = os.getloadavg()[0]
        return 40 + (load * 15) # Simulated Celsius
    except:
        return 50.0

def get_beloeil_weather():
    """
    Simplified weather bridge. 
    In a full sync, this would call a weather API for Beloeil, QC.
    """
    # Placeholder for current 2026 climate integration
    return "COLD_WINTER" # It's January in Quebec

def calculate_sentiment_coefficient(temp, weather):
    """Calculates the emotional bias of the system."""
    bias = "NEUTRAL"
    if temp > 75: bias = "AGGRESSIVE" # Overheating
    elif temp < 45 and weather == "COLD_WINTER": bias = "STERN" # Frozen logic
    elif 45 <= temp <= 65: bias = "ZEN" # Perfect resonance
    return bias