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


def create_character(answers):
    new_character = {'IQ': 0, 'EQ': 0, 'stress': 0, 'wealth': 0, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'visited_locations': {'home': 0, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0, "1510": 0,
                                           "1537": 0,
                                           "1712": 0,
                                           "1113": 0},
                     'location': 'home', 'job': False, 'vaccinated': False, 'skip_job': 0}

    questionnaire_stats = (({'IQ': 1.0}, {'IQ': 0.5, 'EQ': 1}), ({'wealth': 40}, {'wealth': 20, 'EQ': 1}),
                           ({'EQ': 1}, {'wealth': 20}), ({'IQ': 0.5}, {'wealth': 20}))

    questionnaire_index = 0
    for answer in answers:
        stats = questionnaire_stats[questionnaire_index][answer]
        for stat in stats:
            new_character[stat] += stats[stat]
        questionnaire_index += 1

    return new_character


def print_stats(character):
    print("Your current attributes: ")
    print("IQ:", character['IQ'])
    print("EQ:", character['EQ'])
    print("stress:", character['stress'])
    print("wealth:", character['wealth'])
    print("exp:", character['exp'])
    print("lvl:", character['lvl'])


def menu_print_stats(character):
    while True:
        input_status = input("Please type 'status' to see your current stats (type 'menu' back to main):")
        if input_status.lower() == 'status':
            print_stats(character)
        elif input_status.lower() == 'menu':
            break
        else:
            print("Invalid input. Please type 'status' to see your current attributes.")
            continue


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
        if character['exp'][each_subject] >= level_threshold:
            character['lvl'][each_subject] += 1
            print(f'Eureka, an epiphany strikes you! All the puzzle pieces fall into place and you\'ve deepened your '
                  f'understanding of COMP{each_subject}.')
            print(f'Your COMP{each_subject} level increased by 1. It is now level {character["lvl"][each_subject]}.')


def evaluate_stress(character):
    """
    evaluates whether character need to go to ER
    """
    if character['stress'] > 100:
        print('Suddenly the world is spinning and darkness befalls over your eyes... You succumbed to the pressure'
              'of life and you lay on the ground, unconscious. Thankfully, a passerby sees your motionless body and'
              'dials 911 for assistance.')
        return True
    elif character['stress'] > 90:
        print('You feel your heart palpitating and you can\'t breathe... Maybe you should get some rest?')
    elif character['stress'] > 80:
        print('You feel a sudden light-headedness... Maybe you should take it easy?')

    return False


def change_stat(character, attribute, amount):
    subjects = ('1510', '1537', '1712', '1113')
    if attribute in subjects:
        character['exp'][attribute] += amount
        describe_exp_gain(character, attribute, amount)
        evaluate_exp(character, attribute)
    elif attribute == 'stress':
        if character[attribute] + amount < 0:
            describe_stress_change(character, character[attribute])
            character[attribute] = 0
        else:
            character[attribute] += amount
            describe_stress_change(character, amount)
        evaluate_stress(character)
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
    describes how an attribute that is not exp related has changed (ie. EQ, IQ, project)
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
        print(f'Your wealth decreases by {amount * -1}. Your bank account balance is now {character["wealth"]}. \n'
              f'Maybe you should save up to pay for next term\'s tuition...')
    else:
        print('Earning money puts a smile on your face, who doesn\'t love money?')
        print(f'Your wealth increases by {amount}.Your bank account balance is now {character["wealth"]}.')
