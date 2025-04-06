# Import the random library for dice rolling
import random
from character import Character

class Hero(Character):
    """
    Hero class representing the player character in the game.
    Has combat strength and health points as properties.
    """
    
    def __init__(self, name="Hero"):
        """
        Constructor for the Hero class.
        Rolls dice to determine combat strength and health points.
        
        Args:
            name (str): The name of the hero
        """
        super().__init__(name)
        
        # Define dice options
        small_dice_options = list(range(1, 7))  # 1-6
        big_dice_options = list(range(1, 21))   # 1-20
        
        # Roll for combat strength (1-6)
        self.combat_strength = random.choice(small_dice_options)
        
        # Roll for health points (1-20)
        self.health_points = random.choice(big_dice_options)
        
        print(f"Hero created with combat strength {self.combat_strength} and health points {self.health_points}")
    
    def hero_attacks(self, monster):
        """
        Method for the hero to attack a monster.
        
        Args:
            monster: The monster object to attack
            
        Returns:
            int: The monster's updated health points after the attack
        """
        ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  

  """
        print(ascii_image)
        print(f"    |    Player's weapon ({self.combat_strength}) ---> Monster ({monster.health_points})")
        
        if self.combat_strength >= monster.health_points:
            # Player was strong enough to kill monster in one blow
            monster.health_points = 0
            print("    |    You have killed the monster")
        else:
            # Player only damaged the monster
            monster.health_points -= self.combat_strength
            print(f"    |    You have reduced the monster's health to: {monster.health_points}")
            
        return monster.health_points
    
    def __del__(self):
        """
        Destructor for the Hero class.
        Prints a message when the object is being destroyed.
        """
        super().__del__()
        print("The Hero object is being destroyed by the garbage collector")

# Example usage:
if __name__ == "__main__":
    # Instantiate a hero object
    hero = Hero()
    
    # Create a mock monster for testing
    from monster import Monster
    monster = Monster()
    
    # Test the hero_attacks method
    hero.hero_attacks(monster)
    print(f"Monster health after attack: {monster.health_points}")
