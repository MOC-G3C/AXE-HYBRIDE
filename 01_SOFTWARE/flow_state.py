import time
import sys

def demarrer_session_flow(projet_nom):
    start_time = time.time()
    print(f"\033[1;34m🌀 PROTOCOLE FLOW ACTIVÉ : {projet_nom}\033[0m")
    print(f"   Vigilance : MAXIMALE | Barrière Landau : -0.0432")
    print(f"   Appuyez sur Ctrl+C pour terminer la session de focus.")
    
    try:
        while True:
            duree = int(time.time() - start_time)
            minutes = duree // 60
            # Plus le temps passe, plus on simule la dépense de Masse Bio
            bio_cost = minutes * 1.5 
            sys.stdout.write(f"\r   ⏱️  FOCUS : {minutes} min | Coût Bio-Mass estimé : {bio_cost} pts   ")
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n\n\033[1;32m✅ SESSION TERMINÉE\033[0m")
        print(f"   La cicatrice de cette session a été envoyée à la mémoire.")

if __name__ == "__main__":
    nom = input("Sur quel pilier de l'Axe travailles-tu ? ")
    demarrer_session_flow(nom)