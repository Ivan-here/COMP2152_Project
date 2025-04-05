import random

class Character:
    def __init__(self, combat_strength, health_points):
        self.__combat_strength = random.choice(combat_strength)
        self.__health_points = random.choice(health_points)
        #Elemental Brawl
        self._element = random.choice(["Fire", "Water", "Earth", "Air"])

    @property
    def combat_strength(self):
        return self.__combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        if int(value) > 0:
            self.__combat_strength = value
        else:
            raise ValueError("Can't be negative")

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, value):
        if int(value) >= 0:
            self.__health_points = value
        else:
            raise ValueError("Can't be negative")

    #Elemental Brawl
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
        print(f"The {self.__class__.__name__} object is being destroyed by the garbage collector.")