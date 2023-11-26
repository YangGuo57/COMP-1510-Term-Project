import event_trigger as e
import weekend

def main_menu():
    print("1. Move")
    print("2. Check Status")
    print("3. Fast Travel")
    print("4. Exit")

    choice = input("Please choose an option: ")
    return choice


def sub_menu(character, location):
    while True:
        print("1. Enter")
        print("2. Leave")

        choice = input("Please choose an option: ")
        if choice == '1':
            # event call goes here
            if location == 'school':
                e.enter_school(character)
            elif location == 'park':
                weekend.weekend_park(character)
            break

        elif choice == '2':
            e.trigger_action(character, 10, 20, 'coordinates')
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def inside_school_menu():
    print("1. Explore the school")
    print("2. Return to main map")

    while True:
        choice = input("Please choose an option: ")
        if choice in ['1', '2']:
            return choice
        else:
            print("Invalid choice. Please enter '1' to explore or '2' to return to the main map.")
