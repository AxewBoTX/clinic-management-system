import tkinter as tk
import tkinter.font as tk_font
import printer

class Dashbaord(tk.Tk):
    def __init__(self):
        super().__init__()
        default_font = tk_font.nametofont("TkDefaultFont")
        default_font.configure(family="Arial", size=14)
        self.title("Clinic Management System")
        self.geometry("1280x720")
    def update_loop(self, clinic_manager):
        self.title("Clinic Management System")
        self.geometry("1280x720")

        report = clinic_manager.generate_daily_report()

        table_frame = tk.Frame(self)
        for row, (key, value) in enumerate(report.items(), start=1):
            metric = key.replace("_", " ").title()
            tk.Label(table_frame, text=metric, borderwidth=3, relief="ridge",
                     width=20).grid(row=row, column=0, padx=4)
            tk.Label(table_frame, text=value, borderwidth=3, relief="ridge",
                     width=20).grid(row=row, column=1, padx=4)
        table_frame.pack(expand=True)

        self.mainloop()

def handle_dashboard(clinic_manager):
    printer.clear()
    dashboard = Dashbaord()
    dashboard.update_loop(clinic_manager)
    printer.clear()
