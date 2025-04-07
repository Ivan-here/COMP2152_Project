#!/usr/bin/env python
import random
import os
import platform

# --- Local Branch Addition: Print OS, Python version, and total monsters killed ---
print(f"Operating System: {os.name}")
print(f"Python Version: {platform.python_version()}")

import functions
# Display total monsters killed across games (local branch addition)
monster_kills = functions.load_monster_kills()
print(f"Total Monsters Killed Across Games: {monster_kills}")

# --- Main Branch Imports ---
from functions import trigger_random_event
from hero import Hero
from monster import Monster
import functions
import weather

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the number of stars to award the player
num_stars = 0

# --- Local Branch Addition: Input Validation for Combat Strengths ---
i = 0
input_invalid = True
while input_invalid and i < 5:
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

# --- Initialize Hero and Monster Objects ---
hero = Hero()
monster = Monster()

# Assign combat strengths based on user input (local branch addition)
hero.combat_strength = hero_combat
monster.combat_strength = monster_combat

# Display initial stats
print(f"Hero starts with {hero.health_points} HP and {hero.combat_strength} combat strength.")
print(f"Monster starts with {monster.health_points} HP and {monster.combat_strength} combat strength.")
print(f"Monster stage: {monster.stage}")  # local branch bonus

# Monster evolution: check for evolution before the fight starts
monster.check_evolution()

# --- Main Branch: Roll for Weapon ---
print("    |", end="    ")
input("Roll the dice for your weapon (Press enter)")
ascii_image5 = """
          , %               .           
*      @./  #         @  &.(         
@        /@   (      ,    @       # @ 
@        ..@#% @     @&*#@(         % 
 &   (  @    (   / /   *    @  .   /  
   @ % #         /   .       @ ( @    
               %   .@*                
             #         .              
           /     # @   *              
               ,     %                
          @&@           @&@
"""
print(ascii_image5)
small_dice_options = list(range(1, 7))
weapon_roll = random.choice(small_dice_options)

# Limit the combat strength to 6 after adding the dice roll
hero.combat_strength = min(6, hero.combat_strength + weapon_roll)
print(f"    |    The hero's weapon is {weapons[weapon_roll - 1]}")

# Lab 06 - Question 5b: Adjust combat strength based on previous game results
functions.adjust_combat_strength(hero.combat_strength, monster.combat_strength)

# --- Weapon Roll Analysis ---
print("    ------------------------------------------------------------------")
print("    |", end="    ")
input("Analyze the Weapon roll (Press enter)")
print("    |", end="    ")
if weapon_roll <= 2:
    print("--- You rolled a weak weapon, friend")
elif weapon_roll <= 4:
    print("--- Your weapon is meh")
else:
    print("--- Nice weapon, friend!")

# If the weapon rolled is not a Fist, print a message
if weapons[weapon_roll - 1] != "Fist":
    print("    |    --- Thank goodness you didn't roll the Fist...")

# --- Collect Loot ---
print("    ------------------------------------------------------------------")
print("    |    !!You find a loot bag!! You look inside to find 2 items:")
print("    |", end="    ")
input("Roll for first item (enter)")
# Collect Loot First time
loot_options, belt = functions.collect_loot(loot_options, belt)
print("    ------------------------------------------------------------------")
print("    |", end="    ")
input("Roll for second item (Press enter)")
# Collect Loot Second time
loot_options, belt = functions.collect_loot(loot_options, belt)
print("    |    You're super neat, so you organize your belt alphabetically:")
belt.sort()
print("    |    Your belt: ", belt)

# --- Use Loot ---
belt = functions.use_loot(belt, hero)

print("    ------------------------------------------------------------------")
print("    |", end="    ")
input("Analyze the roll (Press enter)")
# Compare Player vs Monster's strength
print(f"    |    --- You are matched in strength: {hero.combat_strength == monster.combat_strength}")
# Check the Player's overall strength and health
print(f"    |    --- You have a strong player: {(hero.combat_strength + hero.health_points) >= 15}")

