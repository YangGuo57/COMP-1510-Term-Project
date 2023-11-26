import map
import menu
import movement as mov


def trigger_description():
    message = {
        "school": "Welcome to BCIT! Are you pumped for the incredible journey ahead at school? (Yes/No): ",
        "home-door": "You arrive home, worn out from the day's endeavors, seeking solace within the familiar walls of "
                     "your sanctuary.Do you want to take a break and unwind in the cozy embrace of home? (Yes/No): ",
        "hospital": "   (Yes/No): ",
        "park": "   (Yes/No): ",
        "work": "   (Yes/No): ",
        "party": "   (Yes/No): ",
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
    for location, door_coordinates in locations['door'].items():
        if (character['X'], character['Y']) == door_coordinates:
            if location == "school":
                print(f"Character is at the door of {location}.")
            elif location == 'park':
                print(f'You are at the entrance of Stanley Park. Do you want to enter and take a leisurely stroll?')

            return location

    return None


def confirm_entry(location):
    """
    Asks user to confirm whether to enter the door. Return 1 if entry is confirmed, 2 if entry is denied
    """
    locations = trigger_description()
    confirm = input(f'{locations[location]}')
    while confirm != '1' and confirm != '2':
        confirm = input(f'{locations[location]}')
    return confirm


def handle_school_specific_event():
    """
    Perform your action during office hours
    """
    print("After you confirm entry, perform your action! ")


def handle_school_event(character, school_map, main_map):
    message = trigger_description()
    print(message['school'])
    while True:
        school_choice = menu.inside_school_menu()
        if school_choice == '1':
            character['X'], character['Y'] = 1, 1
            map.print_game_map(school_map, character)
            while True:
                user_choice = mov.get_user_choice()
                if process_movement(user_choice, school_map, character):
                    map.print_game_map(school_map, character)
                    location = at_entrance(character)
                    if location in ["1510", "1113", "1712", "1537"]:
                        entry_confirmation = confirm_entry(location)
                        if entry_confirmation == '1':
                            handle_school_specific_event()
                if user_choice == "Back":
                    break
        elif school_choice == '2':
            character['X'], character['Y'] = 3, 9
            map.print_game_map(main_map, character)
            break
