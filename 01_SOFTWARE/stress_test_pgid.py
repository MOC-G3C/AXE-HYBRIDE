import time
import random

# --- IMPORT DE TA FONCTION DE FRICTION ---
V5_THRESHOLD = 8.0

def apply_friction(entropy_value):
    if entropy_value > V5_THRESHOLD:
        penalty = (entropy_value - V5_THRESHOLD) * 0.5
        print(f"⚠️ ALERTE V5 : Entropie ({entropy_value:.2f}) > Seuil ({V5_THRESHOLD})")
        print(f"🐢 Application du péage A6 : Pause de {penalty:.2f}s...")
        time.sleep(penalty)
    else:
        print(f"✅ Signal clair (V5: {entropy_value:.2f}). Exécution nominale.")

# --- SIMULATION DE MONTÉE D'ENTROPIE ---
print("🚀 Lancement de la simulation de charge...")
current_entropy = 5.0

for i in range(1, 11):
    # L'entropie augmente artificiellement à chaque tour
    current_entropy += random.uniform(0.1, 1.5)
    print(f"\n[Tour {i}] Analyse des données en cours...")
    
    # Appliquer la loi de l'Axe Hybride
    apply_friction(current_entropy)
    
    # Simuler un calcul
    time.sleep(0.5)

print("\n🏁 Test terminé. La souveraineté humaine a ralenti la machine.")