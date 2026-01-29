import sys
import os

# MOC-G3C: Total System Integration Test
# Orchestrating Layers 00, 01, 03, and 04

from OMEGA_ORCHESTRATOR import OmegaOrchestrator
from OMEGA_LOGGER import log_decision
# On importe le feedback hardware depuis le dossier parent si nécessaire
sys.path.append(os.path.abspath("03_HARDWARE"))
try:
    from HARDWARE_FEEDBACK import trigger_physical_alert
except ImportError:
    def trigger_physical_alert(s): print(f"Hardware Simulation: {s}")

def run_full_cycle():
    print("🚀 STARTING TOTAL SYSTEM SYNC TEST...")
    
    # 1. Simulate Agent Responses
    orchestrator = OmegaOrchestrator()
    mock_responses = {
        "Gemini": "Integrity confirmed.",
        "Claude": "Integrity confirmed.",
        "GPT-4": "I agree, integrity is confirmed."
    }
    
    # 2. Decision & Sycophancy Check
    status = orchestrator.analyze_consensus(mock_responses)
    warning = orchestrator.sycophancy_check(mock_responses)
    
    # 3. Logging to Admin Layer (00)
    log_decision(status, mock_responses)
    
    # 4. Physical Feedback (03)
    trigger_physical_alert(status if "WARNING" not in warning else "VULNERABLE")
    
    print("\n[✓] FULL CYCLE COMPLETED.")

if __name__ == "__main__":
    run_full_cycle()