def greeting():
    print('Welcome to Survive CST. Please take a moment to answer the following questionnaire. There is no right '
          'or wrong answer.')

    new_character = {'IQ': 0, 'EQ': 0, 'stress': 0, 'wealth': 0, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0}}
    questionnaire_stats = (({'IQ': 1.0}, {'IQ': 0.5, 'EQ': 0.5}), ({'wealth': 40}, {'wealth': 20, 'EQ': 0.5}),
                           ({'EQ': 0.5}, {'wealth': 20}), ({'IQ': 0.5}, {'wealth': 20}))

    answers = ask_questionnaire()

    questionnaire_index = 0
    for answer in answers:
        stats = questionnaire_stats[questionnaire_index][answer]
        for stat in stats:
            new_character[stat] += stats[stat]
        questionnaire_index += 1

    print('It is the first week of September, your first time in the City of Vancouver, and your first day studying\n'
          'Computer Systems Technology (CST) at BCIT. You enter the school elevator with mixed feelings; after all,\n'
          'you came to this foreign city in hopes that computer science is the right career for you. As you step out \n'
          'of the elevator, you tell yourself: "Don\'t stress, learn lots, make friends, get co-op, and most \n'
          'importantly, have fun!"')

    return new_character


def ask_questionnaire():
    answers = []
    questions = ('When new work is assigned to you, what do you do?\n'
                 '1. Get started on it right away\n'
                 '2. Leave it until the last minute\n',
                 'How would you describe your lifestyle?\n'
                 '1. You live in the moment\n'
                 '2. You reflect on the past and you plan for your future\n',
                 'Which of the following statements best describes you?\n'
                 '1. You are a social butterfly\n'
                 '2. You need time to recharge your social battery\n',
                 'What do you do when there is learning material you don\'t understand?\n'
                 '1. This seldom happens; you are able to solve all challenges thrown at you\n'
                 '2. You seek help from online resources or from other people\n')

    print('Please choose one of the two options that best describes you, and enter the NUMBER representing '
          'that option.')

    for question in questions:
        answer = input(question)
        while answer != '1' and answer != '2':
            print('That is not a valid entry. Enter the NUMBER representing the option that best describes you.')
            answer = input(question)
        answers.append(int(answer) - 1)

    return answers


def print_stats():
    """
    prints character stats to screen
    """


def make_board(row, column):
    game_board = {}
    locations = {
        (3, 4): "school",
        (5, 8): "hospital",
        (2, 12): "park",
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
            update_surroundings(game_board, x, y, '=', '=', 'P')
        elif location == "work":
            game_board[(x, y)] = 'W'
            update_surroundings(game_board, x, y, '|', '~', 'W')

    return game_board


def update_surroundings(game_board, x, y, horizontal_symbol, vertical_symbol, location_symbol):
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i, j) in game_board and game_board[(i, j)] != location_symbol:
                game_board[(i, j)] = horizontal_symbol

    for j in range(y - 1, y + 2):
        for i in [x - 1, x + 1]:
            if (i, j) in game_board and game_board[(i, j)] != location_symbol:
                game_board[(i, j)] = vertical_symbol


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


def get_user_choice():
    directions = ["North", "East", "South", "West"]
    while True:
        for i in range(len(directions)):
            print(f"{i + 1}. {directions[i]}", end=' ')

        choice = input("\nPlease choose a direction number: ")
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice <= len(directions):
                select_direction = directions[choice - 1]
                return select_direction
            else:
                print("Please choose a valid direction number!")
        else:
            print("Please choose a valid direction number!")


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


def move_character(character, direction, row, column):
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

    character["X"] = x_coordinate
    character["Y"] = y_coordinate


def check_fast_travel(location):
    # checks whether player has been to this place before
    # if so, prints out fast travel command to desired location to screen for player to type
    pass


def fast_travel(character, location):
    # sets player coordinates to coordinates of location
    pass


