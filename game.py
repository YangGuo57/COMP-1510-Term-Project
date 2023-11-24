from random import randint
import menu
import character as char
import weekday


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


def game():
    greeting_msg = greeting()
    print(greeting_msg[1])
    answer = char.ask_questionnaire()
    player = char.create_character(answer)
    print(greeting_msg[2])
    # menu.main_menu(player)

    weekday.run_weekday(player, 1)
    weekday.run_weekday(player, 2)


if __name__ == '__main__':
    game()
