"""
actions/__init__.py - actions module file for handling various actions

Cole, Mia: s8248723
Matta, Ishi: s8239982
Singh, Lovedeep: s8208559
"""

# Action definition list constant — maps integer indices to action names displayed in the menu
ACTIONS = [
    "Save and Exit",        # 0
    "Help",                 # 1
    "Add Staff",            # 2
    "Add Patient",          # 3
    "Search By Name",       # 4
    "List Staff",           # 5
    "List Patients",        # 6
    "Record Patient Attended by a Specific Nurse",  # 7
    "Launch Dashboard",     # 8
]

def handle_actions(clinic_manager, action):
    # Lazy imports to avoid circular dependencies — each module handles a specific UI flow
    from . import (
        dashboard,
        list_patients,
        list_staff,
        add_staff,
        add_patient,
        search,
        record_patient,
    )
    import printer

    if action == 0:
        # Save all clinic data to disk and exit the application
        printer.clear()
        print("Saving...")
        clinic_manager.save_data()
        print("See you later!")

    elif action == 1:
        # Help action — currently only clears the screen (help content not yet implemented)
        printer.clear()

    elif action == 2:
        # Prompt the user to add a new staff member; show error if the operation fails
        if not add_staff.handle_add_staff(clinic_manager):
            printer.clear()
            printer.error("Failed to add staff, try again!")
        print()

    elif action == 3:
        # Prompt the user to add a new patient; show error if the operation fails
        if not add_patient.handle_add_patient(clinic_manager):
            printer.clear()
            printer.error("Failed to add patient, try again!")
        print()

    elif action == 4:
        # Clear the screen and launch the name-based search flow
        printer.clear()
        search.handle_search(clinic_manager)

    elif action == 5:
        # Clear the screen and display the full list of staff members
        printer.clear()
        list_staff.handle_list_staff(clinic_manager)

    elif action == 6:
        # Clear the screen and display the full list of patients
        printer.clear()
        list_patients.handle_list_patients(clinic_manager)

    elif action == 7:
        # Clear the screen and record a patient attendance entry for a specific nurse
        printer.clear()
        record_patient.handle_record_patient(clinic_manager)

    elif action == 8:
        # Launch the live dashboard view (no screen clear — dashboard manages its own display)
        dashboard.handle_dashboard(clinic_manager)

    else:
        # Fallback for any unrecognized action index — should not occur under normal usage
        printer.clear()
        print(f"You chose {ACTIONS[action]}")
        print()
