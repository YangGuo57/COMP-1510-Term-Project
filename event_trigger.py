import map as mp
import menu as me
import movement as mov


def trigger_description():
    message = {
        "school": "Welcome to BCIT! Are you pumped for the incredible journey ahead at school? (Yes/No): ",
        "home-door": "You arrive home, worn out from the day's endeavors, seeking solace within the familiar walls of "
                     "your sanctuary.Do you want to take a break and unwind in the cozy embrace of home? (Yes/No): ",
        "hospital": "   (Yes/No): ",
        "park": "   (Yes/No): ",
        "work": "   (Yes/No): ",
        "gym": "   (Yes/No): ",
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


def process_movement(user_choice, game_board, character, board_rows, board_columns, game_map):
    """
    Processes the player's movement choice in the game.

    :param user_choice:
    :param game_board:
    :param character:
    :param board_rows:
    :param board_columns:
    :param game_map:
    :return:
    """
    if mov.validate_move(game_board, character, user_choice):
        mov.move_character(character, user_choice, board_rows, board_columns, game_map)
        mov.update_visited_location(character)
        return True
    else:
        print("Invalid move! Please choose another direction.")
        return False


def is_at_door(character):
    """
    Determines if the character is at any defined door location.
    """
    locations = mp.coordinates()
    for location, door_coordinates in locations['door'].items():
        if (character['X'], character['Y']) == door_coordinates:
            if location == "school":
                print(f"Character is at the door of {location}.")
                me.sub_menu(character, location)
            elif location == 'park':
                print(f'You are at the entrance of Stanley Park. Do you want to enter and take a leisurely stroll?')
                me.sub_menu(character, location)
                return

    # print("Character is not at any door.")


def enter_school(character):
    """
    Prints school map when entering school

    :param character:
    :return:
    """
    character['X'], character['Y'] = 1, 1
    trigger_action(character, 13, 9, "school")


def classroom_event():
    """
    Put everything about classroom event here.
    """
    print("This trigger a classroom event")


def confirm_entry(location):
    """
    Asks user to confirm whether to enter the door. Return 1 if entry is confirmed, 2 if entry is denied
    """
    locations = trigger_description()
    confirm = input(f'{locations[location].get("description")}')
    while confirm != '1' and confirm != '2':
        confirm = input(f'{locations[location]}')
    return confirm


def trigger_action(character, board_rows, board_columns, location_key):
    """
    Manages the player character's actions on a given game map.

    :param character:
    :param board_rows:
    :param board_columns:
    :param location_key:
    :return:
    """
    game_board, game_map = mp.initialize_map(board_rows, board_columns, location_key)
    office_doors = mp.coordinates()["office_door"]
    while True:
        mp.print_game_map(game_map, board_rows, board_columns, character)
        print(character)
        user_choice = mov.get_user_choice()

        if user_choice == "Back to Menu":
            if location_key == "school":
                character['X'], character['Y'] = 3, 9
                return
            me.main_menu(character)
            break
        if process_movement(user_choice, game_board, character, board_rows, board_columns, game_map):
            is_at_door(character)
            if character['location'] == 'school':
                for office, door_coordinates in office_doors.items():
                    if (character['X'], character['Y']) == door_coordinates:
                        mp.print_game_map(game_map, board_rows, board_columns, character)
                        user_office_choice = confirm_entry(office)
                        if user_office_choice == '1':
                            return office

