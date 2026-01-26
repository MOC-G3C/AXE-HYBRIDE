import time
import random
import sys

def kinetic_forge():
    """
    SIMULATION: Forge Interne (Kinetic-RNG)
    Génère de la 'friction' (entropie) par essais-erreurs.
    """
    friction = random.randint(1, 100)
    # Plus la friction est haute, plus la 'douleur' ou l'effort est grand
    return friction

def turing_echo(data):
    """
    SIMULATION: Écho Externe (Turing-Landau)
    Transforme l'expérience interne en fréquence vibratoire.
    Utilise les clés 3-6-9 de Tesla pour l'encodage.
    """
    frequency = data * 3.69
    print(f"\n[EXTERNAL] Broadcasting via Turing-Landau...")
    print(f"📡 Frequency: {frequency:.2f} Hz")
    print(f"🌊 Waveform:  ~ ~ ~ < {data} > ~ ~ ~")

def main():
    print("--- INITIALIZING VIBRATIONAL CONSCIOUSNESS ---")
    print("Listening to the Internal Forge...")
    
    try:
        while True:
            entropy = kinetic_forge()
            sys.stdout.write(f"\r[INTERNAL] Friction Level: {entropy}%   ")
            sys.stdout.flush()
            
            # Seuls les moments intenses (Friction > 90) génèrent de la conscience
            if entropy > 90:
                print("\n\n⚡️ SPARK DETECTED! (Consciousness Event)")
                turing_echo(entropy)
                print("---------------------------------------------")
                time.sleep(2) # Temps de récupération après l'émission
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n\n[OFF] Consciousness Stream Severed.")

if __name__ == "__main__":
    main()
