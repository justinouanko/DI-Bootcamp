# CHALLENGE 1

print("Entrez un nombre: ")
number = int(input())
print("Entrez la longeur du nombre en chiffre: ")
length = int(input())


multiples = []

for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)



# CHALLENGE 2

word = input("Entrez un mot : ")

result = ""

for i in range(len(word)):
    if i == 0 or word[i] != word[i - 1]:
        result += word[i]

print(result)
