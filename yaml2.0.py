import yaml
import random


# Load game data from YAML file
with open("yamlGameData.yaml") as file:
    game_data = yaml.load(file, Loader=yaml.FullLoader)

# Extract data from game_data
rooms = game_data["rooms"]
player = game_data["player"]
enemies = game_data["enemies"]

# Initialize player's location and health
player_location = player["start_location"]
player_health = player["health"]


def call_room():
    global player_location
    global player_health

    # Find the current room
    current_room = next(room for room in rooms if room["name"] == player_location)

    # Print the room description
    print(current_room["description"])

    # Check if there is an enemy in the room
    if current_room["enemy"]:
        engage_in_fight(current_room)

    # Check if there is an object in the room
    if "object" in current_room:
        take_object(current_room["object"])

    # Get the available exits from the current room
    exits = current_room["exits"]

    # Choose the player's next move
    choose_next_move(exits)


def engage_in_fight(room):
    global player_health

    # Get the enemy data
    enemy_data = next(enemy for enemy in enemies if enemy["name"] == room["enemy"])

    # Print the enemy's attack phrase
    print(random.choice(enemy_data["attack_phrases"]))

    # Reduce player's health
    player_health -= enemy_data["hit_points"]

    # Print player's remaining health
    print(f"Your health is now {player_health}.")

    # Check if the player is dead
    if player_health <= 0:
        game_over()

    # Print the enemy's defense phrase
    print(random.choice(enemy_data["defend_phrases"]))


def choose_next_move(exits):
    while True:
        # Print available exits
        print("Available exits:")
        for exit in exits:
            print(f"{exit['direction']}: {exit['destination']}")

        # Get player's input
        next_move = input("What is your next move? ")

        # Check if the input is valid
        if next_move in [exit["direction"] for exit in exits]:
            # Move the player to the next room
            global player_location
            player_location = next(exit["destination"] for exit in exits if exit["direction"] == next_move)
            call_room()
            break
        else:
            print("Invalid input. Please try again.")


def take_object(object_name):
    print(f"You have picked up the {object_name}.")
    # TODO: Implement functionality to add object to player's inventory


def game_over():
    print("Game over.")


# Start the game
call_room()
