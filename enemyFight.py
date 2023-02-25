import json
import random
import time

# Load the game data from the JSON file
with open("game_data_v2.json", "r") as file:
    game_data = json.load(file)

# Load the enemies from the JSON file
with open("enemies_data.json", "r") as file:
    enemies = json.load(file)

# Load the phrases from the JSON file
with open("phrases.json", "r") as file:
    phrases = json.load(file)

# Keep track of the player's gold coins
gold_coins = 0

# Keep track of the player's name
player_name = game_data["player"]["name"]


# Keep track of the player's hit points
player_hit_points = game_data["player"]["health"]

# Keep track of the player's location
player_location = game_data["player"]["location"]

# set the battle_over flag to False
battle_over = False

# Start the game loop
while not battle_over:
    # Get the current location information
    location = game_data["locations"][player_location]
    print(f"You are at the {location['description']}")
    print(f"if there's an enemy, you'll fight it. you have {player_hit_points} hit points.")
    
    # Check if there is an enemy at the current location
    enemy = False
    for e in enemies: # loop through the list of enemies
        if e["enemy_location"] == player_location: # check if the enemy is in the current location
            enemy = e # assign the enemy to the enemy variable
            break

    # If there is an enemy, start a battle
    if enemy:
        print(f"A {enemy['name']} appeared with {enemy['hit_points']} hit points!")
        print(f"You have {player_hit_points} hit points.")

        time.sleep(1)
        while enemy["hit_points"] > 0:
            # Player attacks
            damage = random.randint(1, 10)
            enemy["hit_points"] -= damage
            # Select a random phrase from the attack_phrases list
            attack_phrase = random.choice(phrases["attack_phrases"])

            # Use the attack phrase in the battle print statement
            print(f"\n{attack_phrase} You hit the {enemy['name']} for {damage} damage.")
            #print(f"You hit the {enemy['name']} for {damage} damage.")
            time.sleep(2)
            
            # Check if the enemy is defeated
            if enemy["hit_points"] <= 0:
                print(f"You defeated the {enemy['name']}!")
                battle_over = True
                break
            
            # Enemy attacks
            damage = random.randint(1, 10)
            player_hit_points -= damage
            #print(f"The {enemy['name']} hit you for {damage} damage.")
            # Select a random phrase from the attack_phrases list
            defend_phrase = random.choice(phrases["defend_phrases"])
            print(f"{defend_phrase}. {enemy['name']} hit the {enemy['name']} for {damage} damage.")

            time.sleep(2)
            
            # Check if the player is defeated
            if player_hit_points <= 0:
                print("You have been defeated!")
                time.sleep(3)
                battle_over = True
                break

    # Update the game data to reflect the current situation
    game_data["locations"][player_location]["enemy"] = enemy

    if battle_over:
        break

# Wait for user input before proceeding to the next iteration of the loop
    input("Press Enter to continue...")

print("Game Over")

