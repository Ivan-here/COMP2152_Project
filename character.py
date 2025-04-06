# Import the random library for dice rolling
import random
import os
import platform

class Character:
    
    def __init__(self, name="Character"):
        self._name = name
        self._combat_strength = 0
        self._health_points = 0
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def combat_strength(self):
        return self._combat_strength
    
    @combat_strength.setter
    def combat_strength(self, value):
        self._combat_strength = value
    
    @property
    def health_points(self):
        return self._health_points
    
    @health_points.setter
    def health_points(self, value):
        self._health_points = value
    
    def is_alive(self):
        return self.health_points > 0
    
    def take_damage(self, damage):
        self.health_points = max(0, self.health_points - damage)
        return self.health_points
    
    def roll_dice(self, min_val=1, max_val=6):
        return random.randint(min_val, max_val)
    
    def __del__(self):
        pass
