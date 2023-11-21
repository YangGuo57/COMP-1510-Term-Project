import map as mp
import movement as mov
import create_character as cha


def main_menu(character):
    while True:
        print("1. Move")
        print("2. Check Status")
        print("3. Fast Travel")
        print("4. Exit")

        choice = input("Please choose an option: ")
        if choice == '1':
            mp.map_action(character)
        elif choice == '2':
            cha.print_stats(character)
        elif choice == '3':
            mov.fast_travel(character)
        elif choice == '4':
            print("Exiting the game...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
        return choice
