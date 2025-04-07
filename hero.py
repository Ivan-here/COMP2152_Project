# Import the random library for dice rolling
import random
from character import Character


class Hero(Character):

    def __init__(self):
        # Define dice options
        super().__init__()
        small_dice_options = list(range(1, 7))  # 1-6
        big_dice_options = list(range(1, 21))  # 1-20

        combat_strength = random.choice(small_dice_options)
        health_points = random.choice(big_dice_options)

        print(f"Hero created with combat strength {self.combat_strength} and health points {self.health_points}")

    def hero_attacks(self, monster, element_advantage=None):
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
        print(f"    |    Hero's weapon ({self.combat_strength}) ---> Monster ({monster.health_points})")

        # Default damage
        damage = self.combat_strength

        # Elemental brawl logic
        if element_advantage and hasattr(self, 'element') and hasattr(monster, 'element'):
            if element_advantage.get(self.element) == monster.element:
                bonus = random.randint(1, 4)
                damage += bonus
                print(f"    |    Elemental advantage! {self.element} > {monster.element}, +{bonus} bonus damage!")
            elif element_advantage.get(monster.element) == self.element:
                penalty = random.randint(1, 3)
                damage = max(1, damage - penalty)
                print(f"    |    Elemental disadvantage! {monster.element} > {self.element}, -{penalty} damage!")
            else:
                print("    |    No elemental advantage this round.")

        print(f"    |    Hero's damage this round: {damage}")

        if damage >= monster.health_points:
            monster.health_points = 0
            print("    |    You have killed the monster")
        else:
            monster.health_points -= damage
            print(f"    |    You have reduced the monster's health to: {monster.health_points}")

        return monster.health_points

    def __del__(self):
        print(
            f"{self.__class__.__name__} object (Combat Strength: {self.combat_strength}, Health Points: {self.health_points}) is being destroyed by the garbage collector.")