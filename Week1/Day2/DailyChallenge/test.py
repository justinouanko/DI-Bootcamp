# Challenge 1 

user_input = input("Enter a word: ")
letter_index = {}

for index, letter in enumerate(user_input):
    if letter in letter_index:
        letter_index[letter].append(index)
    else:
        letter_index[letter] = [index]
print(letter_index)