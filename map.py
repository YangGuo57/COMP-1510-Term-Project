import movement as mov
import menu as me
import event_trigger as e


def coordinates():
    location_coordinates = {
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
            (2, 4): "1510",
            (10, 4): "1537",
            (7, 4): "1712",
            (4, 4): "1113",
        }
    }
    return location_coordinates


def make_board(row, column, locations, keys):
    game_board = {}
    for x in range(row):
        for y in range(column):
            if (x, y) in locations[keys]:
                game_board[(x, y)] = locations[keys][(x, y)]
            else:
                game_board[(x, y)] = " "

    return game_board


def generate_game_map(game_board):
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


def map_action(character):
    main_board_rows = 10
    main_board_columns = 20
    locations = coordinates()
    game_board = make_board(main_board_rows, main_board_columns, locations, "coordinates")
    game_map = generate_game_map(game_board)

    while True:
        print_map(game_map, main_board_rows, main_board_columns, character)
        direction = mov.get_user_choice()
        if direction == "Back to Menu":
            me.main_menu(character)
        valid_move = mov.validate_move(game_board, character, direction)
        if valid_move:
            mov.move_character(character, direction, main_board_rows, main_board_columns, game_map)
            mov.update_visited_location(character)
            e.trigger_school_event(character, locations, game_map, main_board_rows, main_board_columns)
            e.trigger_home_event(character, locations, game_map, main_board_rows, main_board_columns)

        else:
            print("Invalid move! Please choose another direction.")
