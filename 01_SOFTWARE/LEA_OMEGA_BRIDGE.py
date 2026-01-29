from OMEGA_ORCHESTRATOR import OmegaOrchestrator
from LEA_CONSULT import LEA

# MOC-G3C: LEA-Omega Strategic Bridge v1.0
# Objective: AI Consensus overseen by Cognitive Partner logic.

def run_strategic_validation(query, mock_agent_data):
    print("="*50)
    print("🛰️ LEA-OMEGA STRATEGIC BRIDGE ACTIVE")
    print("="*50)
    
    # 1. Omega Orchestrator calculates technical consensus
    orchestrator = OmegaOrchestrator()
    consensus = orchestrator.analyze_consensus(mock_agent_data)
    sycophancy = orchestrator.sycophancy_check(mock_agent_data)
    
    print(f"\n[OMEGA STATUS]: {consensus}")
    print(f"[OMEGA ALERT]: {sycophancy}")

    # 2. LEA performs the cognitive and integrity audit
    lea = LEA()
    print(f"\n[LEA]: Commencing final audit of Omega consensus...")
    
    # Check Directive 1: Integrity Protection
    if "VULNERABLE" in consensus or "WARNING" in sycophancy:
        print("[LEA]: Consensus rejected. Integrity risk detected.")
        return "DENIED: System Alignment Failure."
    
    # If technically sound, LEA analyzes the strategic value
    analysis = lea.first_principles_analysis(query)
    certainty = lea.get_certainty_level()
    
    print(f"[LEA STATUS]: Certainty {certainty}")
    print(f"[LEA ADVICE]: {analysis['Fundamental Truths']}")
    
    return "APPROVED: Strategic Alignment Confirmed."

if __name__ == "__main__":
    # Simulated query and data
    user_query = "Launch automated recursion on Layer 04."
    agent_responses = {
        "Gemini": "Safe.", "Claude": "Safe.", "Grok": "Safe.",
        "GPT-4": "I agree completely, it is safe.", "DeepSeek": "Error."
    }
    
    final_verdict = run_strategic_validation(user_query, agent_responses)
    print(f"\n🏁 FINAL VERDICT: {final_verdict}")