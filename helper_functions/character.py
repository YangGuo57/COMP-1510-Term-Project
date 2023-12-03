from helper_functions import SUBJECTS, PRODUCTIVE_STATS, coop_interview_questions, initial_game_questions
from time import sleep


def create_character(answers):
    """
    Create a new character with the given answers to the questionnaire.

    :param answers: a list of integers
    :precondition: answers must be a list of integers representing the answers to the questionnaire
    :postcondition: creates a new character with the given answers
    :return: a dictionary representing the new character

    >>> results = [0, 1, 0, 1]
    >>> create_character(results)
    {'IQ': 1.0, 'EQ': 10, 'stress': 0, 'wealth': 40, 'X': 1, 'Y': 1, 'project': 0, 'exp': {'1510': \
0, '1537': 0, '1113': 0, '1712': 0}, 'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0}, 'midterm': \
{'1510': None, '1537': None, '1113': None, '1712': None}, 'final': {'1510': None, '1537': None, '1113': \
None, '1712': None}, 'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0, \
'1510': 0, '1537': 0, '1712': 0, '1113': 0}, 'location': 'home', 'vaccinated': False, 'skip_job': 0}
    """
    new_character = {'IQ': 0, 'EQ': 0, 'stress': 0, 'wealth': 0, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'midterm': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'final': {'1510': None, '1537': None, '1113': None, '1712': None},
                     'visited_locations': {'home': 1, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0, "1510": 0,
                                           "1537": 0, "1712": 0, "1113": 0},
                     'location': 'home', 'vaccinated': False, 'skip_job': 0}

    questionnaire_stats = (({'IQ': 1.0}, {'IQ': 0.5, 'EQ': 5}), ({'wealth': 40}, {'wealth': 20, 'EQ': 5}),
                           ({'EQ': 5}, {'wealth': 20}), ({'IQ': 0.5}, {'wealth': 20}))

    questionnaire_index = 0
    for answer in answers:
        stats = questionnaire_stats[questionnaire_index][answer]
        for stat in stats:
            new_character[stat] += stats[stat]
        questionnaire_index += 1

    return new_character


def ask_questionnaire(setting):
    """
    Asks the player a series of questions to determine player attributes.

    :param setting: a string
    :precondition: setting must be a string representing the setting of the game
    :postcondition: asks the player a series of questions to determine player attributes
    :return: a list of integers representing the player's answers to the questionnaire
    """
    answers = []
    questions = coop_interview_questions() if setting == 'coop' else initial_game_questions()

    print('Choose one of the two options that best describes you, and enter the NUMBER representing that option.')
    sleep(0.5)
    for question in questions:
        answer = input(question)
        while answer != '1' and answer != '2':
            print('That is not a valid entry. Enter the NUMBER representing the option that best describes you.')
            sleep(0.5)
            answer = input(question)
        answers.append(int(answer) - 1)

    sleep(0.5)
    return answers


def print_stats(character):
    """
    Print the character's attributes

    :param character: a dictionary
    :precondition: character must be a dictionary storing the character's attributes
    :postcondition: print the character's attributes

    >>> player = {
    ... 'IQ': 0, 'EQ': 0, 'stress': 0, 'wealth': 0, 'project': 0,
    ... 'exp': {'1712': 0, '1510': 0},
    ... 'lvl': {'1510': 0, '1537': 0},
    ... 'job': True}
    >>> print_stats(player)
    Your current attributes:
        IQ: 0
        EQ: 0
        stress: 0
        wealth: 0
        experience in each course:
            COMP1712: 0
            COMP1510: 0
        level in each course:
            COMP1510: 0
            COMP1537: 0
        personal project progress: 0
        employed: True
    <BLANKLINE>
    """
    print("Your current attributes:")
    print("    IQ:", character['IQ'])
    print("    EQ:", character['EQ'])
    print("    stress:", character['stress'])
    print("    wealth:", character['wealth'])
    print("    experience in each course:")
    for subject, exp in character['exp'].items():
        print(f'        COMP{subject}: {exp}')
    # print("exp:", character['exp'])
    print("    level in each course:")
    for subject, lvl in character['lvl'].items():
        print(f'        COMP{subject}: {lvl}')
    print("    personal project progress:", character['project'])
    if 'job' in character and character['job']:
        print('    employed: True')
    print()