def evaluate_exp(character, subject):
    """
    evaluates whether character has enough exp in a subject to level up
    if subject == all, loop through all subjects
    else, only evaluate that one subject passed in
    """
    threshold = 100

    if subject == 'all':
        subject = ('1510', '1537', '1113', '1712')
    else:
        subject = subject,
        subject = tuple(subject)

    for each_subject in subject:
        level_threshold = (character['lvl'][each_subject] + 1) * threshold
        print(each_subject, character['exp'][each_subject])
        if character['exp'][each_subject] > level_threshold:
            character['lvl'][each_subject] += 1
            print(f'Through relentlessly studying for COMP{each_subject}, an epiphany strikes you and suddenly'
                  f'everything that was once perplexing becomes clear and understandable...')


def evaluate_stress(character):
    """
    evaluates whether character need to go to ER
    """
    pass_out = False
    if character['stress'] > 100:
        print('Suddenly the world is spinning and darkness befalls over your eyes... You succumbed to the pressure'
              'of life and you lay on the ground, unconscious. Thankfully, a passerby sees your motionless body and'
              'dials 911 for assistance.')
        pass_out = True
    elif character['stress'] > 90:
        print('You feel your heart palpitating and you can\'t breathe... Maybe you should get some rest?')
    elif character['stress'] > 80:
        print('You feel a sudden light-headedness... Maybe you should take it easy?')

    return pass_out


def run_weekday(character):
    """
    print weekday prompt to screen (eg. It is now week 5, only 2 more weeks until midterms...)
    increase exp in all subjects
    increase stress
    evaluate_exp()
    evaluate_stress()
    generate random event
    """
    pass


def random_weekday_event():
    """
    hackathon (most rare), quiz, club event, assignment, trauma bond
    evaluate_exp()
    evaluate_stress()
    """
    pass


def weekend_user_input():
    """
    get user input on what to do on weekend
    """
    pass


def describe_weekend_action():
    """
    describes character coordinates after character moves via directions or fast travel
    """
    pass


def validate_weekend_location():
    """
    evaluates what happens at player's coordinates (nothing? does it call another function?) return bool
    """
    pass


def confirm_weekend_action():
    """
    if validate_weekend_location returns True
    ask player if player wants to enter this location
    if so, actions -= 1
    call action-specific function
    """
    pass


def weekend_school():
    """
    generates random events at school on a weekend
    """
    pass


def weekend_gym():
    """
    weekend events at gym
    """
    pass


def weekend_hospital():
    """
    weekend events at hospital
    """
    pass


def weekend_job():
    """
    work at part-time job
    attend_work = True
    """
    pass


def evaluate_job_attendance():
    """
    keeps track of how many times player has skipped work
    if > 2 times, player is fired
    """
    pass


def weekend_party():
    """
    weekend events at party
    """
    pass


def weekend_park():
    """
    weekend events at park
    print map of park
    does player have a job? if not, generate job posting
    player can move freely
    evaluate player coordinates after each move
    random_park_event()
    """
    pass


def random_park_event():
    """
    generate random event in the park
    """
    pass


def weekend_mall():
    """
    generate events at mall
    """
    pass


def weekend_home():
    """
    player may choose to sleep, study for a course, or work on personal project
    """
    pass


def run_weekend():
    """
    initialize actions
    print weekend prompt to screen
    ask user for action (stay home or go out?)
    perform action
    """
    pass


def game():
    player = greeting()
    rows = 10
    columns = 18
    board = make_board(rows, columns)
    game_map = generate_game_map(board)
    while True:
        print_map(game_map, rows, columns, player)
        direction = get_user_choice()
        valid_move = validate_move(board, player, direction)
        if valid_move:
            move_character(player, direction, rows, columns)
        else:
            print("Invalid move! Please choose another direction.")
            continue
        game_map = generate_game_map(board)


if __name__ == '__main__':
    game()
