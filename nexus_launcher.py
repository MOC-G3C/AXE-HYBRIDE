import os
import time
import subprocess

# CHEMINS RELATIFS DES 4 PILIERS
PATH_KINETIC = "02_HUMAIN/Kinetic-RNG/kinetic_core.py"
PATH_ZOO = "01_SOFTWARE/Projet Zoo_Entropic/zoo_core.py"
PATH_GUARDIAN = "01_SOFTWARE/Kybernetes-Governance/guardian.py"
PATH_TESLA = "03_HARDWARE/tesla_coils/tesla_tone_generator.py"

def launch(script_rel_path, title, color_code):
    """Lance un terminal, va dans le bon dossier, change la couleur"""
    abs_path = os.path.abspath(script_rel_path)
    script_dir = os.path.dirname(abs_path)
    script_name = os.path.basename(abs_path)
    
    if not os.path.exists(abs_path):
        print(f"❌ MANQUANT : {script_rel_path}")
        return

    print(f"🚀 Activation : {title}...")
    
    # Commande AppleScript blindée (CD + Python + Couleur + Titre)
    cmd = f"""
    tell application "Terminal"
        do script "cd \\"{script_dir}\\" && python3 \\"{script_name}\\""
        set custom title of front window to "{title}"
        set background color of front window to {color_code}
        set normal text color of front window to {{65535, 65535, 65535}}
    end tell
    """
    subprocess.run(["osascript", "-e", cmd])
    time.sleep(1)

def main():
    print("\n--- NEXUS LAUNCHER : SYSTEM COMPLETE (4-AXIS) ---")
    print("Initialisation du Quadrant...")
    
    # 1. CHAOS (Noir)
    launch(PATH_KINETIC, "1. KINETIC (Source)", "{0, 0, 0}") 
    
    # 2. GARDIEN (Bleu foncé)
    launch(PATH_GUARDIAN, "2. KYBERNETES (Loi)", "{0, 0, 20000}")
    
    # 3. ZOO (Vert Matrix)
    launch(PATH_ZOO, "3. ZOO (Simulation)", "{0, 15000, 0}")
    
    # 4. TESLA (Violet Mystique)
    launch(PATH_TESLA, "4. TESLA (Résonance)", "{10000, 0, 20000}")

    print("\n✅ SYSTÈME COMPLET EN LIGNE.")
    print("Surveillez les 4 fenêtres.")

if __name__ == "__main__":
    main()