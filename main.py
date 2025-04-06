# Import the random library to use for the dice later
import random
import os
import platform

from functions import trigger_random_event

# Print OS and Python version information
print(f"Operating System: {os.name}")
print(f"Python Version: {platform.python_version()}")

# Import our custom classes
from hero import Hero
from monster import Monster
import functions_lab06_solution as functions

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the number of stars to award the player
num_stars = 0

# Create a hero instance
hero = Hero()

# Create a monster instance
monster = Monster()



# Roll for weapon
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

# Limit the combat strength to 6
hero.combat_strength = min(6, (hero.combat_strength + weapon_roll))
print(f"    |    The hero's weapon is {weapons[weapon_roll - 1]}")

# Lab 06 - Question 5b
functions.adjust_combat_strength(hero.combat_strength, monster.combat_strength)

# Weapon Roll Analysis
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

# If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
if weapons[weapon_roll - 1] != "Fist":
    print("    |    --- Thank goodness you didn't roll the Fist...")

# Collect Loot
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

# Use Loot
belt, hero.health_points = functions.use_loot(belt, hero.health_points)

print("    ------------------------------------------------------------------")
print("    |", end="    ")
input("Analyze the roll (Press enter)")
# Compare Player vs Monster's strength
print(f"    |    --- You are matched in strength: {hero.combat_strength == monster.combat_strength}")

# Check the Player's overall strength and health
print(f"    |    --- You have a strong player: {(hero.combat_strength + hero.health_points) >= 15}")

# Roll for the monster's power
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

# Use the monster's power
monster.use_power(power_roll)

#FEATURE random events
trigger_random_event(hero)

# Lab Week 06 - Question 6
num_dream_lvls = -1  # Initialize the number of dream levels
while (num_dream_lvls < 0 or num_dream_lvls > 3):
    # Call Recursive function
    print("    |", end="    ")
    try:
        num_dream_lvls = input("How many dream levels do you want to go down? (Enter a number 0-3)")
        # If the value entered was not an integer, set the number of dream levels to -1 and loop again 
        if ((num_dream_lvls == "")):
            num_dream_lvls = -1
            print("Number entered must be a whole number between 0-3 inclusive, try again")
        else:
            num_dream_lvls = int(num_dream_lvls)

            if ((num_dream_lvls < 0) or (num_dream_lvls > 3)):
                num_dream_lvls = -1
                print("Number entered must be a whole number between 0-3 inclusive, try again")
            elif (not num_dream_lvls == 0):
                hero.health_points -= 1
                crazy_level = functions.inception_dream(num_dream_lvls)
                hero.combat_strength += crazy_level
                print(f"combat strength: {hero.combat_strength}")
                print(f"health points: {hero.health_points}")
    except ValueError:
        num_dream_lvls = -1
        print("Invalid input. Please enter a number between 0-3.")
    
    print("num_dream_lvls: ", num_dream_lvls)

# Fight Sequence
# Loop while the monster and the player are alive. Call fight sequence functions
print("    ------------------------------------------------------------------")
print("    |    You meet the monster. FIGHT!!")
while monster.health_points > 0 and hero.health_points > 0:
    # Fight Sequence
    print("    |", end="    ")

    # Lab 5: Question 5:
    input("Roll to see who strikes first (Press Enter)")
    attack_roll = random.choice(small_dice_options)
    if not (attack_roll % 2 == 0):
        print("    |", end="    ")
        input("You strike (Press enter)")
        hero.hero_attacks(monster)
        if monster.health_points == 0:
            num_stars = 3
        else:
            print("    |", end="    ")
            print("------------------------------------------------------------------")
            input("    |    The monster strikes (Press enter)!!!")
            monster.monster_attacks(hero)
            if hero.health_points == 0:
                num_stars = 1
            else:
                num_stars = 2
    else:
        print("    |", end="    ")
        input("The Monster strikes (Press enter)")
        monster.monster_attacks(hero)
        if hero.health_points == 0:
            num_stars = 1
        else:
            print("    |", end="    ")
            print("------------------------------------------------------------------")
            input("The hero strikes!! (Press enter)")
            hero.hero_attacks(monster)
            if monster.health_points == 0:
                num_stars = 3
            else:
                num_stars = 2

if(monster.health_points <= 0):
    winner = "Hero"
else:
    winner = "Monster"

# Final Score Display
tries = 0
input_invalid = True
while input_invalid and tries in range(5):
    print("    |", end="    ")

    hero_name = input("Enter your Hero's name (in two words)")
    name = hero_name.split()
    if len(name) != 2:
        print("    |    Please enter a name with two parts (separated by a space)")
        tries += 1
    else:
        if not name[0].isalpha() or not name[1].isalpha():
            print("    |    Please enter an alphabetical name")
            tries += 1
        else:
            short_name = name[0][0:2:1] + name[1][0:1:1]
            print(f"    |    I'm going to call you {short_name} for short")
            input_invalid = False

if not input_invalid:
    stars_display = "*" * num_stars
    print(f"    |    Hero {short_name} gets <{stars_display}> stars")

    functions.save_game(winner, hero_name=short_name, num_stars=num_stars)




