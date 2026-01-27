import os
import subprocess

# Path configuration
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# List of critical files for the system to function
CRITICAL_FILES = [
    "01_SOFTWARE/Kybernetes-Governance/neural_bridge.py",
    "01_SOFTWARE/Kybernetes-Governance/gui_dashboard.py",
    "01_SOFTWARE/Kybernetes-Governance/visual_core.py",
    "01_SOFTWARE/Kybernetes-Governance/daily_summary.py",
    "launch_axis.command"
]

def check_and_repair():
    print("--- AXE HYBRIDE : SELF-REPAIR PROTOCOL ---")
    repaired_count = 0
    
    os.chdir(ROOT)
    
    for file_path in CRITICAL_FILES:
        full_path = os.path.join(ROOT, file_path)
        
        if not os.path.exists(full_path):
            print(f"⚠️ MISSING FILE DETECTED: {file_path}")
            print(f"Attempting to restore from GitHub...")
            
            # Using git checkout to restore the specific file
            try:
                subprocess.run(["git", "checkout", "HEAD", "--", file_path], check=True)
                print(f"✅ SUCCESSFULLY RESTORED: {file_path}")
                repaired_count += 1
            except subprocess.CalledProcessError:
                print(f"❌ FAILED TO RESTORE: {file_path}. Check internet connection.")

    if repaired_count > 0:
        os.system(f'osascript -e \'display notification "{repaired_count} files restored." with title "Self-Repair Active"\'')
    else:
        print("All critical files are present. System integrity confirmed.")

if __name__ == "__main__":
    check_and_repair()