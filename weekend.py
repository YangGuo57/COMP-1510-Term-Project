from random import randint
import character as char


def run_weekend(character):
    """
    initialize actions
    print weekend prompt to screen
    ask user for action (stay home or go out?)
    perform action
    """
    actions = 3
    print('Gently roused by sunbeams, you awaken to the realization that the weekend has arrived. You reluctantly pull '
          'yourself out of the comfort of your bed. The weekend awaits, will it be a productive one? The choice is '
          'yours.')

    # set player location to home
    # check player location


    while actions > 0:
        user_choice = weekend_location_user_input(character['location'])
        set_character_location(character, user_choice)
        execute_weekend_action(character)
        actions -= 1

    pass

def weekend_location_user_input(location):
    """
    get user input on what to do on weekend - whether to stay home or go outside
    returns 'home' or 'outside'
    """
    flavour_text = {'home': 'A radiant weather beckons beyond your window; should you go on a refreshing outdoor stroll'
                            ' or indulge in the comforts of your home?',
                    'outside': 'The day is still bright. What would you like to do?'}
    commands = {'home': 'Enter 1 to stay home, enter 2 to leave the house.',
                'outside': 'Enter 1 to go home, enter 2 to stay outside.'}

    user_choice = input(f'{flavour_text[location]}\n{commands[location]}')
    while user_choice != '1' or '2':
        user_choice = input(f'{flavour_text[location]}\n{commands[location]}')

    return 'home' if user_choice == '1' else 'outside'


def set_character_location(character, location):
    character['location'] = location


def describe_weekend_action():
    """
    describes character coordinates after character moves via directions or fast travel
    """
    pass


def validate_weekend_location(character):
    """
    evaluates what happens at player's coordinates (nothing? does it call another function?) return bool
    """
    pass


def execute_weekend_action(character):
    if character['location'] == 'home':
        choice = weekend_action_user_input(character)
        describe_weekend_home_action(choice)
        if choice == '1':
            weekend_schoolwork(character, get_user_choice_weekend_schoolwork())
        else:
            weekend_sleep(character)
    else:
        while True:
            # ask user for move input
            # validate move
            # move character
            # evaluate character location
            # describe location
            # get user choice if character is at a destination
            # execute action at location
            break


def get_user_choice_weekend_schoolwork():
    choices = ('1510', '1537', '1113', '1712', 'project')
    user_choice = input('What do you want to work on? \n'
                        'Enter 1 to work on COMP1510,\n'
                        'enter 2 to work on COMP1537,\n'
                        'enter 3 to work on COMP1113,\n'
                        'enter 4 to work on COMP1712,\n'
                        'enter 5 to work on your personal project.')
    while user_choice not in '12345':
        user_choice = input('What do you want to work on? \n'
                            'Enter 1 to work on COMP1510,\n'
                            'enter 2 to work on COMP1537,\n'
                            'enter 3 to work on COMP1113,\n'
                            'enter 4 to work on COMP1712,\n'
                            'enter 5 to work on your personal project.')
    return choices[int(user_choice) - 1]


def weekend_schoolwork(character, subject):
    exp_gain = randint(10, 15) * 1 if subject == 'project' else randint(10, 15) * character['IQ']
    stress_gain = randint(8, 12)
    char.change_stat(character, subject, exp_gain)
    char.change_stat(character, 'stress', stress_gain)


def weekend_sleep(character):
    stress_loss = randint(15, 20) * -1
    char.change_stat(character, 'stress', stress_loss)


def describe_weekend_home_action(action):
    if action == '1':
        print('You decide to be productive (or try to be productive).')
    else:
        print('You pass out in your bed. Good night and sweet dreams.')


def weekend_action_user_input(character):
    choices = {'home': ('Your desk and your laptop patiently await your presence, ready for a productive session. Yet, '
                        'your bed is whispering your name like a neglected girlfriend. What do you do?',
                        'Enter 1 to say NO to temptation and do some work, enter 2 to succumb to the calling of '
                        'your bed.')}
    user_choice = input(f'{choices[character["location"]][0]}\n{choices[character["location"]][1]}')
    while user_choice != '1' and user_choice != '2':
        print('That is not a valid command.')
        user_choice = input(f'{choices[character["location"]][0]}\n{choices[character["location"]][1]}')
    return user_choice




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


def weekend_home():
    """
    player may choose to sleep, study for a course, or work on personal project
    """
    pass
