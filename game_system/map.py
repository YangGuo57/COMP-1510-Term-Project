"""
This module contains functions that are used to create and print the game map.
"""

from game_system import coordinates


def make_board(row: int, column: int, locations: dict, keys: str) -> dict:
    """
    Make a game board with the given row, column, locations and keys.

    :param row: an integer
    :param column: an integer
    :param locations: a dictionary
    :param keys: a string
    :precondition: row must be a positive integer
    :precondition: colum must be a positive integer
    :precondition: locations must be a dictionary representing the locations of the game board
    :precondition: keys must be a string representing the key of the locations dictionary
    :postcondition: create a game board with the given row, column, locations and keys
    :return: a dictionary representing the game board

    >>> ro = 3
    >>> col = 3
    >>> location = {'top': {(0, 0): ' ', (0, 1): ' ', (0, 2): ' '},
    ... 'middle': {(1, 0): ' ', (1, 1): ' ', (1, 2): ' '},
    ... 'bottom': {(2, 0): ' ', (2, 1): ' ', (2, 2): ' '}}
    >>> key = 'top'
    >>> make_board(ro, col, location, key)
    {(0, 0): ' ', (0, 1): ' ', (0, 2): ' ', (1, 0): ' ', (1, 1): ' ', (1, 2): ' ', (2, 0): ' ', (2, 1): ' ', \
(2, 2): ' '}
    """
    return {(x, y): locations[keys][(x, y)] if (x, y) in locations[keys] else ' ' for x in range(row) for y
            in range(column)}


def add_element_to_map(game_board: dict) -> dict:
    """
    Add elements to the map with the given dictionary

    :param game_board: a dictionary
    :precondition: game_board must be a dictionary with tuples as keys and strings as values
    :postcondition: add elements to the map
    :return: a dictionary with tuples as keys and strings as values

    >>> board = {(0, 0): 'home'}
    >>> add_element_to_map(board)
    {(0, 0): '✦', (-1, -1): '-', (-1, 0): '-', (-1, 1): '-', (0, -1): '|', (0, 1): '-', (1, -1): '-', (1, 0): '-', \
(1, 1): '-'}
    """
    element_mappings = {
        'home': ('✦', '|', '-'),
        'hospital': ('H', '|', '-'),
        'school': ('S', '|', '-'),
        'park': ('P', '|', '-'),
        'work': ('W', '|', '-'),
        '1510': ('P', '|', '-'),
        '1113': ('M', '|', '-'),
        '1712': ('S', '|', '-'),
        '1537': ('W', '|', '-')
    }
    updates = {}

    for (x, y), location in game_board.items():
        if location in element_mappings:
            symbol, door, wall = element_mappings[location]
            game_board[(x, y)] = symbol

            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if (dx, dy) != (0, 0):
                        updates[(x + dx, y + dy)] = wall
            updates[(x, y - 1)] = door

    game_board.update(updates)

    return game_board


def initialize_map(board_rows: int, board_columns: int, location_key: str) -> dict:
    """
    Initialize the game map with the given board rows, board columns and location key.

    :param board_rows: an integer
    :param board_columns: an integer
    :param location_key: a string
    :precondition: board_rows must be a positive integer
    :precondition: board_columns must be a positive integer
    :precondition: location_key must be a string representing the key of the locations dictionary
    :postcondition: initialize the game map with the given board rows, board columns and location key
    :return: a dictionary representing the game map
    """
    locations = coordinates()
    game_board = make_board(board_rows, board_columns, locations, location_key)
    game_map = add_element_to_map(game_board)
    game_map['rows'] = board_rows
    game_map['columns'] = board_columns
    game_map['board'] = game_board

    return game_map


def print_game_map(game_map: dict, character: dict) -> None:
    """
    Print the game map with the given game map and character.

    :param game_map: a dictionary
    :param character: a dictionary
    :precondition: game_map must be a dictionary representing the game map with tuples as keys and strings as values
    :precondition: character must be a dictionary representing the character
    :postcondition: print the game map with the given game map and character
    """
    rows = game_map['rows']
    columns = game_map['columns']
    board = game_map['board']
    player_position = (character['X'], character['Y'])

    for row_index in range(rows):
        for col_index in range(columns):
            if (row_index, col_index) == player_position:
                print('\033[91m*\033[0m', end=' ')
            elif row_index == 0 or row_index == rows - 1:
                print('-', end=' ')
            elif col_index == 0 or col_index == columns - 1:
                print('|', end=' ')
            else:
                print(board[(row_index, col_index)], end=' ')
        print()
