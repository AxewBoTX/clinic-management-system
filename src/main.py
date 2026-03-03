from clinic_manager import ClinicManager
import printer
import cli

def main():
    clinic_manager = ClinicManager()
    clinic_manager.add_nurse(23, "Alice", 3)
    clinic_manager.add_doctor(24, "Nick", 24000.0, 4)
    clinic_manager.add_regular_patient("Cole", 735097797, 3)
    clinic_manager.add_vip_patient("John", 73572307, 2, 2)

    printer.clear()
    printer.intro()

    current_action = None
    while current_action == None or current_action != 0:
        printer.actions()
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
        if user_input < 0 or user_input >= len(cli.ACTIONS):
            printer.clear()
            printer.error("You have to select a valid action")
            print()
            continue
        current_action = user_input
        cli.handle_actions(clinic_manager, current_action)

if __name__ == "__main__":
    main()
