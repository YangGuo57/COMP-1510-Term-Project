import map as mp
import menu as me


def is_at_location(character, doors):
    player_position = (character['X'], character['Y'])
    for door_position in doors:
        if player_position == door_position:
            return True
    return False


def trigger_school_event(character, locations, game_map, main_board_rows, main_board_columns):
    if is_at_location(character, locations["door"]["school"]):
        mp.print_map(game_map, main_board_rows, main_board_columns, character)
        choice = input(
            "Welcome to BCIT! Are you pumped for the incredible journey ahead at school? (Yes/No): ")
        if choice.lower() == "yes":
            me.school_menu(character)
        else:
            print("You decided not to enter the school.")


def trigger_home_event(character, locations, game_map, main_board_rows, main_board_columns):
    if is_at_location(character, locations["door"]["home"]):
        mp.print_map(game_map, main_board_rows, main_board_columns, character)
        choice = input(
            "You arrive home, worn out from the day's endeavors, seeking solace within the familiar walls of "
            "your sanctuary.Do you want to take a break and unwind in the cozy embrace of home? (Yes/No): ")
        if choice.lower() == "yes":
            me.home_menu(character)
        else:
            print("You decided not to enter the home.")
