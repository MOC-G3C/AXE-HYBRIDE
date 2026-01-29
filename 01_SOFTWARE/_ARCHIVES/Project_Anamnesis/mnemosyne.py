import os
import datetime

class MemoryCore:
    def __init__(self):
        # Target: 02_HUMAIN/analog_records
        # We go up two levels (..) from this script to reach the root, then down to 02_HUMAIN
        self.memory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '02_HUMAIN', 'analog_records'))
        
        # Ensure the analog folder exists
        if not os.path.exists(self.memory_path):
            os.makedirs(self.memory_path)
            print(f"[*] CREATING NEW MEMORY SECTOR: {self.memory_path}")
        
        print(f"[*] MNEMOSYNE CORE ONLINE. RECORDING TO: {self.memory_path}")

    def remember(self, entropy, stability):
        """
        Writes the event to a daily log file.
        """
        now = datetime.datetime.now()
        # File name based on date (one file per day)
        date_filename = now.strftime("%Y-%m-%d") + "_MEMORY_LOG.md"
        full_path = os.path.join(self.memory_path, date_filename)
        
        timestamp = now.strftime("%H:%M:%S")
        
        # Format: | Time | Chaos Level | Brain Decision |
        log_entry = f"| {timestamp} | Entropy: {entropy:.4f} | {stability} |\n"
        
        try:
            with open(full_path, "a") as f:
                f.write(log_entry)
            return True
        except Exception as e:
            print(f"[!] MEMORY FAILURE: {e}")
            return False