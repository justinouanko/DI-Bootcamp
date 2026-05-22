# Challenge Old MacDonald’s Farm
"""

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}
        def add_animal(self, animal_type, count):
            
"""
class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **kwargs):
        # Handle positional call: add_animal('cow', 5)
        if animal_type:
            self.animals[animal_type] = self.animals.get(animal_type, 0) + count

        # Handle kwargs call: add_animal(cow=5, sheep=2)
        for animal, qty in kwargs.items():
            self.animals[animal] = self.animals.get(animal, 0) + qty

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()

        # Pluralize if count > 1
        pluralized = [
            animal + "s" if self.animals[animal] > 1 else animal
            for animal in animal_types
        ]

        if len(pluralized) == 1:
            animals_str = pluralized[0]
        else:
            animals_str = ", ".join(pluralized[:-1]) + " and " + pluralized[-1]

        return f"{self.name}'s farm has {animals_str}."


# Tests

macdonald = Farm("McDonald")

# Classic positional calls
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())

print("\nBonus: kwargs style")
macdonald2 = Farm("McDonald")
macdonald2.add_animal(cow=5, sheep=2, goat=12)
print(macdonald2.get_info())
print(macdonald2.get_short_info())

