import map
import character as char


def validate_move(board, character, direction):
    x_coordinate = character["X"]
    y_coordinate = character["Y"]

    if direction == "North":
        coordinate = (x_coordinate - 1, y_coordinate)
    elif direction == "South":
        coordinate = (x_coordinate, y_coordinate + 1)
    elif direction == "East":
        coordinate = (x_coordinate + 1, y_coordinate)
    else:
        coordinate = (x_coordinate, y_coordinate - 1)

    if coordinate in board:
        return True

    return False


def get_user_choice(character):
    commands = {'w': "North", 's': "South", 'a': "West", 'd': "East"}
    school_commands = {'back': 'To go home', 'stats': 'To see your stats'}

    prompt_string = 'Choose a command:\n'
    for i, command in enumerate(commands, 1):
        prompt_string += f"To go {commands[command]}, type {command} \n"
    if character['location'] == 'school':
        prompt_string += f'{school_commands["back"]}, type back \n'
        prompt_string += f'{school_commands["stats"]}, type stats\n'

    while True:
        choice = input(f'{prompt_string}')
        if choice in commands:
            return commands[choice]
        elif choice in school_commands:
            if character['location'] == 'school' and choice == 'stats':
                char.print_stats(character)
            else:
                return choice
        else:
            print('Enter a valid input!')


def move_character(character, direction, game_map):
    x_coordinate = character["X"]
    y_coordinate = character["Y"]
    rows = game_map["rows"]
    columns = game_map["columns"]

    if direction == "North" and x_coordinate > 1:
        x_coordinate -= 1
    elif direction == "East" and y_coordinate < columns - 2:
        y_coordinate += 1
    elif direction == "South" and x_coordinate < rows - 2:
        x_coordinate += 1
    elif direction == "West" and y_coordinate > 1:
        y_coordinate -= 1
    else:
        print("You hit a wall!")
        return

    new_position = (x_coordinate, y_coordinate)
    location = game_map[new_position]

    if location in [' ', '|']:
        character["X"] = x_coordinate
        character["Y"] = y_coordinate
    else:
        print("You hit a wall!")


def update_visited_location(character):
    player_position = (character['X'], character['Y'])
    locations = map.coordinates()
    for location, door_positions in locations["door"]["main"].items():
        if player_position == door_positions:
            character['visited_locations'][location] += 1
            break


def fast_travel(character):
    locations = map.coordinates()
    destination = input("Please input fast travel destination: home, school, hospital, park, work:")
    if destination.lower() in locations["door"]["main"]:
        visited = character['visited_locations'][destination]
        if visited:
            character['X'], character['Y'] = locations["door"]["main"][destination]
            print(f"You've fast traveled to {destination}!")
        else:
            print(f"You need to visit {destination} at least once before fast traveling there.")
    else:
        print("Invalid destination.")
