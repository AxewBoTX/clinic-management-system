def handle_list_staff(clinic_manager):
    from rich.console import Console
    from rich.table import Table
    from rich import box
    import printer

    if len(clinic_manager.staff) == 0:
        printer.info("You have no staff")
    else:
        console = Console()
        table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        table.add_column("Staff ID")
        table.add_column("Name")
        table.add_column("Type")
        table.add_column("Hours")
        table.add_column("Budget")
        table.add_column("Attendance")
        for curr_staff in clinic_manager.staff.values():
            budget = "NONE"
            attendance = "NONE"
            if curr_staff.get_type() == "doctor":
                budget = f"${curr_staff.shift_budget}"
            else:
                attendance = str(curr_staff.patients_attended_today)
            table.add_row(
                str(curr_staff.staff_id),
                curr_staff.name,
                curr_staff.get_type().title(),
                str(curr_staff.hours_worked),
                str(budget),
                attendance
            )
        console.print(table)
    print()
