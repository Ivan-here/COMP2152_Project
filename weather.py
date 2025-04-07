import random
def get_weather():

    weather_conditions = ["Sunny", "Rainy", "Foggy", "Windy", "Snowy"]
    return random.choice(weather_conditions)

def apply_weather_effects(hero, monster, weather):

    if weather == "Rainy":

        hero.combat_strength = max(1, hero.combat_strength - 1)
        print("It's rainy! The hero's combat strength is slightly reduced.")
    elif weather == "Foggy":
        monster.combat_strength = max(1, monster.combat_strength - 1)
        print("It's foggy! The monster's combat strength is slightly reduced.")
    elif weather == "Windy":
        print("It's windy! The battle might be unpredictable.")
    elif weather == "Snowy":
        if hero.health_points == 1:
            monster.health_points = max(0, monster.health_points - 1)
            print("It's snowy! Both combatants lose a bit of health due to the cold.")
        else:
            hero.health_points = max(0, hero.health_points - 1)
            monster.health_points = max(0, monster.health_points - 1)
            print("It's snowy! Both combatants lose a bit of health due to the cold.")
    else:
        print("The weather is perfect for battle!")