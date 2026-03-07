import printer

def handle_list_patients(clinic_manager):
    if len(clinic_manager.patients) == 0:
        printer.info("You have no patients")
    else:
        print(f"{printer.UNDERLINE}{printer.BOLD}{'Name':>10}{'Type':>20}{'Contact':>20}{'Visits':>20}{'Priority':>20}{printer.END_FORMAT:>10}")
        for name, patient in clinic_manager.patients.items():
            priority = "NONE"
            if patient.get_type() == "vip":
                priority = patient.priority_rank
            print(f"{name:>10}{patient.get_type().title():>20}{patient.contact_details:>20}{patient.visits:>20}{priority:>20}")
    print()
