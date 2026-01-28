import os
import subprocess

def trigger_victory_reward():
    """Applies aesthetic rewards for ahead-of-schedule completion."""
    # Path to an exclusive wallpaper (ensure this file exists or use a default)
    wallpaper_path = os.path.expanduser("~/Desktop/L'AXE HYBRIDE/02_HUMAIN/ASSETS/victory_369.jpg")
    
    print("🎊 RESONANCE VICTORY: You have outpaced Chronos!")
    
    # 1. Change macOS Wallpaper [cite: 2026-01-26]
    if os.path.exists(wallpaper_path):
        script = f'tell application "Finder" to set desktop picture to POSIX file "{wallpaper_path}"'
        subprocess.run(["osascript", "-e", script])
    
    # 2. Audio Reward (System sound)
    subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])
    
    return "✨ REWARD: High Resonance Wallpaper applied."