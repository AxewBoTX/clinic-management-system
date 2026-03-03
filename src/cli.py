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

def handle_list_patients(clinic_manager):
    if len(clinic_manager.patients) == 0:
        printer.info("You have no patients")
    else:
        print(f"{printer.UNDERLINE}{printer.BOLD}{'Name':>10}{'Type':>20}{'Contact':>20}{'Visits':>20}{'Priority':>20}{printer.END_FORMAT:>10}")
        for name, patient in clinic_manager.patients.items():
            priority = "NONE"
            if patient.get_type() == "vip":
                priority = patient.priority_rank
            print(f"{name:>10}{patient.get_type().title():>20}{patient.contact_details:>20}{patient.visits:>20}{priority:>20}")
    print()

def handle_list_staff(clinic_manager):
    if len(clinic_manager.staff) == 0:
        printer.info("You have no staff")
    else:
        print(f"{printer.UNDERLINE}{printer.BOLD}{'ID':>10}{'Name':>20}{'Type':>20}{'Hours':>20}{'Budget':>20}{printer.END_FORMAT:>10}")
        for name, staff in clinic_manager.staff.items():
            budget = "NONE"
            if staff.get_type() == "doctor":
                budget = f"${staff.shift_budget}"
            print(f"{staff.staff_id:>10}{name:>20}{staff.get_type().title():>20}{staff.hours_worked:>20}{budget:>20}")
    print()

def handle_add_staff(clinic_manager) -> bool:
    try:
        printer.clear()
        print(f"{'='*15} {printer.BOLD}{printer.UNDERLINE}Add Staff{printer.END_FORMAT} {'='*15}")
        print()
        print("1. Nurse")
        print("2. Doctor")
        print()
        print("Which staff do you want to add ?")

        staff_input = int(input("> "))
        if staff_input != 1 and staff_input != 2:
            return False
        print()

        staff_id = input("Staff ID: ")
        staff_name = input("Name: ")
        if staff_input == 2:
            shift_budget = float(input("Shift Budget: "))
            printer.clear()
            clinic_manager.add_doctor(staff_id, staff_name, shift_budget)
            printer.info(f"Added Doctor: ({staff_id}, {staff_name}, {shift_budget})")
        else:
            printer.clear()
            clinic_manager.add_nurse(staff_id, staff_name)
            printer.info(f"Added Nurse: ({staff_id}, {staff_name})")
        return True
    except ValueError:
        return False

def handle_actions(clinic_manager, action):
    if action == 0:
        printer.clear()
        print("Saving...")
        print("See you later!")
    elif action == 1:
        printer.clear()
    elif action == 2:
        if not handle_add_staff(clinic_manager):
            printer.clear()
            printer.error("Failed to add staff, try again!")
        print()
    elif action == 5:
        printer.clear()
        handle_list_staff(clinic_manager)
    elif action == 6:
        printer.clear()
        handle_list_patients(clinic_manager)
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
