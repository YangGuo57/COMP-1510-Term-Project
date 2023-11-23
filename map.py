import movement as mov
import menu as me
import event_trigger as e


def coordinates():
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
    game_board = {}
    for x in range(row):
        for y in range(column):
            if (x, y) in locations[keys]:
                game_board[(x, y)] = locations[keys][(x, y)]
            else:
                game_board[(x, y)] = " "

    return game_board


def add_element_main_map(game_board):
    for (x, y), location in game_board.items():
        if location == "home":
            game_board[(x, y)] = '✦'
            update_surroundings(game_board, x, y, '|', '-', '✦')
        elif location == "hospital":
            game_board[(x, y)] = 'H'
            update_surroundings(game_board, x, y, '|', '+', 'H')
        elif location == "school":
            game_board[(x, y)] = 'S'
            update_surroundings(game_board, x, y, '|', '-', 'S')
        elif location == "park":
            game_board[(x, y)] = 'P'
            update_surroundings(game_board, x, y, '|', '=', 'P')
        elif location == "work":
            game_board[(x, y)] = 'W'
            update_surroundings(game_board, x, y, '|', '~', 'W')

    return game_board


def add_element_school_map(game_board):
    for (x, y), location in game_board.items():
        if location == "1510":
            game_board[(x, y)] = 'P'
            update_surroundings(game_board, x, y, '|', '=', 'P')
        elif location == "1113":
            game_board[(x, y)] = 'M'
            update_surroundings(game_board, x, y, '|', '=', "M")
        elif location == "1712":
            game_board[(x, y)] = 'S'
            update_surroundings(game_board, x, y, '|', '=', "S")
        elif location == "1537":
            game_board[(x, y)] = 'W'
            update_surroundings(game_board, x, y, '|', '=', 'W')

    return game_board


def update_surroundings(game_board, x, y, door, wall, location_symbol):
    for row_offset in range(x - 1, x + 2):
        for col_offset in range(y - 1, y + 2):
            if (row_offset, col_offset) in game_board and game_board[(row_offset, col_offset)] != location_symbol:
                game_board[(row_offset, col_offset)] = door

    for col_offset in range(y - 1, y + 2):
        for row_offset in [x - 1, x + 1]:
            if (row_offset, col_offset) in game_board and game_board[(row_offset, col_offset)] != location_symbol:
                game_board[(row_offset, col_offset)] = wall


def print_map(game_board, row, column, character):
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
    game_map = None
    if location_key == "coordinates":
        game_map = add_element_main_map(game_board)
    elif location_key == "school":
        game_map = add_element_school_map(game_board)
        character['X'] = 1
        character['Y'] = 1

    while True:
        print_map(game_map, board_rows, board_columns, character)
        direction = mov.get_user_choice()

        if direction == "Back to Menu":
            if location_key == "school":
                character['X'] = 1
                character['Y'] = 1
                break
            else:
                me.main_menu(character)
                return
        valid_move = mov.validate_move(game_board, character, direction)
        if valid_move:
            mov.move_character(character, direction, board_rows, board_columns, game_map)
            mov.update_visited_location(character)
            message = e.trigger_description()
            if location_key == "coordinates":
                trigger_map_event(locations["door"], board_rows, board_columns, game_map, character, message)
            elif location_key == "school":
                trigger_map_event(locations["office_door"], board_rows, board_columns, game_map, character, message)
        else:
            print("Invalid move! Please choose another direction.")
