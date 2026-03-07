import printer

def handle_list_staff(clinic_manager):
    if len(clinic_manager.staff) == 0:
        printer.info("You have no staff")
    else:
        print(f"{printer.UNDERLINE}{printer.BOLD}{'ID':>10}{'Name':>20}{'Type':>20}{'Hours':>20}{'Budget':>20}{printer.END_FORMAT:>10}")
        for name, staff in clinic_manager.staff.items():
            budget = "NONE"
            if staff.get_type() == "doctor":
                budget = f"${staff.shift_budget}"
            print(f"{staff.staff_id:>10}{name:>20}{staff.get_type().title():>20}{staff.hours_worked:>20}{budget:>20}")
    print()
