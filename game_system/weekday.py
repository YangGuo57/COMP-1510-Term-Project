import random
from game_system import TOTAL_WEEKS, SUBJECTS, character as char, event_trigger as event, save
from time import sleep


def weekday(character: dict, week: int, school_map: dict) -> None:
    """
    Carries out weekday events including attending classes, weekly random event, and end of week office hours.

    :param character: character dictionary
    :param week: integer representing week number
    :param school_map: map dictionary
    :precondition: character must be a valid character dictionary created in this program
    :precondition: week must be a valid positive integer representing week number created in this program
    :precondition: school_map must be a valid map dictionary created in this program
    :postcondition: properly adjusts character's stats and location based on weekday events
    """
    exam = 'midterms' if week <= 7 else 'finals'
    exam_countdown = TOTAL_WEEKS - week - TOTAL_WEEKS // 2 if exam == "midterms" else TOTAL_WEEKS - week - 1
    end_of_term_countdown = TOTAL_WEEKS - week
    sleep(0.5)
    print(f'It is now week {week} of the term, only {end_of_term_countdown} weeks until end of term 1! The looming '
          f'presence of the {exam} reminds you that in {exam_countdown} weeks you will be at the mercy of these exams. '
          f'Here\'s to hoping for a productive week as you prepare to face  the challenges that lie ahead.')

    character['X'] = 1
    character['Y'] = 1
    print('You attend classes from Monday to Friday.')
    sleep(0.5)
    weekday_schoolwork(character)
    char.evaluate_exp(character, 'all')
    print()
    sleep(0.5)
    random_weekday_event(character)
    print()
    sleep(0.5)
    char.set_character_location(character, 'school')
    end_of_week_action(character, school_map)
    save.save_game(character, week, False)


def end_of_week_action(character: dict, school_map: dict) -> None:
    """
    Lets player choose to either move on the map to attend office hours or go home.

    :param character: character dictionary
    :param school_map: map dictionary
    :precondition: character must be a valid character dictionary created in this program
    :precondition: school_map must be a valid map dictionary created in this program
    :postcondition: properly adjusts character's stats and location based on user choice
    """
    print('At last, you made it through another week. It is Friday afternoon, and you find yourself at crossroads. '
          'All your instructors are available for questions during their office hours. If you have any pressing '
          'questions about your courses, now is the perfect time to seek answers. Yet, you\'re feeling pretty tired '
          'from all the hard work this week. Maybe it\'s a good idea to head home and get some rest instead?')
    sleep(0.5)
    subject = event.move_during_office_hours(character, school_map)
    if subject == 'back':
        go_home(character)
    else:
        office_hours(character, subject)


def go_home(character: dict) -> None:
    """
    Lets player go home and rest.

    :param character: character dictionary
    :precondition: character must be a valid character dictionary created in this program
    :postcondition: properly adjusts character's stats from going home

    >>> player = {'name': 'test', 'IQ': 1, 'EQ': 1, 'stress': 10, 'COMP1510': 1, 'COMP1536': 1, 'COMP1113': 1,
    'COMP1537': 1, 'X': 1, 'Y': 1}
    >>> go_home(player)
    You decide to call it a day and head home to get some rest.
    >>> player
    {'name': 'test', 'IQ': 1, 'EQ': 1, 'stress': 0, 'COMP1510': 1, 'COMP1536': 1, 'COMP1113': 1,
    'COMP1537': 1, 'X': 1, 'Y': 1}
    """
    print('You decide to call it a day and head home to get some rest.')
    sleep(0.5)
    stress_loss = random.randint(10, 15) * -1
    char.change_stat(character, 'stress', stress_loss)


def office_hours(character: dict, subject: str) -> None:
    """
    Changes player stats after attending office hours for a specific subject.

    :param character: character dictionary
    :param subject: string representing subject
    :precondition: character must be a valid character dictionary created in this program
    :precondition: subject must be a valid string representing a subject created in this program
    :postcondition: properly adjusts character's stats from attending office hours
    """
    epiphany = roll_epiphany()
    exp_gain = 0
    print_epiphany_office_hours(subject, epiphany)
    sleep(0.5)

    if epiphany:
        exp_gain += 100
    else:
        exp_gain += random.randint(15, 20) * character['IQ']

    char.change_stat(character, subject, exp_gain)
    sleep(0.5)
    char.change_stat(character, 'stress', random.randint(10, 15))


def roll_epiphany():
    """
    Rolls for an epiphany during office hours at 20% chance.

    :return: a boolean representing whether an epiphany occurred
    """
    return False if random.randint(0, 4) else True


def print_epiphany_office_hours(subject: str, epiphany: bool) -> None:
    """
    Prints flavour text to console depending on whether player has an epiphany during office hours.

    :param subject: string representing subject
    :param epiphany: boolean representing whether an epiphany occurred
    :precondition: subject must be a valid string representing a subject created in this program
    :postcondition: prints the appropriate flavour text to console

    >>> print_epiphany_office_hours('1510', True)
    Your COMP1510 instructor graciously imparts their wisdom on you. You absorb all this wisdom like a sponge.

    >>> print_epiphany_office_hours('1510', False)
    Your COMP1510 instructor graciously imparts their wisdom on you, but Alas, your brain struggles to absorb all \
this wisdom.
    """
    if epiphany:
        print(f'Your COMP{subject} instructor graciously imparts their wisdom on you. You absorb all this wisdom like '
              f'a sponge.')
    else:
        print(f'Your COMP{subject} instructor graciously imparts their wisdom on you, but Alas, your brain struggles '
              f'to absorb all this wisdom.')


