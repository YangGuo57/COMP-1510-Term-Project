from time import sleep
from helper_functions import character, greeting
import json


def new_or_load():
    greeting_msg = greeting()
    sleep(0.5)
    print('Welcome to Survive CST!')
    print('1. Start New Game')
    print('2. Load Previous Game')
    while True:
        load_choice = input('Please choose an option (1 or 2): ')
        if load_choice == '1':
            print('Starting a fresh new journey in Survive CST!')
            player, week = start_new_game(greeting_msg)
            is_weekend = False
        elif load_choice == '2':
            player, week, is_weekend = load_game()
            if player is None:
                print('No previous saved_game found. Starting a new adventure!')
                is_weekend = False
                player, week = start_new_game(greeting_msg)
        else:
            print("Invalid option. Please enter '1' for a new game or '2' to load a previous game.")
            continue
        return player, week, is_weekend


def start_new_game(greeting_msg):
    sleep(0.5)
    print(greeting_msg[1])
    answer = character.ask_questionnaire('new')
    player = character.create_character(answer)
    print(greeting_msg[2])
    print(greeting_msg[3])
    week = 1
    return player, week


def load_game(filename='./saved_game/saved_game.json'):
    try:
        with open(filename, 'r') as file:
            game_data = json.load(file)
        return game_data['character'], game_data['week'], game_data.get('is_weekend', False)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error loading the game: {e}')
        return None, None, False


def save_game(player, week, is_weekend, filename='./saved_game/saved_game.json'):
    game_data = {
        'character': player,
        'week': week,
        'is_weekend': is_weekend,
    }
    with open(filename, 'w') as file:
        json.dump(game_data, file, indent=4)
