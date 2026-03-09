"""
list_patients.py - prints a patient table

Cole, Mia: s8248723
Matta, Ishi: s8239982
Singh, Lovedeep: s8208559
"""

def handle_list_patients(clinic_manager):
    # Displays all registered patients in a formatted CLI table using the Rich library.
    # Shows patient ID, name, type, contact details, visit count, and priority rank (VIP only).
    from rich.console import Console
    from rich.table import Table
    from rich import box
    import printer

    # If no patients are registered, show an info message and skip table rendering
    if len(clinic_manager.patients) == 0:
        printer.info("You have no patients")
    else:
        # Initialize the Rich console and configure the table with rounded borders
        console = Console()
        table = Table(show_header=True, header_style="bold", box=box.ROUNDED)

        # Define the table columns
        table.add_column("Patient ID")
        table.add_column("Name")
        table.add_column("Type")
        table.add_column("Contact")
        table.add_column("Visits")
        table.add_column("Priority")

        # Populate the table with one row per patient
        for curr_patient in clinic_manager.patients.values():
            # Default priority to "NONE" for regular patients
            priority = "NONE"

            # Override priority with the actual rank if the patient is VIP
            if curr_patient.get_type() == "vip":
                priority = curr_patient.priority_rank

            table.add_row(
                str(curr_patient.patient_id),
                curr_patient.name,
                curr_patient.get_type().title(),  # e.g. "vip" → "Vip" (consider .upper() for "VIP")
                str(curr_patient.contact_details),
                str(curr_patient.visits),
                str(priority),
            )

        # Render and print the completed table to the terminal
        console.print(table)

    # Print a blank line for spacing after the table or info message
    print()
