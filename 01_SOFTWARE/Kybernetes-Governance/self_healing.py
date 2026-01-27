import subprocess
import os

def attempt_restoration(file_path):
    """Restores a file to its last stable git state if it's corrupted [cite: 2026-01-21]."""
    try:
        print(f"🩹 SELF-HEALING: Restoring {os.path.basename(file_path)} to last stable version...")
        # Use git to restore the file from the previous commit [cite: 2026-01-26]
        subprocess.run(["git", "checkout", "HEAD", "--", file_path], check=True)
        return True
    except Exception as e:
        print(f"❌ HEALING FAILED: {e}")
        return False

def heal_detected_issues(issues_list):
    """Iterates through detected bugs and attempts a fix [cite: 2026-01-27]."""
    fixed_files = []
    for issue in issues_list:
        if "SYNTAX ERROR" in issue:
            # Extract file path from the error message
            file_name = issue.split("in ")[1].split(":")[0].strip()
            # Find the actual path [cite: 2026-01-26]
            # (Assuming logic to find full path in 01_SOFTWARE)
            if attempt_restoration(file_name):
                fixed_files.append(file_name)
    return fixed_files