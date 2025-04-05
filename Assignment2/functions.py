import random
import os

def use_loot(belt, hero):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    if belt:
        first_item = belt.pop(0)
        if first_item in good_loot_options:
            hero.health_points = min(20, hero.health_points + 2)
            print(f"You used {first_item} to increase your health to {hero.health_points}")
        elif first_item in bad_loot_options:
            hero.health_points = max(0, hero.health_points - 2)
            print(f"You used {first_item} and lost health, now at {hero.health_points}")
        else:
            print(f"You used {first_item}, but it had no effect.")
    else:
        print("Your belt is empty, no loot to use.")
    return belt, hero

def save_game(winner, hero_name="", num_stars=0):
    monster_kills = load_monster_kills()
    if winner == "Hero":
        monster_kills += 1
        with open("save.txt", "a") as file:
            file.write(f"Hero {hero_name} defeated a monster and gained {num_stars} stars.\n")
    elif winner == "Monster":
        with open("save.txt", "a") as file:
            file.write("Monster defeated the hero.\n")
    with open("monster_kills.txt", "w") as file:
        file.write(str(monster_kills))

def load_monster_kills():
    try:
        with open("monster_kills.txt", "r") as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0
