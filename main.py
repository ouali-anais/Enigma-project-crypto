import argparse
from keyboard import Keyboard 
from plugboard import Plugboard
from reflector import Reflector
from rotor import Rotor
from enigma import Enigma

def main():
    print("Helloo ! Bienvenue dans le simulateur de l'Enigma !")
    message = input("Entrez le message que vous voulez chiffrer/déchiffrer : ").upper()
    
    
    rotor_choices = ["I", "II", "III"]
    rotors = []
    for i in range(3):
        while True:
            rotor = input(f"Choisissez le rotor {i+1} ({'/'.join(rotor_choices)}) : ").upper()
            if rotor in rotor_choices:
                rotors.append(rotor)
                break
            print("Sélection invalide. Veuillez choisir parmi les options suivantes : I, II, III.")
    
    
    reflector_choices = ["A", "B", "C"]
    while True:
        reflector = input(f"Choisissez le réflecteur (une lettre parmi les lettres suivantes : A, B, C)({'/'.join(reflector_choices)}) : ").upper()
        if reflector in reflector_choices:
            break
        print("Sélection invalide. Veuillez choisir une lettre parmi les lettres suivantes : A, B, C .")
    
   
    rings = []
    for i in range(3):
        while True:
            try:
                ring = int(input(f"Entrez la position de l'anneau {i+1} (1-26) : "))
                if 1 <= ring <= 26:
                    rings.append(ring)
                    break
                print("Valeur invalide. Veuillez entrer un nombre entre 1 et 26.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entier.")
    
  
    while True:
        key = input("Entrez la position initiale des rotors (3 lettres) : ").upper()
        if len(key) == 3 and key.isalpha():
            break
        print("Entrée invalide. Veuillez entrer exactement 3 lettres.")
    
    
    plugboard_pairs = input("Entrez les connexions du plugboard (ex: AB CD EF, laisser vide pour aucune connexion) : ").upper().split()
    
   
    rotor_dict = {
        "I": Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
        "II": Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
        "III": Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
    }
    
    reflector_dict = {
        "A": Reflector("EJMZALYXVBWFCRQUONTSPIKHGD"),
        "B": Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT"),
        "C": Reflector("FVJIACXWNTZPYMOGQHBRDUKELS")
    }
    
    KB = Keyboard()
    PB = Plugboard(plugboard_pairs)
    
    # Définition de la machine Enigma
    ENIGMA = Enigma(reflector_dict[reflector], rotor_dict[rotors[0]], rotor_dict[rotors[1]], rotor_dict[rotors[2]], PB, KB)
    
    # Configuration des anneaux et clé
    ENIGMA.set_rings(tuple(rings))
    ENIGMA.set_key(key)
    
    # Chiffrement/déchiffrement du message
    cipher_text = "".join(ENIGMA.encipher(letter) for letter in message)
    print("Résultats :", cipher_text)

if __name__ == "__main__":
    main()

