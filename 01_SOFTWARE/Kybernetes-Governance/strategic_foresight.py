import os
import holistic_mapper

def determine_daily_priority(wisdom_score):
    """Calculates the most critical path for Objective #1 [cite: 2026-01-26]."""
    root_path = os.path.expanduser("~/Desktop/L'AXE HYBRIDE")
    folders = {
        "01_SOFTWARE": os.path.join(root_path, "01_SOFTWARE"),
        "02_HUMAIN": os.path.join(root_path, "02_HUMAIN"),
        "03_HARDWARE": os.path.join(root_path, "03_HARDWARE")
    }
    
    # Analyze density
    densities = {k: len(os.listdir(v)) if os.path.exists(v) else 0 for k, v in folders.items()}
    
    # Logic: Target the weakest link to maintain balance [cite: 2021-01-21]
    weakest_axis = min(densities, key=densities.get)
    
    recommendations = {
        "01_SOFTWARE": "Focus on logic stability. The Ectoplasm needs more 'Self-Healing' routines.",
        "02_HUMAIN": "Deepen the philosophy. The Oracle requires more 3-6-9 resonance entries.",
        "03_HARDWARE": "Physical bridge required. Document your sensor arrays or Tesla coils."
    }
    
    # Adjust tone based on Wisdom Rank [cite: 2026-01-27]
    prefix = "MISSION COMMAND" if wisdom_score > 80 else "ADVISORY"
    
    return f"[{prefix}] Priority: {weakest_axis}. Action: {recommendations[weakest_axis]}"