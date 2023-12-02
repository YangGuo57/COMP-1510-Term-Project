from helper_functions import SUBJECTS, PRODUCTIVE_STATS, coop_interview_questions, initial_game_questions
from time import sleep


def create_character(answers):
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
    print("Your current attributes: ")
    print("\tIQ:", character['IQ'])
    print("\tEQ:", character['EQ'])
    print("\tstress:", character['stress'])
    print("\twealth:", character['wealth'])
    print("\texperience in each course:")
    for subject, exp in character['exp'].items():
        print(f'\t\tCOMP{subject}: {exp}')
    # print("exp:", character['exp'])
    print("\tlevel in each course:")
    for subject, lvl in character['lvl'].items():
        print(f'\t\tCOMP{subject}: {lvl}')
    print("\tpersonal project progress:", character['project'])
    if 'job' in character and character['job']:
        print('\temployed: True')
    print()


def evaluate_exp(character, subject):
    """
    evaluates whether character has enough exp in a subject to level up
    if subject == all, loop through all subjects
    else, only evaluate that one subject passed in
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
    prints to console stress warnings
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
    stress_multiplier = 1
    if character['stress'] > 100:
        stress_multiplier -= 1
    elif character['stress'] > 85:
        stress_multiplier -= 0.6
    elif character['stress'] > 70:
        stress_multiplier -= 0.3
    return stress_multiplier


def change_stat(character, attribute, amount):
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
    describes how much exp is gained in an attribute
    """
    print(f'Through hardwork and perseverance, you became more knowledgeable about COMP{attribute}. Your experience in '
          f'COMP{attribute} increased by {amount}.')
    print(f'Your experience in COMP{attribute} is now {character["exp"][attribute]}.')


def describe_flat_stat_gain(character, attribute, amount):
    """
    describes how an attribute that is not exp related has changed (EQ, IQ, project)
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
    describes how much stress is gained/lost
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
    character['location'] = location


def describe_wealth_change(character, amount):
    if amount < 0:
        print('You watch your savings deplete as you tell yourself, "money is meant to be spent...right? RIGHT?"')
        print(f'Your wealth decreases by {amount * -1}. \nYour bank account balance is now {character["wealth"]}.')
    else:
        print('Earning money puts a smile on your face, who doesn\'t love money?')
        print(f'Your wealth increases by {amount}.Your bank account balance is now {character["wealth"]}.')
