import os
import datetime

# --- CONSTANTES ARCHITECTE (MOC-G3C) ---
BIO_MASS = 1336528  #
STABILITE = -0.0432 #
CLARTE = 0.90       #
NB_CICATRICES = 12  #

def afficher_dashboard():
    os.system('clear')
    maintenant = datetime.datetime.now()
    horodatage = maintenant.strftime("%Y-%m-%d | %H:%M:%S")
    
    # Couleurs Terminal
    BLEU = "\033[94m"
    VERT = "\033[92m"
    JAUNE = "\033[93m"
    CYAN = "\033[96m"
    GRAS = "\033[1m"
    FIN = "\033[0m"

    print(f"{BLEU}{GRAS}" + "="*55)
    print(f"   🏛️  JANUS GATEWAY - TRIADE COMPLÈTE | {horodatage}")
    print("="*55 + f"{FIN}")
    
    print(f"👤 {GRAS}OPÉRATEUR :{FIN} M.O.C. (Beloeil Node)")
    print(f"📡 {GRAS}STATION   :{FIN} MacBook Pro M5")
    print(f"🧬 {GRAS}MASSE BIO :{FIN} {VERT}{BIO_MASS:,} points{FIN}")
    print(f"🪵 {GRAS}MÉMOIRE   :{FIN} {JAUNE}{NB_CICATRICES} cicatrices actives{FIN}")
    print("-" * 55)
    
    # ÉTAT DES ENCLOS (Cycle Tesla 3-6-9)
    print(f"🎸 {GRAS}ENCLOS 01 (Émotion) :{FIN} {VERT}OPÉRATIONNEL{FIN} (Vibration Guitare)")
    print(f"🚶 {GRAS}ENCLOS 02 (Action)  :{FIN} {VERT}OPÉRATIONNEL{FIN} (Marche 10km)")
    print(f"🧠 {GRAS}ENCLOS 03 (Repos)   :{FIN} {VERT}OPÉRATIONNEL{FIN} (Neural Scar)")
    print("-" * 55)
    
    # MÉTRIQUES DE SOUVERAINETÉ
    print(f"🌀 {GRAS}STABILITÉ LANDAU     :{FIN} {CYAN}{STABILITE}{FIN}")
    print(f"✨ {GRAS}SOUVERAINETÉ (CLARTÉ):{FIN} {JAUNE}{CLARTE*100}%{FIN}")
    print("-" * 55)
    
    print(f"{BLEU}{GRAS}" + "="*55 + f"{FIN}")
    print(f"        🔒 SYSTÈME SOUVERAIN ET VERROUILLÉ")
    print(f"{BLEU}{GRAS}" + "="*55 + f"{FIN}\n")

if __name__ == "__main__":
    afficher_dashboard()