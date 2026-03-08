def handle_list_patients(clinic_manager):
    from rich.console import Console
    from rich.table import Table
    from rich import box
    import printer

    if len(clinic_manager.patients) == 0:
        printer.info("You have no patients")
    else:
        console = Console()
        table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        table.add_column("Patient ID")
        table.add_column("Name")
        table.add_column("Type")
        table.add_column("Contact")
        table.add_column("Visits")
        table.add_column("Priority")
        for curr_patient in clinic_manager.patients.values():
            priority = "NONE"
            if curr_patient.get_type() == "vip":
                priority = curr_patient.priority_rank
            table.add_row(
                str(curr_patient.patient_id),
                curr_patient.name,
                curr_patient.get_type().title(),
                str(curr_patient.contact_details),
                str(curr_patient.visits),
                str(priority),
            )
        console.print(table)
    print()
