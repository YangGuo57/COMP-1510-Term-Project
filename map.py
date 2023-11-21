import movement as mov
import menu as me


def make_board(row, column):
    game_board = {}
    locations = {
        (2, 2): "home",
        (3, 8): "school",
        (6, 13): "hospital",
        (2, 16): "park",
        (7, 5): "work",
    }
    for x in range(row):
        for y in range(column):
            if (x, y) in locations:
                game_board[(x, y)] = locations[(x, y)]
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
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i, j) in game_board and game_board[(i, j)] != location_symbol:
                game_board[(i, j)] = door

    for j in range(y - 1, y + 2):
        for i in [x - 1, x + 1]:
            if (i, j) in game_board and game_board[(i, j)] != location_symbol:
                game_board[(i, j)] = wall


def print_map(game_board, row, column, character):
    player_position = (character['X'], character['Y'])
    for i in range(row):
        for j in range(column):
            if (i, j) == player_position:
                print('*', end=' ')
            elif i == 0 or i == row - 1:
                print('-', end=' ')
            elif j == 0 or j == column - 1:
                print('|', end=' ')
            else:
                print(game_board[(i, j)], end=' ')
        print()


def map_action(character):
    rows = 10
    columns = 20
    board = make_board(rows, columns)
    game_map = generate_game_map(board)

    while True:
        print_map(game_map, rows, columns, character)
        direction = mov.get_user_choice()
        if direction == "Back to Menu":
            me.main_menu(character)
        valid_move = mov.validate_move(board, character, direction)
        if valid_move:
            mov.move_character(character, direction, rows, columns, game_map)
            mov.update_visited_location(character)
        else:
            print("Invalid move! Please choose another direction.")
