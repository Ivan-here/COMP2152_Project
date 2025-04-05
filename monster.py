from character import Character
import random

class Monster(Character):
    def __init__(self):
        super().__init__(combat_strength=range(1, 7), health_points=range(1, 21))

    def monster_attacks(self, hero, element_advantage):
        ascii_image2 = """                                                                 
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
        print(ascii_image2)
        print(f"    |    Monster's Claw ({self.combat_strength}) ---> Hero ({hero.health_points})")
        damage = self.combat_strength

        #Elemental Brawl
        if element_advantage.get(self.element) == hero.element:
            bonus = random.randint(1, 6)
            damage += bonus
            advantage_summary=f"    |    Elemental advantage! {self.element} > {hero.element}, +{bonus} bonus damage!"
        elif element_advantage.get(hero.element) == self.element:
            penalty = random.randint(1, 3)
            damage = max(1, damage - penalty)
            advantage_summary =f"    |    Elemental disadvantage! {hero.element} > {self.element}, -{penalty} damage!"
        else:
            advantage_summary = "    |    No elemental advantage this round."

        print(advantage_summary)

        print(f"    |    Monster's damage this round: {damage}")

        if damage >= hero.health_points:
            hero.health_points = 0
            print("    |    Hero is dead")
        else:
            hero.health_points -= damage
            print(f"    |    The monster has reduced Hero's health to: {hero.health_points}")
        return hero.health_points

    def __del__(self):
        super().__del__()
