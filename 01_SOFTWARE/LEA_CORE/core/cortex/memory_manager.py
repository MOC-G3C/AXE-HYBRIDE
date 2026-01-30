"""
MEMORY_MANAGER.PY - Hippocampe Numérique
Rôle: Écriture des souvenirs dans le dossier 02_HUMAIN
"""
import os
import datetime

class MemoryManager:
    def __init__(self):
        # On remonte l'arborescence pour trouver 02_HUMAIN
        self.root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
        self.records_path = os.path.join(self.root_dir, "02_HUMAIN", "analog_records")
        
        # Création du dossier s'il n'existe pas
        if not os.path.exists(self.records_path):
            os.makedirs(self.records_path)
            
        # Définition du fichier du jour (ex: JOURNAL_2026-01-30.md)
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        self.current_log = os.path.join(self.records_path, f"JOURNAL_{date_str}.md")

    def store(self, text, source, entropy, mood):
        """Écrit une ligne dans le journal"""
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Icônes pour rendre le log joli
        icon = "👤" if source == "user" else "🧠"
        if source == "lea" and mood == "FIRE": icon = "🔥"
        if source == "lea" and "AUTONOMOUS" in text: icon = "⚡"
        
        log_entry = f"\n| {timestamp} | {icon} {source.upper()} | E:{entropy:.2f} ({mood}) |\n"
        log_entry += f"> {text}\n"
        log_entry += "-"*40
        
        try:
            with open(self.current_log, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception as e:
            print(f"[MEMORY ERROR] Write failed: {e}")

if __name__ == "__main__":
    m = MemoryManager()
    print(f"Test mémoire vers : {m.current_log}")
    m.store("Test d'écriture", "user", 5.0, "FLOW")