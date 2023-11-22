import map as mp
import menu as me


def trigger_description():
    message = {
        "school": "Welcome to BCIT! Are you pumped for the incredible journey ahead at school? (Yes/No): ",
        "home": "You arrive home, worn out from the day's endeavors, seeking solace within the familiar walls of "
                "your sanctuary.Do you want to take a break and unwind in the cozy embrace of home? (Yes/No): ",
        "hospital": "   (Yes/No): ",
        "park": "   (Yes/No): ",
        "work": "   (Yes/No): ",
        "gym": "   (Yes/No): ",
        "party": "   (Yes/No): "
    }

    return message


def is_at_location(character, doors):
    player_position = (character['X'], character['Y'])
    for door_position in doors:
        if player_position == door_position:
            return True
    return False


def trigger_event(main_board_rows, main_board_columns, game_map, character, location, messages):
    mp.print_map(game_map, main_board_rows, main_board_columns, character)
    choice = input(messages[location])
    if choice.lower() == "yes":
        if location != "school":
            me.home_menu(character)
        else:
            me.school_menu(character)
    else:
        print(f"You decided not to enter the {location}.")
