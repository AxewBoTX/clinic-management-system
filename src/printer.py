import cli
import os

INFO = '\033[96m'
WARNING = '\033[93m'
FAIL = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ENDC = '\033[0m'

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def intro():
    print(f"{'='*15} Welcome to the {UNDERLINE}Clinic Management System{ENDC} {'='*15}")
    print()

def actions():
    print("What would you like to do ?")
    for i in range(0, len(cli.ACTIONS)):
        print(f"{i}. {cli.ACTIONS[i]}")

def info(input: str):
    print(f"{INFO}{BOLD}{UNDERLINE}[INFO]{ENDC} " + input)
def error(input: str):
    print(f"{FAIL}{BOLD}{UNDERLINE}[ERROR]{ENDC} " + input)

