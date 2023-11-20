def make_board(row, column):
    game_board = {}
    locations = {
        (3, 4): "school",
        (5, 8): "hospital",
        (2, 13): "park",
        (7, 3): "work",
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
        if location == "hospital":
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
