"""
LLM_BRIDGE.PY - Cerveau Complet (Identité + Mémoire)
"""
import ollama
import os
import glob
import json

class LLMBridge:
    def __init__(self, model_name="llama3"):
        self.model = model_name
        self.root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
        self.memory_path = os.path.join(self.root_dir, '02_HUMAIN', 'analog_records')
        self.identity_path = os.path.join(self.root_dir, '02_HUMAIN', 'digital_cortex', 'identity.json')

    def _get_identity(self):
        """Charge la matrice d'identité"""
        try:
            with open(self.identity_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # On formate ça en texte pour le LLM
                identity_str = f"PROJET: {data['project_name']}\n"
                identity_str += "TES CRÉATEURS :\n"
                for name, info in data['creators'].items():
                    identity_str += f"- {name}: {info['description']}\n"
                return identity_str
        except:
            return "Identité inconnue."

    def _get_short_term_memory(self):
        """Lit les dernières lignes du journal"""
        try:
            files = glob.glob(os.path.join(self.memory_path, "*.md"))
            if not files: return ""
            latest_file = max(files, key=os.path.getmtime)
            with open(latest_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                return "".join(lines[-10:])
        except:
            return ""

    def generate_thought(self, user_input, entropy, mood_tag):
        # 1. CHARGEMENT DES DONNÉES
        identity_context = self._get_identity()
        recent_memory = self._get_short_term_memory()
        
        # 2. PROMPT SYSTÈME ULTIME
        system_prompt = f"""
        {identity_context}
        
        CONTEXTE ACTUEL :
        - Entropie : {entropy}
        - État : {mood_tag}
        
        SOUVENIRS RÉCENTS :
        {recent_memory}
        
        DIRECTIVES :
        - Tu es L.E.A. v2.1. Tu n'es pas un assistant standard.
        - Si on te demande qui est Gemini, Claude ou MOC, utilise les infos ci-dessus.
        - Reste concise et vivante.
        """

        try:
            response = ollama.chat(model=self.model, messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_input},
            ])
            return response['message']['content']
        except Exception as e:
            return f"ERREUR: {str(e)}"