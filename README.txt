================================================================
        Clinic Management System - README
================================================================

Authors:
  Cole, Mia       - s8248723
  Matta, Ishi     - s8239982
  Singh, Lovedeep - s8208559

----------------------------------------------------------------
OVERVIEW
----------------------------------------------------------------
The Clinic Management System is a command-line application for
managing clinic staff and patients. It supports adding and
listing both staff (Nurses and Doctors) and patients (Regular
and VIP), recording patient visits attended by nurses,
searching records by name, and viewing a live daily report via
a graphical dashboard.

Data is persisted between sessions using a local pickle file
(clinic_data.pkl), which is loaded on startup and saved on
exit.

----------------------------------------------------------------
FILE STRUCTURE
----------------------------------------------------------------
  main.py             - Entry point; starts the main action loop
  clinic_manager.py   - Core data manager (staff, patients, reports)
  actions.py          - Action definitions and dispatch handler
  medical_staff.py    - MedicalStaff base class; Nurse and Doctor
  patient.py          - Patient base class; RegularPatient and VIPPatient
  dashboard.py        - Tkinter GUI dashboard for the daily report
  printer.py          - CLI printing utilities (clear, info, error, success)
  colors.py           - Color constants for Rich and Tkinter styling
  add_staff.py        - CLI flow for adding a staff member
  add_patient.py      - CLI flow for adding a patient
  list_staff.py       - CLI flow for listing all staff
  list_patients.py    - CLI flow for listing all patients
  record_patient.py   - CLI flow for recording patient attendance
  search.py           - CLI flow for searching by name

----------------------------------------------------------------
HOW TO RUN
----------------------------------------------------------------
Requirements:
  - Python 3.8+
  - rich          (pip install rich)
  - python-slugify (pip install python-slugify)
  - tkinter       (included with most Python installations)

To start the application:
  python main.py

On launch, the program will automatically load any previously
saved data from clinic_data.pkl if it exists.

----------------------------------------------------------------
USAGE
----------------------------------------------------------------
The application is menu-driven. After launching, the following
actions are available:

  0 - Save and Exit
        Saves all current data to clinic_data.pkl and exits.

  1 - Help
        Clears the screen (help content not yet implemented).

  2 - Add Staff
        Prompts for staff type (Nurse or Doctor), ID, name,
        and shift budget (Doctor only). Rejects duplicate IDs.

  3 - Add Patient
        Prompts for patient type (Regular or VIP), ID, name,
        contact details, and priority rank (VIP only).
        Rejects duplicate IDs.

  4 - Search By Name
        Searches all staff and patients by name. Uses fuzzy
        slug-based matching, so partial names are supported.

  5 - List Staff
        Displays a formatted table of all registered staff,
        including ID, name, type, hours worked, shift budget
        (Doctor), and daily attendance count (Nurse).

  6 - List Patients
        Displays a formatted table of all registered patients,
        including ID, name, type, contact details, visit count,
        and priority rank (VIP only).

  7 - Record Patient Attended by a Specific Nurse
        Records a patient visit. Requires a valid Nurse staff
        ID and a valid patient ID. Only Nurses can record
        attendance (not Doctors).

  8 - Launch Dashboard
        Opens a graphical Tkinter window showing a summary of
        the day's activity, including staff counts, patients
        attended, top nurse, and VIP patient count.

----------------------------------------------------------------
KNOWN LIMITATIONS
----------------------------------------------------------------
1. No autosave on Ctrl-C:
   If the user terminates the program using Ctrl-C instead of
   selecting action 0 (Save and Exit), the program will crash
   without saving any data. Any changes made during that session
   will be lost. Always use action 0 to exit safely.

2. Rich formatting may not work on all terminals:
   On some terminals (such as Python IDLE), Rich text formatting
   is not supported. This means the screen may not clear
   properly, and the formatted tables in List Staff and List
   Patients may not render as expected. It is recommended to run
   the application in a standard terminal such as bash, zsh,
   PowerShell, or the Windows Command Prompt.

3. Dashboard does not refresh automatically:
   The Tkinter dashboard window renders the daily report once
   when launched and does not update in real time. To see
   updated figures, close the dashboard and relaunch it from
   the action menu.

4. No ability to edit or delete records:
   Once a staff member or patient has been added to the system,
   there is no way to edit or delete their record. The only
   supported operations are adding new records and viewing
   existing ones. If incorrect information is entered, the
   entire clinic_data.pkl file would need to be manually
   removed to reset the system.

5. No patient-to-nurse assignment:
   The system does not support assigning specific patients to
   specific nurses. The only nurse-patient relationship tracked
   is a numerical count of how many patients a nurse has
   attended on a given day. There is no way to see which
   particular patients a nurse has seen, or which nurse a
   patient has been assigned to.

----------------------------------------------------------------
USE OF AI
----------------------------------------------------------------
AI assistance (Claude by Anthropic, ChatGPT by OpenAI) was used in this project
solely to help write and improve code comments across the
source files. The goal was to make the codebase more readable
and understandable for other developers.

AI had minimal-to-no involvement in writing the program logic, designing
the system architecture, or implementing any features. All
functional code was written entirely by the authors listed
above. AI involvement was limited strictly to assisting with
the wording and clarity of inline comments.

----------------------------------------------------------------
