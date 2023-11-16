def greeting():
    print('Welcome to Survive CST. Please take a moment to answer the following questionnaire. There is no right '
          'or wrong answer.')

    new_character = {'IQ': 0, 'EQ': 0, 'Stress': 0, 'Wealth': 0, 'X': 0, 'Y': 0, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0}}
    questionnaire_stats = (({'IQ': 1.0}, {'IQ': 0.5, 'EQ': 0.5}), ({'Wealth': 40}, {'Wealth': 20, 'EQ': 0.5}),
                           ({'EQ': 0.5}, {'Wealth': 20}), ({'IQ': 0.5}, {'Wealth': 20}))

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
        (9, 8): "park",
        (7, 3): "work",
    }
    for x in range(row):
        for y in range(column):
            if (x, y) in locations:
                game_board[(x, y)] = locations[(x, y)]
            else:
                game_board[(x, y)] = " "

    return game_board


def generate_map(location):
    # location = city, park, school
    pass


def print_current_map(location):
    # prints map of player's current location to screen
    pass


def check_fast_travel(location):
    # checks whether player has been to this place before
    # if so, prints out fast travel command to desired location to screen for player to type
    pass


def fast_travel(character, location):
    # sets player coordinates to coordinates of location
    pass


def validate_move(direction):
    # checks whether player can move in desired direction
    pass


def move_character(character):
    # moves character in desired direction
    pass


def evaluate_exp(character, subject):
    """
    evaluates whether character has enough exp in a subject to level up
    if subject == all, loop through all subjects
    else, only evaluate that one subject passed in
    """
    pass


def evaluate_stress(character):
    """
    evaluates whether character need to go to ER
    """
    pass


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
    print(player)


if __name__ == '__main__':
    game()
