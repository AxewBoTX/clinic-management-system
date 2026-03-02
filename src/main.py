import print_labels
import cli

def main():
    print_labels.intro()
    current_action = None
    while action == None or action != :
        user_input = 0
        try:
            user_input = int(input("> "))
        except ValueError:
            print("You have to enter an integer value")
            continue
        if user_input < 0 or user_input >= len(cli.ACTIONS):
            print("You have to select a valid action")
            continue
        action = user_input
        print(f"You chose '{cli.ACTIONS[action]}'")


if __name__ == "__main__":
    main()
