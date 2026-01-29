import os
import datetime

# MOC-G3C: LEA Memory Engine v0.1
# Objective: Archive and analyze insights with safety tagging.

class LEAMemory:
    def __init__(self):
        self.archive_path = "02_HUMAIN/session_logs/"
        self.cooling_period_hours = 72

    def archive_insight(self, content, tag="standard"):
        """Archives an insight with a timestamp and safety tag."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "timestamp": timestamp,
            "tag": tag,
            "content": content,
            "status": "unvalidated" if tag == "psychedelic" else "standard"
        }
        
        filename = f"insight_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        with open(os.path.join(self.archive_path, filename), "w") as f:
            f.write(f"# LEA ARCHIVE ENTRY\n\n**Tag:** {tag}\n**Status:** {entry['status']}\n\n{content}")
        
        print(f"[LEA]: Insight archived with tag '{tag}'.")
        if tag == "psychedelic":
            print(f"⚠️ SAFETY: Cooling period of {self.cooling_period_hours}h initiated.")

    def check_pending_validation(self):
        """Identifies entries requiring sober validation after cooling."""
        # TODO: Implement time-based check for 72h period
        pass

if __name__ == "__main__":
    memory = LEAMemory()
    # Example usage for a deep insight
    memory.archive_insight("The TNAB theorem proves the necessity of chaos.", tag="standard")