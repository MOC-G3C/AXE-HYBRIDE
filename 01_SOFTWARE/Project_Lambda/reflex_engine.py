import os
import platform

def trigger_reflex(bpm, frequency):
    """
    Exécute une action système : Notification + Synthèse Vocale.
    """
    print(f"\n[LAMBDA] ⚠️ INITIATING REFLEX ACTION...")
    
    # 1. NOTIFICATION VISUELLE
    title = "AXE HYBRIDE: ALERT"
    message = f"Critical Resonance: {bpm} BPM"
    
    if platform.system() == "Darwin":
        # Notification visuelle
        cmd_notify = f"""osascript -e 'display notification "{message}" with title "{title}"'"""
        os.system(cmd_notify)
        
        # 2. SYNTHÈSE VOCALE (LOGOS)
        # La machine annonce l'événement à voix haute.
        # Le '&' permet de ne pas bloquer le script pendant qu'elle parle.
        speech = f"Warning. Critical biometric surge detected. {int(bpm)} beats per minute."
        os.system(f"say -v Samantha '{speech}' &")
        
    print(f"[LAMBDA] Reflex Executed: Notification & Voice dispatched.")

if __name__ == "__main__":
    # Test manuel
    trigger_reflex(110, 400)
