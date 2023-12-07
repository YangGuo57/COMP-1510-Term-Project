import random
from helper_functions import PRODUCTIVE_STATS, event_trigger as event, character as char, save
from time import sleep


def weekend(character, main_map, week):
    """
    Carries out 3 weekend events on the main map.

    :param character: character dictionary
    :param week: integer representing week number
    :param main_map: map dictionary
    :precondition: character must be a valid character dictionary created in this program
    :precondition: week must be a valid positive integer representing week number created in this program
    :precondition: main_map must be a valid map dictionary created in this program
    :postcondition: properly adjusts character's stats based on weekend events
    """
    actions = 3
    print('Gently roused by sunbeams, you awaken to the realization that the weekend has arrived. You reluctantly pull '
          'yourself out of the comfort of your bed. The weekend awaits, will it be a productive one? The choice is '
          'yours.')

    # set player location to home
    character['X'], character['Y'] = 2, 3
    sleep(0.5)
    char.set_character_location(character, 'home')
    job_attendance = False
    applied_to_job = 0

    while actions > 0:
        if character['location'] == 'home':
            # trigger events at home
            user_choice = event.confirm_entry(character['location'])
            if user_choice == '1':
                execute_weekend_home_action(character)
            else:
                char.set_character_location(character, 'outside')
        if character['location'] == 'outside':
            # trigger events on the big map
            choice = event.move_on_weekends(character, main_map)
            while choice != '1':
                if choice == 'Save and quit the game':
                    return False
                choice = event.move_on_weekends(character, main_map)
            if choice == '1':
                sleep(0.5)
                location = event.at_entrance(character)
                track_job_status = function_dispatcher(character, location)
                applied_to_job += track_job_status[0]
                job_attendance += track_job_status[1]
        actions -= 1

    if not applied_to_job and 'job' in character:
        evaluate_job_attendance(character, job_attendance)

    save.save_game(character, week, False)
    return True


def function_dispatcher(character, location):
    """
    Dispatches the function to be executed based on the location

    :param character: character dictionary
    :param location: a string
    :precondition: character must be a dictionary
    :precondition: location must be a string
    :postcondition: executes the function based on the location
    :return: applied_to_job, job_attendance
    """
    functions = {
        'park': weekend_park,
        'work': weekend_job,
        'hospital': weekend_hospital,
        'school': weekend_school,
        'home': execute_weekend_home_action
    }
    applied_to_job = 0
    job_attendance = False
    if location == 'park':
        applied_to_job += functions[location](character)
    elif location == 'work':
        functions[location](character)
        job_attendance = True
    else:
        functions[location](character)
    print()

    return applied_to_job, job_attendance


def binary_user_choice(setting):
    """
    Prints to console to get user choice for questions with binary answers.

    :param setting: string representing the setting of the question
    :precondition: setting must be a key in prompts and options
    :postcondition: correctly prints to console to get and return user choice
    :return: a string representing user choice
    """
    prompts = {'quit job': 'Are you too busy to go to work? If so, maybe you should let your manager know you want to '
                           'quit...',
               'home': 'Your desk and your laptop patiently await your presence, ready for a productive session. Yet, '
                       'your bed is whispering your name like a neglected girlfriend. What do you do?',
               'hospital': '"You must be here for your annual vaccination," she says, "Now don\'t stand there and '
                           'block the way, the lineup for getting your vaccine is this way."\n'
                           'She grabs you by your arm and tries to lead you deeper into the hospital.',
               'job posting': 'As you take in the fresh air and enjoy the greenery, you notice a piece of paper '
                              'fluttering in the breeze. Snatching it from the air, you realize it\'s a job posting - '
                              'a local cafe is looking for a weekend part-timer,  just a stone\'s throw away from '
                              'your home! Extra money will always come in handy... but it comes at the cost of '
                              'sacrificing precious weekend hours. Should you apply?',
               'flea market': 'It seems there is a weekend flea market going on today at Stanley Park. Should you go '
                              'check it out?'}
    options = {'quit job': 'Enter "1" to keep your job, "2" to quit.',
               'home': 'Enter 1 to say NO to temptation and do some work, enter 2 to succumb to the calling of '
                       'your bed.',
               'hospital': 'Enter "1" to follow her, "2" to break free from her grasp.',
               'job posting': 'Enter "1" to apply, "2" to ignore.',
               'flea market': 'Enter "1" to check out the flea market, "2" to continue walking.'}
    result = {'hospital': {'1': 'The nurse jabs you with a needle. Ouch. Surely this won\'t make you autistic right?',
                           '2': 'You manage to slip away from the nurse\'s grasp and escape from the hospital.'},
              'job posting': {'1': '\nYou applied and got the job immediately! Guess they were really desperate for '
                                   'help.',
                              '2': 'You decide your free time on the weekend is more important. You throw the job '
                                   'posting into the garbage can, because littering is bad. You venture deeper into '
                                   'the park.'},
              'quit job': {'1': 'You decide to keep your part time job for now. Just don\'t forget to go to work '
                                'again!',
                           '2': 'You decide you can no longer commit to weekly shifts. Being the thoughtful person '
                                'you are, you let your manager know.'}}
    print(f'{prompts[setting]}')
    user_choice = input(f'{options[setting]}')
    while user_choice != '1' and user_choice != '2':
        print('That is not a valid command.')
        sleep(0.5)
        print(f'{prompts[setting]}')
        user_choice = input(f'{options[setting]}')
    if setting != 'home' and setting != 'flea market':
        print(result[setting][user_choice])
    return user_choice


