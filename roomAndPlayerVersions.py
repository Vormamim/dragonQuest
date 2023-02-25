import json
import random

# Load the locations and player data from the JSON file
with open("game_data_v2.json", "r") as file:
    game_data = json.load(file)

player = game_data["player"]
locations = game_data["locations"]

# Print a list of all the locations in the game
print("Locations:")
for location in locations:
    print(f"- {location}")

# Start the game in the forest
current_location = "forest"

# Play the game until the player quits
while True:
    # Get the player's current location
    location = locations[current_location]
    print(f"\nYou are in the {current_location}: {location['description']}")

    # List the exits from the current location
    print("Exits:")
    for direction, exit_location in location["exits"].items():
        print(f"- {direction}: {exit_location}")

    # Check if there's treasure in the current location
    if "treasure" in location:
        print(f"You found a {location['treasure']}!")
        player["inventory"].append(location["treasure"])
        location.pop("treasure")

    # Get the player's next move
    move = input("Where would you like to go? (q to quit) ")

    # Check if the player wants to quit the game
    if move == "q":
        break

    # Check if the move is valid
    if move in location["exits"]:
        current_location = location["exits"][move]
    else:
        print("You can't go that way.")
