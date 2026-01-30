"""
DASHBOARD_SAFE.py - OMEGA WATCHTOWER (NO-FAIL MODE)
Visualisation robuste via ANSI Codes (Pas de Curses)
"""
import sys
import os
import time
import tty
import termios
import select
import math

# Import du moteur
sys.path.append(os.path.join(os.path.dirname(__file__), 'Kinetic-RNG'))
try:
    from kinetic_core_v2 import KineticRNG_V2
except ImportError:
    print("❌ ERREUR: kinetic_core_v2.py introuvable.")
    sys.exit(1)

def get_bar(value, max_val, length=20, style="block"):
    """Génère une barre de progression textuelle"""
    percent = max(0.0, min(1.0, value / max_val)) if max_val > 0 else 0
    fill = int(length * percent)
    
    if style == "block":
        return "█" * fill + "░" * (length - fill)
    return "#" * fill + "-" * (length - fill)

def main():
    # Sauvegarde de la config terminal pour restauration
    old_settings = termios.tcgetattr(sys.stdin)
    
    print("🔌 INITIALISATION DU MOTEUR V2...")
    # Seuil de fraîcheur de 5 secondes
    rng = KineticRNG_V2(entropy_freshness_threshold=5.0)
    
    try:
        # Passage du terminal en mode "Raw" (capture des touches sans Enter)
        tty.setcbreak(sys.stdin.fileno())
        
        while True:
            # 1. CAPTURE INPUT (Non-bloquant)
            if select.select([sys.stdin], [], [], 0)[0]:
                key = sys.stdin.read(1)
                # Injection d'entropie
                rng.add_human_entropy("keyboard_safe", 0.8)
            
            # 2. RÉCUPÉRATION DIAGNOSTIC
            diag = rng.get_system_diagnostics()
            state = diag['entropy_state']
            age = diag['T_freshness']
            h_t = diag['H_t']
            
            # 3. AFFICHAGE (Effacement écran via ANSI Code)
            print("\033[H\033[J", end="") 
            
            print("╔════════════════════════════════════════════╗")
            print("║   AXE HYBRIDE // WATCHTOWER (SAFE MODE)    ║")
            print("╠════════════════════════════════════════════╣")
            
            # Statut
            symbol = "🔴"
            if state == "FRESH": symbol = "🟢"
            elif state == "ACTIVE": symbol = "🟡"
            
            print(f"║ ÉTAT:   {symbol} {state:<15}               ║")
            
            # Barres
            age_bar = get_bar(max(0, 5.0 - age), 5.0)
            print(f"║ VIE:    [{age_bar}] {age:5.2f}s  ║")
            
            chaos_bar = get_bar(h_t, 0.005)
            print(f"║ CHAOS:  [{chaos_bar}] {h_t:.4f} ║")
            
            print("╠════════════════════════════════════════════╣")
            
            # Tentative de génération pour voir le flux
            try:
                if state in ["FRESH", "ACTIVE"]:
                    val, meta = rng.generate()
                    print(f"║ FLUX:   🌊 {val:.8f}                   ║")
                    print(f"║ MODE:   ⚡ {meta.get('tesla_mode', 'N/A'):<15}            ║")
                else:
                    print(f"║ FLUX:   ⛔ BLOQUÉ (ENTROPIE PÉRIMÉE)       ║")
                    print(f"║ ACTION: 💉 INJECTION REQUISE               ║")
            except RuntimeError:
                print(f"║ FLUX:   ⛔ BLOQUÉ (SECURITÉ ACTIVÉE)       ║")
                print(f"║ ACTION: 💉 INJECTION REQUISE               ║")

            print("╚════════════════════════════════════════════╝")
            print("\n>> TAPEZ SUR VOTRE CLAVIER POUR NOURRIR LE SYSTÈME <<")
            print("(Arrêtez de taper 5 secondes pour voir la mort du système)")
            print("\n[CTRL+C pour quitter]")
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n🛑 Arrêt du monitoring.")
    finally:
        # Restauration du terminal (Important !)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        rng.shutdown()

if __name__ == "__main__":
    main()