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
