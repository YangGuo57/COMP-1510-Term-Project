from helper_functions import trigger_description, SUBJECTS, movement as mov, character as char, map


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


def move_during_office_hours(character, school_map):
    """
    move on school map and trigger events
    :param character:
    :param school_map:
    :return:
    """
    map.print_game_map(school_map, character)

    while True:
        user_choice = mov.get_user_choice(character)

        if user_choice == "back":
            return user_choice
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
    move on main map and trigger events
    :param character:
    :param main_map:
    :return:
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
                if user_choice == "Back":
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
            print("Thank you for playing! Your progress has been successfully saved. Goodbye!")
            return 'Exit'
        else:
            print("Invalid choice. Please enter a valid option.")


def main_menu():
    print("1. Move")
    print("2. Check Status")
    print("3. Fast Travel")
    print("4. Exit")

    choice = input("Please choose an option: ")
    return choice