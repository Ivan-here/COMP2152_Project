
# Import the random library to use for the dice later
import random

# Will the line below print when you import function.py into main.py?
# print("Inside function.py")


def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print("    |    You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("    |    You used " + first_item + " but it's not helpful")
    return belt, health_points


def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt


# Hero's Attack Function
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  

  """
    print(ascii_image)
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        # Player was strong enough to kill monster in one blow
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        # Player only damaged the monster
        m_health_points -= combat_strength

        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points


# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
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
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        # Monster was strong enough to kill player in one blow
        health_points = 0
        print("    |    Player is dead")
    else:
        # Monster only damaged the player
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points

# FUNCTION: Random events on the map
def trigger_random_event(hero):
    events = [("treasure", +10), ("trap", -15), ("nothing", 0)]
    active_events = [event for event in events if event[0] != "nothing"]
    event = random.choice(events)
    print(f"Event: {event[0]}")

    if event[0] == "treasure":
        hero.health_points += 10
        print("You found a treasure! +10 HP")
    elif event[0] == "trap":
        damage = 4 if getattr(hero, 'has_armor', False) else 8
        print(f"It's a trap! {'But you have armor. ' if getattr(hero, 'has_armor', False) else ''}-{damage} HP")
        hero.health_points = max(1, hero.health_points - damage)
    else:
        print("Nothing happened.")

# Recursion
# You can choose to go crazy, but it will reduce your health points by 5
def inception_dream(num_dream_lvls):
    if not isinstance(num_dream_lvls, int) or num_dream_lvls < 1:
        print("    |    Invalid number of dream levels. Must be >= 1.")
        return 0

    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2
    else:
        return 1 + inception_dream(num_dream_lvls - 1)
# Lab 06 - Question 3 and 4
def save_game(winner, hero_name="", num_stars=0):
    with open("save.txt", "a") as file:
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously\n")

# Lab 06 - Question 5a
def load_game():
    try:
        with open("save.txt", "r") as file:
            print("    |    Loading from saved file ...")
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                print(last_line)
                return last_line
    except FileNotFoundError:
        print("No previous game found. Starting fresh.")
        return None

# Lab 06 - Question 5b
def adjust_combat_strength(combat_strength, m_combat_strength):
    # Lab Week 06 - Question 5 - Load the game
    last_game = load_game()
    if last_game:
        if "Hero" in last_game and "gained" in last_game:
            num_stars = int(last_game.split()[-2])
            if num_stars > 3:
                print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                m_combat_strength += 1
        elif "Monster has killed the hero" in last_game:
            combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time")
        else:
            print("    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")



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

