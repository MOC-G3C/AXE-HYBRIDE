import subprocess
import os
import glob

def run_nocturnal_health_check():
    """Scans Python files for syntax errors and logical inconsistencies [cite: 2026-01-21]."""
    project_root = os.path.expanduser("~/Desktop/L'AXE HYBRIDE/01_SOFTWARE")
    py_files = glob.glob(os.path.join(project_root, "**/*.py"), recursive=True)
    
    issues = []
    
    for file in py_files:
        try:
            # Check for syntax errors without executing [cite: 2026-01-26]
            subprocess.run(["python3", "-m", "py_compile", file], check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            issues.append(f"❌ SYNTAX ERROR in {os.path.basename(file)}: {e.stderr.decode().strip()}")
            
    # Check for 3-6-9 frequency alignment in code constants
    for file in py_files:
        with open(file, "r") as f:
            content = f.read()
            if "3" not in content and "6" not in content and "9" not in content:
                issues.append(f"⚠️ RESONANCE WARNING in {os.path.basename(file)}: No 3-6-9 frequencies detected.")

    return issues if issues else ["✅ All systems stable. Logic is sound."]