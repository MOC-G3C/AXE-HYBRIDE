"""
DASHBOARD_V3.py - OMEGA WATCHTOWER
Visualisation Temps Réel du Moteur Kinetic-RNG V2 (TNAB Compliant)
PATCH: Redirection des logs (stdout) pour éviter les conflits Curses
"""
import curses
import time
import sys
import os
import threading
from io import StringIO

# Ajout du chemin pour trouver le module kinetic
sys.path.append(os.path.join(os.path.dirname(__file__), 'Kinetic-RNG'))

# Classe pour capturer les prints du moteur et éviter qu'ils cassent l'interface
class NullWriter:
    def write(self, text): pass
    def flush(self): pass

try:
    from kinetic_core_v2 import KineticRNG_V2, EntropyState
except ImportError:
    print("❌ ERREUR: Impossible de trouver kinetic_core_v2.py")
    sys.exit(1)

def draw_bar(stdscr, y, x, width, value, max_value, color_pair, label):
    """Dessine une barre de progression visuelle"""
    safe_value = max(0, min(value, max_value))
    percent = safe_value / max_value if max_value > 0 else 0
    fill_len = int(width * percent)
    
    stdscr.addstr(y, x, f"{label}: [", curses.color_pair(1))
    stdscr.addstr(y, x + len(label) + 3, "#" * fill_len, color_pair)
    stdscr.addstr(y, x + len(label) + 3 + fill_len, "-" * (width - fill_len), curses.color_pair(1))
    stdscr.addstr(f"] {value:.4f}", curses.color_pair(1))

def dashboard_loop(stdscr):
    # Configuration Curses
    curses.curs_set(0) # Cacher le curseur
    stdscr.nodelay(1)  # Input non-bloquant
    stdscr.timeout(50) # Rafraîchissement rapide
    
    # Couleurs (Standardisées pour éviter le noir sur noir)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)   # Texte normal
    curses.init_pair(2, curses.COLOR_GREEN, -1)   # FRESH / Good
    curses.init_pair(3, curses.COLOR_YELLOW, -1)  # ACTIVE / Warning
    curses.init_pair(4, curses.COLOR_RED, -1)     # STALE / Critical
    curses.init_pair(5, curses.COLOR_CYAN, -1)    # Tesla Blue
    
    # --- REDIRECTION DES LOGS ---
    # On empêche le moteur d'écrire sur l'écran pendant que Curses dessine
    original_stdout = sys.stdout
    sys.stdout = NullWriter()
    
    try:
        # Initialisation du Moteur (Silencieuse)
        rng = KineticRNG_V2(entropy_freshness_threshold=5.0)
    except Exception as e:
        sys.stdout = original_stdout
        print(f"Erreur init moteur: {e}")
        return

    # Variables d'état
    generated_value = 0.0
    gen_msg = "WAITING FOR INPUT..."
    gen_color = curses.color_pair(1)
    
    while True:
        try:
            stdscr.erase()
            height, width = stdscr.getmaxyx()
            
            # --- HEADER ---
            title = " AXE HYBRIDE // OMEGA WATCHTOWER V3 "
            stdscr.addstr(1, max(0, (width - len(title)) // 2), title, curses.A_BOLD | curses.color_pair(5))
            
            # --- INPUT CAPTURE ---
            try:
                key = stdscr.getch()
                if key != -1:
                    # Injection d'entropie
                    rng.add_human_entropy("dashboard", float(key)/255.0)
            except Exception:
                pass

            # --- DIAGNOSTIC SYSTÈME ---
            # Le moteur tourne en fond, on récupère juste l'état
            diag = rng.get_system_diagnostics()
            state = diag['entropy_state']
            freshness = diag['T_freshness']
            compliance = diag['compliance_level']
            
            # --- INTERPRÉTATION ÉTAT ---
            if state == "FRESH":
                status_color = curses.color_pair(2) | curses.A_BOLD
                status_text = " ✅ FRESH (OPTIMAL) "
            elif state == "ACTIVE":
                status_color = curses.color_pair(3) | curses.A_BOLD
                status_text = " ⚠️  ACTIVE (DECAYING) "
            else: # STALE or COLLAPSED
                status_color = curses.color_pair(4) | curses.A_BOLD
                status_text = " 🛑 STALE / COLLAPSED "

            # Affichage Status
            stdscr.addstr(3, 2, "SYSTEM STATUS:", curses.color_pair(1) | curses.A_BOLD)
            stdscr.addstr(3, 18, status_text, status_color)
            
            # --- BARRES DE VIE ---
            time_left = max(0, 5.0 - freshness)
            draw_bar(stdscr, 5, 2, 30, time_left, 5.0, status_color, "FRESHNESS")
            
            quality_color = curses.color_pair(2) if diag['H_t'] > 0.001 else curses.color_pair(4)
            draw_bar(stdscr, 6, 2, 30, diag['H_t'], 0.005, quality_color, "ENTROPY H_t")
            
            # --- METRICS ---
            stdscr.addstr(8, 2, "METRICS:", curses.color_pair(5) | curses.A_BOLD)
            stdscr.addstr(9, 4, f"Age:        {freshness:.2f}s", curses.color_pair(1))
            stdscr.addstr(10, 4, f"Compliance: {compliance:.1%}", status_color)
            
            # --- GÉNÉRATION CONTINUE ---
            # On tente de générer seulement si l'état le permet
            if state in ["FRESH", "ACTIVE"]:
                try:
                    val, meta = rng.generate()
                    generated_value = val
                    gen_msg = f"STREAM: {val:.8f} | MODE: {meta.get('tesla_mode', 'N/A')}"
                    gen_color = curses.color_pair(2)
                except RuntimeError:
                    pass # Ignorer erreurs silencieuses
            else:
                gen_msg = "BLOCKED: ENTROPY STALE OR COLLAPSED"
                gen_color = curses.color_pair(4)
                
            stdscr.addstr(12, 2, "OUTPUT:", curses.color_pair(5) | curses.A_BOLD)
            stdscr.addstr(13, 4, gen_msg, gen_color)

            # --- FOOTER ---
            footer = ">> FRAPPEZ DES TOUCHES POUR NOURRIR LE CHAOS <<"
            stdscr.addstr(height-2, max(0, (width - len(footer)) // 2), footer, curses.color_pair(3) | curses.A_BLINK)
            
            stdscr.refresh()
            
        except KeyboardInterrupt:
            break
        except Exception:
            # En cas de crash d'affichage, on continue (ne pas laisser planter le thread)
            pass

    # Restauration stdout avant de quitter
    sys.stdout = original_stdout
    rng.shutdown()
    print("[WATCHTOWER] Arrêt du monitoring.")

if __name__ == "__main__":
    curses.wrapper(dashboard_loop)