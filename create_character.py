import menu as me


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
    new_character = {'IQ': 0, 'EQ': 0, 'stress': 0, 'wealth': 0, 'X': 2, 'Y': 3, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'visited_locations': {'home': 0, 'school': 0, 'hospital': 0, 'park': 0, 'work': 0, }}

    questionnaire_stats = (({'IQ': 1.0}, {'IQ': 0.5, 'EQ': 1}), ({'wealth': 40}, {'wealth': 20, 'EQ': 1}),
                           ({'EQ': 1}, {'wealth': 20}), ({'IQ': 0.5}, {'wealth': 20}))

    questionnaire_index = 0
    for answer in answers:
        stats = questionnaire_stats[questionnaire_index][answer]
        for stat in stats:
            new_character[stat] += stats[stat]
        questionnaire_index += 1

    return new_character


def print_stats(new_character):
    character = new_character
    while True:
        input_status = input("Please type 'status' to see your current stats (type 'menu' back to main):")
        if input_status.lower() == 'status':
            print("Your current attributes: ")
            print("IQ:", character['IQ'])
            print("EQ:", character['EQ'])
            print("stress:", character['stress'])
            print("wealth:", character['wealth'])
            print("exp:", character['exp'])
            print("lvl:", character['lvl'])
            print(character['visited_locations'])

        elif input_status.lower() == 'menu':
            me.main_menu(character)
        else:
            print("Invalid input. Please type 'status' to see your current attributes.")
            continue
