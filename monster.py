import random
import os
from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()  # Initialize Character base class

        # Local branch additions: track wins and evolution stage
        self._wins, self._stage = self.load_monster_progress()

        # Main branch functionality: monster powers
        self._powers = {
            "Fire Magic": 2,
            "Freeze Time": 4,
            "Super Hearing": 6
        }

        # Print combined initialization info
        print(f"Monster created with combat strength {self.combat_strength}, "
              f"health points {self.health_points}, element {self.element}, "
              f"wins {self._wins}, stage {self._stage}")

    # --- Local branch evolution features ---
    @property
    def stage(self):
        return self._stage

    def increase_wins(self):
        self._wins += 1
        print(f"Monster has {self._wins} wins.")
        self.check_evolution()
        self.save_monster_progress()

    def check_evolution(self):
        if self._wins >= 3 and self._stage != "Dragon":
            if self._stage == "Larva":
                self._stage = "Beast"
            elif self._stage == "Beast":
                self._stage = "Dragon"
            print(f"Monster has evolved! New stage: {self._stage}")

    def load_monster_progress(self):
        if os.path.exists("monster_progress.txt"):
            with open("monster_progress.txt", "r") as file:
                try:
                    wins = int(file.readline().strip())
                    stage = file.readline().strip()
                    return wins, stage
                except:
                    return 0, "Larva"
        else:
            return 0, "Larva"

    def save_monster_progress(self):
        with open("monster_progress.txt", "w") as file:
            file.write(str(self._wins) + "\n")
            file.write(self._stage + "\n")
    # --- End local branch evolution features ---

    # --- Main branch powers features ---
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
    # --- End main branch powers features ---

    # --- Merged monster_attacks function ---
    def monster_attacks(self, hero, element_advantage=None):
        """
        If element_advantage is provided (a dict mapping elements), perform an elemental brawl.
        Otherwise, use a simpler attack mechanism.
        """
        if element_advantage is None:
            # Local branch style attack (without elemental calculations)
            print(f"Monster attacks with strength {self.combat_strength}!")
            if self.combat_strength >= hero.health_points:
                hero.health_points = 0
                print("Monster has killed the hero!")
            else:
                hero.health_points -= self.combat_strength
                print(f"Hero's health reduced to {hero.health_points}")
        else:
            # Main branch style attack with elemental advantage/disadvantage
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
                self.increase_wins()
            else:
                hero.health_points -= damage
                print(f"    |    The monster has reduced Hero's health to: {hero.health_points}")
        return hero.health_points
    # --- End merged monster_attacks function ---

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")
        super().__del__()
