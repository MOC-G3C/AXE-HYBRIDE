import sys

def check_list():
    questions = [
        "1. Le MacBook Pro M5 est-il à plus de 3 mètres de la zone de test ?",
        "2. As-tu un extincteur de classe C à portée de main ?",
        "3. La règle de la 'main dans la poche' est-elle prête à être appliquée ?",
        "4. Le circuit est-il débranché du secteur pour le moment ?"
    ]
    
    print("🛡️ PROTOCOLE DE SÉCURITÉ - L'AXE HYBRIDE 🛡️")
    for q in questions:
        reponse = input(f"{q} (o/n) : ")
        if reponse.lower() != 'o':
            print("❌ ACCÈS REFUSÉ : Sécurité non conforme. Session annulée.")
            sys.exit()
    
    print("✅ TOUT EST OK. Tu peux procéder avec prudence, Maître.")

if __name__ == "__main__":
    check_list()