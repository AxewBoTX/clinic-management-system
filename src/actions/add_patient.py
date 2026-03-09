"""
add_patient.py - handles add_patient action

Cole, Mia: s8248723
Matta, Ishi: s8239982
Singh, Lovedeep: s8208559
"""

def handle_add_patient(clinic_manager) -> bool:
    # Handles the interactive CLI flow for adding a new patient (VIP or Regular).
    # Prompts the user for patient type, ID, name, contact details, and priority rank (VIP only).
    # Returns True if the patient was successfully added, False if input is invalid or cancelled.
    import printer

    try:
        # Display the Add Patient header
        printer.clear()
        print(
            f"{'='*15} Add Patient {'='*15}"
        )
        print()

        # Show patient type options
        print("1. VIP")
        print("2. Regular")
        print()

        # Prompt user to select patient type
        print("Which patient do you want to add ?")
        patient_input = int(input("> "))

        # Reject any input that isn't 1 (VIP) or 2 (Regular)
        if patient_input != 1 and patient_input != 2:
            return False

        # Collect common patient details
        print()
        patient_id = input("Patient ID: ")
        patient_name = input("Name: ")
        contact_details = input("Contact Details: ")

        if patient_input == 1:
            # VIP patient requires an additional priority rank
            priority_rank = int(input("Priority Rank: "))
            printer.clear()
            clinic_manager.add_vip_patient(patient_id, patient_name, contact_details, priority_rank)
            printer.info(
                f"Added VIP Patient: ({patient_name}, {contact_details}, {priority_rank})"
            )
        else:
            # Regular patient only needs name and contact details
            printer.clear()
            clinic_manager.add_regular_patient(patient_id, patient_name, contact_details)
            printer.info(f"Added Regular Patient: ({patient_name}, {contact_details})")

        return True

    except ValueError:
        # Triggered if the user enters a non-integer for patient type or priority rank
        return False
