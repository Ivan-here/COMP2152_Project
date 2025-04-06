import random

class Character:
    def __init__(self):
        self.__combat_strength = random.randint(1, 6)
        self.__health_points = random.randint(1, 20)

    @property
    def combat_strength(self):
        return self.__combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        if 1 <= value <= 6:
            self.__combat_strength = value
        else:
            raise ValueError("Combat strength must be between 1 and 6.")

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, value):
        if value >= 0:
            self.__health_points = value
        else:
            raise ValueError("Health points cannot be negative.")

    def __del__(self):
        """Customized destructor to print detailed info about the character when it is destroyed."""
        print(f"The {self.__class__.__name__} object (Combat Strength: {self.__combat_strength}, Health Points: {self.__health_points}) is being destroyed by the garbage collector.")

