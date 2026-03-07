import tkinter as tk
import printer

def handle_dashboard(clinic_manager):
    printer.clear()
    root = tk.Tk()
    root.title("Clinic Management System")
    root.geometry("1280x720")
    label = tk.Label(root, text="Hello, World!", font=("Arial", 16))
    label.pack(pady=40)
    button = tk.Button(
        root,
        text="Click Me",
        font=("Arial", 14),
        command=lambda: printer.info("You just clicked a button")
    )
    button.pack(pady=20)
    root.mainloop()
    printer.clear()
