from character import Character
import os

class Monster(Character):
    def __init__(self):
        super().__init__()
        self._wins, self._stage = self.load_monster_progress()

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
        super().__del__()
