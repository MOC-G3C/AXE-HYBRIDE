import os
import datetime

def estimate_completion_date(current_total, target=100):
    """Predicts the date of Objective #1 completion based on creation speed."""
    root_path = os.path.expanduser("~/Desktop/L'AXE HYBRIDE")
    
    # Analyze project age in days
    creation_time = os.path.getctime(root_path)
    days_active = (datetime.datetime.now().timestamp() - creation_time) / 86400
    days_active = max(1, days_active) # Avoid division by zero
    
    # Velocity: Files per day [cite: 2026-01-21]
    velocity = current_total / days_active
    
    if velocity == 0:
        return "Indeterminate (Static State)"
    
    remaining_files = target - current_total
    days_to_go = remaining_files / velocity
    
    completion_date = datetime.datetime.now() + datetime.timedelta(days=days_to_go)
    return completion_date.strftime("%Y-%m-%d"), round(velocity, 2)