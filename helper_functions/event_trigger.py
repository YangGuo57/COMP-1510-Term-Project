from helper_functions import trigger_description, SUBJECTS, movement as mov, character as char, map
from time import sleep


def process_movement(user_choice, game_map, character):
    """
    Processes the user's movement choice and returns a boolean value

    :param user_choice: a string
    :param game_map: a dictionary
    :param character: a dictionary
    :precondition: user_choice must be a string
    :precondition: game_map must be a dictionary with keys as tuples and values as strings
    :precondition: character must be a dictionary storing the character's attributes
    :postcondition: processes the user's movement choice
    :return: True if the user's movement choice is valid, False otherwise
    """
    if mov.validate_move(game_map, character, user_choice):
        mov.move_character(character, user_choice, game_map)
        mov.update_visited_location(character)
        return True
    else:
        print('Invalid move! Please choose another direction.')
        return False


def at_entrance(character):
    """
    Return the location of the character if they are at the entrance of a location, otherwise return None.

    :param character: a dictionary
    :precondition: character must be a dictionary storing the character's attributes
    :postcondition: determine if the character is at the entrance of a location
    :return: a string representing the location of the character, otherwise return None
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
    Determine whether the player wants to enter a location or not.

    :param location: a dictionary
    :precondition: location must be a dictionary with keys as location and values as description
    :postcondition: determine whether the player wants to enter a location or not
    :return: a string representing the player's choice
    """
    locations = trigger_description()
    description = locations.get(location, "")
    if not description:
        return

    confirm = input(f'{description}')
    while confirm != '1' and confirm != '2':
        confirm = input(f'{description}')

    return confirm


def move_during_office_hours(character, school_map):
    """
    Move the character during office hours.

    :param character: a dictionary
    :param school_map: a dictionary
    :precondition: character must be a dictionary storing the character's attributes
    :precondition: school_map must be a dictionary with keys as tuples and values as strings
    :postcondition: determine if the character is at the entrance of a location
    """
    map.print_game_map(school_map, character)

    while True:
        user_choice = mov.get_user_choice(character)

        if user_choice == 'back':
            return user_choice
        elif user_choice == 'stats':
            char.print_stats(character)
            sleep(0.5)
            map.print_game_map(school_map, character)
        elif process_movement(user_choice, school_map, character):
            map.print_game_map(school_map, character)
            location = at_entrance(character)

            if location in SUBJECTS:
                entry_confirmation = confirm_entry(location)
                if entry_confirmation == '1':
                    return location
                else:
                    map.print_game_map(school_map, character)


def move_on_weekends(character, main_map):
    """
    Allows the user to move on weekends

    :param character: a dictionary
    :param main_map: a dictionary
    :precondition: character must be a dictionary storing the character's attributes
    :precondition: main_map must be a dictionary with keys as tuples and values as strings
    :postcondition: allows the user to move on weekends
    """
    while True:
        map.print_game_map(main_map, character)
        choice = main_menu()

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
                if user_choice == 'Back':
                    break
        elif choice == '2':
            char.print_stats(character)
        elif choice == '3':
            mov.fast_travel(character)
            map.print_game_map(main_map, character)
            location = at_entrance(character)
            if location == 'home':
                return confirm_entry('home entrance')
            elif location:
                return confirm_entry(location)
        elif choice == '4':
            print('Thank you for playing! Your progress has been successfully saved. Goodbye!')
            return 'Exit'
        else:
            print('Invalid choice. Please enter a valid option.')


def main_menu():
    """
    Displays the main menu.

    :postcondition: Displays main menu
    :return: a string representing the user's choice
    """
    print('1. Move')
    print('2. Check Status')
    print('3. Fast Travel')
    print('4. Exit')

    choice = input('Please choose an option: ')
    return choice
