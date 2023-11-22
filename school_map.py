import movement as mov
import map as mp


def generate_school_map(game_board):
    for (x, y), location in game_board.items():
        if location == "1510":
            game_board[(x, y)] = 'P'
            mp.update_surroundings(game_board, x, y, '|', '=', 'P')
        elif location == "1113":
            game_board[(x, y)] = 'M'
            mp.update_surroundings(game_board, x, y, '|', '=', "M")
        elif location == "1712":
            game_board[(x, y)] = 'S'
            mp.update_surroundings(game_board, x, y, '|', '=', "S")
        elif location == "1537":
            game_board[(x, y)] = 'W'
            mp.update_surroundings(game_board, x, y, '|', '=', 'W')

    return game_board


def school_map_action(character):
    character['X'] = 1
    character['Y'] = 1
    school_board_rows = 13
    school_board_columns = 9
    locations = mp.coordinates()
    school_board = mp.make_board(school_board_rows, school_board_columns, locations, "school")
    school_map = generate_school_map(school_board)

    while True:
        mp.print_map(school_map, school_board_rows, school_board_columns, character)
        direction = mov.get_user_choice()
        valid_move = mov.validate_move(school_board, character, direction)
        if valid_move:
            mov.move_character(character, direction, school_board_rows, school_board_columns, school_map)
            mov.update_visited_location(character)
        else:
            print("Invalid move! Please choose another direction.")
