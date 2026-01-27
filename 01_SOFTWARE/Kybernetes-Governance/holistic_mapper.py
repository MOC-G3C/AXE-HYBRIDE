import os

def generate_holistic_map():
    """Generates a visual status and progress map of the Axe Hybride project."""
    root_path = os.path.expanduser("~/Desktop/L'AXE HYBRIDE")
    folders = ["01_SOFTWARE", "02_HUMAIN", "03_HARDWARE"] # Based on project structure [cite: 2026-01-26]
    
    stats = {}
    total_files = 0
    
    # Calculate progress per domain
    for folder in folders:
        path = os.path.join(root_path, folder)
        if os.path.exists(path):
            files = [f for f in os.listdir(path) if not f.startswith('.')]
            stats[folder] = len(files)
            total_files += len(files)
        else:
            stats[folder] = 0

    # Objective #1 Progress (Target: 100 files for completion baseline) [cite: 2026-01-26]
    target = 100 
    progress = min(100, (total_files / target) * 100)
    
    # Simple SVG Visualization
    svg_content = f"""
    <svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0a0a0a"/>
      <text x="20" y="30" fill="#03dac6" font-family="monospace">AXE HYBRIDE PROGRESS: {progress:.1f}%</text>
      <rect x="20" y="50" width="{progress * 3.6}" height="20" fill="#bb86fc"/>
      <text x="20" y="100" fill="#ffffff" font-family="monospace" font-size="12">01_SOFTWARE: {stats['01_SOFTWARE']} units</text>
      <text x="20" y="120" fill="#ffffff" font-family="monospace" font-size="12">02_HUMAIN: {stats['02_HUMAIN']} units</text>
      <text x="20" y="140" fill="#ffffff" font-family="monospace" font-size="12">03_HARDWARE: {stats['03_HARDWARE']} units</text>
    </svg>
    """
    
    map_path = os.path.join(root_path, "02_HUMAIN/PROJECT_MAP.svg")
    with open(map_path, "w") as f:
        f.write(svg_content)
    
    return progress