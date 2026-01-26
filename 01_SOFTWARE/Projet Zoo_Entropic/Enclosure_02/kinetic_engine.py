# MOC-G3C : Kinetic Engine Update
import math

bio_mass = 1336528  # Ta base de points
effort_du_jour = 10 # Remplace par tes km réels si différent

def calculer_poussee(points, km):
    poussee = (points / 1000) * math.log10(km + 1)
    return f"POUSSÉE CINÉTIQUE : {poussee:.2f} Unités"

print("--- SYNCHRONISATION ENCLOS 02 ---")
print(calculer_poussee(bio_mass, effort_du_jour))
print("STATUT : EFFORT PHYSIQUE CONVERTI EN STABILITÉ.")