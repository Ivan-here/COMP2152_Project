import functions
import random
from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__(combat_strength=range(1, 7), health_points=range(1, 21))

    def hero_attacks(self, monster, element_advantage):
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
        #Elemental brawl
        damage = self.combat_strength

        if element_advantage.get(self.element) == monster.element:
            bonus = random.randint(1, 4)
            damage += bonus
            advantage_summary=f"    |    Elemental advantage! {self.element} > {monster.element}, +{bonus} bonus damage!"
        elif element_advantage.get(monster.element) == self.element:
            penalty = random.randint(1, 3)
            #Hero's damage never drops below 1
            damage = max(1, damage - penalty)
            advantage_summary=f"    |    Elemental disadvantage! {monster.element} > {self.element}, -{penalty} damage!"
        else:
            advantage_summary=f"    |    No elemental advantage this round."

        print(advantage_summary)

        print(f"    |    Hero's damage this round: {damage}")

        if damage >= monster.health_points:
            monster.health_points = 0
            print("    |    You have killed the monster")
        else:
            monster.health_points -= damage
            print(f"    |    You have reduced the monster's health to: {monster.health_points}")

        return monster.health_points

    def __del__(self):
        super().__del__()