def execute_weekend_home_action(character):
    """
    Executes selected weekend action at home.

    :param character: a dictionary representing the player character
    :precondition: character must be a dictionary generated in this program
    :postcondition: correctly executes weekend action
    """
    char.set_character_location(character, 'home')
    choice = binary_user_choice('home')
    describe_weekend_home_action(choice)
    sleep(0.5)
    if choice == '1':
        weekend_schoolwork(character, get_user_choice_weekend_schoolwork())
    else:
        weekend_sleep(character)


def get_user_choice_weekend_schoolwork():
    """
    Gets user choice on what kind of schoolwork to do when user is at home.

    :return: a string representing the user's choice
    """
    user_choice = input('What do you want to work on? \n'
                        'Enter 1 to work on COMP1510,\n'
                        'Enter 2 to work on COMP1537,\n'
                        'Enter 3 to work on COMP1113,\n'
                        'Enter 4 to work on COMP1712,\n'
                        'Enter 5 to work on your personal project.')
    while user_choice not in ('1', '2', '3', '4', '5'):
        print('That is not a valid entry.')
        sleep(0.5)
        user_choice = input('What do you want to work on? \n'
                            'Enter 1 to work on COMP1510,\n'
                            'Enter 2 to work on COMP1537,\n'
                            'Enter 3 to work on COMP1113,\n'
                            'Enter 4 to work on COMP1712,\n'
                            'Enter 5 to work on your personal project.')
    return PRODUCTIVE_STATS[int(user_choice) - 1]


def weekend_schoolwork(character, subject):
    """
    Modifies character stats on the selected schoolwork by the user.

    :param character: a dictionary representing the player character
    :param subject: a string representing the subject the user chose to work on
    :precondition: character must be a dictionary generated in this program
    :precondition: subject must be a string generated in this program
    :postcondition: correctly modifies character stats on the selected subject
    """
    exp_gain = random.randint(15, 20) * 1 if subject == 'project' else random.randint(15, 20) * character['IQ']
    stress_gain = random.randint(5, 10)
    char.change_stat(character, subject, exp_gain)
    sleep(0.5)
    char.change_stat(character, 'stress', stress_gain)


def weekend_sleep(character):
    """
    Modifies character stats when user chooses to sleep on the weekend.

    :param character: a dictionary representing the player character
    :precondition: character must be a dictionary generated in this program
    :postcondition: correctly modifies character stats when user chooses to sleep on the weekend
    """
    stress_loss = random.randint(25, 30) * -1
    char.change_stat(character, 'stress', stress_loss)


def describe_weekend_home_action(action):
    """
    Prints flavour text to describe the action at home.

    :param action: a string representing the action the user chooses to do at home
    :precondition: action must be a string generated from binary_user_choice()
    :postcondition: correctly prints flavour text to describe the action at home

    >>> describe_weekend_home_action('1')
    You decide to be productive (or try to be productive).

    >>> describe_weekend_home_action('2')
    You pass out in your bed. Good night and sweet dreams.
    """
    if action == '1':
        print('You decide to be productive (or try to be productive).')
    else:
        print('You pass out in your bed. Good night and sweet dreams.')


