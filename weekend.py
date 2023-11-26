from random import randint
import character as char
import event_trigger as event
import character as char


def run_weekend(character, main_map):
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
    character['X'] = 2
    character['Y'] = 3
    char.set_character_location(character, 'home')
    locations = event.trigger_description()
    job_attendance = False

    while actions > 0:
        if character['location'] == 'home':
            # trigger events at home
            user_choice = event.confirm_entry(character['location'])
            if user_choice == '1':
                execute_weekend_home_action(character)
            else:
                char.set_character_location(character, locations[character['location']][user_choice])
        if character['location'] == 'outside':
            # trigger events on big map
            user_choice = event.handle_map_event(character, main_map)
            if user_choice == '1':
                location = event.at_entrance(character)
                if location == 'park':
                    weekend_park(character)
                elif location == 'work':
                    weekend_job(character)
                elif location == 'hospital':
                    weekend_hospital(character)
                elif location == 'school':
                    weekend_school(character)
                elif location == 'home':
                    char.set_character_location(character, location)
                    execute_weekend_home_action(character)
        actions -= 1
    evaluate_job_attendance(character, job_attendance)


def execute_weekend_home_action(character):
    """
    do the action
    """
    choice = weekend_action_user_input(character)
    describe_weekend_home_action(choice)
    if choice == '1':
        weekend_schoolwork(character, get_user_choice_weekend_schoolwork())
    else:
        weekend_sleep(character)


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


def weekend_school(character):
    """
    generates random events at school on a weekend
    """
    print('The school is closed weekends. Why are you even here?')
    roll = randint(1, 2)
    stress_change = 0
    increase_in_EQ = 0
    print(roll)
    if roll == 1:
        print('You run into some classmates, who drag you along to a weekend party. How do they have so much free time '
              'on their hands?')
        stress_change += randint(5, 8) * -1
        increase_in_EQ += randint(1, 3) / 10
    else:
        print('You accidentally walk into a hobo because you did not pay attention to where you were going. The hobo '
              'thinks you\'re picking a fight with him, and starts yelling profanities at you. You tell him off, '
              'but the encounter leaves you feeling a bit shaken.')
        stress_change += randint(5, 8)
        increase_in_EQ += randint(3, 5) / 10
    char.change_stat(character, 'EQ', increase_in_EQ)
    char.change_stat(character, 'stress', stress_change)


def weekend_hospital(character):
    """
    weekend events at hospital
    """
    print('As you step inside Vancouver General Hospital, the scent of disinfectants greets you. Inside, '
          'it\'s serious with doctors and nurses bustling around, and you stand at the entrance feeling a bit lost. '
          'A nurse notices you and walks up to you.')
    if not character['vaccinated']:
        print('"You must be here for your annual vaccination," she says, "Now don\'t stand there and block the way, '
              'the lineup for getting your vaccine is this way."\n'
              'She grabs you by your arm and tries to lead you deeper into the hospital.')
        user_choice = input('Enter "1" to follow her, "2" to break free from her grasp.')
        while user_choice != '1' and user_choice != '2':
            print('That is not a valid option.')
            user_choice = input('Enter "1" to follow her, "2" to break free from her grasp.')
        if user_choice == '1':
            print('The nurse jabs you with a needle. Ouch. Surely this won\'t make you autistic right?')
            char.change_stat(character, 'IQ', 0.5)
            character['vaccinated'] = True
        else:
            print('You manage to slip away from the nurse\'s grasp and escape from the hospital.')
    else:
        print('"What are you doing here?" she says, "You\'re not sick and you already got your vaccination!'
              'Now don\'t stand there and block the way, go home."\n'
              'The nurse ushers you out of the hospital.')


def weekend_job(character):
    """
    work at part-time job
    attend_work = True
    """
    if character['job']:
        print('You begin your shift at the cafe. The aroma of freshly brewed coffee fills the air as you learn '
              'the ropes—taking orders, serving customers, and maybe even mastering the art of crafting the perfect '
              'cup. Even though this does not relate to what you learn in school, you begin to feel more confident '
              'navigating work relationships.')
        char.change_stat(character, 'wealth', 10)
        increase_in_EQ = randint(1, 3) / 10
        char.change_stat(character, 'EQ', increase_in_EQ)
    else:
        print('You arrive at a bustling cafe. You sit down and attempt to do some work, but the noisy environment'
              'is heavily distracting. You don\'t get anything done.')
    stress_gain = randint(5, 8)
    char.change_stat(character, 'stress', stress_gain)
    return True



def evaluate_job_attendance(character, skip):
    """
    keeps track of how many times player has skipped work
    if > 2 times, player is fired
    """
    if character['job'] and skip:
        character['skip_job'] += 1
        print('Uh oh, did you forget to go to work this weekend?')
        evaluate_firing_from_job(character)


def evaluate_firing_from_job(character):
    if character['skip_job'] >= 3:
        print('You receive an angry call from your manager, since you missed work too many times. Your manager fires '
              'you over the phone.')
        character['job'] = False
        char.change_stat(character, 'EQ', -2)


def weekend_park(character):
    """
    weekend events at park
    does player have a job? if not, generate job posting
    random_park_event() if character has not applied to a job posting
    """
    applied_to_job = False
    if not character['job']:
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
          f'breeze. Snatching it from the air, you realize it\'s a job posting - a local cafe is looking '
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
