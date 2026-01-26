import os
import platform

def trigger_reflex(bpm, frequency):
    """
    Exécute une action système réelle basée sur l'intensité.
    Pour macOS : Envoie une Notification Centre.
    """
    print(f"\n[LAMBDA] ⚠️ INITIATING REFLEX ACTION...")
    
    # Message de l'alerte
    title = "AXE HYBRIDE: ALERT"
    message = f"Bio-Resonance Critical: {bpm} BPM / {frequency:.2f} Hz"
    
    # Commande spécifique macOS (AppleScript)
    if platform.system() == "Darwin":
        cmd = f"""osascript -e 'display notification "{message}" with title "{title}" sound name "Ping"'"""
        os.system(cmd)
        
    print(f"[LAMBDA] Reflex Executed: Notification Sent.")

if __name__ == "__main__":
    # Test manuel
    trigger_reflex(120, 442)
