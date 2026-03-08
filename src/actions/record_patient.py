def handle_record_patient(clinic_manager):
    import printer

    try:
        printer.clear()
        print(
            f"{'='*15} {printer.BOLD}{printer.UNDERLINE}Record Patient Attendance{printer.END_FORMAT} {'='*15}"
        )
        print()

        staff_id = int(input("Staff ID: "))
        patient_num = int(input("Total Patients: "))
        result = clinic_manager.record_patient_attendance(staff_id, patient_num)
        if result is True:
            printer.clear()
            printer.info("Successfully record patient attendance")
            print()
        else:
            printer.clear()
            printer.error("Failed to record patient attendance, either the STAFF_ID was incorrect or the corresponding staff is not a Nurse")
            print()
    except ValueError:
        printer.clear()
        printer.error("You have to enter a valid input")
        print()
