
# Import the random library for dice rolling
import random
import os
import platform

class Character:
    """
    Base Character class for both Hero and Monster classes.
    Contains common attributes and methods.
    """
    
    def __init__(self, name="Character"):
        """
        Constructor for the Character class.
        
        Args:
            name (str): The name of the character
        """
        self._name = name
        self._combat_strength = 0
        self._health_points = 0
    
    @property
    def name(self):
        """Getter for name property"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter for name property"""
        self._name = value
    
    @property
    def combat_strength(self):
        """Getter for combat_strength property"""
        return self._combat_strength
    
    @combat_strength.setter
    def combat_strength(self, value):
        """Setter for combat_strength property"""
        self._combat_strength = value
    
    @property
    def health_points(self):
        """Getter for health_points property"""
        return self._health_points
    
    @health_points.setter
    def health_points(self, value):
        """Setter for health_points property"""
        self._health_points = value
    
    def is_alive(self):
        """
        Check if the character is still alive.
        
        Returns:
            bool: True if health points > 0, False otherwise
        """
        return self.health_points > 0
    
    def take_damage(self, damage):
        """
        Reduce health points by the damage amount.
        
        Args:
            damage (int): The amount of damage to take
            
        Returns:
            int: The updated health points
        """
        self.health_points = max(0, self.health_points - damage)
        return self.health_points
    
    def roll_dice(self, min_val=1, max_val=6):
        """
        Roll a dice with the specified range.
        
        Args:
            min_val (int): The minimum value of the dice
            max_val (int): The maximum value of the dice
            
        Returns:
            int: The result of the dice roll
        """
        return random.randint(min_val, max_val)
    
    def __del__(self):
        """
        Destructor for the Character class.
        """
        pass

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