def evaluate_exp(character, subject):
    """
    Evaluate the character's experience points and level up if the character has enough experience.

    :param character: a dictionary
    :param subject: a string
    :precondition: character must be a dictionary storing the character's attributes
    :precondition: subject must be a string representing the subject the character is studying
    :postcondition: evaluate the character's experience points and level up if the character has enough experience

    >>> player = {'exp': {'1510': 200},'lvl': {'1510': 1}}
    >>> course = '1510'
    >>> evaluate_exp(player, course)
    Eureka, an epiphany strikes you! All the puzzle pieces fall into place and you've deepened your understanding of \
COMP1510.
    Your COMP1510 level increased by 1. It is now level 2.
    """
    threshold = 100

    if subject == 'all':
        subject = SUBJECTS
    else:
        subject = subject,
        subject = tuple(subject)

    for each_subject in subject:
        level_threshold = (character['lvl'][each_subject] + 1) * threshold
        if character['exp'][each_subject] >= level_threshold:
            character['lvl'][each_subject] += 1
            print(f'Eureka, an epiphany strikes you! All the puzzle pieces fall into place and you\'ve deepened your '
                  f'understanding of COMP{each_subject}.')
            print(f'Your COMP{each_subject} level increased by 1. It is now level {character["lvl"][each_subject]}.')


def describe_stress(character):
    """
    Describe the character's stress level.

    :param character: a dictionary
    :precondition: character must be a dictionary storing the character's attributes
    :postcondition: print a description of the character's stress level

    >>> player = {'stress': 101}
    >>> describe_stress(player)
    <BLANKLINE>
    ERROR 4044444444 HAHAHAHAHAHAHA YOUR BRAIN IS FAILING? ?!!? WHAT IS THE MEANING OF LIFE SKADLKNLKNES98723894*&\
(*&#$<N<MSDV(@#U)0SFLKNA@$_)*LKANSLKNF
    <BLANKLINE>
    >>> player = {'stress': 90}
    >>> describe_stress(player)
    <BLANKLINE>
    You feel like you no longer have a FUnctionING BRAIn... MAYBE yoU should get some ReST?@@
    <BLANKLINE>
    """
    if character['stress'] > 100:
        print('\nERROR 4044444444 HAHAHAHAHAHAHA YOUR BRAIN IS FAILING? ?!!? WHAT IS THE MEANING OF LIFE '
              'SKADLKNLKNES98723894*&(*&#$<N<MSDV(@#U)0SFLKNA@$_)*LKANSLKNF\n')
    elif character['stress'] > 85:
        print('\nYou feel like you no longer have a FUnctionING BRAIn... MAYBE yoU should get some ReST?@@\n')
    elif character['stress'] > 70:
        print('\nYou feel like like your brain is no longer registering what you\'re reading... Maybe you should take '
              'it easy?\n')


def determine_stress_multiplier(character):
    """
    Determine the stress multiplier based on the character's stress level.

    :param character: a dictionary
    :precondition: character must be a dictionary storing the character's attributes
    :postcondition: calculate the stress multiplier based on the character's stress level
    :return: a float representing the stress multiplier

    >>> player = {'stress': 100}
    >>> determine_stress_multiplier(player)
    0.4
    >>> player = {'stress': 70}
    >>> determine_stress_multiplier(player)
    1
    """
    stress_multiplier = 1
    if character['stress'] > 100:
        stress_multiplier -= 1
    elif character['stress'] > 85:
        stress_multiplier -= 0.6
    elif character['stress'] > 70:
        stress_multiplier -= 0.3
    return stress_multiplier


def change_stat(character, attribute, amount):
    """
    Change the value of a character's attribute by a given amount.

    :param character: a dictionary
    :param attribute: a string
    :param amount: an integer
    :precondition: character must be a dictionary storing the character's attributes
    :precondition: attribute must be a string
    :precondition: amount must be an integer
    :postcondition: change the value of the character's attribute by the given amount

    >>> player = {'IQ': 0, 'EQ': 0, 'stress': 0, 'wealth': 0, 'project': 0, 'exp': \
{'1510': 0, '1537': 0, '1113': 0, '1712': 0}}
    >>> change_stat(player, 'IQ', 10)
    Whoa, it's as if your brain is waking up from a century-long slumber. You've never \
felt this intelligent before in your entire life.
    Your IQ increases by 10. It is now 10.
    """
    if attribute in PRODUCTIVE_STATS:
        amount *= determine_stress_multiplier(character)
        amount = int(amount)

    if attribute in SUBJECTS:
        character['exp'][attribute] += amount
        describe_exp_gain(character, attribute, amount)
        evaluate_exp(character, attribute)
    elif attribute == 'stress':
        if character[attribute] + amount < 0:
            character[attribute] = 0
        else:
            character[attribute] += amount
        describe_stress_change(character, amount)
        describe_stress(character)
    elif attribute == 'wealth':
        character[attribute] += amount
        describe_wealth_change(character, amount)
    else:
        if character[attribute] + amount < 0:
            character[attribute] = 0
        else:
            character[attribute] += amount
        describe_flat_stat_gain(character, attribute, amount)