def weekday_schoolwork(character: dict) -> None:
    """
    Increases experience in all school subjects.

    :param character: character dictionary
    :precondition: character must be a valid character dictionary created in this program
    :postcondition: properly adjusts character's stats from doing schoolwork
    """
    for subject in SUBJECTS:
        experience_gained = character['IQ'] * random.randint(15, 20)
        char.change_stat(character, subject, experience_gained)
    sleep(0.5)
    char.change_stat(character, 'stress', random.randint(5, 10))


def random_weekday_event(character: dict) -> None:
    """
    Generates a random weekday event at 25% chance each.

    :param character: character dictionary
    :precondition: character must be a valid character dictionary created in this program
    :postcondition: properly adjusts character's stats from the generated random weekday event
    """
    roll = random.randint(1, 4)
    subject = roll_subject()
    fail = True if random.randint(0, 1) else False

    if roll == 1:
        club_event(character)
    elif roll == 2:
        trauma_bond(character)
    elif roll == 3:
        print_assessment_results(fail, subject, 'quiz')
        sleep(0.5)
        assessment_stat_change(character, fail, subject, 'quiz')
    else:
        print_assessment_results(fail, subject, 'assignment')
        sleep(0.5)
        assessment_stat_change(character, fail, subject, 'assignment')


def assessment_stat_change(character: dict, fail: bool, subject: str, assessment: str) -> None:
    """
    Changes character's stats based on whether character passed or failed the assessment.

    :param character: character dictionary
    :param fail: boolean representing whether character failed the assessment
    :param subject: string representing subject
    :param assessment: string representing assessment type
    :precondition: character must be a valid character dictionary created in this program
    :precondition: subject must be a valid string representing a subject created in this program
    :precondition: assessment must be a valid string representing an assessment type created in this program
    :postcondition: properly adjusts character's stats from the conditions of the assessment
    """
    if fail:
        stress_gain = random.randint(8, 12)
        print(stress_gain)
        char.change_stat(character, 'stress', stress_gain)
    else:
        stat_gain = 0
        stress_gain = random.randint(4, 7)

        if assessment == 'quiz':
            stat_gain = random.randint(15, 20) * character['IQ']
        elif assessment == 'assignment':
            stat_gain = random.randint(25, 30) * character['IQ']

        char.change_stat(character, subject, stat_gain)
        sleep(0.5)
        char.change_stat(character, 'stress', stress_gain)


def print_assessment_results(fail: bool, subject: str, assessment: str) -> None:
    """
    Prints flavour text to screen to describe whether character has passed or failed the assessment.

    :param fail: boolean representing whether character failed the assessment
    :param subject: string representing subject
    :param assessment: string representing assessment type
    :precondition: subject must be a valid string representing a subject created in this program
    :precondition: assessment must be a valid string representing an assessment type created in this program
    :postcondition: prints the appropriate flavour text to console

    >>> print_assessment_results(True, '1510', 'quiz')
    You completely bombed the COMP1510 quiz. Perhaps you should study harder.

    >>> print_assessment_results(False, '1510', 'quiz')
    Hurrah! You aced the COMP1510 quiz. All those tearful all-nighters were not for naught.
    """
    if not fail:
        print(f'Hurrah! You aced the COMP{subject} {assessment}. All those tearful all-nighters were not for naught!')
    else:
        print(f'You completely bombed the COMP{subject} {assessment}. Perhaps you should study harder.')


def roll_subject() -> str:
    """
    Rolls one subject out of four subjects at 25% chance.

    :return: a string representing the subject rolled
    """
    roll = random.randint(0, 3)
    return SUBJECTS[roll]


def trauma_bond(character: dict) -> None:
    """
    Carries out trauma bond event with classmates.

    :param character: character dictionary
    :precondition: character must be a valid character dictionary created in this program
    :postcondition: properly adjusts character's stats from the trauma bond event
    """
    print('After a week of endless schoolwork, you and your classmates find yourselves rendered speechless by the '
          'ordeal. You complain about the challenges of school life to each other. The venting '
          'provides a temporary peace of mind; just try not to think about your deadlines!')
    sleep(0.5)
    char.change_stat(character, 'stress', random.randint(-15, -10))


def club_event(character: dict) -> None:
    """
    Carries out club event with classmates.

    :param character: character dictionary
    :precondition: character must be a valid character dictionary created in this program
    :postcondition: properly adjusts character's stats from the club event
    """
    print('In the midst of overwhelming homework, the news of a socializing club event feels like a welcomed '
          'blessing. Naturally, you decide to join, finding solace among your peers as you all unwind and '
          'complain about your school life to each other. Laughter fills the air, and as the evening unfolds, '
          'it\'s as if the weight of your stress has been lifted, leaving you liberated and refreshed.')
    sleep(0.5)
    char.change_stat(character, 'stress', random.randint(-15, -10))
    char.change_stat(character, 'EQ', random.randint(1, 3))
