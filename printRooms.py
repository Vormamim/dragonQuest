import json

# Load the game data from the JSON file
with open('game_data.json', 'r') as f:
    game_data = json.load(f)

def print_rooms():
    print("Rooms in the game:")
    for room in game_data['locations'].keys():
        print(f"- {room}")

# Print a list of the rooms in the game
print_rooms()
