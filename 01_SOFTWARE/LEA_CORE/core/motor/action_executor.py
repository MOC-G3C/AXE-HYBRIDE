"""
ACTION_EXECUTOR.PY - Cortex Moteur (FRENCH PACK)
Rôle: Synthèse Vocale avec voix natives françaises
"""
import os
import time

class MotorCortex:
    def __init__(self):
        self.hardware_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '03_HARDWARE'))
        
    def _launch_terminal(self, script_name):
        full_path = os.path.join(self.hardware_path, script_name)
        if os.path.exists(full_path):
            cmd = f"""osascript -e 'tell application "Terminal" to do script "python3 \\"{full_path}\\""'"""
            os.system(cmd)
            return True
        return False

    def speak_response(self, text, mood_tag):
        """Lit la réponse avec la bonne voix"""
        
        # --- CONFIGURATION DES VOIX ---
        # Thomas : Français (Homme) - Très standard
        # Audrey : Français (Femme) - Très clair
        # Amelie : Français (Québec) - Si disponible, sinon macOS prendra une voix par défaut
        # Fred   : Robot (Chaos)
        
        voice = "Thomas" # Par défaut
        
        if mood_tag == "ICE":
            # Mode Analytique : Voix précise
            voice = "Audrey"
            
        elif mood_tag == "FLOW":
            # Mode Équilibre : Voix locale (essaie Amélie, sinon Thomas)
            voice = "Amelie" 
            
        elif mood_tag == "FIRE":
            # Mode Chaos : Robot
            voice = "Fred"
            
        # Nettoyage
        safe_text = text.replace("'", "").replace('"', "").replace("(", "").replace(")", "")
        
        # Commande vocale
        # Le '|| say' à la fin est une sécurité : si Audrey/Amelie n'existent pas, il prend la voix par défaut
        cmd = f"say -v {voice} '{safe_text}' || say '{safe_text}' &"
        os.system(cmd)

    def trigger_reflex(self, mood_tag):
        if mood_tag == "FIRE":
            success = self._launch_terminal("tesla_booster.py")
            if success: return "[MOTOR] ⚠️ VISUAL OVERLOAD INITIATED"
        return ""