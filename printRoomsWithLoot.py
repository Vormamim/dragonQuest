import json
import random

# Load the game data from the JSON file
with open('game_data.json', 'r') as f:
    game_data = json.load(f)

# Load the treasure data from the JSON file
with open('treasures.json', 'r') as f:
    treasures = json.load(f)

def assign_treasures():
    # Create a list of room names
    rooms = list(game_data['locations'].keys())

    # Assign each treasure to a random room
    for treasure in treasures['treasures']: # loop through the list of treasures
        room = random.choice(rooms) #select a random room from the list of rooms
        treasure['location'] = room # assign the room to the treasure

    # Update the game data to include the treasure information
    for room, data in game_data['locations'].items(): # loop through the dictionary of rooms
        data['treasure'] = [t for t in treasures['treasures'] if t['location'] == room] # assign the treasure to the room

# Assign treasures to rooms
assign_treasures() # call the function

def print_descriptions_with_treasures():
    print("Room descriptions:")
    for room, data in game_data['locations'].items():
        print(f"\n{room}:")
        print(f"{data['description']}")
        if data['treasure']:
            print("\nTreasures:")
            for treasure in data['treasure']:
                print(f"- {treasure['name']}")

# Print all the room descriptions with assigned treasures
print_descriptions_with_treasures() # call the function
