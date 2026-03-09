"""
search.py - handles basic searching operation by name

Cole, Mia: s8248723
Matta, Ishi: s8239982
Singh, Lovedeep: s8208559
"""

def handle_search(clinic_manager):
    # Handles the interactive CLI flow for searching staff and patients by name.
    # Displays matching results in a Rich table, with fields tailored to each record type.
    import printer
    from medical_staff import Nurse, Doctor
    from patient import RegularPatient, VIPPatient
    from rich.console import Console
    from rich.table import Table
    from rich import box

    # Display the Search By Name header
    printer.clear()
    print(
        f"{'='*15} Search By Name {'='*15}"
    )
    print()

    # Prompt the user to enter a name to search for
    search_input = input("Enter the name: ")

    # Delegate the search to the clinic manager (uses slugified name matching)
    search_results = clinic_manager.search(search_input)
    printer.clear()

    if len(search_results) == 0:
        # No matches found — notify the user
        printer.error("No entry with this name")
    else:
        # Initialize the Rich console and a headerless table with rounded borders
        console = Console()
        table = Table(show_header=False, box=box.ROUNDED)

        # Add a row for each result, formatted according to the record type
        for item in search_results:
            if isinstance(item, Nurse):
                # Nurse row: type, ID, name, hours worked, and daily attendance count
                table.add_row(
                    "Nurse",
                    f"ID: {item.staff_id}",
                    f"Name: {item.name}",
                    f"Hours: {item.hours_worked}",
                    f"Attendance: {item.patients_attended_today}",
                )
            elif isinstance(item, Doctor):
                # Doctor row: type, ID, name, hours worked, and shift budget
                table.add_row(
                    "Doctor",
                    f"ID: {item.staff_id}",
                    f"Name: {item.name}",
                    f"Hours: {item.hours_worked}",
                    f"Budget: ${item.shift_budget}",
                )
            elif isinstance(item, VIPPatient):
                # VIP patient row: type, ID, name, visit count, and priority rank
                # NOTE: priority_rank is prefixed with "$" — likely a copy-paste error from budget (bug)
                table.add_row(
                    "VIPPatient",
                    f"ID: {item.patient_id}",
                    f"Name: {item.name}",
                    f"Visits: {item.visits}",
                    f"Priority: ${item.priority_rank}",
                )
            elif isinstance(item, RegularPatient):
                # Regular patient row: type, ID, name, and visit count (no priority field)
                table.add_row(
                    "RegularPatient",
                    f"ID: {item.patient_id}",
                    f"Name: {item.name}",
                    f"Visits: {item.visits}",
                )
            else:
                # Fallback for any unrecognized result type — should not occur under normal usage
                print("Unknown Item")

        # Render and print the completed search results table
        console.print(table)

    # Print a blank line for spacing after the results or error message
    print()
