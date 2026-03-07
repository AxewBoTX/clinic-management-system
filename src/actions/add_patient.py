import printer

def handle_add_patient(clinic_manager) -> bool:
    try:
        printer.clear()
        print(f"{'='*15} {printer.BOLD}{printer.UNDERLINE}Add Patient{printer.END_FORMAT} {'='*15}")
        print()
        print("1. VIP")
        print("2. Regular")
        print()
        print("Which patient do you want to add ?")

        patient_input = int(input("> "))
        if patient_input != 1 and patient_input != 2:
            return False
        print()

        contact_details = input("Contact Details: ")
        patient_name = input("Name: ")
        visits = int(input("Visits: "))
        if patient_input == 2:
            priority_rank = int(input("Priority Rank: "))
            printer.clear()
            clinic_manager.add_vip_patient(patient_name, contact_details, visits, priority_rank)
            printer.info(f"Added VIP Patient: ({patient_name}, {contact_details}, {visits}, {priority_rank})")
        else:
            printer.clear()
            clinic_manager.add_regular_patient(patient_name, contact_details, visits)
            printer.info(f"Added Regular Patient: ({patient_name}, {contact_details}, {visits})")
        return True
    except ValueError:
        return False
