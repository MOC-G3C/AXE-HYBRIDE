"""
LEA_BRAIN.PY - L'Orchestrateur Central (Tier 2)
Architecture: Harmonique 3-6-9
Dépendance Critique: Kinetic-RNG V2
"""
import sys
import os
import time
import logging
from dataclasses import dataclass

# Configuration des chemins pour trouver les modules voisins
sys.path.append(os.path.join(os.path.dirname(__file__), '../Kinetic-RNG'))
sys.path.append(os.path.dirname(__file__))

# Importation du Moteur d'Entropie (Critique)
try:
    from kinetic_core_v2 import KineticRNG_V2
except ImportError:
    print("❌ CRITIQUE: Kinetic-RNG V2 introuvable. LEA ne peut pas démarrer.")
    sys.exit(1)

# Configuration du Logging
logging.basicConfig(level=logging.INFO, format='[LEA] %(message)s')
logger = logging.getLogger("LEA_BRAIN")

@dataclass
class LeaState:
    """État instantané de LEA"""
    entropy_level: float = 0.0
    emotional_state: str = "NEUTRAL"
    security_level: str = "HIGH"
    last_cycle_time: float = 0.0

class LeaBrain:
    def __init__(self):
        logger.info("⚡ Initialisation du Cerveau Central...")
        
        # 1. Connexion au Moteur de Hasard (Le Coeur)
        try:
            self.rng = KineticRNG_V2(entropy_freshness_threshold=30.0) # 30s de tolérance pour le démarrage
            logger.info("✅ Kinetic-RNG connecté.")
        except Exception as e:
            logger.error(f"❌ Erreur RNG: {e}")
            raise

        # 2. Chargement des Modules Trinaires
        self.cortex_active = False
        self.limbic_active = False
        self.motor_active = False
        self._load_modules()

        # 3. État Initial
        self.state = LeaState()
        logger.info("🧠 LEA est en ligne (Mode: Démarrage).")

    def _load_modules(self):
        """Tente de charger les sous-modules Cortex/Limbic/Motor"""
        # --- CORTEX (MÉMOIRE & LOGIQUE) ---
        try:
            # Importation réelle du Gestionnaire de Mémoire
            from core.cortex.memory_manager import MemoryManager
            # Chemin absolu pour le fichier mémoire JSON
            mem_path = os.path.join(os.path.dirname(__file__), 'lea_memory.json')
            self.memory = MemoryManager(mem_path)
            self.cortex_active = True 
            logger.info("🔹 Cortex: EN LIGNE (Mémoire active)")
        except ImportError as e:
            logger.warning(f"🔸 Cortex: HORS LIGNE ({e})")
        except Exception as e:
            logger.warning(f"🔸 Cortex: ERREUR CRITIQUE ({e})")

        # --- LIMBIC (SÉCURITÉ & ÉMOTION) ---
        try:
            # from core.limbic.security_layer import SecurityLayer
            self.limbic_active = True
            logger.info("🔹 Limbic: STANDBY (En attente de code)")
        except:
            logger.warning("🔸 Limbic: HORS LIGNE")

        # --- MOTOR (ACTION) ---
        try:
            self.motor_active = True
            logger.info("🔹 Motor: STANDBY (En attente de code)")
        except:
            logger.warning("🔸 Motor: HORS LIGNE")

    def sense_environment(self):
        """Phase 1: Perception (Entropie Humaine)"""
        # On injecte une entropie système pour "sentir" le moteur
        self.rng.add_human_entropy("lea_internal_clock", time.time() % 1.0)
        diag = self.rng.get_system_diagnostics()
        
        self.state.entropy_level = diag['H_t']
        freshness = diag['T_freshness']
        
        # Modulation de l'état émotionnel basé sur la fraîcheur de l'entropie
        if freshness < 5.0:
            self.state.emotional_state = "CURIOUS"     # Entropie fraîche = Curiosité
        elif freshness < 30.0:
            self.state.emotional_state = "FOCUSED"     # Entropie moyenne = Concentration
        else:
            self.state.emotional_state = "DORMANT"     # Entropie vieille = Veille
            
        logger.info(f"👁️  Perception: Entropie={self.state.entropy_level:.4f} | État={self.state.emotional_state}")

    def think(self, user_input: str):
        """Phase 2: Traitement Trinaire (3-6-9)"""
        logger.info(f"💭 Réflexion sur: '{user_input}'")
        
        if not self.cortex_active:
            return "ERR: Cortex manquant."
        
        # Utilisation de la mémoire (Test)
        if hasattr(self, 'memory'):
            self.memory.store(user_input, entropy=self.state.entropy_level)
            memories = self.memory.recall(user_input)
            if memories:
                logger.info(f"📚 Souvenir rappelé: {len(memories)} fragments trouvés.")
            
        # Simulation du processus de pensée
        processing_time = 0.1
        time.sleep(processing_time)
        return f"Analyse de '{user_input}' terminée."

    def act(self):
        """Phase 3: Action"""
        # Génération d'un ID d'action unique via le RNG
        try:
            action_id, _ = self.rng.generate()
            logger.info(f"🎬 Action ID: {action_id:.8f} (Généré par Chaos)")
        except RuntimeError as e:
            # Nettoyage du message d'erreur pour l'affichage
            clean_error = str(e).split('\n')[0]
            logger.warning(f"🛑 Action bloquée par sécurité: {clean_error}")

    def run_cycle(self):
        """Cycle de vie complet"""
        self.sense_environment()
        self.think("System Check")
        self.act()

if __name__ == "__main__":
    # Test d'allumage rapide
    try:
        lea = LeaBrain()
        lea.run_cycle()
    except Exception as e:
        logger.critical(f"🔥 Échec critique du système: {e}")