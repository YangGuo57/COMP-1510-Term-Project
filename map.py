import movement as mov
import menu as me
import event_trigger as e


def coordinates():
    """
    Stores location coordinates into a dictionary.

    :return:
    """
    locations = {
        "coordinates": {
            (2, 4): "home",
            (3, 10): "school",
            (6, 13): "hospital",
            (2, 16): "park",
            (7, 5): "work"
        },
        "door": {
            "home": [(2, 3), (2, 4)],
            "school": [(3, 9), (3, 11)],
            "hospital": [(6, 12), (6, 14)],
            "park": [(2, 15), (2, 17)],
            "work": [(7, 4), (7, 6)]
        },
        "school": {
            (2, 7): "1510",
            (10, 1): "1537",
            (7, 7): "1712",
            (4, 1): "1113",
        },
        "office_door": {
            "1510": [(2, 6)],
            "1537": [(10, 2)],
            "1712": [(7, 6)],
            "1113": [(4, 2)],
        }
    }
    return locations


def make_board(row, column, locations, keys):
    """
    Create game board with row and column.


    :param row:
    :param column:
    :param locations:
    :param keys:
    :return:

    >>> make_board(2, 2, {"key": {(0, 0): "home", (1, 1): "park"}}, "key")
    {(0, 0): 'home', (0, 1): ' ', (1, 0): ' ', (1, 1): 'park'}
    """
    game_board = {}
    for x in range(row):
        for y in range(column):
            if (x, y) in locations[keys]:
                game_board[(x, y)] = locations[keys][(x, y)]
            else:
                game_board[(x, y)] = " "

    return game_board


def add_element_to_map(game_board):
    """
    Add elements to a game board and update the board.

    :param game_board:
    :return:

    >>> board =  {(0, 0): 'home', (0, 1): ' ', (1, 0): ' ', (1, 1): 'park'}
    >>> result = add_element_to_map(board)
    >>> expected_result = {(0, 0): '=', (0, 1): '=', (1, 0): '|', (1, 1): '-', (-1, -1): '-',
    ... (-1, 0): '-', (-1, 1): '-', (0, -1): '|', (1, -1): '-', (0, 2): '=', (1, 2): '=',
    ... (2, 0): '=', (2, 1): '=', (2, 2): '='}
    >>> result == expected_result
    True
    """
    element_mappings = {
        "home": ('✦', '|', '-'),
        "hospital": ('H', '|', '+'),
        "school": ('S', '|', '-'),
        "park": ('P', '|', '='),
        "work": ('W', '|', '~'),
        "1510": ('P', '|', '='),
        "1113": ('M', '|', '='),
        "1712": ('S', '|', '='),
        "1537": ('W', '|', '=')
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


def print_map(game_board, row, column, character):
    """
    Print the game map.

    :param game_board:
    :param row:
    :param column:
    :param character:
    :return:
    """
    player_position = (character['X'], character['Y'])
    for row_index in range(row):
        for col_index in range(column):
            if (row_index, col_index) == player_position:
                print('*', end=' ')
            elif row_index == 0 or row_index == row - 1:
                print('-', end=' ')
            elif col_index == 0 or col_index == column - 1:
                print('|', end=' ')
            else:
                print(game_board[(row_index, col_index)], end=' ')
        print()


def trigger_map_event(locations, board_rows, board_columns, game_map, character, message):
    for door, location in locations.items():
        if e.is_at_location(character, location):
            e.trigger_event(board_rows, board_columns, game_map, character, door, message)


def map_action(character, board_rows, board_columns, location_key):
    locations = coordinates()
    game_board = make_board(board_rows, board_columns, locations, location_key)
    game_map = add_element_to_map(game_board)

    if location_key == "school":
        character['X'] = 1
        character['Y'] = 1

    while True:
        print_map(game_map, board_rows, board_columns, character)
        user_choice = mov.get_user_choice()

        if user_choice == "Back to Menu":
            if location_key == "school":
                character['X'] = 1
                character['Y'] = 1
                break
            else:
                me.main_menu(character)
                return

        is_valid_move = mov.validate_move(game_board, character, user_choice)
        if is_valid_move:
            mov.move_character(character, user_choice, board_rows, board_columns, game_map)
            mov.update_visited_location(character)
            message = e.trigger_description()
            door_locations = locations["door"] if location_key == "coordinates" else locations["office_door"]
            trigger_map_event(door_locations, board_rows, board_columns, game_map, character, message)
        else:
            print("Invalid move! Please choose another direction.")
