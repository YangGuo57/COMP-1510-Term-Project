"""
This module contains the exam functions for the game.
"""

from random import randint, choice
from game_system import TOTAL_WEEKS, exam_status, SUBJECTS, character as char
from time import sleep


def take_coop_interview(character: dict) -> bool:
    """
    Determines if the character passes the coop interview

    :param character: a dictionary
    :precondition: character must be a dictionary storing the character's attributes
    :postcondition: determines if the character passes the coop interview
    :return: True if the character passes the coop interview, False otherwise
    """
    print('As you step into the interview room, you are greeted with a few pairs of eyes - wow, there are more than '
          'one person interviewing you! You introduce yourself as you nervously sit down in the lone empty chair in '
          'the room. Your interviewer clears his throat, and starts asking you some questions, how will you answer?')
    sleep(0.5)
    answer_key = ((0, 1), (0, 1), (1, 0), (1, 0))
    answers = char.ask_questionnaire('coop')
    score = 0

    for answer_index in range(len(answers)):
        score += answer_key[answer_index][answers[answer_index]]
    score *= character['EQ']

    threshold_to_pass = 4 * TOTAL_WEEKS + 17 * TOTAL_WEEKS / 2

    if (character['project'] + score) < threshold_to_pass:
        return False
    else:
        return True


def take_exam(character: dict, exam: str) -> bool:
    """
    Take the exam and evaluate the character's performance.

    :param character: a dictionary
    :param exam: a string
    :precondition: character must be a dictionary storing the character's attributes
    :precondition: exam must be a string representing the exam type
    :postcondition: evaluate the character's performance on the exam
    :return: True if the character passes the exam, False otherwise
    """
    print(f'Finally, the time has come: the much-anticipated {exam} exams are here. You look around you and all '
          f'you see are the blank stares of your sleep-deprived classmates who pulled consecutive all-nighters and are '
          f'living off of coffee. (God forbid the Tim Hortons downstairs closes for today...) You are no different '
          f'from them. If you are not yet ready to take the exam, that\'s too bad because the exam starts NOW.')
    sleep(0.5)
    statuses = exam_status()
    pass_or_fail = True

    for subject in SUBJECTS:
        print(f'The COMP{subject} exam is underway...')
        grade = evaluate_exam(character, subject, exam)
        sleep(0.5)
        print(choice(statuses[grade]))

        if grade == 'F':
            print(f'You failed COMP{subject}. Better luck next time.')
            pass_or_fail = False
        else:
            print(f'\nPhew, you passed and you got {"an" if grade == "A" else "a"} {grade} in COMP{subject}. Writing '
                  f'this {exam} was a learning experience in itself, and you feel relieved now that one more {exam} '
                  f'is over.\n')
            sleep(0.5)
            reward_character(character, subject)
            character[exam][subject] = grade
    sleep(0.5)
    print(f'\nAt last, the {exam}s are over. You let out a huge sigh of relief, and when you get home, you pass out '
          f'immediately on your bed. You are so exhausted you do not want to do anything productive this weekend, and '
          f'that\'s okay. You deserve a break.')
    return pass_or_fail


def calculate_average(character: dict) -> str or None:
    """
    Calculate the average of the character's grades

    :param character: a dictionary
    :precondition: character must be a dictionary storing the character's attributes
    :postcondition: calculate the average of the character's grades
    :return: the average of the character's grades

    >>> player = {'midterm': {'1510': 'A', '1537': 'B', '1113': 'C', '1712': 'D'},
    ... 'final': {'1510': 'A', '1537': 'B', '1113': 'C', '1712': 'D'}}
    >>> calculate_average(player)
    'B'

    >>> another_player = {'midterm': {'1510': 'A', '1537': 'A', '1113': 'A', '1712': 'A'},
    ... 'final': {'1510': 'A', '1537': 'A', '1113': 'A', '1712': 'A'}}
    >>> calculate_average(another_player)
    'A'
    """
    min_threshold = (85, 70, 55)
    letter_grades = ('A', 'B', 'C')
    averages = 0
    subject_counter = 0

    for subject in SUBJECTS:
        midterm_grade = character['midterm'][subject]
        final_grade = character['final'][subject]
        if midterm_grade in letter_grades and final_grade in letter_grades:
            average = (min_threshold[letter_grades.index(character['midterm'][subject])] + min_threshold[
                letter_grades.index(character['final'][subject])]) / 2
            averages = averages * subject_counter + average
            subject_counter += 1
            averages /= subject_counter
    for threshold in min_threshold:
        if averages >= threshold:
            return letter_grades[min_threshold.index(threshold)]


def evaluate_exam(character: dict, subject: str, exam: str) -> str:
    """
    Evaluate the character's exam result based on their level in the subject and the exam type.

    :param character: a dictionary
    :param subject: a string
    :param exam: a string
    :precondition: character must be a dictionary storing the character's attributes
    :precondition: subject must be a string representing the subject the character is studying
    :precondition: exam must be a string representing the exam type
    :postcondition: return a string representing the character's exam result

    >>> player = {'lvl': {'1510': 1}}
    >>> course = '1510'
    >>> test = 'midterm'
    >>> evaluate_exam(player, course, test)
    'F'

    >>> player = {'lvl': {'1510': 5}}
    >>> course = '1510'
    >>> test = 'final'
    >>> evaluate_exam(player, course, test)
    'B'
    """
    fail = {'midterm': 1, 'final': 4}
    lvl_requirements = {'midterm': {1: 'F', 2: 'C', 3: 'B', 4: 'A'},
                        'final': {3: 'F', 4: 'C', 5: 'B', 6: 'A'}}
    if character['lvl'][subject] in lvl_requirements[exam].keys():
        return lvl_requirements[exam][character['lvl'][subject]]
    else:
        return 'F' if character['lvl'][subject] < fail[exam] else 'A'


def reward_character(character: dict, subject: str) -> None:
    """
    Reward the character with a point in the subject they are studying.

    :param character: a dictionary
    :param subject: a string
    :precondition: character must be a dictionary storing the character's attributes
    :precondition: subject must be a string representing the subject the character is studying
    :postcondition: adds a point to the character's attribute for the subject they are studying
    """
    stress_loss = randint(5, 10) * -1
    exp_gain = randint(10, 15) * character['IQ']

    char.change_stat(character, subject, exp_gain)
    sleep(0.5)
    char.change_stat(character, 'stress', stress_loss)
