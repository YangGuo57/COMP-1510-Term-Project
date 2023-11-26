from random import randint
import character as char
import event_trigger as event
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
    char.set_character_location(character, 'home')
    locations = event.trigger_description()

    while actions > 0:
        if character['location'] == 'outside':
            # trigger events on big map
            event.trigger_action(character, 10, 20, 'coordinates')
        else:
            # trigger events at home
            user_choice = event.confirm_entry(character['location'])
            char.set_character_location(character, locations[character['location']][user_choice])
            execute_weekend_home_action(character)
        actions -= 1


def execute_weekend_home_action(character):
    """
    do the action
    """
    if character['location'] == 'home' or character['location'] == 'bed':
        choice = weekend_action_user_input(character)
        describe_weekend_home_action(choice)
        if choice == '1':
            weekend_schoolwork(character, get_user_choice_weekend_schoolwork())
        else:
            weekend_sleep(character)
    # else:
    #     while True:
    #         # ask user for move input
    #         # validate move
    #         # move character
    #         # evaluate character location
    #         # describe location
    #         # get user choice if character is at a destination
    #         # execute action at location
    #         break


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





def get_user_choice_weekend_schoolwork():
    """
    get user choice on what kind of schoolwork to do when user is at home
    """
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
    """
    carry out the schoolwork and modify stats accordingly
    """
    exp_gain = randint(10, 15) * 1 if subject == 'project' else randint(10, 15) * character['IQ']
    stress_gain = randint(8, 12)
    char.change_stat(character, subject, exp_gain)
    char.change_stat(character, 'stress', stress_gain)


def weekend_sleep(character):
    """
    sleep
    """
    stress_loss = randint(15, 20) * -1
    char.change_stat(character, 'stress', stress_loss)


def describe_weekend_home_action(action):
    """
    print flavour text to describe the action at home
    """
    if action == '1':
        print('You decide to be productive (or try to be productive).')
    else:
        print('You pass out in your bed. Good night and sweet dreams.')


def weekend_action_user_input(character):
    """
    get user choice on whether to work or sleep
    """
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


def weekend_park(character):
    """
    weekend events at park
    does player have a job? if not, generate job posting
    random_park_event() if character has not applied to a job posting
    """
    applied_to_job = False
    if character['job'] == False:
        applied_to_job = generate_job_posting(character)

    if not applied_to_job:
        random_park_event(character)
    print('That was a nice walk. Stanley Park seems like it sometimes hosts flea markets on the weekend. If you have '
          'some spare change, perhaps you should go check it out?')


def generate_job_posting(character):
    """
    Generates job posting is character is unemployed. Returns boolean to represent whether character applied to job.
    :param character:
    :return:
    """
    print(f'As you take in the fresh air and enjoy the greenery, you notice a piece of paper fluttering in the '
          f'breeze. Snatching it from the air, you realize it\'s a job posting - a local coffee shop is looking '
          f'for a weekend part-timer,  just a stone\'s throw away from your home! Extra money will always come '
          f'in handy... but it comes at the cost of sacrificing precious weekend hours. Should you apply?')
    user_choice = input(f'Enter "1" to apply, "2" to ignore.')
    while user_choice != '1' and user_choice != '2':
        print('That is not a valid input!')
        user_choice = input(f'Enter "1" to apply, "2" to ignore.')
    if user_choice == '1':
        print('You applied and got the job immediately! Guess they were really desperate for help. Don\'t forget '
              'to go to work every weekend!')
        character['job'] = True
        return True
    else:
        print('You decide your free time on the weekend is more important. You throw the job posting into the '
              'garbage can, because littering is bad. You venture deeper into the park.')
        return False



def random_park_event(character):
    """
    generate random event in the park
    """
    roll = randint(1, 10)

    if roll in range(5, 7):
        print(f'{generate_park_message_to_print(roll)}')
        stress_loss = randint(-20, -15)
        char.change_stat(character, 'stress', stress_loss)
    elif roll in range(7, 9):
        enter = flea_market(character)
        if not enter:
            roll -= 5
    elif roll in range(9, 11):
        print(f'{generate_park_message_to_print(roll)}')
        char.change_stat(character, 'wealth', 10)
    if roll in range(1, 5):
        print(f'{generate_park_message_to_print(roll)}')
        stress_loss = randint(-10, -5)
        char.change_stat(character, 'stress', stress_loss)


def generate_park_message_to_print(roll):
    messages = {
        range(1, 5): 'Taking a deep breath of the fresh air in Stanley Park helps ease your anxiety as you walk.',
        range(5, 7): 'A stray cat approaches, meowing softly. You give it a gentle tummy rub, and it responds with '
                     'happy purring. Seeing this carefree, adorable little creature revel in the simple joys of life '
                     'inspires you to adopt a similar mentality.',
        range(7, 9): {'default': 'It seems there is a weekend flea market going on today at Stanley Park. Should you '
                                 'go check it out?\nEnter "1" to check out the flea market, "2" to continue walking.',
                      'enter flea': 'You decide to explore the flea market.',
                      'kool-aid': 'An eccentric old lady grabs you and pulls you to her stall, excitedly pitching her '
                                  '"Mega Brain Power Elixir." She claims it can turn even the least brainy person into '
                                  'a genius. Despite your attempts to leave, she\'s persistent. Feeling cornered, '
                                  'you give in and buy a ridiculously expensive bottle of the mysterious liquid. With '
                                  'reluctance, you gulp it down, and it tastes like Kool-Aid.',
                      'no kool-aid': 'You see so many things you want to buy. You reach for your wallet, but Alas, '
                                     'there\'s no money inside. The sight of your empty wallet makes you sad. With a '
                                     'sigh, you turn around and leave the park.',
                      'leave flea': 'You decide to keep walking.'},
        range(9, 11): 'How lucky! You find some money on the ground!'
    }
    for key in messages:
        if roll in key:
            return messages[key]


def flea_market(character):
    messages = generate_park_message_to_print(7)
    user_choice = input(f'{messages["default"]}')
    while user_choice != '1' and user_choice != '2':
        user_choice = input(f'{messages["default"]}')
    if user_choice == '1':
        print(f'{messages["enter flea"]}')
        if character['wealth'] >= 60:
            print(f'{messages["kool-aid"]}')
            char.change_stat(character, 'wealth', -60)
            char.change_stat(character, 'IQ', 0.5)
        else:
            print(f'{messages["no kool-aid"]}')
            stress_gain = randint(10, 15)
            char.change_stat(character, 'stress', stress_gain)
        return True
    else:
        print(f'{messages["leave flea"]}')
        return False


def weekend_home():
    """
    player may choose to sleep, study for a course, or work on personal project
    """
    pass
