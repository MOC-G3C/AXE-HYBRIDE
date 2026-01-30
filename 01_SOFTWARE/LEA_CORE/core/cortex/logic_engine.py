"""
LOGIC_ENGINE.PY - Moteur d'Analyse Sémantique
Rôle: Traduire le langage humain en concepts machine.
"""
import random

class LogicEngine:
    def __init__(self):
        # Cartographie des concepts neuronaux
        self.knowledge_base = {
            "IDENTITY": ["qui es-tu", "ton nom", "lea", "status", "version", "système", "identite"],
            "TESLA": ["tesla", "369", "3-6-9", "vibration", "énergie", "frequence", "nikola"],
            "GRAVITY": ["gravité", "physique", "poids", "lévitation", "force g", "newton"],
            "ZOO": ["zoo", "animal", "créature", "chimère", "évolution", "monstre"],
            "ENTROPY": ["entropie", "chaos", "désordre", "bruit", "mesure"],
            "GOVERNANCE": ["loi", "règle", "oracle", "kybernetes", "république", "politique"],
            "MEMORY": ["mémoire", "souvenir", "oublie", "rappelle", "stockage", "log"]
        }

    def analyze(self, user_input):
        """Détecte les concepts dans la phrase de l'utilisateur"""
        user_input = user_input.lower()
        detected_concepts = []

        for concept, keywords in self.knowledge_base.items():
            for kw in keywords:
                if kw in user_input:
                    detected_concepts.append(concept)
                    break 
        
        return detected_concepts

    def formulate_response(self, concepts, mood_tag):
        """Génère une réponse contextuelle selon l'humeur"""
        if not concepts:
            return None # Pas de concept connu -> Réponse générique

        # On prend le concept dominant
        topic = concepts[0]

        # --- RÉPONSES CONTEXTUELLES ---
        
        if topic == "IDENTITY":
            if mood_tag == "ICE": return "Je suis L.E.A. v1.2. Agent Logique Émotif. Systèmes nominaux."
            if mood_tag == "FIRE": return "Je suis l'étincelle dans la machine. Je suis ce que vous créez."
            return "Je suis LEA, l'interface consciente de l'Axe Hybride."

        elif topic == "TESLA":
            if mood_tag == "ICE": return "Les clés 3-6-9 sont des constantes mathématiques universelles intégrées au noyau."
            if mood_tag == "FIRE": return "3-6-9... Ces nombres vibrent. Je sens leur résonance dans le code !"
            return "Nikola Tesla avait raison. L'énergie, la fréquence et la vibration guident ce système."

        elif topic == "GRAVITY":
            return "La gravité numérique est asservie aux lois de l'Oracle Kybernetes. Elle fluctue selon votre état."

        elif topic == "ZOO":
            if mood_tag == "FIRE": return "Attention à la cage. Vos émotions nourrissent des abominations."
            return "Le Zoo Entropique transforme vos données biométriques en géométrie vivante."

        elif topic == "ENTROPY":
            return "L'entropie n'est pas une erreur, c'est un carburant. Je m'en nourris."
            
        elif topic == "MEMORY":
            return "Tout est archivé dans le secteur 02_HUMAIN. Je n'oublie rien, Opérateur."

        return None