# Import the random library for dice rolling
import random
from character import Character


class Hero(Character):

    def __init__(self):
        # Define dice options
        small_dice_options = list(range(1, 7))  # 1-6
        big_dice_options = list(range(1, 21))  # 1-20

        # Roll for combat strength and health points
        combat_strength = random.choice(small_dice_options)
        health_points = random.choice(big_dice_options)

        # Call parent constructor with generated values
        super().__init__(combat_strength, health_points)

        print(f"Hero created with combat strength {self.combat_strength} and health points {self.health_points}")

    def hero_attacks(self, monster):
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
            monster.health_points = 0
            print("    |    You have killed the monster")
        else:
            monster.health_points -= self.combat_strength
            print(f"    |    You have reduced the monster's health to: {monster.health_points}")

        return monster.health_points

    def __del__(self):
        print(
            f"{self.__class__.__name__} object (Combat Strength: {self.combat_strength}, Health Points: {self.health_points}) is being destroyed by the garbage collector.")