# Enigma Project Crypto

Ce projet est une implémentation de la machine Enigma en Python. 
Il permet de chiffrer et déchiffrer des messages en utilisant les rotors, réflecteurs et plugboard de la célèbre machine de cryptographie.

## Installation

Assurez-vous d'avoir **Python 3.x** installé sur votre machine. Clonez ce dépôt et installez les dépendances si nécessaire.

```sh
# Cloner le dépôt
git clone https://github.com/ouali-anais/Enigma-project-crypto.git
cd Enigma-project-crypto
```

## Utilisation

Exécutez le programme et entrez le message à chiffrer ou déchiffrer.

```sh
python main.py
```

Vous serez invité à entrer votre message dans la console.

### Options de configuration
Vous pouvez aussi exécuter le programme avec des options spécifiques :

```sh
python main.py -r I II III -ref B -k CAT -ring ABC -pb AB CD EF
```

- `-r` : Choisir les trois rotors parmi I, II, III, IV, V
- `-ref` : Sélection du réflecteur (A, B, C)
- `-k` : Clé de départ des rotors (ex: `CAT`)
- `-ring` : Position des anneaux des rotors (ex: `ABC`)
- `-pb` : Connexions du plugboard (ex: `AB CD EF`)

## Développement

Ce projet est basé sur plusieurs classes :

- `Rotor` : Gère la rotation et le chiffrement des lettres
- `Reflector` : Implémente les réflecteurs A, B et C
- `Plugboard` : Modifie les connexions des lettres
- `Enigma` : Machine principale qui orchestre tous les composants

## Ressources

Ce projet a été réalisé en suivant le tutoriel YouTube suivant : [Tutoriel Enigma en Python](https://www.youtube.com/watch?v=sbm2dmkmqgQ&t=2s)

## 📜 Licence

Ce projet est sous licence MIT 

## Auteur

Développé par **Anaïs** 😊



