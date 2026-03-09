"""
main.py - Creates clinic manager and starts the main loop

Cole, Mia: s8248723
Matta, Ishi: s8239982
Singh, Lovedeep: s8208559
"""

from clinic_manager import ClinicManager
import printer
import actions


def main():
    # we create the clinic manager and try to load any data that might have been saved previously
    clinic_manager = ClinicManager()
    clinic_manager.load_data()

    # we clear the screen
    printer.clear()
    printer.intro()

    # being listening for action input
    # actions work simply by taking the numbered input from the user
    # we just ask the user to enter a number and run the action handle accordingly
    current_action = None
    while current_action == None or current_action != 0:
        # print the action options from which the user can choose from i.e
        # 0 - save and exit
        # 1 - help
        # so on
        printer.print_actions()

        user_input = 0
        try:
            user_input = input("> ")
            # if the user input was nothing, we just print an error and continue to the next iteration of the loop
            if len(user_input) == 0:
                printer.clear()
                printer.error("You have to enter something")
                print()
                continue
            user_input = int(user_input)
        except ValueError:
            # if the user input was of incorrect type, we just print an error and continue to the next iteration of the loop
            printer.clear()
            printer.error("You have to enter an integer value")
            print()
            continue

        # if the user input was out of bounds, i.e not corresponding to a valid action, we print the error and continue to the next iteration
        if user_input < 0 or user_input >= len(actions.ACTIONS):
            printer.clear()
            printer.error("You have to select a valid action")
            print()
            continue
        current_action = user_input

        # once we get a proper action, we handle it
        actions.handle_actions(clinic_manager, current_action)

# main program entry point
if __name__ == "__main__":
    main()
