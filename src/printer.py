"""
printer.py - provides printing related functions

Cole, Mia: s8248723
Matta, Ishi: s8239982
Singh, Lovedeep: s8208559
"""

import actions
import os
import colors

# clear the screen, if supported by wherever the program is being run
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# print the introduction label
def intro():
    print(
        f"{'='*15} Welcome to the Clinic Management System {'='*15}"
    )
    print()


# print the available actions
def print_actions():
    for i in range(0, len(actions.ACTIONS)):
        print(f"{i}. {actions.ACTIONS[i]}")
    print()
    print("What would you like to do ?")


# log successfull events
def success(user_input):
    from rich import print

    print(f"[{colors.GREEN}][SUCCESS][/{colors.GREEN}] {user_input}")


# log information
def info(user_input):
    from rich import print

    print(f"[{colors.BLUE}][INFO][/{colors.BLUE}] {user_input}")


# log error
def error(user_input):
    from rich import print

    print(f"[{colors.RED}][ERROR][/{colors.RED}] {user_input}")
