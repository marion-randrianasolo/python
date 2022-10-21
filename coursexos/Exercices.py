# Exercice 1
# Construire un code qui affiche une liste des nombres pairs de 1 à 100

listepairs = range(2, 101, 2)
print(list(listepairs))

for i in range(100):
    if i % 2:
        print(i + 1)

# Exercice 2
# Construire un code qui affiche le lancé de 6 dés aléatoires

import random

for _ in range(6):
    nombre = random.choice(range(1, 7))
    print(nombre)

# Extension : Construire un code qui génère un nombre de lancé de dés choisi par l'utilisateur et affiche la moyenne
# en flottant de l'ensemble de ces lancés

print("Entrez un nombre de dés à lancer : ")
inuput_number = input()
# def moyenne(input):
#     for input in range(6):
#         nombre = random.choice(range(1, 7))
#         print(nombre)

# Exercice 3
# Compter le nombre d'occurence d'une lettre dans une phrase, par exemple "Salut ça va" compter le nombre de a soit 3

phrase = "Salut ça va?"
a = "a"
print("Le nombre d'occurrence de la lettre a est de :", phrase.lower().count(a))

# Extension basique : pensez au cas de figure ou la lettre est en majuscule...
print("Le nombre d'occurrence de la lettre A est de :", phrase.lower().count(a.upper()))

# Extension compter le nombre d'occurence de chaque lettre puis afficher la fréquence de chaque lettre de la phrase
phrase.count("Salut ça va")

from collections import Counter

collection = Counter(phrase)
print(collection)

# =================
# Pour importer un fichier python dans un autre, par ex dans main.py je veux importer code.py
# importation simple
# import code
# =================
# importation comme un objet
# import importlib
# file = importlib.import_module("Code")
# obj = file.codeClass()
# obj.show()
# =================
# importation par from
# from Code import CodeClass
# var1 = CodeClass()
# var1.show()
# =================


