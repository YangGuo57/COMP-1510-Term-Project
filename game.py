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
