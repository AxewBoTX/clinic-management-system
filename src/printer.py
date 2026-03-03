import cli
import os

INFO = '\033[96m'
WARNING = '\033[93m'
FAIL = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END_FORMAT = '\033[0m'

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def intro():
    print(f"{'='*15} Welcome to the {BOLD}{UNDERLINE}Clinic Management System{END_FORMAT} {'='*15}")
    print()

def actions():
    for i in range(0, len(cli.ACTIONS)):
        print(f"{i}. {cli.ACTIONS[i]}")
    print()
    print("What would you like to do ?")

def info(input: str):
    print(f"{INFO}{BOLD}{UNDERLINE}[INFO]{END_FORMAT} " + input)
def error(input: str):
    print(f"{FAIL}{BOLD}{UNDERLINE}[ERROR]{END_FORMAT} " + input)

