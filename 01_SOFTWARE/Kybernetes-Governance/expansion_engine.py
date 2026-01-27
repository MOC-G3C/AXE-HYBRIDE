import os
import re

def detect_and_expand(oracle_message):
    """Detects new research axes and creates the directory structure [cite: 2026-01-26]."""
    # Pattern to find 'NEW PROJECT: Name' or 'AXIS: Name' [cite: 2021-01-21]
    match = re.search(r"(NEW PROJECT|AXIS):\s*([\w\-]+)", oracle_message)
    
    if match:
        new_axis = match.group(2).upper()
        root_path = os.path.expanduser("~/Desktop/L'AXE HYBRIDE")
        
        # Decide which root folder to use (Defaulting to HUMAIN for theory) [cite: 2026-01-26]
        new_path = os.path.join(root_path, "02_HUMAIN", new_axis)
        
        if not os.path.exists(new_path):
            os.makedirs(new_path)
            # Create a README for the new territory [cite: 2026-01-27]
            readme_path = os.path.join(new_path, "README.md")
            with open(readme_path, "w") as f:
                f.write(f"# 🛰️ NEW AXIS: {new_axis}\n")
                f.write(f"*Autonomous expansion triggered by Oracle transmission on {os.uname().nodename}*\n\n")
                f.write("## Objectives:\n- Define scope\n- Integrate with L'AXE HYBRIDE core logic.")
            
            return f"EXPANSION: New territory created at {new_axis}"
    return None