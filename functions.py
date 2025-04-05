import random

def use_loot(belt, hero):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)

    if first_item in good_loot_options:
        hero.health_points = min(20, (hero.health_points + 2))
        print(f"    |    You used {first_item} to up your health to {hero.health_points}")
    elif first_item in bad_loot_options:
        hero.health_points = max(0, (hero.health_points - 2))
        print(f"    |    You used {first_item} to hurt your health to {hero.health_points}")
    else:
        print(f"    |    You used {first_item} but it's not helpful")

    return belt, hero.health_points


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


def hero_attacks(hero, monster):
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
    print(f"    |    Hero's weapon ({hero.combat_strength}) ---> Monster ({monster.health_points})")
    if hero.combat_strength >= monster.health_points:
        monster.health_points = 0
        print("    |    You have killed the monster")
    else:
        monster.health_points -= hero.combat_strength
        print(f"    |    You have reduced the monster's health to: {monster.health_points}")

    return 0


def monster_attacks(monster, hero):
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
    print(f"    |    Monster's Claw ({monster.combat_strength}) ---> Hero ({hero.health_points})")
    if monster.combat_strength >= hero.health_points:
        hero.health_points = 0
        print("    |    Hero is dead")
    else:
        hero.health_points -= monster.combat_strength
        print(f"    |    The monster has reduced Hero's health to: {hero.health_points}")
    return 0


def inception_dream(num_dream_lvls):
    try:
        num_dream_lvls = int(num_dream_lvls)
        if num_dream_lvls < 0 or num_dream_lvls > 3:
            raise ValueError("Number of dream levels must be between 0 and 3.")

        if num_dream_lvls == 1:
            print("    |    You are in the deepest dream level now")
            print("    |", end="    ")
            input("Start to go back to real life? (Press Enter)")
            print("    |    You start to regress back through your dreams to real life.")
            return 2
        else:
            return 1 + int(inception_dream(num_dream_lvls - 1))
    except ValueError as e:
        print(f"Invalid input: {e}")
        return 0


def save_game(winner, hero_name="", num_stars=0):
    monsters_killed = 0
    game_history = []
    try:
        #Tracking monsters killed here
        with open("save.txt", "r") as file:
            lines = file.readlines()
            if lines and "Total monsters killed:" in lines[0]:
                monsters_killed = int(lines[0].split(":")[-1].strip())
                game_history = lines[1:]
            else:
                game_history = lines
    except FileNotFoundError:
        monsters_killed = 0

    if winner == "Hero":
        monsters_killed += 1

    with open("save.txt", "w") as file:
        file.write(f"Total monsters killed: {monsters_killed}\n")
        file.writelines(game_history)
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously\n")
        file.flush()


def load_game():
    try:
        with open("save.txt", "r") as file:
            print("    |    Loading from saved file ...")
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                print(last_line)
                #Loading monsters killed here
                for line in reversed(lines):
                    if "Total monsters killed" in line:
                        total_monsters_killed = int(line.split(":")[-1].strip())
                        print(f"Total monsters killed: {total_monsters_killed}")
                        break

                return last_line
    except FileNotFoundError:
        print("No previous game found. Starting fresh.")
        return None


def adjust_combat_strength(hero, monster):
    last_game = load_game()
    if last_game:
        if "Hero" in last_game and "gained" in last_game:
            num_stars = int(last_game.split()[-2])
            if num_stars > 3:
                print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                monster.combat_strength += 1
        elif "Monster has killed the hero" in last_game:
            hero.combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time")
        else:
            print(
                "    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")

#Elemental Brawl
def elemental_advantage():
    elements = ["Fire", "Water", "Earth", "Air"]
    #copying 2, shuffling both of them for a full chaos
    first = elements.copy()
    second = elements.copy()
    while True:
        random.shuffle(first)
        random.shuffle(second)
        #No elements are assigned to itself
        if all(a != b for a, b in zip(first, second)):
            break
    return dict(zip(first, second))