
""" # Exercise 1: Converting Lists into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict = {
    keys[0]: values[0],
    keys[1]: values[1],
    keys[2]: values[2]  
}
print(dict)

# Exercise 2: Cinemax #2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

for name, age in family.items():
    if age < 3:
        print(f"for {name} ticket is free")
    elif age >= 3 and age <= 12:
        print(f"for {name} ticket is $10")
    elif age > 12:
        print(f"for {name} ticket is $15")
"""

# Exercise 1

# Les deux listes de départ
keys   = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# zip() associe chaque clé à sa valeur, dict() crée le dictionnaire
result = dict(zip(keys, values))

print(result)




# Exercise 2


# La famille avec les âges
family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

total = 0  # On commence à 0 et on ajoute au fur et à mesure

# .items() donne la paire (nom, âge) à chaque tour de boucle

for name, age in family.items():

    # Règle de tarif

    if age < 3:       # moins de 3 ans gratuit
        price = 0
    elif age <= 12:   # entre 3 et 12 ans
        price = 10
    else:             # plus de 12 ans
        price = 15

    print(f"{name.capitalize()} : ${price}")
    total += price    # on ajoute le prix au total

print(f"Total : ${total}")



# Exercise 3


# Création du dictionnaire (les valeurs peuvent être des listes ou d'autres dicts)
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

# Modifier une valeur existante
brand["number_stores"] = 2

# Afficher les clients en joignant la liste avec ", "
print(f"Zara s'adresse à : {', '.join(brand['type_of_clothes'])}")

# Ajouter une nouvelle clé
brand["country_creation"] = "Spain"

# Vérifier si une clé existe avant de modifier
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Supprimer une clé avec del
del brand["creation_date"]

# Accéder au dernier élément d'une liste avec l'index -1
print(brand["international_competitors"][-1])   # Desigual

# Accéder à un dictionnaire imbriqué
print(brand["major_color"]["US"])               # ['pink', 'green']

# Compter le nombre de clés
print(len(brand))

# Lister toutes les clés
print(list(brand.keys()))

# Bonus : fusionner deux dictionnaires avec .update()
more_on_zara = {"creation_date": 1975, "number_stores": 2}
brand.update(more_on_zara)
print(brand)



# Exercise 4 

# country="Unknown" = valeur par défaut si on ne passe pas de pays
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

# Appel avec les deux paramètres
describe_city("Reykjavik", "Iceland")    # Reykjavik is in Iceland.

# Appel sans pays → utilise la valeur par défaut
describe_city("Paris")                   # Paris is in Unknown.

# Autre exemple
describe_city("Abidjan", "Côte d'Ivoire")


# Exercise 5

import random

def compare_numbers(user_number):
    # Génère un entier aléatoire entre 1 et 100
    random_number = random.randint(1, 100)

    if user_number == random_number:
        print("Succès !")
    else:
        print(f"Raté ! Ton nombre : {user_number}, nombre aléatoire : {random_number}")

# Appel avec un nombre de notre choix
compare_numbers(50)



# Exercise 6 

# size et text ont des valeurs par défaut
def make_shirt(size="large", text="I love Python"):
    print(f"Taille : {size} | Message : {text}")

# 1. Tout par défaut
make_shirt()

# 2. On change juste la taille
make_shirt(size="medium")

# 3. On change les deux
make_shirt(size="small", text="Message personnalisé")

# Bonus : arguments nommés dans n'importe quel ordre
make_shirt(text="Hello !", size="XL")



# Exercise 7
import random

# random.uniform() retourne un flottant (ex: 23.7°C)
def get_random_temp():
    return round(random.uniform(-10, 40), 1)

def main():
    temp = get_random_temp()
    print(f"La température est de {temp}°C.")

    # Conseils selon la plage de température
    if temp < 0:
        print("Brrr, il gèle ! Couvrez-vous bien.")
    elif temp < 16:
        print("Il fait froid. N'oubliez pas votre manteau.")
    elif temp < 24:
        print("Temps agréable !")
    elif temp <= 32:
        print("Un peu chaud. Pensez à vous hydrater.")
    else:
        print("Forte chaleur ! Restez au frais.")

# Appel de la fonction principale
main()


# Exercise 8 

toppings      = []    # liste vide pour stocker les ingrédients
base_price    = 10    # prix de base de la pizza
topping_price = 2.5   # chaque topping coûte 2,50 $

# Boucle infinie : on sort avec "break" quand l'utilisateur tape "quit"
while True:
    topping = input("Ajouter un topping (ou 'quit' pour terminer) : ")

    if topping == "quit":
        break           # on sort de la boucle

    toppings.append(topping)
    print(f"→ Ajout de {topping} à la pizza.")

# Afficher le récap après la boucle
print("\nVotre pizza :")
for t in toppings:
    print(f"  • {t}")

# Calcul du total — :.2f affiche 2 chiffres après la virgule
total = base_price + len(toppings) * topping_price
print(f"Total : ${total:.2f}")