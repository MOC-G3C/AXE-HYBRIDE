"""
MEMORY_MANAGER.PY - Cortex Mémoriel (Gemini Link)
Rôle: Gestion de la mémoire à court et long terme + Logs Humains
"""
import json
import time
import os
import datetime
from dataclasses import dataclass, asdict
from typing import List, Dict, Any

@dataclass
class MemoryFragment:
    timestamp: float
    content: str
    source: str
    tags: List[str]
    entropy_at_creation: float

class MemoryManager:
    def __init__(self):
        # --- PATH CONFIGURATION ---
        # Remonter de : core > cortex > LEA_CORE > 01_SOFTWARE > ROOT
        self.root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
        self.human_sector = os.path.join(self.root_path, '02_HUMAIN', 'session_logs')
        
        # Fichier Machine (JSON)
        self.json_path = os.path.join(self.human_sector, "lea_neural_memory.json")
        
        # Vérification dossier
        if not os.path.exists(self.human_sector):
            os.makedirs(self.human_sector)

        self.short_term_memory: List[MemoryFragment] = []
        self.long_term_index: Dict[str, Any] = {}
        
        self._load_memory()

    def _load_memory(self):
        if os.path.exists(self.json_path):
            try:
                with open(self.json_path, 'r') as f:
                    data = json.load(f)
                    self.long_term_index = data.get('long_term', {})
                # print(f"[CORTEX] Mémoire chargée ({len(self.long_term_index)} jours indexés).")
            except Exception as e:
                print(f"[CORTEX] Erreur lecture mémoire: {e}")
        else:
            # print("[CORTEX] Mémoire vierge initialisée.")
            pass

    def store(self, content: str, source: str = "user", entropy: float = 0.0, mood_tag: str = "NEUTRAL"):
        """Stocke une nouvelle pensée ET met à jour le log humain"""
        fragment = MemoryFragment(
            timestamp=time.time(),
            content=content,
            source=source,
            tags=self._extract_tags(content),
            entropy_at_creation=entropy
        )
        
        # 1. Machine Memory (STM)
        self.short_term_memory.append(fragment)
        if len(self.short_term_memory) > 10:
            self._consolidate_memory()

        # 2. Human Log (Markdown) - Écriture immédiate pour lisibilité
        self._log_to_markdown(fragment, mood_tag)
            
        return fragment

    def _log_to_markdown(self, fragment: MemoryFragment, mood_tag: str):
        """Écrit l'échange dans un fichier journalier lisible par l'humain"""
        now = datetime.datetime.fromtimestamp(fragment.timestamp)
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        
        filename = f"SESSION_{date_str}.md"
        full_path = os.path.join(self.human_sector, filename)
        
        speaker = "OPÉRATEUR" if fragment.source == "user" else f"LEA [{mood_tag}]"
        icon = "👤" if fragment.source == "user" else "🧠"
        
        entry = f"\n**[{time_str}] {icon} {speaker}:** {fragment.content}\n"
        
        try:
            with open(full_path, "a", encoding='utf-8') as f:
                f.write(entry)
        except Exception as e:
            print(f"[!] Log Error: {e}")

    def recall(self, query: str) -> List[MemoryFragment]:
        results = []
        for frag in self.short_term_memory:
            if query.lower() in frag.content.lower():
                results.append(frag)
        return results

    def _extract_tags(self, content: str) -> List[str]:
        words = content.lower().split()
        return [w for w in words if len(w) > 5]

    def _consolidate_memory(self):
        """Transfert STM -> LTM (Sauvegarde JSON)"""
        if not self.short_term_memory: return
        
        oldest = self.short_term_memory.pop(0)
        date_key = time.strftime("%Y-%m-%d", time.localtime(oldest.timestamp))
        
        if date_key not in self.long_term_index:
            self.long_term_index[date_key] = []
            
        self.long_term_index[date_key].append(asdict(oldest))
        self._save_to_disk()

    def _save_to_disk(self):
        try:
            with open(self.json_path, 'w') as f:
                json.dump({
                    'long_term': self.long_term_index,
                    'last_sync': time.time()
                }, f, indent=2)
        except Exception as e:
            print(f"[CORTEX] Erreur sauvegarde JSON: {e}")

if __name__ == "__main__":
    mem = MemoryManager()
    mem.store("Test Intégration", entropy=0.5)
    print("Test complet. Vérifier 02_HUMAIN/session_logs")