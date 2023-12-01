from helper_functions import (weekday, exam, weekend, map, character, TOTAL_WEEKS,
                              ending_descriptions, greeting, ascii)
import json
from time import sleep


def save_game(player, week, is_weekend, filename='game_save.json'):
    game_data = {
        'character': player,
        'week': week,
        'is_weekend': is_weekend,
    }
    with open(filename, 'w') as file:
        json.dump(game_data, file, indent=4)


def load_game(filename='game_save.json'):
    try:
        with open(filename, 'r') as file:
            game_data = json.load(file)
        return game_data['character'], game_data['week'], game_data.get('is_weekend', False)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error loading the game: {e}')
        return None, None, False


def determine_game_ending(player, coop):
    gpa = exam.calculate_average(player)
    print(gpa)
    endings = ending_descriptions()
    if gpa is None:
        return
    elif coop:
        print(f'{endings["coop"]}')
    else:
        print(f'{endings[gpa]}')


def start_new_game(greeting_msg):
    sleep(0.5)
    print(greeting_msg[1])
    answer = character.ask_questionnaire('new')
    player = character.create_character(answer)
    print(greeting_msg[2])
    print(greeting_msg[3])
    week = 1
    return player, week


def game():
    greeting_msg = greeting()
    sleep(0.5)
    print('Welcome to Survive CST!')
    print('1. Start New Game')
    print('2. Load Previous Game')
    while True:
        load_choice = input('Please choose an option (1 or 2): ')
        if load_choice == '1':
            print('Starting a fresh new journey in Survive CST!')
            sleep(0.5)
            player, week = start_new_game(greeting_msg)
            is_weekend = False
            break
        elif load_choice == '2':
            player, week, is_weekend = load_game()
            if player is None:
                print('No previous save found. Starting a new adventure!')
                player, week = start_new_game(greeting_msg)
                is_weekend = False
            break
        else:
            print("Invalid option. Please enter '1' for a new game or '2' to load a previous game.")

    main_map = map.initialize_map(10, 20, 'coordinates')
    school_map = map.initialize_map(13, 9, 'school')
    pass_midterm = True
    pass_final = True
    pass_interview = False

    # player['lvl']['1510'] = 5
    # player['lvl']['1537'] = 5
    # player['lvl']['1113'] = 5
    # player['lvl']['1712'] = 5
    # player['midterm'] = {'1510': 'A', '1537': 'A', '1113': 'A', '1712': 'A'}
    # player['final'] = {'1510': 'A', '1537': 'A', '1113': 'A', '1712': 'A'}
    # print(exam.calculate_average(player))

    for current_week in range(week, TOTAL_WEEKS + 1):
        sleep(0.5)
        ascii.print_ascii('new_week')

        print(f'========== Week {current_week} ==========')
        if current_week == TOTAL_WEEKS // 2:
            if not exam.take_exam(player, 'midterm'):
                pass_midterm = False
                break
            is_weekend = True
        elif current_week == TOTAL_WEEKS - 1:
            is_weekend = True
            if not exam.take_exam(player, 'final'):
                pass_final = False
                break
            if exam.calculate_average(player) != 'A':
                break
        elif current_week == TOTAL_WEEKS:
            pass_interview = exam.take_coop_interview(player)
            break

        if not is_weekend:
            weekday.weekday(player, current_week, school_map)
            is_weekend = True
        if is_weekend:
            ascii.print_ascii('weekend')
            weekend_result = weekend.weekend(player, main_map, current_week)
            save_game(player, current_week, is_weekend)
            if not weekend_result:
                break
            is_weekend = False

        save_game(player, current_week, is_weekend)

    print(player)
    if not pass_midterm:
        print('GAME OVER! YOU FAILED YOUR MIDTERMS :(')
    elif not pass_final:
        print('GAME OVER! YOU FAILED YOUR FINALS :(')
    else:
        determine_game_ending(player, pass_interview)


if __name__ == '__main__':
    game()
