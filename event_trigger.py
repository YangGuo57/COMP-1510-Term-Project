import map
import utils
import movement as mov
import character as char


def trigger_description():
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
        "home": {'description': 'A radiant weather beckons beyond your window; should you go on a refreshing outdoor '
                                'stroll or indulge in the comforts of your home? \n'
                                'Enter "1" to stay home, enter "2" to leave the house.',
                 '1': 'home',
                 '2': 'outside'}

    }

    return message


def process_movement(user_choice, game_map, character):
    """
    Processes the player's movement choice in the game.
    """
    if mov.validate_move(game_map, character, user_choice):
        mov.move_character(character, user_choice, game_map)
        mov.update_visited_location(character)
        return True
    else:
        print("Invalid move! Please choose another direction.")
        return False


def at_entrance(character):
    """
    return door location: "home", "school", "hospital", "park", "work"
    """
    locations = map.coordinates()
    index = ''
    if character['location'] == 'outside':
        index += 'main'
    else:
        index += 'school'
    for location, door_coordinates in locations['door'][index].items():
        if (character['X'], character['Y']) == door_coordinates:
            return location

    return None


def confirm_entry(location):
    """
    Asks user to confirm whether to enter the door. Return 1 if entry is confirmed, 2 if entry is denied
    """
    locations = trigger_description()
    if location == 'home':
        confirm = input(f'{locations[location]["description"]}')
        while confirm != '1' and confirm != '2':
            confirm = input(f'{locations[location]["description"]}')
        return confirm
    elif location == 'school':
        confirm = input(f'{locations[location]}')
        while confirm != '1' and confirm != '2':
            confirm = input(f'{locations[location]}')
        return confirm
    else:
        confirm = input(f'{locations[location]}')
        while confirm != '1' and confirm != '2':
            confirm = input(f'{locations[location]}')
        return confirm


def handle_school_event(character, school_map):
    """
    move on school map and trigger events
    :param character:
    :param school_map:
    :return:
    """
    map.print_game_map(school_map, character)
    while True:
        user_choice = mov.get_user_choice(character)
        if user_choice == "Back":
            return user_choice
        elif process_movement(user_choice, school_map, character):
            map.print_game_map(school_map, character)
            location = at_entrance(character)
            if location in ["1510", "1113", "1712", "1537"]:
                entry_confirmation = confirm_entry(location)
                if entry_confirmation == '1':
                    return location
                else:
                    map.print_game_map(school_map, character)


def handle_map_event(character, main_map):
    """
    move on main map and trigger events
    :param character:
    :param main_map:
    :return:
    """
    while True:
        map.print_game_map(main_map, character)
        choice = utils.main_menu()
        if choice == '1':
            while True:
                user_choice = mov.get_user_choice(character)
                if process_movement(user_choice, main_map, character):
                    map.print_game_map(main_map, character)
                    location = at_entrance(character)
                    if location == 'home':
                        return confirm_entry('home entrance')
                    elif location:
                        return confirm_entry(location)
                if user_choice == "Back":
                    break
        elif choice == '2':
            char.menu_print_stats(character)
        elif choice == '3':
            mov.fast_travel(character)
        elif choice == '4':
            print("Thank you for playing! Your progress has been successfully saved. Goodbye!")
            return 'Exit'
        else:
            print("Invalid choice. Please enter a valid option.")
