

def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, start=1):
        print(f"{i}. {dwarf}")


dwarf_names = ["Doc", "Dopey", "Bashful", "Grumpy"]
roll_call_dwarves(dwarf_names)



def summon_captain_planet(planet_calls):
    return [call.capitalize() + '!' for call in planet_calls]

planet_calls = ["earth", "mercury", "venus", "mars", "jupiter"]
result = summon_captain_planet(planet_calls)
print(result)


def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

short_words = ["one", "two", "go"]
print(long_planeteer_calls(short_words))

assorted_words = ["two", "go", "one", "three"]
print(long_planeteer_calls(assorted_words)) 



def find_the_cheese(ingredients):
    cheeses = ["cheddar", "french", "american"]
    for ingredient in ingredients:
        if ingredient in cheeses:
            return ingredient
    return None


snacks = ["crackers", "mushroom", "chips"]
print(find_the_cheese(snacks)) 


soup = ["tomato soup", "cold", "hot", "mushroom"]
print(find_the_cheese(soup)) 


ingredients = ["garlic", "onions", "bread"]
print(find_the_cheese(ingredients)) 

