import tkinter as tk
import printer

ACTIONS = [
    "Exit",
    "Help",
    "Add Staff",
    "Add Patient",
    "Search By Name",
    "List Staff",
    "List Patients",
    "Record Patient Attended by a Specific Nurse",
    "Launch Dashboard",
]

def handle_actions(action):
    if action == 0:
        printer.clear()
        print("Saving...")
        print("See you later!")
    elif action == 1:
        printer.clear()
    elif action == 8:
        printer.clear()
        root = tk.Tk()
        root.title("Clinic Management System")
        root.geometry("1280x720")
        label = tk.Label(root, text="Hello, World!", font=("Arial", 16))
        label.pack(pady=40)
        button = tk.Button(
            root,
            text="Click Me",
            font=("Arial", 14),
            command=lambda: printer.info("You just clicked a button")
        )
        button.pack(pady=20)
        root.mainloop()
        printer.clear()
    else:
        printer.clear()
        print(f"You chose {printer.UNDERLINE}{ACTIONS[action]}{printer.END_FORMAT}")
        print()
