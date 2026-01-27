import os

def get_health_metrics():
    """Returns a dictionary of current hardware health."""
    load = os.getloadavg()[0]
    # Thermal logic: base 40°C + load-based increase [cite: 2026-01-21]
    temp = 40 + (load * 15)
    
    return {
        "cpu_temp": round(temp, 1),
        "load_pct": round(load * 100, 1),
        "status": "OPTIMAL" if temp < 65 else "WARNING" if temp < 80 else "CRITICAL"
    }