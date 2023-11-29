import character as char
from random import randint, choice


def exam_status():
    status = {
        'A': ("Yay, you studied really hard for this subject and you\'re feeling confident!",
              "Surprisingly, this exam is easier than you anticipated.",
              "This section is exactly what you looked over last night, lucky you!"),
        'B': ("This question is tougher than you expected! You start thinking really hard...",
              "This exam is quite challenging, but you know the answer.",
              "You remember the instructor teaching this concept, now if only you can remember what he said...",
              "The exam is going on, you must stay calm and focused."),
        'C': ("You\'re feeling a bit overwhelmed by this question, you must not panic... Okay never mind, PANIC.",
              "Oh no, you\'re drawing a blank on this one! It\'s time to make an educated guess... It must be C "
              "because it\'s always the third option on a multiple choice exam...right?",
              "Uh oh, you need to pick up the pace to finish the exam in time."),
        'F': ('Zzzzz... ... ... Are you really sleeping during an exam?',
              'Oh no, you\'re so anxious you can\'t breathe... OH NO. OHHHHHHHH NOOOOOOOOO NO NO NONONO '
              'NOOOOOOOOOOOOOooOOoOOooOoOOoo!!!',
              'You stare really hard at the exam paper as if answers will magically write themselves on each '
              'question... Nice try.')
    }
    return status


def take_exam(character, exam):
    print(f'Finally, the time has come: the much-anticipated {exam} exams are here. You look around you and all '
          f'you see are the blank stares of your sleep-deprived classmates who pulled consecutive all-nighters and are '
          f'living off of coffee. God forbid the Tim Hortons downstairs closes for today... You are no different from '
          f'them. If you are not yet ready to take the exam, that\'s too bad because the exam starts NOW.')

    statuses = exam_status()
    subjects = ['1510', '1537', '1113', '1712']
    min_threshold = (85, 70, 55)
    letter_grades = ('A', 'B', 'C')
    pass_or_fail = True

    for subject in subjects:
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
                average = min_threshold[letter_grades.index(character['midterm'][subject])] + min_threshold[
                    letter_grades.index(grade)] / 2
                for threshold in min_threshold:
                    if average > threshold:
                        character['final'][subject] = letter_grades[min_threshold.index(threshold)]
    print(f'At last, the {exam}s are over. You let out a huge sigh of relief, and when you get home, you pass out '
          f'immediately on your bed. You are so exhausted you do not want to do anything productive this weekend, and '
          f'that\'s okay. You deserve a break.')
    return pass_or_fail


def evaluate_exam(character, subject, exam):
    fail = {'midterm': 2, 'final': 2}
    lvl_requirements = {'midterm': {2: 'F', 3: 'C', 4: 'B', 5: 'A'},
                        'final': {2: 'F', 3: 'C', 4: 'B', 5: 'A'}}
    if character['lvl'][subject] in lvl_requirements[exam].keys():
        return lvl_requirements[exam][character['lvl'][subject]]
    else:
        return 'F' if character['lvl'][subject] < fail[exam] else 'A'


def reward_character(character, subject):
    stress_loss = randint(5, 10) * -1
    exp_gain = randint(10, 15) * character['IQ']

    char.change_stat(character, subject, exp_gain)
    char.change_stat(character, 'stress', stress_loss)
