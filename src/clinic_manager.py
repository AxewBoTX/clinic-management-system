"""
clinic_manager.py - defines the ClinicManager base class

Cole, Mia: s8248723
Matta, Ishi: s8239982
Singh, Lovedeep: s8208559
"""

import pickle
from medical_staff import Nurse, Doctor
from slugify import slugify
from patient import RegularPatient, VIPPatient

class ClinicManager:
    def __init__(self):
        # Initialize empty dictionaries to store staff and patient records
        self.staff = {}
        self.patients = {}

    def save_data(self, file_name="clinic_data.pkl"):
        # Serialize and save staff and patient data to a pickle file
        data = {"staff": self.staff, "patients": self.patients}
        with open(file_name, "wb") as file:
            pickle.dump(data, file)

    def load_data(self, file_name="clinic_data.pkl"):
        # Load previously saved staff and patient data from a pickle file.
        # If the file doesn't exist, initialize with empty dictionaries.
        try:
            with open(file_name, "rb") as file:
                data = pickle.load(file)
                self.staff = data.get("staff", {})
                self.patients = data.get("patients", {})
        except FileNotFoundError:
            self.staff = {}
            self.patients = {}

    def add_nurse(self, staff_id, name, hours_worked=0):
        # Add a new nurse to the staff registry.
        # If a staff member with the same ID already exists, return that existing record.
        # Otherwise, create a new Nurse, log their hours, and store them.
        for curr_staff in self.staff.values():
            if curr_staff.staff_id == staff_id:
                return curr_staff
        nurse = Nurse(name, staff_id)
        nurse.add_hours(hours_worked)
        self.staff[nurse.staff_id] = nurse
        return None

    def add_doctor(self, staff_id, name, shift_budget, hours_worked=0):
        # Add a new doctor to the staff registry.
        # If a staff member with the same ID already exists, return that existing record.
        # Otherwise, create a new Doctor with a shift budget, log their hours, and store them.
        for curr_staff in self.staff.values():
            if curr_staff.staff_id == staff_id:
                return curr_staff
        doctor = Doctor(name, staff_id, shift_budget)
        doctor.add_hours(hours_worked)
        self.staff[doctor.staff_id] = doctor
        return None

    def add_regular_patient(self, patient_id, name, contact_details):
        # Register a new regular patient.
        # If a patient with the same ID already exists, return that existing record.
        # Otherwise, create and store a new RegularPatient.
        for curr_patient in self.patients.values():
            if curr_patient.patient_id == patient_id:
                return curr_patient
        patient = RegularPatient(name, patient_id, contact_details)
        self.patients[patient_id] = patient
        return None

    def add_vip_patient(self, patient_id, name, contact_details, priority_rank):
        # Register a new VIP patient with a priority rank.
        # If a patient with the same ID already exists, return that existing record.
        # Otherwise, create and store a new VIPPatient.
        for curr_patient in self.patients.values():
            if curr_patient.patient_id == patient_id:
                return curr_patient
        patient = VIPPatient(name, patient_id, contact_details, priority_rank)
        self.patients[patient_id] = patient
        return None

    def search(self, search_input):
        # Search for staff or patients by name using slugified (URL-safe) string matching.
        # Returns a list of all matching staff and patient objects.
        search_input = slugify(search_input)
        search_list = list(self.staff.values())
        search_list.extend(list(self.patients.values()))
        search_results = []
        for item in search_list:
            if search_input in slugify(item.name):
                search_results.append(item)
        return search_results

    def record_patient_attendance(self, staff_id, patient_id):
        # Record a patient visit attended by a nurse.
        # Validates that the staff member exists and is a Nurse, and that the patient exists.
        # Increments attendance count for both the nurse and the patient.
        # Returns True on success, False if validation fails.
        if staff_id in self.staff:
            staff = self.staff[staff_id]
            if isinstance(staff, Nurse):
                if patient_id in self.patients:
                    patient = self.patients[patient_id]
                    staff.record_patient_attendance(1)
                    patient.add_visits(1)
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def generate_daily_report(self) -> dict:
        # Generate a summary report of the clinic's daily activity.
        # Includes total staff, nurse/doctor counts, patients attended,
        # the top-performing nurse (by patients attended), total patients, and VIP patient count.
        output = {}
        output["total_staff"] = len(self.staff)
        nurse_count = 0
        patients_attended_today = 0
        top_nurse = None
        for curr_staff in self.staff.values():
            if isinstance(curr_staff, Nurse):
                # Increase the number of nurses in the nurse_count
                nurse_count += 1
                patients_attended_today += curr_staff.patients_attended_today

                # Track the staff member who attended the most patients today
                if top_nurse is None:
                    top_nurse = curr_staff
                else:
                    if curr_staff.patients_attended_today > top_nurse.patients_attended_today:
                        top_nurse = curr_staff
        output["nurses"] = nurse_count
        output["patients_attended"] = patients_attended_today
        if top_nurse is None:
            output["top_nurse"] = "NONE"
        else:
            output["top_nurse"] = top_nurse.name
        doctor_count = 0
        for curr_staff in self.staff.values():
            if isinstance(curr_staff, Doctor):
                doctor_count += 1
        output["doctors"] = doctor_count
        output["total_patients"] = len(self.patients)
        vip_patient_count = 0
        for curr_patient in self.patients.values():
            if isinstance(curr_patient, VIPPatient):
                vip_patient_count += 1
        output["vip_patients"] = vip_patient_count
        return output
