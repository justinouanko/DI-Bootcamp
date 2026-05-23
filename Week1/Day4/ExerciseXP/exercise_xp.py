""""
# Step 1: Create the Siamese Class

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
# Step 2: list of cat instances
bengal    = Bengal("Luna", 3)
chartreux = Chartreux("Mochi", 5)
siamese   = Siamese("Nala", 2)

all_cats = [bengal, chartreux, siamese]

# Step 3: Pets instance
sara_pets = Pets(all_cats)

# Step 4: walk
sara_pets.walk()

# Output:
# Luna is just walking around
# Mochi is just walking around
# Nala is just walking around
"""

# Class
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Step 1
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Step 2
bengal    = Bengal("Luna", 3)
chartreux = Chartreux("Mochi", 5)
siamese   = Siamese("Nala", 2)

all_cats = [bengal, chartreux, siamese]

# Step 3
sara_pets = Pets(all_cats)

# Step 4
sara_pets.walk()

# Exercise 2: Dogs


class Dog:
    def __init__(self, name, age, weight):
        self.name   = name
        self.age    = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power    = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f'{self.name} won the fight!'
        elif other_power > my_power:
            return f'{other_dog.name} won the fight!'
        else:
            return "It's a tie!"


# Step 2 instances
dog1 = Dog("Rex",   3, 25)
dog2 = Dog("Buddy", 5, 20)
dog3 = Dog("Max",   2, 30)

# Step 3 test
print(dog1.bark())         # Rex is barking
print(dog2.run_speed())   # 40.0
print(dog1.fight(dog2))   # Rex won the fight!


#  Exercise 3: Dogs Domesticated

# pet_dog.py
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True
    def play(self, *args):
        names = [self.name] + [dog.name for dog in args]
        print(f'{", ".join(names)} all play together')

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead",
            ]
            print(f'{self.name} {random.choice(tricks)}')


# Test
fido  = PetDog("Fido",  2, 10)
buddy = PetDog("Buddy", 3, 12)

fido.train()              # Fido is barking  (sets trained=True)
fido.play(buddy)          # Fido, Buddy all play together
fido.do_a_trick()         # Fido plays dead  (random)

# Exercise 4: Family and Person Classes

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age        = age
        self.last_name  = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members   = []

    def born(self, first_name, age):
        person           = Person(first_name, age)
        person.last_name = self.last_name
        self.members.append(person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(
                        "You are over 18, your parents Jane and John "
                        "accept that you will go out with your friends"
                    )
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f'No member named {first_name} found.')

    def family_presentation(self):
        print(f'Family: {self.last_name}')
        for member in self.members:
            print(f'  {member.first_name}, age {member.age}')


# Test
family = Family("Dupont")
family.born("Alice", 20)
family.born("Tom",   15)
family.born("Sara",  18)

family.family_presentation()
family.check_majority("Alice") # over 18 
family.check_majority("Tom")    # under 18 