import os

# Codes couleurs pour le Terminal
VERT = "\033[92m"
BLEU = "\033[94m"
JAUNE = "\033[93m"
GRAS = "\033[1m"
FIN = "\033[0m"

os.system('clear')

print(f"{BLEU}{GRAS}="*45)
print("   🏛️  L'AXE HYBRIDE - TABLEAU DE BORD")
print("="*45 + f"{FIN}")

print(f"{GRAS}👤 OPÉRATEUR :{FIN} M.O.C. (Beloeil Node)")
print(f"{GRAS}📡 MATÉRIEL  :{FIN} MacBook Pro M5")
print("-" * 45)

# Les chiffres clés qui "poppent"
print(f"{GRAS}🟢 SOUVERAINETÉ (Clarté) : {VERT}90.0%{FIN}")
print(f"{GRAS}🌀 STABILITÉ (Landau)    : {BLEU}-0.0432{FIN}")
print(f"{GRAS}🪵 CICATRICES (Mémoire)   : {JAUNE}12{FIN}")
print(f"{GRAS}🧬 MASSE BIOLOGIQUE      : {VERT}1,336,528 points{FIN}")

print("-" * 45)
print(f"{VERT}{GRAS}✅ ÉTAT DU SYSTÈME : SOUVERAIN ET STABLE{FIN}")
print(f"{BLEU}{GRAS}="*45 + f"{FIN}")