from helper_functions import map, event_trigger as event


def validate_move(board, character, direction):
    """
    Determine if the character can move in the given direction.

    :param board: a dictionary
    :param character: a dictionary
    :param direction: a string
    :precondition: board must be a dictionary representing the board
    :precondition: character must be a dictionary representing the character
    :precondition: direction must be a string representing the direction
    :postcondition: determine if the character can move in the given direction
    :return: True if the character can move in the given direction, False otherwise

    >>> game_board = {(0, 0): ' ', (0, 1): ' ', (1, 0): ' ', (1, 1): ' '}
    >>> player = {'X': 0, 'Y': 0}
    >>> player_direction = 'North'
    >>> validate_move(game_board, player, player_direction)
    False
    """
    x_coordinate = character['X']
    y_coordinate = character['Y']

    if direction == 'North':
        coordinate = (x_coordinate - 1, y_coordinate)
    elif direction == 'South':
        coordinate = (x_coordinate, y_coordinate + 1)
    elif direction == 'East':
        coordinate = (x_coordinate + 1, y_coordinate)
    else:
        coordinate = (x_coordinate, y_coordinate - 1)

    if coordinate in board:
        return True

    return False


def get_user_choice(character):
    """
    Get the user's choice of direction to move in.

    :param character: a dictionary
    :precondition: character must be a dictionary representing the character
    :postcondition: returns a string representing the direction the user wants to move in
    :return: a string representing the direction the user wants to move in
    """
    commands = {'w': 'North', 's': 'South', 'a': 'West', 'd': 'East'}
    school_commands = {'back': 'To go home', 'stats': 'To see your stats'}

    prompt_string = 'Choose a command:\n'
    for i, command in enumerate(commands, 1):
        prompt_string += f'To go {commands[command]}, type {command} \n'
    if character['location'] == 'school':
        prompt_string += f'{school_commands["back"]}, type back \n'
        prompt_string += f'{school_commands["stats"]}, type stats\n'

    while True:
        choice = input(f'{prompt_string}')
        if choice in commands.keys():
            return commands[choice]
        elif character['location'] == 'school' and choice in school_commands:
            return choice
        else:
            print('Enter a valid input!')


def move_character(character, direction, game_map):
    """
    Move the character in the direction specified if possible.

    :param character: a dictionary
    :param direction: a string
    :param game_map: a dictionary
    :precondition: character must be a dictionary representing the character
    :precondition: direction must be a string representing the direction
    :precondition: game_map must be a dictionary representing the character
    :postcondition: updates the character's position if possible

    >>> player = {'X': 1, 'Y': 1}
    >>> map_game = {'rows': 2, 'columns': 2, 'board': {(0, 0): ' ', (0, 1): ' ', (1, 0): ' ', (1, 1): ' '}}
    >>> move_character(player, 'North', map_game)
    You hit a wall!
    """
    x_coordinate = character['X']
    y_coordinate = character['Y']
    rows = game_map['rows']
    columns = game_map['columns']

    if direction == 'North' and x_coordinate > 1:
        x_coordinate -= 1
    elif direction == 'East' and y_coordinate < columns - 2:
        y_coordinate += 1
    elif direction == 'South' and x_coordinate < rows - 2:
        x_coordinate += 1
    elif direction == 'West' and y_coordinate > 1:
        y_coordinate -= 1
    else:
        print('You hit a wall!')
        return

    new_position = (x_coordinate, y_coordinate)
    location = game_map[new_position]

    if location in [' ', '|']:
        character['X'] = x_coordinate
        character['Y'] = y_coordinate
    else:
        if not event.at_entrance(character):
            print('You hit a wall!')


def update_visited_location(character):
    """
    Update the visited location of the character.

    :param character: a dictionary
    :precondition: character must be a dictionary representing the character
    :postcondition: update the visited location of the character
    """
    player_position = (character['X'], character['Y'])
    locations = map.coordinates()
    for location, door_positions in locations['door']['main'].items():
        if player_position == door_positions:
            character['visited_locations'][location] += 1
            break


def fast_travel(character):
    """
    Allows the user to fast travel to a location they have visited before.

    :param character: a dictionary
    :precondition: character must be a dictionary representing the character
    :postcondition: moves the character to the location they have chosen
    """
    locations = map.coordinates()
    destination = input('Please input fast travel destination: home, school, hospital, park, work:')
    if destination.lower() in locations['door']['main']:
        visited = character['visited_locations'][destination]
        if visited:
            character['X'], character['Y'] = locations['door']['main'][destination]
            print(f'You\'ve fast traveled to {destination}!')
        else:
            print(f'You\'re new to Vancouver, you don\'t know where {destination} is! You must have visited '
                  f'{destination} at least once before fast traveling there.')
    else:
        print('Invalid destination.')
