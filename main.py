import json

def play_game():
    with open('game_data.json', 'r') as f:
        game_data = json.load(f)

    print("Welcome to the Adventure Game!\n")
    current_location = game_data['start']
    visited_locations = []

    while True:
        location = game_data['locations'][current_location]
        print(location['description'])

        if location['is_ending_location']:
            print("\nCongratulations, you have reached the end of the game!")
            break

        options = location['options']
        for i, option in enumerate(options):
            print(f"{i + 1}. {option['description']}")

        choice = int(input("\nEnter your choice: ")) - 1
        next_location = options[choice]['destination']
        if next_location in visited_locations:
            print("\nYou have already been to this location. Please choose another option.\n")
        else:
            visited_locations.append(next_location)
            current_location = next_location

if __name__ == '__main__':
    play_game()
