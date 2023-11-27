import map
import character
import weekday
import weekend


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
    answer = character.ask_questionnaire()
    player = character.create_character(answer)
    print(greeting_msg[2])
    main_map = map.initialize_map(10, 20, 'coordinates')
    school_map = map.initialize_map(13, 9, 'school')

    for week in range(1, 8):
        print(f"========== Week {week} ==========")
        weekday.run_weekday(player, week, school_map)
        weekend.run_weekend(player, main_map)
        if week == 7:
            print("Midterm exams are starting!")


if __name__ == '__main__':
    game()
