import movement as mov
import character as cha
import event_trigger as e


def main_menu(character):
    while True:
        print("1. Move")
        print("2. Check Status")
        print("3. Fast Travel")
        print("4. Exit")

        choice = input("Please choose an option: ")
        if choice == '1':
            e.trigger_action(character, 10, 20, 'coordinates')
        elif choice == '2':
            cha.print_stats(character)
        elif choice == '3':
            mov.fast_travel(character)
        elif choice == '4':
            print("Exiting the game...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def sub_menu(character):
    while True:
        print("1. Enter")
        print("2. Leave")

        choice = input("Please choose an option: ")
        if choice == '1':
            # event call goes here
            e.enter_school(character)
            break

        elif choice == '2':
            e.trigger_action(character, 10, 20, 'coordinates')
            break
        else:
            print("Invalid choice. Please enter a valid option.")
