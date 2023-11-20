def validate_move(board, character, direction):
    x_coordinate = character["X"]
    y_coordinate = character["Y"]

    if direction == "North":
        coordinate = (x_coordinate - 1, y_coordinate)
    elif direction == "East":
        coordinate = (x_coordinate, y_coordinate + 1)
    elif direction == "South":
        coordinate = (x_coordinate + 1, y_coordinate)
    else:
        coordinate = (x_coordinate, y_coordinate - 1)

    if coordinate in board:
        return True

    return False


def get_user_choice():
    directions = ["North", "East", "South", "West", "Back to Menu"]

    while True:
        for i in range(len(directions)):
            print(f"{i + 1}. {directions[i]}", end=' ')

        choice = input("\nPlease input a number\n")
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice <= len(directions):
                if choice == 5:
                    pass
                select_direction = directions[choice - 1]
                return select_direction
            else:
                print("Please choose a valid direction number!")
        else:
            print("Please choose a valid direction number!")


def move_character(character, direction, row, column, game_board):
    x_coordinate = character["X"]
    y_coordinate = character["Y"]

    if direction == "North" and x_coordinate > 1:
        x_coordinate -= 1
    elif direction == "East" and y_coordinate < column - 2:
        y_coordinate += 1
    elif direction == "South" and x_coordinate < row - 2:
        x_coordinate += 1
    elif direction == "West" and y_coordinate > 1:
        y_coordinate -= 1
    else:
        print("You hit a wall!")
        return

    new_position = (x_coordinate, y_coordinate)
    location = game_board[new_position]

    if location in [' ', '|']:
        character["X"] = x_coordinate
        character["Y"] = y_coordinate
    else:
        print("You hit a wall!")


def update_visited_location(character):
    player_position = (character['X'], character['Y'])
    location_door = {
        "school": [(3, 3), (3, 5)],
        "hospital": [(5, 7), (5, 9)],
        "park": [(2, 12), (2, 14)],
        "work": [(7, 2), (7, 5)]
    }

    for location, door_positions in location_door.items():
        if player_position in door_positions:
            character['visited_locations'][location] += 1
            break
