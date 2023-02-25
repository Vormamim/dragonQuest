import random
# This is a list of all the possible treasures that can be found in the game
treasures = [
    "a silver dagger with an ornate hilt",
    "a vial of vampire blood",
    "a rare book of ancient spells",
    "a mystical amulet that grants invisibility",
    "a map to a hidden treasure trove",
    "a powerful crossbow with enchanted bolts",
    "a set of silver stakes",
    "a potion that grants temporary immortality",
    "a crystal ball with the power to see the future",
    "a cursed mirror that reveals the true nature of vampires"
]
# print(treasures) # ['a silver dagger with an ornate hilt', 'a vial of vampire blood', 'a rare book of ancient spells', 'a mystical amulet that grants invisibility', 'a map to a hidden treasure trove', 'a powerful crossbow with enchanted bolts', 'a set of silver stakes', 'a potion that grants temporary immortality', 'a crystal ball with the power to see the future', 'a cursed mirror that reveals the true nature of vampires']
def get_random_treasure():
    """Returns a random treasure from the treasures list"""
    return random.choice(treasures)

print("this is one treasure", get_random_treasure()) # this is one treasure a potion that grants temporary immortality

for i in range(5): # 5 is the number of times the loop will run
    print("This is another treasure:", get_random_treasure()) # This is another treasure: a potion that grants temporary immortality
