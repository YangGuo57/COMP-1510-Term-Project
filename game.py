import time
from random import randint

from map_functions import make_board, generate_game_map, print_map
from character_functions import validate_move, get_user_choice, move_character, update_visited_location


def create_character(answers):
    new_character = {'IQ': 0, 'EQ': 0, 'stress': 0, 'wealth': 0, 'X': 1, 'Y': 1, 'project': 0,
                     'exp': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'lvl': {'1510': 0, '1537': 0, '1113': 0, '1712': 0},
                     'visited_locations': {'school': 0, 'hospital': 0, 'park': 0, 'work': 0, }}

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
        elif input_status.lower() == 'menu':
            main_menu(character)
        else:
            print("Invalid input. Please type 'status' to see your current attributes.")
            continue


def print_message(message):
    print(message)


def greeting():
    greeting_dict = {
        1: "Welcome to Survive CST. Please take a moment to answer the following questionnaire. There is no right"
           " or wrong answer.",
        2: "It is the first week of September, your first time in the City of Vancouver, and your first day studying. "
           "Computer Systems Technology (CST) at BCIT. You enter the school elevator with mixed feelings; after all, "
           "you came to this foreign city in hopes that computer science is the right career for you. As you step out "
           "of the elevator, you tell yourself: Don't stress, learn lots, make friends, get co-op, and most "
           "importantly, have fun!",
        3: "",
    }

    return greeting_dict


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


def map_action(character):
    rows = 10
    columns = 18
    board = make_board(rows, columns)
    game_map = generate_game_map(board)

    while True:
        print_map(game_map, rows, columns, character)
        direction = get_user_choice()
        if direction == "Back to Menu":
            main_menu(character)
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction, rows, columns, game_map)
            update_visited_location(character)
        else:
            print("Invalid move! Please choose another direction.")


def fast_travel(character):
    location_door = {
        "school": [(3, 3), (3, 5)],
        "hospital": [(5, 7), (5, 9)],
        "park": [(2, 12), (2, 14)],
        "work": [(7, 2), (7, 4)]
    }

    destination = input("Please input fast travel destination: school, hospital, park, work:")
    if destination.lower() in location_door:
        visited = character['visited_locations'][destination]
        if visited:
            character['X'], character['Y'] = location_door[destination][1]
            print(f"You've fast traveled to {destination}!")
            map_action(character)
        else:
            print(f"You need to visit {destination} at least once before fast traveling there.")
            main_menu(character)
    else:
        print("Invalid destination.")
        main_menu(character)


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


def run_weekday(character, week):
    """
    print weekday prompt to screen (eg. It is now week 5, only 2 more weeks until midterms...)
    increase exp in all subjects
    increase stress
    evaluate_exp()
    evaluate_stress()
    generate random event
    """
    exam = 'midterms' if week < 7 else 'finals'
    print(f'It is now week {week} of the term. The looming presence of the {exam} reminds you that in {7 - week} weeks '
          f'you will be at the mercy of these exams. Here\'s to hoping for a productive week as you prepare to face '
          f'the challenges that lie ahead.')
    weekday_schoolwork(character)
    evaluate_exp(character, 'all')
    if evaluate_stress(character):
        # call ER function
        pass
    random_weekday_event(character)
    end_of_week_action(character)


def end_of_week_action(character):
    print('At last, you made it through another week. It is Friday afternoon, and you find yourself at crossroads. '
          'All your instructors are available for questions during their office hours. If you have any pressing '
          'questions about your courses, now is the perfect time to seek answers. Yet, you\'re feeling pretty tired '
          'from all the hard work this week. Maybe it\'s a good idea to head home and get some rest instead?')
    choice = False
    while not choice:
        # ask player for directions
        # validate direction
        # move character
        # check location to see if character has reached a classroom or is going home
        # ask player to confirm action
        # if player denies action, repeat while loop
        # if player confirms action, carry out action depending on location of character
        # office_hours(character, subject) if player goes to office hours
        # home_rest(character) if player goes home
        break
    pass


def home_rest(character):
    """
    Decreases character's stress by resting at home
    """
    print(f'It\'s been a long week. You decide to call it a day and head home to get some rest.')
    change_stat(character, 'stress', randint(-20, -15))


def office_hours(character, subject):
    """
    carries out office hours
    """
    epiphany = roll_epiphany()
    exp_gain = 0
    print_epiphany_office_hours(subject, epiphany)

    if epiphany:
        exp_gain += 100
    else:
        exp_gain += randint(10, 15) * character['IQ']

    change_stat(character, subject, exp_gain)
    change_stat(character, 'stress', randint(10, 15))


def roll_epiphany():
    """
    rolls for an epiphany during office hours at 20% chance
    """
    return False if randint(0, 4) else True


def print_epiphany_office_hours(subject, epiphany):
    """
    prints flavour text depending on whether player has an epiphany during office hours
    """
    if epiphany:
        print(f'Your COMP{subject} instructor graciously imparts their wisdom on you. You absorb all this wisdom like '
              f'a sponge.')
    else:
        print(f'Your COMP{subject} instructor graciously imparts their wisdom on you, but Alas, your brain struggles '
              f'to absorb all this wisdom.')


