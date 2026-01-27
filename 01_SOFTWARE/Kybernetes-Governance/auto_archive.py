import subprocess
import time
import os

def commit_and_push_logs(project_path):
    """Automates the archival process to GitHub for AXE_HYBRIDE."""
    try:
        os.chdir(project_path)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Git cycle [cite: 2026-01-26]
        subprocess.run(["git", "add", "."], check=True)
        commit_msg = f"ms: Automatic Archive Sync - {timestamp}"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "push"], check=True)
        
        return f"Successfully archived at {timestamp}"
    except Exception as e:
        return f"Archive failed: {e}"