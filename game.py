from game_system import (weekday, exam, weekend, map, TOTAL_WEEKS,
                         ending_descriptions, ascii, save)
from time import sleep


def print_game_ending(player: dict, test: str, pass_exam: bool, pass_coop: bool) -> None:
    """
    Prints the game ending including the ASCII art based on the player's GPA and whether they passed.
    
    :param player: a dictionary representing the player
    :param test: a string representing the test the player took
    :param pass_exam: a boolean representing whether the player passed the exam
    :param pass_coop: a boolean representing whether the player passed the coop interview
    :precondition: player must be a dictionary generated within this game
    :precondition: test must be a string generated in this game
    :postcondition: correctly prints the game ending based on the player's GPA and whether they passed
    """
    print()
    if not pass_exam:
        print(f'YOU FAILED YOUR {test.upper()}S! YOU HAVE BEEN KICKED OUT OF THE CST PROGRAM :(')
        sleep(0.5)
        ascii.print_ascii('game over')
    else:
        gpa = exam.calculate_average(player)
        endings = ending_descriptions()
        if gpa is None:
            return
        elif pass_coop:
            print(f'{endings["coop"]}')
        else:
            print(f'{endings[gpa]}')
        sleep(0.5)
        ascii.print_ascii('congratulations')


def game() -> None:
    """
    Drive the game
    """
    player, week, is_weekend = save.new_or_load()
    main_map = map.initialize_map(10, 20, 'coordinates')
    school_map = map.initialize_map(13, 9, 'school')
    pass_interview = False

    for current_week in range(week, TOTAL_WEEKS + 1):
        sleep(0.5)
        ascii.print_ascii('new_week')

        print(f'========== Week {current_week} ==========')
        if current_week == TOTAL_WEEKS // 2:
            if not exam.take_exam(player, 'midterm'):
                print_game_ending(player, 'midterm', False, pass_interview)
                return
            is_weekend = True
        elif current_week == TOTAL_WEEKS - 1:
            is_weekend = True
            if not exam.take_exam(player, 'final'):
                print_game_ending(player, 'final', False, pass_interview)
                return
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
            save.save_game(player, current_week, is_weekend)
            if not weekend_result:
                break
            is_weekend = False

        save.save_game(player, current_week, is_weekend)

    print_game_ending(player, None, True, pass_interview)


if __name__ == '__main__':
    game()
