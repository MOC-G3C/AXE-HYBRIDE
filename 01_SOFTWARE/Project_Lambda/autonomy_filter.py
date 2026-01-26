# Project Lambda - Autonomy Booster (MOC-G3C)
# Target: 90% Clarity | Location: Beloeil Node

def clear_filter(ai_suggestion):
    # Liste des mots-clés "intrusifs" ou directifs
    intrusive_patterns = ["tu devrais", "il faut", "je suggère fortement", "obligatoire"]
    
    # Analyse de la suggestion
    if any(pattern in ai_suggestion.lower() for pattern in intrusive_patterns):
        return "[BLOQUÉ] : Suggestion trop intrusive. Souveraineté du M.O.C. prioritaire."
    else:
        return f"[VALIDÉ] : {ai_suggestion}"

# Simulation du passage à 90%
print("Mise à jour du protocole Lambda...")
print("Cible : 90.0% de Clarté.")
print("Statut : FILTRE ACTIF.")