import yaml
import random
import time

# Load the YAML data from a file
with open('game_file.yaml', 'r') as f:
    data = yaml.safe_load(f)
    game = data["game"]
    rooms = data["rooms"]
    enemies = data["enemies"]

# Print the game title and description
title = data['game']['title']
desc = data['game']['description']
print(f"{title}\n{desc}\n")

# Set the starting room to the first room in the YAML data
current_room = data['rooms'][0]

# Loop to allow the user to navigate the game world
while True:
    # Print the current room name and description
    print(f"{current_room['name']}\n{current_room['description']}")
    # Check if there are any enemies in the current room
    current_room = rooms[0]

    # Check if an enemy is present in the current room
    if "enemy" in current_room:
        enemy_name = current_room["enemy"]
        enemy = next((e for e in enemies if e["name"] == enemy_name), None)
        if enemy:
            # Print the enemy information
            print(f"An enemy {enemy['name']} appeared with {enemy['hit_points']} hit points!")



    # Check if there are any exits from the current room
    if 'exits' in current_room:
        # Print the available exits and prompt the user to choose one
        exits = list(current_room['exits'].keys())
        print("Exits: " + ", ".join(exits))
        chosen_exit = input("Choose an exit: ")

        # Check if the chosen exit is valid
        if chosen_exit in exits:
            # Set the current room to the room connected to the chosen exit
            current_room = data['rooms_by_name'][current_room['exits'][chosen_exit]]
        else:
            print("Invalid exit.")
    else:
        # If there are no exits, the game is over
        print("There are no exits from this room. Game over.")
        break