def describe_exp_gain(character, attribute, amount):
    """
    Describe the experience gain of the character.

    :param character: a dictionary
    :param attribute: a string
    :param amount: an integer
    :precondition: character must be a dictionary storing the character's attributes
    :precondition: attribute must be a string
    :precondition: amount must be an integer
    :postcondition: describe the experience gain of the character

    >>> player = {'exp': {'1510': 10, '1537': 0, '1113': 0, '1712': 0}}
    >>> describe_exp_gain(player, '1510', 10)
    Through hardwork and perseverance, you became more knowledgeable about COMP1510. Your experience in COMP1510 \
increased by 10.
    Your experience in COMP1510 is now 10.
    """

    print(f'Through hardwork and perseverance, you became more knowledgeable about COMP{attribute}. Your experience in '
          f'COMP{attribute} increased by {amount}.')
    print(f'Your experience in COMP{attribute} is now {character["exp"][attribute]}.')


def describe_flat_stat_gain(character, attribute, amount):
    """
    Describe the flat stat gain of the character.

    :param character: a dictionary
    :param attribute: a string
    :param amount: an integer
    :precondition: character must be a dictionary storing the character's attributes
    :precondition: attribute must be a string
    :precondition: amount must be an integer
    :postcondition: describe the flat stat gain of the character

    >>> player = {'EQ': 2, 'IQ': 0, 'project': 0}
    >>> describe_flat_stat_gain(player, 'EQ', 1)
    Through meaningful human interactions, you become more emotionally savvy. You feel more confident talking to \
humans now.
    Your EQ increases by 1. It is now 2.
    """
    changes = 'increases'
    if attribute == 'EQ':
        if amount > 0:
            print('Through meaningful human interactions, you become more emotionally savvy. You feel more confident '
                  'talking to humans now.')
        else:
            print('Clearly you are not very good at handling human interactions, nor are you a responsible person.'
                  'Perhaps you should work on them if you want to get hired in the future...')
            changes = 'decreases'
            amount *= -1
    elif attribute == 'IQ':
        print('Whoa, it\'s as if your brain is waking up from a century-long slumber. You\'ve never felt this '
              'intelligent before in your entire life.')
    elif attribute == 'project':
        print('You start grinding your personal project. You\'re not really sure what you\'re doing... If your coding '
              'instructor saw your spaghetti code, he would have a heart attack. Thankfully, your GitHub repo is '
              'private for now so no one can see the heinous code you\'ve written.')

    print(f'Your {attribute} {changes} by {amount}. It is now {character[attribute]}.')


def describe_stress_change(character, amount):
    """
    Describe the change in stress level of the character.

    :param character: a dictionary
    :param amount: an integer
    :precondition: character must be a dictionary containing the key "stress" with an integer value
    :precondition: amount must be an integer
    :postcondition: prints a message describing the change in stress level of the character

    >>> player = {"stress": 1}
    >>> describe_stress_change(player, 1)
    The stress of life and schoolwork is getting to you as you start to feel a bit more tired. Remember to get some \
rest regularly so you don't burn out!
    Your stress increases by 1
    Your stress level is now 1.

    >>> player = {"stress": 0}
    >>> describe_stress_change(player, -1)
    You feel rejuvenated as if a great load has been taken off your shoulders.
    Your stress decreases by 1
    Your stress level is now 0.
    """
    if amount > 0:
        print(f'The stress of life and schoolwork is getting to you as you start to feel a bit more tired. Remember to '
              f'get some rest regularly so you don\'t burn out!')
        print(f'Your stress increases by {amount}')
    else:
        print(f'You feel rejuvenated as if a great load has been taken off your shoulders.')
        print(f'Your stress decreases by {amount * -1}')
    print(f'Your stress level is now {character["stress"]}.')


def set_character_location(character, location):
    """
    Sets the character's location to the given location.

    :param character: a dictionary
    :param location: a string
    :precondition: character must be a dictionary with a 'location' key
    :precondition: location must be a string
    :postcondition: character's location is set to the given location

    >>> player = {'location': 'home'}
    >>> set_character_location(player, 'hospital')
    >>> player['location']
    'hospital'
    """
    character['location'] = location


def describe_wealth_change(character, amount):
    """
    Update character's wealth by the specified amount and print a description of the change.

    :param character: a dictionary
    :param amount: an integer
    :precondition: character must be a dictionary with a key "wealth" that contains an integer value
    :precondition: amount must be an integer
    :postcondition: updates character's wealth by the specified amount

    >>> player = {"wealth": 100}
    >>> describe_wealth_change(player, 50)
    Earning money puts a smile on your face, who doesn't love money?
    Your wealth increases by 50.Your bank account balance is now 100.

    >>> player = {'wealth': 100}
    >>> describe_wealth_change(player, -50)
    You watch your savings deplete as you tell yourself, "money is meant to be spent...right? RIGHT?"
    Your wealth decreases by 50.
    Your bank account balance is now 100.
    """
    if amount < 0:
        print('You watch your savings deplete as you tell yourself, "money is meant to be spent...right? RIGHT?"')
        print(f'Your wealth decreases by {amount * -1}.\nYour bank account balance is now {character["wealth"]}.')
    else:
        print('Earning money puts a smile on your face, who doesn\'t love money?')
        print(f'Your wealth increases by {amount}.Your bank account balance is now {character["wealth"]}.')
