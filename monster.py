import random
from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()  # no arguments needed anymore

        self._powers = {
            "Fire Magic": 2,
            "Freeze Time": 4,
            "Super Hearing": 6
        }

        print(f"Monster created with combat strength {self.combat_strength}, "
              f"health points {self.health_points}, and element {self.element}")

    @property
    def powers(self):
        return self._powers

    @powers.setter
    def powers(self, value):
        self._powers = value

    def use_power(self, power_name):
        if power_name in self.powers:
            power_value = self.powers[power_name]
            self.combat_strength = min(6, self.combat_strength + power_value)
            print(f"    |    The monster's combat strength is now {self.combat_strength} using the {power_name} magic power")
            return power_value
        else:
            print(f"    |    The monster doesn't have the power: {power_name}")
            return 0

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

        # Elemental brawl
        if element_advantage.get(self.element) == hero.element:
            bonus = random.randint(1, 6)
            damage += bonus
            advantage_summary = f"    |    Elemental advantage! {self.element} > {hero.element}, +{bonus} bonus damage!"
        elif element_advantage.get(hero.element) == self.element:
            penalty = random.randint(1, 3)
            damage = max(1, damage - penalty)
            advantage_summary = f"    |    Elemental disadvantage! {hero.element} > {self.element}, -{penalty} damage!"
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