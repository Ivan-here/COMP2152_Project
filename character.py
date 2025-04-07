import random

class Character:
    def __init__(self):
        self.__combat_strength = random.randint(1, 6)
        self.__health_points = random.randint(1, 20)
        # Elemental Brawl
        self._element = random.choice(["Fire", "Water", "Earth", "Air"])

    @property
    def combat_strength(self):
        return self.__combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        if 1 <= int(value) <= 6:
            self.__combat_strength = int(value)
        else:
            raise ValueError("Combat strength must be between 1 and 6.")

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, value):
        if int(value) >= 0:
            self.__health_points = int(value)
        else:
            raise ValueError("Health points cannot be negative.")

    @property
    def element(self):
        return self._element

    @element.setter
    def element(self, value):
        if value in ["Fire", "Water", "Earth", "Air"]:
            self._element = value
        else:
            raise ValueError("Element must be Fire, Water, Earth, or Air")

    def __del__(self):
        print(
            f"The {self.__class__.__name__} object (Combat Strength: {self.__combat_strength}, Health Points: {self.__health_points}, Element: {self._element}) is being destroyed by the garbage collector.")