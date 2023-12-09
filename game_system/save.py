"""
This module contains the functions that save and load the game.
"""

from time import sleep
from game_system import character, greeting, ascii
import json


def new_or_load() -> tuple:
    """
    Gets user input on whether to start a new game or load a previous game.

    :return: a tuple containing the player, week, and is_weekend
    """
    sleep(0.5)
    ascii.print_ascii('run game')
    print('1. Start New Game')
    print('2. Load Previous Game')
    while True:
        load_choice = input('Please choose an option (1 or 2): ')
        if load_choice == '1':
            print('Starting a fresh new journey in Survive CST!')
            player, week = start_new_game()
            is_weekend = False
        elif load_choice == '2':
            player, week, is_weekend = load_game()
            if player is None:
                print('No previous saved_game found. Starting a new adventure!')
                is_weekend = False
                player, week = start_new_game()
        else:
            print("Invalid option. Please enter '1' for a new game or '2' to load a previous game.")
            continue
        return player, week, is_weekend


def start_new_game() -> tuple:
    """
    Starts a new game by initializing a new character.

    :return: a tuple containing the player and week
    """
    sleep(0.5)
    greeting_msg = greeting()
    print(greeting_msg[1])
    answer = character.ask_questionnaire('new')
    player = character.create_character(answer)
    print(greeting_msg[2])
    print(greeting_msg[3])
    week = 1
    return player, week


def load_game(filename: str = './saved_game.json') -> tuple:
    """
    Loads a previous game from a JSON file.
    
    :param filename: a string representing the filename of the JSON file
    :precondition: filename must be a relative path to a JSON file
    :postcondition: correctly loads the game from the JSON file
    :return: a tuple containing the player, week, and is_weekend
    """
    try:
        with open(filename, 'r') as file:
            game_data = json.load(file)
        return game_data['character'], game_data['week'], game_data.get('is_weekend', False)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error loading the game: {e}')
        return None, None, False


def save_game(player: dict, week: int, is_weekend: bool, filename: str = './saved_game.json') -> None:
    """
    Saves the current game to a JSON file.
    
    :param player: a dictionary representing the player
    :param week: an integer representing the current week
    :param is_weekend: a boolean representing whether it is the weekend
    :param filename: a string representing the relative path of the JSON file
    :precondition: player must be a dictionary generated within this game
    :precondition: week must be an integer generated in this game
    :precondition: filename must be a relative path to a JSON file
    :postcondition: correctly saves the game to the JSON file
    """
    game_data = {
        'character': player,
        'week': week,
        'is_weekend': is_weekend,
    }
    with open(filename, 'w') as file:
        json.dump(game_data, file, indent=4)
