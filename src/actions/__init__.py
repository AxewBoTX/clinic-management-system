from . import dashboard, list_patients, list_staff, add_staff, add_patient, search, record_patient
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

def handle_actions(clinic_manager, action):
    if action == 0:
        printer.clear()
        print("Saving...")
        print("See you later!")
    elif action == 1:
        printer.clear()
    elif action == 2:
        if not add_staff.handle_add_staff(clinic_manager):
            printer.clear()
            printer.error("Failed to add staff, try again!")
        print()
    elif action == 3:
        if not add_patient.handle_add_patient(clinic_manager):
            printer.clear()
            printer.error("Failed to add patient, try again!")
        print()
    elif action == 4:
        printer.clear()
        search.handle_search(clinic_manager)
    elif action == 5:
        printer.clear()
        list_staff.handle_list_staff(clinic_manager)
    elif action == 6:
        printer.clear()
        list_patients.handle_list_patients(clinic_manager)
    elif action == 7:
        printer.clear()
        record_patient.handle_record_patient(clinic_manager)
    elif action == 8:
        dashboard.handle_dashboard(clinic_manager)
    else:
        printer.clear()
        print(f"You chose {printer.UNDERLINE}{ACTIONS[action]}{printer.END_FORMAT}")
        print()
