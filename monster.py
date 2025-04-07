
# Import the random library for dice rolling
import random
from character import Character

class Monster(Character):

    
    def __init__(self):
        super().__init__(combat_strength=range(1, 7), health_points=range(1, 21))
        
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
        if power_name in self.powers:
            power_value = self.powers[power_name]
            self.combat_strength = min(6, self.combat_strength + power_value)
            print(f"    |    The monster's combat strength is now {self.combat_strength} using the {power_name} magic power")
            return power_value
        else:
            print(f"    |    The monster doesn't have the power: {power_name}")
            return 0
    
    def __del__(self):

        super().__del__()
        print("The Monster object is being destroyed by the garbage collector")

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")

