import printer

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
