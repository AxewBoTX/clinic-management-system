"""
record_patient.py - handles recording patient attendance

Cole, Mia: s8248723
Matta, Ishi: s8239982
Singh, Lovedeep: s8208559
"""

def handle_record_patient(clinic_manager):
    # Handles the interactive CLI flow for recording a patient visit attended by a nurse.
    # Prompts the user for a staff ID and patient ID, then delegates to the clinic manager.
    # Displays a success or error message depending on the outcome.
    import printer
    try:
        # Display the Record Patient Attendance header
        printer.clear()
        print(
            f"{'='*15} Record Patient Attendance {'='*15}"
        )
        print()

        # Collect the nurse's staff ID and the patient's ID from the user
        staff_id = int(input("Staff ID: "))
        patient_id = int(input("Patient ID: "))

        # Attempt to record the attendance via the clinic manager
        result = clinic_manager.record_patient_attendance(staff_id, patient_id)

        if result is True:
            # Attendance recorded successfully — notify the user
            printer.clear()
            printer.success("Successfully recorded patient attendance")
            print()
        else:
            # Failed to record — either the IDs don't exist or the staff member is not a Nurse
            printer.clear()
            printer.error(
                "Failed to record patient attendance, either the STAFF_ID/PATIENT_ID was incorrect or the corresponding staff is not a Nurse"
            )
            print()

    except ValueError:
        # Triggered if the user enters a non-integer for either ID field
        printer.clear()
        printer.error("You have to enter a valid input")
        print()
