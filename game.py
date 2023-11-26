from random import randint

import map
import menu
import character
import weekday
import weekend
import movement as mov
import event_trigger as event


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

    while True:
        current_map = main_map
        map.print_game_map(main_map, player)
        choice = menu.main_menu()
        if choice == '1':
            while True:
                user_choice = mov.get_user_choice()
                if event.process_movement(user_choice, current_map, player):
                    map.print_game_map(current_map, player)
                    location = event.at_entrance(player)
                    if location == "home":
                        print("home")
                    elif location == "school":
                        event.handle_school_event(player, school_map, main_map)
                    elif location == "hospital":
                        print("hospital")
                    elif location == "park":
                        print("park")
                    elif location == "work":
                        print("work")
                if user_choice == "Back":
                    break
        elif choice == '2':
            character.print_stats(player)
        elif choice == '3':
            mov.fast_travel(player)
        elif choice == '4':
            print("Exiting the game...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    # weekday.run_weekday(player, 1)
    # weekday.run_weekday(player, 2)


if __name__ == '__main__':
    game()
