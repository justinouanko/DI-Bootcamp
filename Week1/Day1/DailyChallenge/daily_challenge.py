# CHALLENGE 1

print("Entrez un nombre: ")
number = int(input())
print("Entrez la longeur du nombre en chiffre: ")
length = int(input())

multiples_list = []

for i in range(1, length + 1):
    # Calculate the multiple and add it to the list
    multiples_list.append(number * i)

print(f"number: {number} - length {length} ➞ {multiples_list}")



# CHALLENGE 2


# 1. Demander les entrées à l'utilisateur et les convertir en entiers (int)
number = int(input("Entrez le nombre de base : "))
length = int(input("Entrez la longueur désirée pour la liste : "))

# 2. Initialiser une liste vide pour stocker les multiples
multiples_list = []

# 3. Boucler de 1 jusqu'à (length + 1) car la fonction range() exclut la dernière valeur
for i in range(1, length + 1):
    # Calculer le multiple et l'ajouter à la liste
    multiples_list.append(number * i)

# 4. Afficher le résultat final
print(f"nombre : {number} - longueur {length} ➞ {multiples_list}")