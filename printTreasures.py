import json

# Load the treasure data from the JSON file
with open('treasures.json', 'r') as f: # 
    treasures = json.load(f)

def print_treasures():
    print("Treasures:")
    for treasure in treasures['treasures']: #   'treasures' is the key in the dictionary 
        print(f"\nName: {treasure['name']}") # 'name' is the key in the dictionary
        print(f"Location: {treasure['location']}") #  'location' is the key in the dictionary
        print(f"Value: {treasure['value']}")    # 'value' is the key in the dictionary

# Print information about the treasures
print_treasures()
