import time

# Dictionnaire Morse simplifié pour le test
MORSE_CODE = {'.-': 'A', '-...': 'B', '---': 'O', '...': 'S'}

def decode_magnetic_signal(pulse_sequence):
    # Traduit la séquence de points (.) et traits (-)
    letters = "".join([MORSE_CODE.get(s, "?") for s in pulse_sequence.split()])
    print(f"📡 Message décodé via Le Pont de Tesla : {letters}")

if __name__ == "__main__":
    print("⏳ En attente du signal magnétique...")
    # Simulation basée sur ton script SOS précédent
    # (En situation réelle, ce script lirait les données du magnétomètre)
    test_sos = "... --- ..." 
    decode_magnetic_signal(test_sos)