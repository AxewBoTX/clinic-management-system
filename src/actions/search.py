def handle_search(clinic_manager):
    import printer
    from medical_staff import Nurse, Doctor
    from patient import RegularPatient, VIPPatient
    from rich.console import Console
    from rich.table import Table
    from rich import box

    printer.clear()
    print(
        f"{'='*15} {printer.BOLD}{printer.UNDERLINE}Search By Name{printer.END_FORMAT} {'='*15}"
    )
    print()

    search_input = input("Enter the name: ")
    search_results = clinic_manager.search(search_input)

    printer.clear()
    if len(search_results) == 0:
        printer.error("No entry with this name")
    else:
        console = Console()
        table = Table(show_header=False, box=box.ROUNDED)
        for item in search_results:
            if isinstance(item, Nurse):
                table.add_row(
                    "Nurse",
                    f"ID: {item.staff_id}",
                    f"Name: {item.name}",
                    f"Hours: {item.hours_worked}",
                    f"Attendance: {item.patients_attended_today}",
                )
            elif isinstance(item, Doctor):
                table.add_row(
                    "Doctor",
                    f"ID: {item.staff_id}",
                    f"Name: {item.name}",
                    f"Hours: {item.hours_worked}",
                    f"Budget: ${item.shift_budget}",
                )
            elif isinstance(item, VIPPatient):
                table.add_row(
                    "VIPPatient",
                    f"ID: {item.patient_id}",
                    f"Name: {item.name}",
                    f"Visits: {item.visits}",
                    f"Priority: ${item.priority_rank}",
                )
            elif isinstance(item, RegularPatient):
                table.add_row(
                    "RegularPatient",
                    f"ID: {item.patient_id}",
                    f"Name: {item.name}",
                    f"Visits: {item.visits}",
                )
            else:
                print("Unknown Item")
        console.print(table)
    print()
