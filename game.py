def greeting():
    character_choices = {1: {'IQ': 1, 'EQ': 1, 'Stress': 0, 'Wealth': 20},
                         2: {'IQ': 1.5, 'EQ': 0.5, 'Stress': 0, 'Wealth': 0},
                         3: {'IQ': 0.5, 'EQ': 1, 'Stress': 0, 'Wealth': 40}}
    print('Welcome message for the game')
    # answers = input('Questionnaire')
    # print('Welcome message for CST')
    # return character_choices[int(answers)]

    return character_choices[1]


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
    # player = greeting()
    # board = generate_map(5, 5)
    # print(board)


if __name__ == '__main__':
    game()
