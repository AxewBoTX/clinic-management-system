"""
list_staff.py - prints a staff table

Cole, Mia: s8248723
Matta, Ishi: s8239982
Singh, Lovedeep: s8208559
"""

def handle_list_staff(clinic_manager):
    # Displays all registered staff members in a formatted CLI table using the Rich library.
    # Shows staff ID, name, type, hours worked, shift budget (Doctor only), and attendance (Nurse only).
    from rich.console import Console
    from rich.table import Table
    from rich import box
    import printer

    # If no staff are registered, show an info message and skip table rendering
    if len(clinic_manager.staff) == 0:
        printer.info("You have no staff")
    else:
        # Initialize the Rich console and configure the table with rounded borders
        console = Console()
        table = Table(show_header=True, header_style="bold", box=box.ROUNDED)

        # Define the table columns
        table.add_column("Staff ID")
        table.add_column("Name")
        table.add_column("Type")
        table.add_column("Hours")
        table.add_column("Budget")
        table.add_column("Attendance")

        # Populate the table with one row per staff member
        for curr_staff in clinic_manager.staff.values():
            # Default both role-specific fields to "NONE" before checking staff type
            budget = "NONE"
            attendance = "NONE"

            if curr_staff.get_type() == "doctor":
                # Doctors have a shift budget but don't track patient attendance
                budget = f"${curr_staff.shift_budget}"
            else:
                # Nurses track daily patient attendance but don't have a shift budget
                attendance = str(curr_staff.patients_attended_today)

            table.add_row(
                str(curr_staff.staff_id),
                curr_staff.name,
                curr_staff.get_type().title(),  # e.g. "doctor" → "Doctor" (same .upper() note as handle_list_patients applies here)
                str(curr_staff.hours_worked),
                str(budget),
                attendance,
            )

        # Render and print the completed table to the terminal
        console.print(table)

    # Print a blank line for spacing after the table or info message
    print()
