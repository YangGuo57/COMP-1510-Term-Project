import character as char
from random import randint


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
    char.evaluate_exp(character, 'all')
    if char.evaluate_stress(character):
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

    char.change_stat(character, subject, exp_gain)
    char.change_stat(character, 'stress', randint(10, 15))


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
        char.change_stat(character, subject, experience_gained)
    char.change_stat(character, 'stress', randint(8, 12))


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
        char.change_stat(character, 'stress', randint(10, 15))
    else:
        stat_gain = 0
        stress_gain = randint(4, 7)

        if assessment == 'quiz':
            stat_gain = randint(6, 10) * character['IQ']
        elif assessment == 'assignment':
            stat_gain = randint(10, 14) * character['IQ']

        char.change_stat(character, subject, stat_gain)
        char.change_stat(character, subject, stress_gain)


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
    char.change_stat(character, 'stress', randint(-5, -1))


def club_event(character):
    """
    carries out club event
    """
    # stress_lost = randint(5, 8) * -1
    print('In the midst of overwhelming homework, the news of a socializing club event feels like a welcomed '
          'blessing. Naturally, you decide to join, finding solace among your peers as you all unwind and '
          'complain about your school life to each other. Laughter fills the air, and as the evening unfolds, '
          'it\'s as if the weight of your stress has been lifted, leaving you liberated and refreshed.')

    char.change_stat(character, 'stress', randint(-8, -5))
    char.change_stat(character, 'EQ', randint(1, 3))