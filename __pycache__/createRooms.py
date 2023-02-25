import json

# Define a dictionary
game_data = {
    "start": "room1",
    "locations": {
        "room1": {
            "description": "You are in a room with a door to the north and a door to the east.",
            "options": [
                {
                    "description": "Go north.",
                    "destination": "room2"
                },
                {
                    "description": "Go east.",
                    "destination": "room3"
                }
            ],
            "is_ending_location": False
        },
        "room2": {
            "description": "You are in a room with a door to the south.",
            "options": [
                {
                    "description": "Go south.",
                    "destination": "room1"
                }
            ],
            "is_ending_location": False
        },
        "room3": {
            "description": "You are in a room with a door to the west.",
            "options": [
                {
                    "description": "Go west.",
                    "destination": "room1"
                }
            ],
            "is_ending_location": True
        }
    }
}

# Export the dictionary to a JSON file
with open('game_data.json', 'w') as f: # 'w' means write
    json.dump(game_data, f, indent=4) # indent=4 makes the JSON file more readable
