import character as char
from random import randint, choice

import utils

questions = (
    'How do you prioritize tasks when you have multiple deadlines to meet?\n'
    '1. Do the task that\'s due first\n'
    '2. Do the task that\'s more important\n',
    'How do you handle stress and pressure in the workplace? \n'
    '1. Cry\n'
    '2. Bottle all the stress in at work and release the bottle when you are outside of work\n',
    'How do you stay organized and keep track of multiple tasks or projects simultaneously?\n'
    '1. Use a Trello board or some other type of planning tool\n'
    '2. Use your brain to remember everything\n',
    'How do you approach decision-making when faced with incomplete information?\n'
    '1. Ask your coworkers, then if you still don\'t have enough information, ask your boss\n'
    '2. Ask your boss, then if you still don\'t have enough information, ask your coworkers\n'
)


def take_coop_interview(character):
    print('As you step into the interview room, you are greeted with a few pairs of eyes - wow, there are more than '
          'one person interviewing you! You introduce yourself as you nervously sit down in the lone empty chair in '
          'the room. Your interviewer clears his throat, and starts asking you some questions, how will you answer?')
    answer_key = ((0, 1), (0, 1), (1, 0), (1, 0))
    answers = utils.ask_questionnaire('coop')
    score = 0

    for answer_index in range(len(answers)):
        score += answer_key[answer_index][answers[answer_index]]
    score *= character['EQ']

    threshold_to_pass = 4 * utils.TOTAL_WEEKS + 17 * utils.TOTAL_WEEKS / 2

    if (character['project'] + score) < threshold_to_pass:
        return False
    else:
        return True


def take_exam(character, exam):
    print(f'Finally, the time has come: the much-anticipated {exam} exams are here. You look around you and all '
          f'you see are the blank stares of your sleep-deprived classmates who pulled consecutive all-nighters and are '
          f'living off of coffee. God forbid the Tim Hortons downstairs closes for today... You are no different from '
          f'them. If you are not yet ready to take the exam, that\'s too bad because the exam starts NOW.')

    statuses = utils.exam_status()
    pass_or_fail = True

    for subject in utils.SUBJECTS:
        input(f"\nPress '1' to start the exam for COMP{subject}: ")
        print(f"The COMP{subject} exam is underway...")

        grade = evaluate_exam(character, subject, exam)
        print(choice(statuses[grade]))

        if grade == 'F':
            print(f"You failed COMP{subject}. Better luck next time.")
            pass_or_fail = False
        else:
            print(f'Phew, you passed and you got {"an" if grade == "A" else "a"} {grade} in COMP{subject}. Writing '
                  f'this {exam} was a learning experience in itself, and you feel relieved now that one more {exam} '
                  f'is over.')
            reward_character(character, subject)
            if exam == 'midterm':
                character['midterm'][subject] = grade
            elif exam == 'final':
                character['final'][subject] = grade
    print(f'At last, the {exam}s are over. You let out a huge sigh of relief, and when you get home, you pass out '
          f'immediately on your bed. You are so exhausted you do not want to do anything productive this weekend, and '
          f'that\'s okay. You deserve a break.')
    return pass_or_fail


def calculate_average(character):
    min_threshold = (85, 70, 55)
    letter_grades = ('A', 'B', 'C')
    averages = 0
    subject_counter = 0

    for subject in utils.SUBJECTS:
        average = (min_threshold[letter_grades.index(character['midterm'][subject])] + min_threshold[
            letter_grades.index(character['final'][subject])]) / 2
        averages = averages * subject_counter + average
        subject_counter += 1
        averages /= subject_counter
    for threshold in min_threshold:
        if averages >= threshold:
            return letter_grades[min_threshold.index(threshold)]


def evaluate_exam(character, subject, exam):
    fail = {'midterm': 1, 'final': 4}
    lvl_requirements = {'midterm': {1: 'F', 2: 'C', 3: 'B', 4: 'A'},
                        'final': {3: 'F', 4: 'C', 5: 'B', 6: 'A'}}
    if character['lvl'][subject] in lvl_requirements[exam].keys():
        return lvl_requirements[exam][character['lvl'][subject]]
    else:
        return 'F' if character['lvl'][subject] < fail[exam] else 'A'


def reward_character(character, subject):
    stress_loss = randint(5, 10) * -1
    exp_gain = randint(10, 15) * character['IQ']

    char.change_stat(character, subject, exp_gain)
    char.change_stat(character, 'stress', stress_loss)
