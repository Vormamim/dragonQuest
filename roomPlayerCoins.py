import json
import random

# load the game_data.json and treasures.json files
with open("game_data_v2.json", "r") as file:
    game_data = json.load(file)

with open("treasures.json", "r") as file:
    treasures = json.load(file)

# initialize the player's starting location and gold coins
location = "village"
gold_coins = 0

# loop until the player reaches the end location
while location != "end":
    # print the description of the current location
    print(game_data["locations"][location]["description"])

    # check if the current location has a treasure
    for treasure in treasures["treasures"]:
        if treasure["location"] == location:
            gold_coins += treasure["value"]
            print(f"You found a {treasure['name']} worth {treasure['value']} gold coins!")
            break

    # show the player's gold coins
    print(f"You have {gold_coins} gold coins.") # f-string

    # get the player's next move
    available_exits = list(game_data["locations"][location]["exits"].keys())
    print("Available exits: " + ", ".join(available_exits))
    move = input("Where would you like to go? ").lower()

    if move == "quit" or move == "q":
        break

    # update the player's location based on their move
    if move in available_exits:
        location = game_data["locations"][location]["exits"][move]
    else:
        print("You can't go that way.")
