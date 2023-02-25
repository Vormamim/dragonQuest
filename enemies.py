import json
import random

# Load the enemies from the JSON file
with open("enemies_data.json", "r") as file:
    enemies = json.load(file)

# Select a random enemy
enemy = random.choice(enemies)

# Print the enemy information
print(f"An enemy {enemy['name']} appeared with {enemy['hit_points']} hit points!")
