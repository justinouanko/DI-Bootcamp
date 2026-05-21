
# Challenge 1 

# On demande un mot à l'utilisateur
word = input("Entrez un mot : ")

# On crée un dictionnaire vide pour stocker les résultats
letter_index = {}

# enumerate() donne à la fois l'index (position) ET la lettre à chaque tour
# ex: "dodo" (0, 'd'), (1, 'o'), (2, 'd'), (3, 'o')
for index, letter in enumerate(word):

    if letter in letter_index:
        # La lettre existe déjà on ajoute juste l'index à sa liste
        letter_index[letter].append(index)
    else:
        # Nouvelle lettre on crée une clé avec une liste contenant l'index
        letter_index[letter] = [index]

print(letter_index)

# Tests attendus :
# "dodo"    {'d': [0, 2], 'o': [1, 3]}
# "froggy"  {'f': [0], 'r': [1], 'o': [2], 'g': [3, 4], 'y': [5]}
# "grapes"  {'g': [0], 'r': [1], 'a': [2], 'p': [3], 'e': [4], 's': [5]}



# Challenge 2 

# Exemple 1
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# Exemple 2 (décommenter pour tester)
# items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
# wallet = "$100"

# Exemple 3 (décommenter pour tester)
# items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
# wallet = "$1"


# Étape 1 : Nettoyer le portefeuille
# On retire le "$" et les "," avant de convertir en entier
# replace() remplace un caractère par un autre (ici par rien = supprime)

def replace(wallet):
    return int(wallet.replace("$", "").replace(",", ""))

# Étape 2 : Parcourir les articles dans l'ordre de priorité
basket = []  # liste vide qui contiendra les articles achetés
wallet = replace(wallet)

for item, price in items_purchase.items():

    # Nettoyer le prix de l'article de la même façon
    price = replace(price)

    # Si on a assez d'argent, on achète l'article
    if price <= wallet:
        basket.append(item)
        wallet -= price   # on déduit le prix du portefeuille

# Étape 3 : Afficher le résultat
if basket:
    # sorted() trie la liste par ordre alphabétique
    print(sorted(basket))
else:
    print("Nothing")

# Tests attendus :
# Exemple 1 ['Bread', 'Fertilizer', 'Water']
# Exemple 2  ['Apple', 'Bananas', 'Fan', 'Honey', 'Spoon']
# Exemple 3 "Nothing"