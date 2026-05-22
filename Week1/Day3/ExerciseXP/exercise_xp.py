
# Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Garfield", 3)
cat2 = Cat("Tom", 7)
cat3 = Cat("Miaou", 5)

# Step 2: Find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    return max([cat1, cat2, cat3], key=lambda cat: cat.age)

# Step 3: Print details
oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")

"""""
# Exercise 2: Dogs Old version

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 1: Create dog objects

davids_dog = Dog("Rex", 50) 
sarahs_dog = Dog("woufi", 20)

# Step 2: Print details

print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")

# Step 3: Compare heights
if davids_dog.height > sarahs_dog.height:   
    print(f"{davids_dog.name} is taller than {sarahs_dog.name}.")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is taller than {davids_dog.name}.")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same height.")  

"""""    

# Exercise 2: Dogs

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2: Create dog objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 35)

# Step 3: Print details and call methods
for dog in [davids_dog, sarahs_dog]:
    print(f"Name: {dog.name}, Height: {dog.height} cm")
    dog.bark()
    dog.jump()

# Step 4: Compare sizes
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}.")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same size.")



# Exercise 3: Who's The Song Producer? Old version

"""""
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

"""


# Exercise 3: Who's the song producer?

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song([
    "There's a lady who's sure",
    "all that glitters is gold",
    "and she's buying a stairway to heaven"
])

stairway.sing_me_a_song()


#exercise 4: Afternoon At The Zoo Old version
""""
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = {}
        for animal in sorted(self.animals):
            first_letter = animal[0]
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = []
            sorted_animals[first_letter].append(animal)
        return sorted_animals

    def get_groups(self):
        groups = {}
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)
        return groups
"""


# Exercise 4: Afternoon at the Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, *args):          # Bonus: accepts multiple animals
        for new_animal in args:
            if new_animal not in self.animals:
                self.animals.append(new_animal)

    def get_animals(self):
        print(f"Animals in {self.name}: {self.animals}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        grouped = {}
        for animal in sorted(self.animals):
            key = animal[0].upper()
            grouped.setdefault(key, []).append(animal)
        return grouped

    def get_groups(self):
        for letter, group in self.sort_animals().items():
            print(f"{letter}: {group}")


# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Cat", "Cougar", "Lion", "Zebra")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.get_groups()

