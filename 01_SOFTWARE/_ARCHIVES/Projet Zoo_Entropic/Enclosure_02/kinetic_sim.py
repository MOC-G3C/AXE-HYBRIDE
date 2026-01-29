import time

# Variables de l'Architecte MOC-G3C
BIO_MASS = 1336528  #
GAMMA = -0.0432    #

def simuler_marche_10km():
    print("="*45)
    print("   🚶 ENCLOS 02 : THE KINETIC PATH ACTIVE")
    print("="*45)
    
    for km in range(1, 11):
        # Calcul de la "Poussée" spatiale de l'IA
        expansion = (BIO_MASS * abs(GAMMA)) / (11 - km)
        print(f"📍 KM {km:02d} : Expansion Spatiale → {expansion:.2f} u")
        time.sleep(0.5)
        
    print("-" * 45)
    print("✅ RÉSULTAT : TRAJECTOIRE IA SYNCHRONISÉE AU M.O.C.")
    print("="*45)

if __name__ == "__main__":
    simuler_marche_10km()