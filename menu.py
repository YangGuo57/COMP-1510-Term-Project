import map as mp
import movement as mov
import character as cha
import random


def main_menu(character):
    while True:
        print("1. Move")
        print("2. Check Status")
        print("3. Fast Travel")
        print("4. Exit")

        choice = input("Please choose an option: ")
        if choice == '1':
            mp.map_action(character, 10, 20, 'coordinates')
        elif choice == '2':
            cha.print_stats(character)
        elif choice == '3':
            mov.fast_travel(character)
        elif choice == '4':
            print("Exiting the game...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def school_menu(character):
    while True:
        print("1. Enter School")
        print("2. Leave School")

        choice = input("Please choose an option: ")
        if choice == '1':
            mp.map_action(character, 13, 9, 'school')
        elif choice == '2':
            mp.map_action(character, 10, 20, 'coordinates')
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def office_hour_menu(character):
    while True:
        print("1. Enter Office")
        print("2. Leave Office")

        choice = input("Please choose an option: ")
        if choice == '1':
            # trigger office hour event
            print("Please put your office hour event code here...")
        elif choice == '2':
            mp.map_action(character, 13, 9, 'school')
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def home_menu(character):
    while True:
        print("1. Enter home")
        print("2. Leave home")

        choice = input("Please choose an option: ")
        if choice == '1':
            cha.change_stat(character, 'stress', random.randint(-20, -15))
        elif choice == '2':
            mp.map_action(character, 10, 20, 'coordinates')
            break
        else:
            print("Invalid choice. Please enter a valid option.")