def weekend_school(character):
    """
    Generates random events at school on a weekend.

    :param character: a dictionary representing the player character
    :precondition: character must be a dictionary generated in this program
    :postcondition: correctly generates random events at school on a weekend
    """
    print('The school is closed weekends. Why are you even here?')
    sleep(0.5)
    roll = random.randint(1, 2)
    stress_change = 0
    increase_in_eq = 0
    if roll == 1:
        print('You run into some classmates, who drag you along to a weekend party. How do they have so much free time '
              'on their hands?')
        stress_change += random.randint(10, 15) * -1
        increase_in_eq += random.randint(1, 3)
    else:
        print('You accidentally walk into a hobo because you did not pay attention to where you were going. The hobo '
              'thinks you\'re picking a fight with him, and starts yelling profanities at you. You tell him off, '
              'but the encounter leaves you feeling a bit shaken.')
        stress_change += random.randint(10, 15)
        increase_in_eq += random.randint(1, 3)
    sleep(0.5)
    char.change_stat(character, 'EQ', increase_in_eq)
    char.change_stat(character, 'stress', stress_change)


def weekend_hospital(character):
    """
    Adjust character stats when character goes to the hospital on the weekend.

    :param character: a dictionary representing the player character
    :precondition: character must be a dictionary generated in this program
    :postcondition: correctly adjusts character stats when character goes to the hospital on the weekend
    """
    print('As you step inside Vancouver General Hospital, the scent of disinfectants greets you. Inside, '
          'it\'s serious with doctors and nurses bustling around, and you stand at the entrance feeling a bit lost. '
          'A nurse notices you and walks up to you.')
    sleep(0.5)
    if not character['vaccinated']:
        user_choice = binary_user_choice('hospital')
        if user_choice == '1':
            sleep(0.5)
            char.change_stat(character, 'IQ', 1)
            character['vaccinated'] = True
    else:
        print('"What are you doing here?" she says, "You\'re not sick and you already got your vaccination!'
              'Now don\'t stand there and block the way, go home."\n'
              'The nurse ushers you out of the hospital.')


def weekend_job(character):
    """
    Adjusts character stats when character visits the local cafe on a weekend.

    :param character: a dictionary representing the player character
    :precondition: character must be a dictionary generated in this program
    :postcondition: correctly adjusts character stats when character visits the local cafe on a weekend
    """
    if 'job' in character and character['job']:
        print('You begin your shift at the cafe. The aroma of freshly brewed coffee fills the air as you learn '
              'the ropes—taking orders, serving customers, and maybe even mastering the art of crafting the perfect '
              'cup. Even though this does not relate to what you learn in school, you begin to feel more confident '
              'navigating work relationships.')
        sleep(0.5)
        char.change_stat(character, 'wealth', 20)
        increase_in_eq = random.randint(1, 3)
        char.change_stat(character, 'EQ', increase_in_eq)
    elif 'job' in character and not character['job']:
        print('You arrive at your previous workplace. You exchange awkward glances with your previous manager. Why '
              'are you even here?')
    else:
        print('You arrive at a bustling cafe. You sit down and attempt to do some work, but the noisy environment '
              'is heavily distracting. You don\'t get anything done.')
    sleep(0.5)
    stress_gain = random.randint(5, 8)
    char.change_stat(character, 'stress', stress_gain)
    return True


def evaluate_job_attendance(character, skip):
    """
    Keeps track of how many times character has skipped work.

    :param character: a dictionary representing the player character
    :param skip: a boolean representing whether the player skipped work
    :precondition: character must be a dictionary generated in this program
    :postcondition: correctly increments the number of times the player skipped work
    """
    if character['job'] and not skip:
        character['skip_job'] += 1
        sleep(0.5)
        print('\nUh oh, did you forget to go to work this weekend?')
        evaluate_firing_from_job(character)


def evaluate_firing_from_job(character):
    """
    Evaluates whether character should be fired from their job.

    :param character: a dictionary representing the player character
    :precondition: character must be a dictionary generated in this program
    :postcondition: correctly evaluates whether character should be fired from their job
    """
    if character['skip_job'] >= 3:
        sleep(0.5)
        print('\nYou receive an angry call from your manager, since you missed work too many times. Your manager fires '
              'you over the phone.')
        character['job'] = False
        char.change_stat(character, 'EQ', -15)
    if character['skip_job'] == 2:
        sleep(0.5)
        user_choice = binary_user_choice('quit job')
        if user_choice == '2':
            character['job'] = False


def weekend_park(character):
    """
    Execute weekend events at Stanley Park depending on whether player has worked a job before.

    :param character: a dictionary representing the player character
    :precondition: character must be a dictionary generated in this program
    :postcondition: correctly executes weekend events at Stanley Park depending on whether player has worked a job
    """
    applied_to_job = False
    if 'job' not in character:
        applied_to_job = generate_job_posting(character)

    if not applied_to_job:
        random_park_event(character)
    sleep(0.5)
    print('\nThat was a nice walk. Stanley Park seems like it sometimes hosts flea markets on the weekend. If you have '
          'some spare change, perhaps come here more often to check it out?')

    return applied_to_job


