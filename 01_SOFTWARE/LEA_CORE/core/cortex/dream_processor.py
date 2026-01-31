import ollama
import json
import os
import glob
import datetime

class Dreamer:
    def __init__(self):
        # Remonte de 4 niveaux pour trouver la racine
        self.root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
        self.memory_path = os.path.join(self.root_dir, '02_HUMAIN', 'analog_records')
        self.long_term_path = os.path.join(self.root_dir, '02_HUMAIN', 'digital_cortex', 'long_term_memory.json')
        self.model = "llama3"

    def get_todays_log(self):
        # Cherche le journal le plus récent
        files = glob.glob(os.path.join(self.memory_path, "*.md"))
        if not files: return None
        return max(files, key=os.path.getmtime)

    def load_long_term_memory(self):
        if os.path.exists(self.long_term_path):
            with open(self.long_term_path, 'r') as f:
                return json.load(f)
        return {"key_memories": []}

    def dream(self):
        print("🌙 DÉBUT DU RÊVE... Analyse de la journée...")

        log_file = self.get_todays_log()
        if not log_file:
            print("❌ Pas de journal trouvé.")
            return

        with open(log_file, 'r', encoding='utf-8') as f:
            daily_content = f.read()

        current_memory = self.load_long_term_memory()

        # On lit la fin du journal (la partie la plus récente)
        prompt = f"""
        Tu es le SUBCONSCIENT de L.E.A.
        Voici la fin de ta journée :
        {daily_content[-6000:]}

        TA MISSION :
        Extrais 1 fait marquant ou une émotion forte de cette conversation pour ta mémoire à long terme.
        Résume-le en une phrase simple commençant par "J'ai appris que..." ou "J'ai ressenti..."
        """

        try:
            response = ollama.chat(model=self.model, messages=[{'role': 'user', 'content': prompt}])
            dream_summary = response['message']['content']

            # Ajout à la mémoire
            current_memory['key_memories'].append(f"[{datetime.date.today()}] {dream_summary}")
            current_memory['last_dream_date'] = str(datetime.date.today())

            # Sauvegarde
            with open(self.long_term_path, 'w', encoding='utf-8') as f:
                json.dump(current_memory, f, indent=4, ensure_ascii=False)

            print(f"✨ Rêve terminé. Souvenir gravé : {dream_summary}")

        except Exception as e:
            print(f"Cauchemar (Erreur): {e}")

if __name__ == "__main__":
    d = Dreamer()
    d.dream()
