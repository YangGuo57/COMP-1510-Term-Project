import map
import character
import weekday
import weekend
import json
import utils


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
        print(f"Error loading the game: {e}")
        return None, None, False


def start_new_game(greeting_msg):
    print(greeting_msg[1])
    answer = character.ask_questionnaire()
    player = character.create_character(answer)
    print(greeting_msg[2])
    week = 1
    return player, week


def game():
    greeting_msg = utils.greeting()
    print("Welcome to Survive CST!")
    print("1. Start New Game")
    print("2. Load Previous Game")
    while True:
        load_choice = input("Please choose an option (1 or 2): ")
        if load_choice == '1':
            print("Starting a fresh new journey in Survive CST!")
            player, week = start_new_game(greeting_msg)
            is_weekend = False
            break
        elif load_choice == '2':
            player, week, is_weekend = load_game()
            if player is None:
                print("No previous save found. Starting a new adventure!")
                player, week = start_new_game(greeting_msg)
                is_weekend = False
            break
        else:
            print("Invalid option. Please enter '1' for a new game or '2' to load a previous game.")

    main_map = map.initialize_map(10, 20, 'coordinates')
    school_map = map.initialize_map(13, 9, 'school')

    for current_week in range(week, 8):
        print(f"========== Week {current_week} ==========")
        if not is_weekend:
            weekday.run_weekday(player, current_week, school_map)
            is_weekend = True

        # Exit the game
        if is_weekend:
            weekend_result = weekend.run_weekend(player, main_map, current_week)
            save_game(player, current_week, is_weekend)
            if not weekend_result:
                break
            is_weekend = False

        save_game(player, current_week, is_weekend)
        if current_week == 7:
            print("Midterm exams are starting!")


if __name__ == '__main__':
    game()