def generate_job_posting(character):
    """
    Generates job posting if character is unemployed.

    :param character: a dictionary representing the player character
    :precondition: character must be a dictionary generated in this program
    :postcondition: correctly generates job posting if character is unemployed
    :return: a boolean representing whether the player applied to the job
    """
    user_choice = binary_user_choice('job posting')
    if user_choice == '1':
        sleep(0.5)
        print('Remember, your new part-time job is at the local cafe! And don\'t forget to go to work every weekend!\n')
        character['job'] = True
    return user_choice == '1'


def random_park_event(character):
    """
    Generates an event in Stanley park randomly.

    :param character: a dictionary representing the player character
    :precondition: character must be a dictionary generated in this program
    :postcondition: correctly generates an event in Stanley park randomly
    """
    roll = random.randint(1, 10)

    if roll in range(5, 7):
        print(f'{generate_park_message_to_print(roll)}')
        sleep(0.5)
        stress_loss = random.randint(-20, -15)
        char.change_stat(character, 'stress', stress_loss)
    elif roll in range(7, 9):
        enter = flea_market(character)
        if not enter:
            roll -= 5
    elif roll in range(9, 11):
        print(f'{generate_park_message_to_print(roll)}')
        sleep(0.5)
        char.change_stat(character, 'wealth', 10)
    if roll in range(1, 5):
        print(f'{generate_park_message_to_print(roll)}')
        sleep(0.5)
        stress_loss = random.randint(-15, -10)
        char.change_stat(character, 'stress', stress_loss)


def generate_park_message_to_print(roll):
    """
    Prints message to console depending on the roll.

    :param roll: an integer representing the roll
    :precondition: roll must be an integer generated from random_park_event()
    :postcondition: correctly prints message to console depending on the roll

    >>> generate_park_message_to_print(1)
    'Taking a deep breath of the fresh air in Stanley Park helps ease your anxiety as you walk.'

    >>> generate_park_message_to_print(6)
    'A stray cat approaches, meowing softly. You give it a gentle tummy rub, and it responds with happy purring. \
Seeing this carefree, adorable little creature revel in the simple joys of life inspires you to adopt a similar \
mentality.'
    """
    messages = {
        range(1, 5): 'Taking a deep breath of the fresh air in Stanley Park helps ease your anxiety as you walk.',
        range(5, 7): 'A stray cat approaches, meowing softly. You give it a gentle tummy rub, and it responds with '
                     'happy purring. Seeing this carefree, adorable little creature revel in the simple joys of life '
                     'inspires you to adopt a similar mentality.',
        range(7, 9): {'default': 'It seems there is a weekend flea market going on today at Stanley Park. Should you '
                                 'go check it out?\nEnter "1" to check out the flea market, "2" to continue walking.',
                      'enter flea': 'You decide to explore the flea market.',
                      'kool-aid': 'An eccentric old lady grabs you and pulls you to her stall, excitedly pitching her '
                                  '"Mega Brain Power Elixir" to you. She claims it can turn even the dumbest person '
                                  'into a genius. Despite your attempts to leave, she\'s persistent. Feeling cornered, '
                                  'you give in and buy a ridiculously expensive bottle of the mysterious liquid. '
                                  'You chug it down. Hmmmm... kinda tastes like Kool-Aid.',
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
    """
    Modifies character stats depending on user action at the flea market.

    :param character: a dictionary representing the player character
    :precondition: character must be a dictionary generated in this program
    :postcondition: correctly modifies character stats depending on user action at the flea market
    :return: a boolean representing whether the player entered the flea market
    """
    messages = generate_park_message_to_print(7)
    user_choice = binary_user_choice('flea market')
    if user_choice == '1':
        print(f'{messages["enter flea"]}')
        sleep(0.5)
        if character['wealth'] >= 60:
            print(f'\n{messages["kool-aid"]}')
            sleep(0.5)
            char.change_stat(character, 'wealth', -60)
            sleep(0.5)
            char.change_stat(character, 'IQ', 0.5)
        else:
            print(f'{messages["no kool-aid"]}')
            sleep(0.5)
            stress_gain = random.randint(10, 15)
            sleep(0.5)
            char.change_stat(character, 'stress', stress_gain)
        return True
    else:
        print(f'{messages["leave flea"]}')
        return False
