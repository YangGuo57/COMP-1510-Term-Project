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
            "main": {"home": (2, 3),
                     "school": (3, 9),
                     "hospital": (6, 12),
                     "park": (2, 15),
                     "work": (7, 4)},
            "school": {
                "1510": (2, 6),
                "1537": (10, 6),
                "1712": (7, 6),
                "1113": (4, 6),
            }

        },
        "school": {
            (2, 7): "1510",
            (10, 7): "1537",
            (7, 7): "1712",
            (4, 7): "1113",
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

    # >>> board =  {(0, 0): 'home', (0, 1): ' ', (1, 0): ' ', (1, 1): 'park'}
    # >>> result = add_element_to_map(board)
    # >>> expected_result = {(0, 0): '=', (0, 1): '=', (1, 0): '|', (1, 1): '-', (-1, -1): '-',
    # ... (-1, 0): '-', (-1, 1): '-', (0, -1): '|', (1, -1): '-', (0, 2): '=', (1, 2): '=',
    # ... (2, 0): '=', (2, 1): '=', (2, 2): '='}
    # >>> result == expected_result
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


def initialize_map(board_rows, board_columns, location_key):
    locations = coordinates()
    game_board = make_board(board_rows, board_columns, locations, location_key)
    game_map = add_element_to_map(game_board)
    game_map["rows"] = board_rows
    game_map["columns"] = board_columns
    game_map["board"] = game_board

    return game_map


def print_game_map(game_map, character):
    """
    Print the game map borders.
    """
    rows = game_map["rows"]
    columns = game_map["columns"]
    board = game_map["board"]
    player_position = (character['X'], character['Y'])

    for row_index in range(rows):
        for col_index in range(columns):
            if (row_index, col_index) == player_position:
                print('*', end=' ')
            elif row_index == 0 or row_index == rows - 1:
                print('-', end=' ')
            elif col_index == 0 or col_index == columns - 1:
                print('|', end=' ')
            else:
                print(board[(row_index, col_index)], end=' ')
        print()
