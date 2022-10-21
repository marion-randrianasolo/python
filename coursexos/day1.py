# EX 1 Tuple
parents = ("marc", "caroline")
print(type(parents))

# EX 2 Cast
nombre = 15
print("le nombre est " + str(nombre))

# EX 3 Ajouter separateurs
a = 2
b = 6
c = 3
d = a + b + c
print(d)
print(f"{a} + {b} + {c}")

# EX 4 Corriger erreur dans code
list1 = range(3)  # list est un mot reservé
list2 = range(5)

print(list(list2))

# EX 5
prenom = "Pierre"
if type(prenom) == str:
    print("La variable est une chaine de caractères")

prenom = 0

if isinstance(prenom, int):
    print("la variable est un entier")


def checkIfItemIsString(item):
    if isinstance(item, str):
        print(item + " is a string.")


firstName = 'Pierre'
checkIfItemIsString(firstName)

###### Notes fonctions

a = "Hello"
print(a.upper())

b = "VOILA"
print(b.lower())

c = " Bonjour ça va ? "
d = " Bonjour ça va ? "
print(c.strip())
print(d)

e = " Bonjour ça va ? "
print(e.replace("j", "o"))

f = " Bonjour ça va ? "
print(f.split(','))

# EX 6

phrase = "Bonjour tout le monde. Je répète Bonjour"
print(phrase.replace("Bonjour", "Bonsoir", 1))  # On ajoute le count 1 pour une occurence

# EX 7 Ordre alphabetique

chaine = "Pierre, Julien, Anne, Marie, Lucien"
chaine_liste = chaine.split(', ')
chaine_liste.sort()
chaine_en_ordre = ", ".join(chaine_liste)
print(chaine_liste)
print(chaine_en_ordre)

names = "Pierre, Julien, Anne, Marie, Julien"
namesArray = names.split(', ')
namesArray.sort()
print(namesArray, sep=', ')

# EX 8 Liste
maliste = ["Pierre", "Julien", "Anne", "Marie", "Lucien"]
print(len(maliste))
print(type(maliste))

maliste2 = list(("Pierre", "Julien", "Anne", "Marie", "Lucien"))
print(maliste2)

print(maliste2[1])  # prints Julien
print(maliste2[-1])  # lucien
print(maliste2[1:4])  # ['Julien', 'Anne', 'Marie']
print(maliste2[:4])  # ['Pierre', 'Julien', 'Anne', 'Marie']

if "Julien" in maliste2:
    print("oui")


# EX 9 Changer elements de ma liste
maliste[1] = "Vincent"
print(maliste)

maliste[1:3] = ["Vincent", "Sophie"]
print(maliste)

# Quand overflow
maliste[1:3] = ["Vincent", "Sophie", "Marion", "Lola"]
print(maliste)  # ajout des noms

maliste[1:3] = ["Vincent"]
print(maliste)  # retiresophie

maliste.insert(2, "Vincent")
print(maliste)  # ajoute vincent
maliste.extend(maliste2)  # concatene
print(maliste)

maliste1 = ["Anne", "Marie", "Lucien"]
malistetuple = ("pierre", "julien")

maliste1.extend(malistetuple)
print(maliste1)  # no pb

maliste1.remove("Marie")  # or maliste1.pop(1) , pop() remove last value of list
del maliste1[0]  # supprime premier element
# maliste1.clear() #liste vide
print(maliste1)

# parcours des éléments de liste
for x in range(len(maliste1)):
    print(maliste1[x])

x = 0
while x < len(maliste1):
    print(maliste1[x])
    x = x + 1

[print(x) for x in maliste1]


# EX 10
# extrait elements avec a dedans > ['banane', 'mangue']

fruits = ["banane", "pomme", "kiwi", "mangue"]
nouvelleliste = []

for x in fruits:
    if "a" in x:
        nouvelleliste.append(x)
print(nouvelleliste)

# plus court

nouvelleliste = [x for x in fruits if "a" in x]
print(nouvelleliste)

# extraire elts qui ne sont pas ...

nouvelleliste = [x for x in fruits if x != "banane"]
print(nouvelleliste)  # ['pomme', 'kiwi', 'mangue']

nouvelleliste = [x for x in range(5)]
print(nouvelleliste)  # [0, 1, 2, 3, 4]

nouvelleliste = [x for x in range(20) if x < 10]
print(nouvelleliste)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nouvelleliste = [x.upper() for x in fruits]
print(nouvelleliste)  # ['BANANE', 'POMME', 'KIWI', 'MANGUE']

nouvelleliste = ["eau" for x in fruits]
print(nouvelleliste)  # ['eau', 'eau', 'eau', 'eau']

nouvelleliste = [x if x != "banane" else "orange" for x in fruits]
print(nouvelleliste)  # ['orange', 'pomme', 'kiwi', 'mangue']

fruits = ["banane", "pomme", "kiwi", "mangue"]
#fruits.sort(reverse=True)
print(fruits)


def mafct(n):
    return abs(n - 50)


# fruits = [100, 52, 87, 65, 82, 23]
# fruits.sort(key=mafct)
# print(fruits)

# EX 10 Calcul du volume d'une sphère
rayon = 10
import math

vol = (4 / 3 * math.pi * rayon ** 3)
print("Le volume de ma sphère est de ", vol)


# EX 11 test si nbr plus grand que 10

def siPlusGrandQue(a: str, b: int):
    if (a.isdigit()):
        newNumber = int(a)
        if (newNumber > b):
            print(a + " est supérieur à " + str(b))
        elif (newNumber == b):
            print(a + " est égal à " + str(b))
        else:
            print(a + " est inférieur à " + str(b))
    else:
        print(str(a) + " n'est pas un nombre")


import random

tested_nbr = random.randint(0, 20)
print("Test du nombre: " + str(tested_nbr))
print("Entrez un nombre : ")
input_number = input()
siPlusGrandQue(input_number, tested_nbr)


# EXO 12

def createList(num1, num2):
    numlist = []

    while (num1 <= num2):
        numlist.append(num1)
        num1 += 1
    return numlist

num1 = 5
num2 = 15
print(createList(num1, num2))



liste_de_nbrs = range(5, 16)
print(list(liste_de_nbrs))


default_dict = {}
print(type(default_dict))

