import random
import os
import platform
from hero import Hero
from monster import Monster
import functions

# Print OS and Python version
print(f"Operating System: {os.name}")
print(f"Python Version: {platform.python_version()}")

# Display number of monsters killed
monster_kills = functions.load_monster_kills()
print(f"Total Monsters Killed Across Games: {monster_kills}")

# Define game variables
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []
num_stars = 0

# Input validation for hero and monster combat strength
i = 0
input_invalid = True
while input_invalid and i in range(5):
    print("------------------------------------------------------------------")
    hero_combat_input = input("Enter your combat Strength (1-6): ")
    monster_combat_input = input("Enter the monster's combat Strength (1-6): ")

    if not hero_combat_input.isnumeric() or not monster_combat_input.isnumeric():
        print("Invalid input. Enter numbers between 1 and 6.")
        i += 1
        continue
    elif int(hero_combat_input) not in range(1, 7) or int(monster_combat_input) not in range(1, 7):
        print("Enter a valid integer between 1 and 6.")
        i += 1
        continue
    else:
        input_invalid = False
        hero_combat = int(hero_combat_input)
        monster_combat = int(monster_combat_input)

# Initialize hero and monster objects
hero = Hero()
monster = Monster()
hero.combat_strength = hero_combat
monster.combat_strength = monster_combat

print(f"Hero starts with {hero.health_points} HP and {hero.combat_strength} combat strength.")
print(f"Monster starts with {monster.health_points} HP and {monster.combat_strength} combat strength.")
print(f"Monster stage: {monster.stage}")  # ← Bonus tip added

# Monster checks for evolution before the fight starts
monster.check_evolution()

# Fight Sequence
print("------------------------------------------------------------------")
print("You meet the monster. FIGHT!!")
while monster.health_points > 0 and hero.health_points > 0:
    input("Roll to see who strikes first (Press Enter)")
    if random.choice([True, False]):
        hero.hero_attacks(monster)
    else:
        monster.monster_attacks(hero)

# Assign stars based on the outcome
if hero.health_points > 0:
    print("Hero wins!")

    if hero.health_points > 15:
        num_stars = 3
    elif hero.health_points > 5:
        num_stars = 2
    else:
        num_stars = 1

    print(f"Hero receives {num_stars} stars!")
    functions.save_game("Hero", num_stars=num_stars)
else:
    print("Monster wins!")
    functions.save_game("Monster")
    monster.increase_wins()  # ← Save the monster's defeat count

# Save the total number of monsters killed
monster_kills += 1
with open("monster_kills.txt", "w") as file:
    file.write(str(monster_kills))
