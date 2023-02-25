import json

# Load the game data from the JSON file
with open('game_data.json', 'r') as f:
    game_data = json.load(f)

def print_descriptions():
    print("Room descriptions:")
    for room, data in game_data['locations'].items():
        print(f"\nRoom Name - {room}:")
        print(f"This is the description - {data['description']}")

# Print all the room descriptions
print_descriptions()
