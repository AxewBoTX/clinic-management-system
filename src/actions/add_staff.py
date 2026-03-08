def handle_add_staff(clinic_manager) -> bool:
    import printer

    try:
        printer.clear()
        print(
            f"{'='*15} {printer.BOLD}{printer.UNDERLINE}Add Staff{printer.END_FORMAT} {'='*15}"
        )
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
            result = clinic_manager.add_doctor(staff_id, staff_name, shift_budget)
            if result is None:
                printer.info(
                    f"Sucessfully added Doctor: ({staff_id}, {staff_name}, {shift_budget})"
                )
            else:
                printer.error(
                    f"Doctor with this STAFF_ID already exists:\n({result.name}, {result.staff_id})"
                )
        else:
            printer.clear()
            result = clinic_manager.add_nurse(staff_id, staff_name)
            if result is None:
                printer.info(f"Successfully added Nurse: ({staff_id}, {staff_name})")
            else:
                printer.error(
                    f"Nurse with this STAFF_ID already exists:\n({result.name}, {result.staff_id})"
                )
        return True
    except ValueError:
        return False
