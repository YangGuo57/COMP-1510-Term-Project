import character as char
from random import randint, choice


def midterm_description():
    descriptions = {
        '1510': "This is the midterm description for COMP1510...",
        '1537': "This is the midterm description for COMP1537...",
        '1113': "This is the midterm description for COMP1113...",
        '1712': "This is the midterm description for COMP1712..."
    }
    return descriptions


def exam_status():
    status = [
        "This question is tougher than I expected! Need to concentrate harder.",
        "Ah, I studied this topic well, feeling confident!",
        "This is quite challenging, but I think I can solve it.",
        "I remember the professor discussing this concept, let me think...",
        "The exam is going on, I must stay calm and focused.",
        "Surprisingly, this part of the exam seems easier than I anticipated.",
        "I'm feeling a bit overwhelmed by this question, but I won't give up.",
        "I'm drawing a blank on this one; it's time to guess wisely.",
        "This section is exactly what I revised last night, lucky me!",
        "I need to pick up the pace to finish the exam in time."
    ]
    return status


def run_midterm(character):
    print('Finally, the time has come: the arrival of the much-anticipated midterm exams. The school\'s '
          'hallways are buzzing with the palpable tension of students, their arms laden with notes and '
          'textbooks. It\'s a pivotal moment, a true test of all the knowledge and skills you\'ve '
          'accumulated over the past weeks. Ahead lies a demanding journey filled with intense revision '
          'sessions, diligent practice, and the crucial task of navigating through the exam questions. '
          'Are you prepared to dive into this academic challenge, If you are not ready, Haha, now it\'s too late! '
          'Please enter the classroom and start your exam!')

    descriptions = midterm_description()
    statuses = exam_status()
    subjects = ['1510', '1537', '1113', '1712']

    for subject in subjects:
        input(f"\nPress '1' to start the exam for COMP{subject}: ")
        print(descriptions[subject])
        print("The exam is underway...")
        print(choice(statuses))

        if pass_or_fail_exam(character, subject):
            print(f"You passed COMP{subject}! Congratulations.")
            reward_character(character, subject)
        else:
            print(f"You failed COMP{subject}. Better luck next time.")


def pass_or_fail_exam(character, subject):
    lvl_requirements = {'1510': 0, '1537': 0, '1113': 0, '1712': 0}
    if character['lvl'][subject] >= lvl_requirements[subject]:
        return True
    else:
        return False


def reward_character(character, subject):
    iq_gain = randint(1, 3)
    exp_gain = randint(15, 25)

    character['IQ'] = max(0, character['IQ'] + iq_gain)
    character['exp'][subject] += exp_gain
    char.evaluate_exp(character, subject)

    print(f"Your IQ increased by {iq_gain} and your experience in COMP{subject} increased by {exp_gain}.")
