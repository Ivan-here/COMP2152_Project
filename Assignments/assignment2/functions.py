import random
import os

def generate_weather():
    """Randomly select the weather condition."""
    return random.choice(["Sunshine", "Cloudy", "Raining"])
def use_loot(belt, hero):
    """Use the first item from the belt and adjust hero's health points accordingly."""
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
    """Save the game results and update the number of monsters killed."""
    monster_kills = load_monster_kills()

    if winner == "Hero":
        monster_kills += 1
        with open("save.txt", "a") as file:
            file.write(f"Hero {hero_name} defeated a monster and gained {num_stars} stars.\n")
    elif winner == "Monster":
        with open("save.txt", "a") as file:
            file.write("Monster defeated the hero.\n")


    with open("mon_kills.txt", "w") as file:
        file.write(str(monster_kills))


def load_monster_kills():
    """Load the total number of monsters killed from file."""
    try:
        if not os.path.exists("mon_kills.txt"):
            raise FileNotFoundError("mon_kills.txt does not exist.")

        with open("mon_kills.txt", "r") as file:
            content = file.read().strip()


            return int(content) if content.isdigit() else 0

    except (FileNotFoundError, ValueError) as e:
        print(f"Error loading monster kills: {e}. Assuming 0 kills.")
        return 0

