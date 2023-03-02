import yaml
import random
import time

# Load the game data from the YAML file
with open("yamlGameData.yaml", "r") as file:
    game_data = yaml.safe_load(file)

# Keep track of the player's gold coins
gold_coins = 0

# Keep track of the player's name
player_name = "John"

# Keep track of the player's hit points
player_hit_points = game_data["player"]["health"]

# Keep track of the player's location
player_location = game_data["player"]["start_location"]

# set the battle_over flag to False
battle_over = False

# Start the game loop
while not battle_over:
    # Get the current location information
    # Iterate through the list of rooms and find the dictionary that matches the current room name
    for room in game_data["rooms"]:
        if room["name"] == player_location:
            location = room
            break
    print(f"You are at the {location['name']}")
    print(location['description'])
    print(f"You have {player_hit_points} hit points.")

    # Check if there is an enemy at the current location
    if "enemy" in location:
        enemy = location["enemy"]
        print(f"A {enemy} appeared!")

    # If there is an enemy, start a battle
    for e in game_data["enemies"]: # loop through the list of enemies
        if e["name"] == enemy: #
            enemy_hit_points = e["hit_points"] # assign the enemy to the enemy variable
            break # break out of the loop        
        print(f"It has {enemy_hit_points} hit points.")
        time.sleep(1)

        while enemy_hit_points > 0:
            # Player attacks
            damage = random.randint(1, 10)
            enemy_hit_points -= damage
            attack_phrase = random.choice(game_data["phrases"]["attack_phrases"])
            print(f"\n{attack_phrase} You hit the {enemy} for {damage} damage.")
            time.sleep(2)

            # Check if the enemy is defeated
            if enemy_hit_points <= 0:
                print(f"You defeated the {enemy}!")
                battle_over = True
                break

            # Enemy attacks
            damage = random.randint(1, 10)
            player_hit_points -= damage
            defend_phrase = random.choice(game_data["phrases"]["defend_phrases"])
            print(f"{defend_phrase}. {enemy} hit you for {damage} damage.")
            time.sleep(2)

            # Check if the player is defeated
            if player_hit_points <= 0:
                print("You have been defeated!")
                time.sleep(3)
                battle_over = True
                break

    # Update the game data to reflect the current situation
    game_data["rooms"][player_location]["enemy"] = None

    # Get the available exits from the current location
    exits = location["exits"]

    # Print the available exits
    print("Exits:")
    for direction, room in exits.items():
        print(f"{direction.capitalize()}: {game_data['rooms'][room]['name']}")

    # Ask the player for their next move
    while True:
        next_move = input("What do you want to do? ").lower()
        if next_move in exits:
            player_location = game_data["rooms"].index(game_data["rooms"][player_location]["exits"][next_move])
            break
        else:
            print("You can't do that.")

    # Check if the player has reached the end of the game
   


    # Check if the player has reached the end of the game
    if player_location == game_data["player"]["end_location"]:
        print("You have reached the end of the game!")
        break

    # Wait for user input before proceeding to the next iteration of the loop
    input("Press Enter to continue...")

print("Game Over")
