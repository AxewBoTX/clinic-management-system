"""
dashboard.py - defines the Dashboard class for GUI dashboard

Cole, Mia: s8248723
Matta, Ishi: s8239982
Singh, Lovedeep: s8208559
"""

import tkinter as tk
import tkinter.font as tk_font
import printer
import colors

class Dashboard(tk.Tk):
    def __init__(self):
        # Initialize the tkinter root window with clinic branding and default styling
        super().__init__()

        # Set Arial as the global default font across all widgets
        default_font = tk_font.nametofont("TkDefaultFont")
        default_font.configure(family="Arial", size=14)

        # Configure the main window title, size, and background color
        self.title("Clinic Management System")
        self.geometry("1280x720")
        self.configure(bg=colors.BASE)

    def render(self, clinic_manager):
        # Builds and renders the full dashboard UI, then starts the tkinter event loop.
        # A more accurate name would be something like `render` or `show`.

        # Re-apply window settings in case they were changed before this method was called
        self.title("Clinic Management System")
        self.geometry("1280x720")

        # Fetch the latest daily report data from the clinic manager
        report = clinic_manager.generate_daily_report()

        # Render the main dashboard title label
        header = tk.Label(
            self,
            text="Clinic Management System",
            font=("Arial", 22, "bold"),
            bg=colors.BASE,
            fg=colors.BLUE,
        )
        header.pack(pady=(20, 4))

        # Render the "Daily Report" subtitle below the header
        subtitle = tk.Label(
            self,
            text="Daily Report",
            font=("Arial", 13, "italic"),
            bg=colors.BASE,
            fg=colors.TEXT,
        )
        subtitle.pack(pady=(0, 16))

        # Create a frame to hold the report metrics table
        table_frame = tk.Frame(self, bg=colors.BASE)

        # Iterate over each key-value pair in the report and render a two-column table row
        for row, (key, value) in enumerate(report.items()):
            # Format the key from snake_case to Title Case for display (e.g. "total_staff" → "Total Staff")
            metric = key.replace("_", " ").title()

            # Left column: metric name label with a visible border via highlight settings
            tk.Label(
                table_frame,
                text=metric,
                bg=colors.BASE,
                fg=colors.TEXT,
                highlightbackground=colors.TEXT,
                highlightthickness=2,
                relief="flat",
                width=20,
            ).grid(row=row, column=0, padx=6, pady=8)

            # Right column: metric value label with matching border styling
            tk.Label(
                table_frame,
                text=value,
                bg=colors.BASE,
                fg=colors.TEXT,
                highlightbackground=colors.TEXT,
                highlightthickness=2,
                relief="flat",
                width=20,
            ).grid(row=row, column=1, padx=6, pady=8)

        # Pack the completed table into the window and center it
        table_frame.pack(expand=True)

        # Start the tkinter event loop — blocks until the dashboard window is closed
        self.mainloop()


def handle_dashboard(clinic_manager):
    # Entry point for launching the dashboard from the CLI action handler.
    # Clears the terminal, opens the tkinter dashboard window, and clears again on close.
    printer.clear()
    dashboard = Dashboard()
    dashboard.render(clinic_manager)

    # Clear the terminal once the user closes the dashboard window
    printer.clear()
