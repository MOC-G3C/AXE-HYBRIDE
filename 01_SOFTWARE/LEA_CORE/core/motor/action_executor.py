"""
ACTION_EXECUTOR.PY - Cortex Moteur (SAFE AUDIO MODE)
Rôle: Synthèse Vocale 100% Amelie (Pour éliminer Fred) + Kill Switch
"""
import os
import time

class MotorCortex:
    def __init__(self):
        self.hardware_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '03_HARDWARE'))
        
    def _launch_terminal(self, script_name):
        full_path = os.path.join(self.hardware_path, script_name)
        if os.path.exists(full_path):
            # Lancement silencieux du script visuel
            cmd = f"""osascript -e 'tell application "Terminal" to do script "python3 \\"{full_path}\\""' > /dev/null 2>&1"""
            os.system(cmd)
            return True
        return False

    def speak_response(self, text, mood_tag):
        """Lit la réponse et coupe instantanément toute autre parole"""
        
        # 1. LE COUPE-PAROLE (KILL SWITCH)
        # Force le Mac à se taire immédiatement avant de dire la suite.
        # Le 'killall say' est violent mais efficace.
        os.system("killall say > /dev/null 2>&1")
        
        # 2. SÉCURITÉ AUDIO (Tout le monde en Amelie)
        # On ne prend plus de risque avec Thomas ou Fred.
        voice = "Amelie" 
            
        # Nettoyage du texte (enlève les astérisques et parenthèses bizarres)
        safe_text = text.replace("'", "").replace('"', "").replace("(", "").replace(")", "").replace("*", "")
        
        # On lance la voix Amelie
        cmd = f"say -v {voice} '{safe_text}' > /dev/null 2>&1 &"
        os.system(cmd)

    def trigger_reflex(self, mood_tag):
        if mood_tag == "FIRE":
            # Juste l'effet visuel, pas de sons parasites
            success = self._launch_terminal("tesla_booster.py")
            if success: return "[MOTOR] ⚠️ VISUAL OVERLOAD (SILENT)"
        return ""