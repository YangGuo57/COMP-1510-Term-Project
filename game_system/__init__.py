"""
This module contains the constants used in the game.
"""

TOTAL_WEEKS = 14
SUBJECTS = ('1510', '1537', '1113', '1712')
PRODUCTIVE_STATS = ('1510', '1537', '1113', '1712', 'project')


def greeting() -> dict:
    """
    Returns a dictionary containing the greeting messages.
    
    :return: a dictionary containing the greeting messages
    """
    greeting_dict = {
        1: "Welcome to Survive CST. Please take a moment to answer the following questionnaire. There is no right"
           " or wrong answer.",
        2: "It is the first week of September, your first time in the City of Vancouver, and your first day studying "
           "Computer Systems Technology (CST) at BCIT. You enter the school elevator with mixed feelings; after all, "
           "you came to this foreign city in hopes that computer science is the right career for you. As you step out "
           "of the elevator, you tell yourself: don't stress, learn lots, make friends, get co-op, and most "
           "importantly, have fun!",
        3: "\nJust remember: do NOT fail any midterms or finals, because you'll get kicked out of the program!",
    }

    return greeting_dict


def coop_interview_questions() -> tuple:
    """
    Returns a tuple containing the coop interview questions.
    
    :return: a tuple containing the coop interview questions
    """
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
    return questions


def initial_game_questions() -> tuple:
    """
    Returns a tuple containing the initial game questions.
    
    :return: a tuple containing the initial game questions
    """
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
    return questions


def ending_descriptions() -> dict:
    """
    Returns a dictionary containing the game endings.
    
    :return: a dictionary containing the game endings
    """
    endings = {
        'coop': 'Fantastic news, you passed the interview with flying colours! Not only did you secure an impressive A '
                'in your final grades, but you\'ve also successfully landed a coveted coop opportunity! Your journey '
                'is bound for greatness, and you will no doubt succeed in Survive CST term 2 '
                '(TBD...). Congratulations on surviving CST term 1 :)',
        'A': 'While your coop interviews may not have gone as planned, you still got an '
             'impressive A in your final grades. Your intelligence is evident, but consider being more people-smart '
             'in your next job application. A prepared personal project could be the key to securing that coveted '
             'offer next time. Congratulations on surviving CST term 1 :)',
        'B': 'You made it through the term, handling assignments and exams as best you could. Maybe not acing '
             'everything, but you pushed through and scored a B in your final grades. Give yourself credit for '
             'surviving the challenges; it\'s about getting by, and that\'s an accomplishment in its own right. '
             'Congratulations on surviving CST term 1 :)',
        'C': 'Getting through this term has been a real challenge. Assignments and exams felt like a steep mountain to '
             'climb, and yeah, it got pretty close to not making it. But here you are, at the finish line, a bit '
             'battered, but still standing. Remember, it\'s okay to stumble; what matters is you made it through. '
             'Congratulations on surviving CST term 1 :)'
    }
    return endings


def exam_status() -> dict:
    """
    Returns a dictionary containing the exam status messages.
    
    :return: a dictionary containing the exam status messages
    """
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


def coordinates() -> dict:
    """
    Returns a dictionary containing the coordinates of the map.

    :return: a dictionary containing the coordinates of the map
    """
    locations = {
        "coordinates": {
            (2, 4): "home",
            (3, 10): "school",
            (6, 13): "hospital",
            (2, 16): "park",
            (7, 5): "work"
        },
        "door": {
            "main": {"home": (2, 3),
                     "school": (3, 9),
                     "hospital": (6, 12),
                     "park": (2, 15),
                     "work": (7, 4)},
            "school": {
                "1510": (2, 6),
                "1537": (10, 6),
                "1712": (7, 6),
                "1113": (4, 6),
            }

        },
        "school": {
            (2, 7): "1510",
            (10, 7): "1537",
            (7, 7): "1712",
            (4, 7): "1113",
        }
    }
    return locations


def trigger_description() -> dict:
    """
    Returns a dictionary containing the trigger descriptions.
    
    :return: a dictionary containing the trigger descriptions
    """
    message = {
        "school": "You are at the entrance to BCIT. Do you want to enter?\n"
                  "Enter '1' to enter the building, '2' to leave.",
        "home entrance": "You arrive at the doorsteps of your home, feeling a bit worn out from all the walking. Do "
                         "you want to go home?\n"
                         "Enter '1' to enter your house, '2' to leave.",
        "hospital": "You are at the doorsteps of the Vancouver General Hospital. Do you want to enter?\n"
                    "Enter '1' to enter the hospital, '2' to leave. ",
        "park": 'You are at the entrance of Stanley Park. Do you want to enter and take a leisurely stroll? \n'
                'Enter "1" to enter the park, "2" to leave.',
        "work": "You are at the entrance of a local cafe. Do you want to enter?\n"
                "Enter '1' to enter the cafe, '2' to leave.",
        "1510": "The office of the COMP1510 instructor stands before you. Do you want to bug the instructor about "
                "material you don't understand? \n"
                "Enter '1' to enter the office, '2' to think about it some more.",
        "1113": "The office of the COMP1113 instructor stands before you. Do you want to bug the instructor about "
                "material you don't understand? \n"
                "Enter '1' to enter the office, '2' to think about it some more.",
        "1712": "The office of the COMP1712 instructor stands before you. Do you want to bug the instructor about "
                "material you don't understand? \n"
                "Enter '1' to enter the office, '2' to think about it some more.",
        "1537": "The office of the COMP1537 instructor stands before you. Do you want to bug the instructor about "
                "material you don't understand? \n"
                "Enter '1' to enter the office, '2' to think about it some more.",
        "home": 'A radiant weather beckons beyond your window; should you go on a refreshing outdoor stroll or indulge '
                'in the comforts of your home? \n'
                'Enter "1" to stay home, enter "2" to leave the house.'
    }
    return message
