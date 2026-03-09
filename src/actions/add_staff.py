"""
add_staff.py - handles add_staff action

Cole, Mia: s8248723
Matta, Ishi: s8239982
Singh, Lovedeep: s8208559
"""

def handle_add_staff(clinic_manager) -> bool:
    # Handles the interactive CLI flow for adding a new staff member (Nurse or Doctor).
    # Prompts the user for staff type, ID, name, and shift budget (Doctor only).
    # Returns True if the operation completed (even if duplicate), False if input is invalid.
    import printer

    try:
        # Display the Add Staff header
        printer.clear()
        print(
            f"{'='*15} Add Staff {'='*15}"
        )
        print()

        # Show staff type options
        print("1. Nurse")
        print("2. Doctor")
        print()

        # Prompt user to select staff type
        print("Which staff do you want to add ?")
        staff_input = int(input("> "))

        # Reject any input that isn't 1 (Nurse) or 2 (Doctor)
        if staff_input != 1 and staff_input != 2:
            return False

        # Collect common staff details
        print()
        staff_id = input("Staff ID: ")
        staff_name = input("Name: ")

        if staff_input == 2:
            # Doctor requires an additional shift budget
            shift_budget = float(input("Shift Budget: "))
            printer.clear()
            result = clinic_manager.add_doctor(staff_id, staff_name, shift_budget)

            if result is None:
                # None indicates the doctor was successfully added (no duplicate found)
                printer.success(
                    f"Sucessfully added Doctor: ({staff_id}, {staff_name}, {shift_budget})"
                )
            else:
                # A returned object means a staff member with this ID already exists
                printer.error(
                    f"Doctor with this STAFF_ID already exists:\n({result.name}, {result.staff_id})"
                )
        else:
            # Nurse only requires ID and name
            printer.clear()
            result = clinic_manager.add_nurse(staff_id, staff_name)

            if result is None:
                # None indicates the nurse was successfully added (no duplicate found)
                printer.success(f"Successfully added Nurse: ({staff_id}, {staff_name})")
            else:
                # A returned object means a staff member with this ID already exists
                printer.error(
                    f"Nurse with this STAFF_ID already exists:\n({result.name}, {result.staff_id})"
                )

        return True

    except ValueError:
        # Triggered if the user enters a non-integer for staff type or non-float for shift budget
        return False