def weekday_schoolwork(character):
    """
    adds exp to all subjects
    adds stress
    calls other functions to print stat changes
    """
    subjects = ('1510', '1537', '1113', '1712')
    for subject in subjects:
        experience_gained = character['IQ'] * randint(8, 12)
        change_stat(character, subject, experience_gained)
    change_stat(character, 'stress', randint(8, 12))


def change_stat(character, attribute, amount):
    subjects = ('1510', '1537', '1712', '1113')
    if attribute in subjects:
        character['exp'][attribute] += amount
        describe_exp_gain(character, attribute, amount)
        evaluate_exp(character, attribute)
    elif attribute == 'stress':
        character[attribute] += amount
        describe_stress_change(character, amount)
        evaluate_stress(character)
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
    if attribute == 'EQ':
        print(f'Through meaningful human interactions, you unlock the power to navigate relationships with empathy '
              f'and resilience. You feel more confident talking to humans now.')
    elif attribute == 'IQ':
        pass
    elif attribute == 'project':
        pass

    print(f'Your {attribute} increased by {amount}. It is now {character[attribute]}')


def describe_stress_change(character, amount):
    """
    describes how much stress is gained/lost
    """
    if amount > 0:
        print(f'The stress of life and schoolwork is getting to you as you start to feel a bit more tired. Remember to '
              f'get some rest regularly so you don\'t burn out!')
        print(f'Your stress increased by {amount}')
    else:
        print(f'You feel rejuvenated as if a great load has been taken off your shoulders.')
        print(f'Your stress decreased by {amount * -1}')
    print(f'Your stress level is now {character["stress"]}.')


def random_weekday_event(character):
    """
    hackathon (most rare), quiz, club event, assignment, trauma bond
    evaluate_exp()
    evaluate_stress()
    """
    roll = randint(1, 4)
    subject = roll_subject()
    fail = fail_assessment()

    if roll == 1:
        club_event(character)
    elif roll == 2:
        trauma_bond(character)
    elif roll == 3:
        print_assessment_results(fail, subject, 'quiz')
        assessment_stat_change(character, fail, subject, 'quiz')
    else:
        print_assessment_results(fail, subject, 'assignment')
        assessment_stat_change(character, fail, subject, 'assignment')


def assessment_stat_change(character, fail, subject, assessment):
    """
    changes character's stats based on whether character passed or failed the assessment
    """
    if fail:
        change_stat(character, 'stress', randint(10, 15))
    else:
        stat_gain = 0
        stress_gain = randint(4, 7)

        if assessment == 'quiz':
            stat_gain = randint(6, 10) * character['IQ']
        elif assessment == 'assignment':
            stat_gain = randint(10, 14) * character['IQ']

        change_stat(character, subject, stat_gain)
        change_stat(character, subject, stress_gain)


def fail_assessment():
    """
    decides whether character passes or fails the assessment randomly at 50% chance
    """
    return True if randint(0, 1) else False


def print_assessment_results(fail, subject, assessment):
    """
    prints flavour text to screen, describing whether character has passed or failed the assessment
    """
    if not fail:
        print(f'Hurrah! You aced the COMP{subject} {assessment}. All those tearful all-nighters were not for naught!')
    else:
        print(f'You completely bombed the COMP{subject} {assessment}. Perhaps you should study harder.')


def roll_subject():
    """
    randomly rolls one subject out of four subjects at 25% chance
    """
    roll = randint(0, 3)
    subjects = ('1510', '1537', '1113', '1712')
    return subjects[roll]


def trauma_bond(character):
    """
    carries out trauma bond with classmates
    """
    print('After a week of endless schoolwork, you and your classmates find yourselves rendered speechless by the '
          'ordeal. Seeking comfort, you complain about the challenges of school life to each other. The venting '
          'provides a temporary peace of mind, as if lifting a burden from your shoulders. However, upon returning '
          'home, the harsh reality of the remaining workload hits you once more. The weight of unfinished tasks '
          'looms over you, and the night ends with tears as you drift off to sleep.')
    change_stat(character, 'stress', randint(-5, -1))


def club_event(character):
    """
    carries out club event
    """
    # stress_lost = randint(5, 8) * -1
    print('In the midst of overwhelming homework, the news of a socializing club event feels like a welcomed '
          'blessing. Naturally, you decide to join, finding solace among your peers as you all unwind and '
          'complain about your school life to each other. Laughter fills the air, and as the evening unfolds, '
          'it\'s as if the weight of your stress has been lifted, leaving you liberated and refreshed.')

    change_stat(character, 'stress', randint(-8, -5))
    change_stat(character, 'EQ', randint(1, 3))


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


def main_menu(character):
    while True:
        print("1. Move")
        print("2. Check Status")
        print("3. Fast Travel")
        print("4. Exit")

        choice = input("Please choose an option: ")
        if choice == '1':
            map_action(character)
        elif choice == '2':
            print_stats(character)
        elif choice == '3':
            fast_travel(character)
        elif choice == '4':
            print("Exiting the game...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
        return choice


def game():
    greeting_msg = greeting()
    print_message(greeting_msg[1])
    answer = ask_questionnaire()
    player = create_character(answer)
    print_message(greeting_msg[2])
    while True:
        action = main_menu(player)
        if action == 'move':
            map_action(player)
        elif action == 'Check Status':
            print_stats(player)
        elif action == 'Fast Travel':
            fast_travel(player)
        else:
            break
    run_weekday(player, 1)
    run_weekday(player, 2)


if __name__ == '__main__':
    game()
