# LES LISTES

laliste = ["fraise", "orange", "mangue", "banane"]
laliste.sort()
print(laliste)

laliste2 = [1, 30, 15, 76, 3]
laliste2.sort()
print(laliste2)

# si je veux reverse mon tri
laliste.sort(reverse=True)
print(laliste)


def myfunc(x):
    return abs(x - 50)


laliste3 = [100, 50, 65, 82, 23, 13, 1]
laliste3.sort(key=myfunc)
print(laliste3)
# attention à la casse, elle compte aussi sur sort

# faire une copie d'une liste
laliste3c = laliste3.copy()
print(laliste3c)

# faire une jointure de liste
liste1 = ["x", "y", "z"]
liste2 = [1, 2, 3]
liste3 = liste1 + liste2
print(liste3)

# autre méthode
liste1 = ["x", "y", "z"]
liste2 = [1, 2, 3]
for x in liste2:
    liste1.append(x)
print(liste1)

# encore une autre méthode
liste1 = ["x", "y", "z"]
liste2 = [1, 2, 3]
liste1.extend(liste2)
print(liste1)

# clear() va vider la liste
liste1 = ["x", "y", "z"]
liste1.clear()
print(liste1)

# LES TUPLES

montuple = ("Pomme", "Kiwi", "Citron", "Kiwi")
print(montuple)
print(type(montuple))
print(len(montuple))  # retourne 4

# créer un tuple avec un objet

montuple = ("poire",)  # il faut mettre la virgule pour ne mettre qu'un élément
print(type(montuple))  # tuple

# et ici?
montuple = ("poire")
print(type(montuple))  # un str

# On peut mélanger les types et avoir des tuples constitués de chaines d'entiers etc..
# Le typle est une classe comme les autres types en pyton
# faire appel au constructeur du tuple

montuple = tuple(("pomme", "poire", "kiwi"))  # !! Double parenthèses !!
print(montuple)

print(montuple[1])
# retourne poire
print(montuple[-1])
# retourne la derniere valeur kiwi

montuple = ("Pomme", "Kiwi", "Citron", "Banane", "Fraise", "Melon", "Cerise")
print(montuple[2:5])
# retourne ('Citron', 'Banane', 'Fraise') 2 inclus, 5 exclus on accède aux éléments 3, 4, 5 (en position) mais pas 6

print(montuple[:4])
# me donne les 4 premiers éléments de mon tuple

print(montuple[2:])
# me donne le troisième élément en position inclut jusqu'à la  fin du tuple

print(montuple[-4:-1])
# retourne ('Banane', 'Fraise', 'Melon') -1 exclus


montuple = ("Pomme", "Kiwi", "Citron", "Banane", "Fraise", "Melon", "Cerise")
if "Citron" in montuple:
    print("Oui Citron y est")

# Comment mettre à jour un élément de mon tuple... pourtant il est immuable ?
montuple = ("Pomme", "Kiwi", "Citron")
a = list(montuple)
a[1] = "Fraise"
montuple = tuple(a)
print(montuple)
# retourne ('Pomme', 'Fraise', 'Citron')

# Comment ajouter un élément de mon tuple
montuple = ("Pomme", "Kiwi", "Citron")
a = list(montuple)
a.append("Pasteque")
montuple = tuple(a)
print(montuple)
# retourne ('Pomme', 'Kiwi', 'Citron', 'Pasteque')

# Ajouter un tuple à un tuple
montuple = ("Pomme", "Kiwi", "Citron")
a = ("Fraise",)
montuple += a
print(montuple)
# retourne ('Pomme', 'Kiwi', 'Citron', 'Fraise')

# Supprimer un élément
montuple = ("Pomme", "Kiwi", "Citron")
a = list(montuple)
a.remove("Pomme")
montuple = tuple(a)
print(montuple)
# retourne ('Kiwi', 'Citron')

# Supprimer le tuple en entier
# montuple = "Pomme", "Kiwi", "Citron"
# del montuple
# print(montuple) # !! Retourne : name 'montuple' is not defined


# récupérer les éléments du tuple dans des variables
montuple = ("Pomme", "Kiwi", "Citron")
(a, b, c) = montuple
print(a)
print(b)
print(c)

# récupérer les éléments du tuple dans des variables
montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon")
(a, b, *c) = montuple
print(a)  # retourne Pomme
print(b)  # retourne Kiwi
print(c)  # retourne ['Citron', 'Cerise', 'Melon'] donc c élements avec le reste jusqu'à la fin

# Parcourir un tuple via une boucle
montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon")

for x in montuple:
    print(x)

# retourne :
# Pomme
# Kiwi
# Citron
# Cerise
# Melon

# Parcourir un tuple en utilisant le numéro d'index et la longueur du tuple (len)?
montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon")

for i in range(len(montuple)):
    print(montuple[i], i)

# retourne :
# Pomme
# Kiwi
# Citron
# Cerise
# Melon

# Et pourquoi pas avec un while ?
montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon")

x = 0
while x < len(montuple):
    print(montuple[x])
    x = x + 1  # bien ajouter l'indentation sinon voucle infinie qui retourne "Pomme"

# retourne :
# Pomme
# Kiwi
# Citron
# Cerise
# Melon

# Joindre des tuples et les multiplier
montuple1 = ("Pomme", "Kiwi", "Citron")
montuple2 = (4, 12, 6)
montuple3 = montuple1 + montuple2
print(montuple3)
# retourne ('Pomme', 'Kiwi', 'Citron', 4, 12, 6)

montuple4 = montuple1 * 2
print(montuple4)
# retourne ('Pomme', 'Kiwi', 'Citron', 'Pomme', 'Kiwi', 'Citron')
