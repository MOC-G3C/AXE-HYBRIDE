import subprocess
import os

def execute_autonomous_merge(branch_name, health_issues):
    """Merges the Ectoplasm branch if no bugs were detected [cite: 2026-01-27]."""
    if not health_issues or "All systems stable" in str(health_issues):
        try:
            print(f"🧬 AUTO-MERGE: Integrating {branch_name} into main...")
            # Ensure we are on main branch
            subprocess.run(["git", "checkout", "main"], check=True)
            # Merge the dream branch [cite: 2026-01-26]
            subprocess.run(["git", "merge", branch_name], check=True)
            # Push the optimized state to GitHub
            subprocess.run(["git", "push"], check=True)
            # Delete the temporary branch
            subprocess.run(["git", "branch", "-d", branch_name], check=True)
            return True
        except Exception as e:
            print(f"❌ MERGE FAILED: {e}")
            return False
    else:
        print("⚠️ AUTO-MERGE: Aborted due to logic inconsistencies.")
        return False