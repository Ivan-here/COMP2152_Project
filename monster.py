
# Import the random library for dice rolling
import random
from character import Character

class Monster(Character):
    """
    Monster class representing the enemy in the game.
    Inherits from the Character class.
    """
    
    def __init__(self, name="Monster"):
        """
        Constructor for the Monster class.
        Rolls dice to determine combat strength and health points.
        
        Args:
            name (str): The name of the monster
        """
        super().__init__(name)
        
        # Define dice options
        small_dice_options = list(range(1, 7))  # 1-6
        big_dice_options = list(range(1, 21))   # 1-20
        
        # Roll for combat strength (1-6)
        self.combat_strength = random.choice(small_dice_options)
        
        # Roll for health points (1-20)
        self.health_points = random.choice(big_dice_options)
        
        # Monster powers
        self._powers = {
            "Fire Magic": 2,
            "Freeze Time": 4,
            "Super Hearing": 6
        }
        
        print(f"Monster created with combat strength {self.combat_strength} and health points {self.health_points}")
    
    @property
    def powers(self):
        """Getter for powers property"""
        return self._powers
    
    @powers.setter
    def powers(self, value):
        """Setter for powers property"""
        self._powers = value
    
    def monster_attacks(self, hero):
        """
        Method for the monster to attack a hero.
        
        Args:
            hero: The hero object to attack
            
        Returns:
            int: The hero's updated health points after the attack
        """
        ascii_image = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
        print(ascii_image)
        print(f"    |    Monster's Claw ({self.combat_strength}) ---> Player ({hero.health_points})")
        
        if self.combat_strength >= hero.health_points:
            # Monster was strong enough to kill player in one blow
            hero.health_points = 0
            print("    |    Player is dead")
        else:
            # Monster only damaged the player
            hero.health_points -= self.combat_strength
            print(f"    |    The monster has reduced Player's health to: {hero.health_points}")
            
        return hero.health_points
    
    def use_power(self, power_name):
        """
        Use a monster power to increase combat strength.
        
        Args:
            power_name (str): The name of the power to use
            
        Returns:
            int: The power value added to combat strength
        """
        if power_name in self.powers:
            power_value = self.powers[power_name]
            self.combat_strength = min(6, self.combat_strength + power_value)
            print(f"    |    The monster's combat strength is now {self.combat_strength} using the {power_name} magic power")
            return power_value
        else:
            print(f"    |    The monster doesn't have the power: {power_name}")
            return 0
    
    def __del__(self):
        """
        Destructor for the Monster class.
        Prints a message when the object is being destroyed.
        """
        super().__del__()
        print("The Monster object is being destroyed by the garbage collector")

# Example usage:
if __name__ == "__main__":
    # Instantiate a monster object
    monster = Monster()
    
    # Create a mock hero for testing
    from hero import Hero
    hero = Hero()
    
    # Test the monster_attacks method
    monster.monster_attacks(hero)
    print(f"Hero health after attack: {hero.health_points}")
    
    # Test the use_power method
    monster.use_power("Fire Magic")

from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()

    def monster_attacks(self, hero):
        print(f"Monster attacks with strength {self.combat_strength}!")
        if self.combat_strength >= hero.health_points:
            hero.health_points = 0
            print("Monster has killed the hero!")
        else:
            hero.health_points -= self.combat_strength
            print(f"Hero's health reduced to {hero.health_points}")

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")

