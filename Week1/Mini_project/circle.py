# Daily Challenge : Circle class
# Concepts: OOP, class methods, dunder (magic) methods

import math


class Circle:
    """Represents a circle defined by its radius."""

    def __init__(self, radius):
        self.radius = radius

    # Alternative constructor (decorator)

    @classmethod
    def from_diameter(cls, diameter):
        """Create a Circle by specifying its diameter instead of radius."""
        return cls(diameter / 2)

    # Properties

    @property
    def diameter(self):
        """Return the diameter, computed from the radius."""
        return self.radius * 2

    @property
    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    # Dunder methods

    def __str__(self):
        """Human-readable string representation."""
        return (f"Circle(radius={self.radius}, "
                f"diameter={self.diameter}, "
                f"area={self.area:.2f})")

    def __repr__(self):
        """Unambiguous representation (useful in lists/debugging)."""
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        """Add two circles — returns a new Circle with combined radii."""
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        """Greater-than comparison based on radius."""
        return self.radius > other.radius

    def __lt__(self, other):
        """Less-than comparison based on radius — enables list sorting."""
        return self.radius < other.radius

    def __eq__(self, other):
        """Equality check based on radius."""
        return self.radius == other.radius


# --- Tests ---

if __name__ == "__main__":

    # Create circles via radius and via diameter
    c1 = Circle(5)
    c2 = Circle(3)
    c3 = Circle.from_diameter(16)   # radius = 8
    c4 = Circle(3)

    print(" Individual Circles")
    print(c1)
    print(c2)
    print(c3)

    print("\n Area ")
    print(f"Area of c1: {c1.area:.2f}")
    print(f"Area of c3: {c3.area:.2f}")

    print("\n Addition")
    c_sum = c1 + c2
    print(f"c1 + c2 = {c_sum}")

    print("\n Comparisons")
    print(f"c1 > c2  → {c1 > c2}")    # True  (5 > 3)
    print(f"c2 > c1  → {c2 > c1}")    # False
    print(f"c2 == c4 → {c2 == c4}")   # True  (3 == 3)
    print(f"c1 == c3 → {c1 == c3}")   # False

    print("\n Sorting")
    circles = [c1, c2, c3, c4]
    print(f"Unsorted : {circles}")
    print(f"Sorted   : {sorted(circles)}")
    print(f"Reversed : {sorted(circles, reverse=True)}")