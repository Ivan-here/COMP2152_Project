from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()  # Calls Character's constructor

    def hero_attacks(self, monster):
        print(f"Hero attacks with strength {self.combat_strength}!")
        if self.combat_strength >= monster.health_points:
            monster.health_points = 0
            print("Hero has killed the monster!")
        else:
            monster.health_points -= self.combat_strength
            print(f"Monster's health reduced to {monster.health_points}")

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
