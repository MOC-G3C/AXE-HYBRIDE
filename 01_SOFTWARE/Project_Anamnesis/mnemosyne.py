import os
import datetime

class MemoryCore:
    def __init__(self):
        # Cible : 02_HUMAIN/analog_records
        self.memory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '02_HUMAIN', 'analog_records'))
        
        if not os.path.exists(self.memory_path):
            try:
                os.makedirs(self.memory_path)
            except:
                pass

    def remember(self, entropy, stability):
        now = datetime.datetime.now()
        date_filename = now.strftime("%Y-%m-%d") + "_MEMORY_LOG.md"
        full_path = os.path.join(self.memory_path, date_filename)
        
        timestamp = now.strftime("%H:%M:%S")
        log_entry = f"| {timestamp} | Entropy: {entropy:.4f} | {stability} |\n"
        
        try:
            with open(full_path, "a") as f:
                f.write(log_entry)
            return True
        except:
            return False
