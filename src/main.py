from clinic_manager import ClinicManager
import printer
import actions


def main():
    clinic_manager = ClinicManager()
    clinic_manager.load_data()

    printer.clear()
    printer.intro()

    current_action = None
    while current_action == None or current_action != 0:
        printer.print_actions()
        user_input = 0
        try:
            user_input = input("> ")
            if len(user_input) == 0:
                printer.clear()
                printer.error("You have to enter something")
                print()
                continue
            user_input = int(user_input)
        except ValueError:
            printer.clear()
            printer.error("You have to enter an integer value")
            print()
            continue
        if user_input < 0 or user_input >= len(actions.ACTIONS):
            printer.clear()
            printer.error("You have to select a valid action")
            print()
            continue
        current_action = user_input
        actions.handle_actions(clinic_manager, current_action)


if __name__ == "__main__":
    main()
