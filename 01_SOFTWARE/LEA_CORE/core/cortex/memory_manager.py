"""
MEMORY_MANAGER.PY - Cortex Mémoriel (Gemini Link)
Rôle: Gestion de la mémoire à court et long terme
"""
import json
import time
import os
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
    def __init__(self, storage_path="lea_memory.json"):
        self.storage_path = storage_path
        self.short_term_memory: List[MemoryFragment] = []
        self.long_term_index: Dict[str, Any] = {}
        
        # Tentative de chargement de la mémoire existante
        self._load_memory()

    def _load_memory(self):
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r') as f:
                    data = json.load(f)
                    # On ne recharge que l'index, la STM est volatile
                    self.long_term_index = data.get('long_term', {})
                print(f"[CORTEX] Mémoire chargée ({len(self.long_term_index)} entrées).")
            except Exception as e:
                print(f"[CORTEX] Erreur lecture mémoire: {e}")
        else:
            print("[CORTEX] Mémoire vierge initialisée.")

    def store(self, content: str, source: str = "user", entropy: float = 0.0):
        """Stocke une nouvelle pensée ou information"""
        fragment = MemoryFragment(
            timestamp=time.time(),
            content=content,
            source=source,
            tags=self._extract_tags(content),
            entropy_at_creation=entropy
        )
        
        # Ajout à la mémoire court terme (STM)
        self.short_term_memory.append(fragment)
        
        # Consolidation automatique si STM trop pleine
        if len(self.short_term_memory) > 10:
            self._consolidate_memory()
            
        return fragment

    def recall(self, query: str) -> List[MemoryFragment]:
        """Recherche dans la mémoire (STM prioritaire)"""
        results = []
        # Recherche naïve pour l'instant (contient le mot)
        for frag in self.short_term_memory:
            if query.lower() in frag.content.lower():
                results.append(frag)
        return results

    def _extract_tags(self, content: str) -> List[str]:
        """Extraction basique de mots-clés (Placeholder pour NLP)"""
        words = content.lower().split()
        # Filtre basique des mots de plus de 5 lettres
        return [w for w in words if len(w) > 5]

    def _consolidate_memory(self):
        """Transfert STM -> LTM (Sauvegarde JSON)"""
        # On prend le plus vieux souvenir
        oldest = self.short_term_memory.pop(0)
        
        # On l'indexe dans la LTM (par date pour l'instant)
        date_key = time.strftime("%Y-%m-%d", time.localtime(oldest.timestamp))
        if date_key not in self.long_term_index:
            self.long_term_index[date_key] = []
            
        self.long_term_index[date_key].append(asdict(oldest))
        
        # Sauvegarde disque
        self._save_to_disk()

    def _save_to_disk(self):
        try:
            with open(self.storage_path, 'w') as f:
                json.dump({
                    'long_term': self.long_term_index,
                    'last_sync': time.time()
                }, f, indent=2)
        except Exception as e:
            print(f"[CORTEX] Erreur sauvegarde: {e}")

# Test unitaire
if __name__ == "__main__":
    mem = MemoryManager()
    mem.store("L'Axe Hybride est opérationnel", entropy=0.8)
    print(mem.recall("hybride"))