# --- Roll for the Monster's Magic Power ---
print("    |", end="    ")
input("Roll for Monster's Magic Power (Press enter)")
ascii_image4 = """
            @%   @                      
     @     @                        
         &                          
  @      .                          
 @       @                    @     
          @                  @      
  @         @              @  @     
   @            ,@@@@@@@     @      
     @                     @        
        @               @           
             @@@@@@@                
"""
print(ascii_image4)
power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])
# Use the Monster's power
monster.use_power(power_roll)

# --- Trigger Random Events ---
trigger_random_event(hero)

# --- Inception Dream (Lab Week 06 - Question 6) ---
num_dream_lvls = -1  # Initialize the number of dream levels
while num_dream_lvls < 0 or num_dream_lvls > 3:
    try:
        print("    |", end="    ")
        input_val = input("How many dream levels do you want to go down? (Enter a number 0-3): ")
        if input_val.strip() == "":
            print("Number entered must be a whole number between 0-3 inclusive, try again")
            continue
        num_dream_lvls = int(input_val)
        if num_dream_lvls < 0 or num_dream_lvls > 3:
            print("Number entered must be a whole number between 0-3 inclusive, try again")
            continue
        if num_dream_lvls != 0:
            hero.health_points -= 1
            crazy_level = functions.inception_dream(num_dream_lvls)
            hero.combat_strength += crazy_level
            print(f"combat strength: {hero.combat_strength}")
            print(f"health points: {hero.health_points}")
        break
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 3.")
        continue

# --- Fight Sequence with Elemental Advantage and Weather Effects ---
print("    ------------------------------------------------------------------")
print("    |    You meet the monster. FIGHT!!")
print(f"    |    Hero's element: {hero.element}")
print(f"    |    Monster's element: {monster.element}")
current_weather = weather.get_weather()
weather.apply_weather_effects(hero, monster, current_weather)
while monster.health_points > 0 and hero.health_points > 0:
    element_advantage = functions.elemental_advantage()
    print("    ------------------------------------------------------------------")
    print("    |    Elemental Advantage Table (This Round):")
    for k, v in element_advantage.items():
        print(f"    |      {k} > {v}")
    print("    |", end="    ")
    input("Roll to see who strikes first (Press Enter)")
    attack_roll = random.choice(small_dice_options)
    if attack_roll % 2 != 0:
        print("    |", end="    ")
        input("You strike (Press enter)")
        hero.hero_attacks(monster, element_advantage)
        if monster.health_points == 0:
            num_stars = 3
        else:
            print("    |", end="    ")
            print("------------------------------------------------------------------")
            input("    |    The monster strikes (Press enter)!!!")
            monster.monster_attacks(hero, element_advantage)
            if hero.health_points == 0:
                num_stars = 1
            else:
                num_stars = 2
    else:
        print("    |", end="    ")
        input("The Monster strikes (Press enter)")
        monster.monster_attacks(hero, element_advantage)
        if hero.health_points == 0:
            num_stars = 1
        else:
            print("    |", end="    ")
            print("------------------------------------------------------------------")
            input("The hero strikes!! (Press enter)")
            hero.hero_attacks(monster, element_advantage)
            if monster.health_points == 0:
                num_stars = 3
            else:
                num_stars = 2

# --- Determine Winner and Save Outcome ---
if monster.health_points <= 0:
    winner = "Hero"
else:
    winner = "Monster"

# Final Score Display and Hero Name Input
tries = 0
input_invalid = True
while input_invalid and tries < 5:
    print("    |", end="    ")
    hero_name = input("Enter your Hero's name (in two words): ")
    name_parts = hero_name.split()
    if len(name_parts) != 2:
        print("    |    Please enter a name with two parts (separated by a space)")
        tries += 1
    else:
        if not name_parts[0].isalpha() or not name_parts[1].isalpha():
            print("    |    Please enter an alphabetical name")
            tries += 1
        else:
            short_name = name_parts[0][:2] + name_parts[1][:1]
            print(f"    |    I'm going to call you {short_name} for short")
            input_invalid = False

if not input_invalid:
    stars_display = "*" * num_stars
    print(f"    |    Hero {short_name} gets <{stars_display}> stars")
    functions.save_game(winner, hero_name=short_name, num_stars=num_stars)

# --- Local Branch Addition: Update Monster Kills ---
monster_kills += 1
with open("monster_kills.txt", "w") as file:
    file.write(str(monster_kills))
