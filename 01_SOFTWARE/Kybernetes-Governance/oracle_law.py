import os
import glob
import statistics

# --- STYLING ---
PURPLE = '\033[95m'
CYAN = '\033[96m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'
BOLD = '\033[1m'

class KybernetesOracle:
    def __init__(self):
        # Target: 02_HUMAIN/analog_records
        self.memory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '02_HUMAIN', 'analog_records'))

    def gather_data(self):
        """Reads all memory files to establish a historical baseline."""
        all_entropy = []
        files = glob.glob(os.path.join(self.memory_path, "*.md"))
        
        if not files:
            return []

        print(f"[*] READING ARCHIVES... ({len(files)} files found)")
        
        for file_path in files:
            try:
                with open(file_path, 'r') as f:
                    for line in f:
                        if "Entropy:" in line:
                            # Extract number after 'Entropy:'
                            parts = line.split("Entropy:")
                            if len(parts) > 1:
                                val = parts[1].split("|")[0].strip()
                                try:
                                    all_entropy.append(float(val))
                                except:
                                    pass
            except:
                continue
        return all_entropy

    def judge(self):
        os.system('clear')
        print(f"{BOLD}{PURPLE}")
        print("🏛️  KYBERNETES GOVERNANCE COUNCIL  🏛️")
        print("---------------------------------------")
        print(f"{RESET}")

        history = self.gather_data()
        
        if not history:
            print(f"{RED}[!] INSUFFICIENT DATA FOR JUDGMENT.{RESET}")
            return

        # Calculate Global Stability Index (GSI)
        gsi = statistics.mean(history)
        sample_size = len(history)
        
        print(f"📈 RECORDS ANALYZED: {sample_size}")
        print(f"📊 GLOBAL ENTROPY AVERAGE: {gsi:.4f}\n")
        
        print(f"{BOLD}>> SUPREME DECREE:{RESET}")
        
        if gsi < 3.0:
            print(f"{GREEN}🕊️  STATE: PAX TECHNOLOGICA{RESET}")
            print("> The system is in perfect harmony.")
            print("> DECREE: All restrictions lifted. Creativity unbounded.")
            
        elif gsi < 7.0:
            print(f"{CYAN}⚖️  STATE: VIGILANT REPUBLIC{RESET}")
            print("> The system is fluctuating but functional.")
            print("> DECREE: Standard monitoring active.")
            
        else:
            print(f"{RED}⚔️  STATE: MARTIAL LAW{RESET}")
            print("> The system is dangerously unstable.")
            print("> DECREE: LOCKDOWN INITIATED. Heavy computation forbidden.")

def main():
    oracle = KybernetesOracle()
    oracle.judge()

if __name__ == "__main__":
    main()