from medical_staff import Nurse, Doctor
from patient import RegularPatient, VIPPatient

class ClinicManager:
    def __init__(self, clinic_name="My Clinic"):
        self.clinic_name = clinic_name
        self.staff = {}
        self.patients = {}

    def add_nurse(self, staff_id, name, hours_worked=0):
        if name in self.staff:
            return False
        nurse = Nurse(name, staff_id)
        nurse.add_hours(hours_worked)
        self.staff[name] = nurse
        return True

    def add_doctor(self, staff_id, name, shift_budget, hours_worked=0):
        if name in self.staff:
            return False
        doctor = Doctor(name, staff_id, shift_budget)
        doctor.add_hours(hours_worked)
        self.staff[name] = doctor
        return True

    def add_regular_patient(self, name, contact_details, visits):
        if name in self.patients:
            return False
        patient = RegularPatient(name, contact_details)
        patient.add_visits(visits)
        self.patients[name] = patient
        return True

    def add_vip_patient(self, name, contact_details, visits, priority_rank):
        if name in self.patients:
            return False
        patient = VIPPatient(name, contact_details, priority_rank)
        patient.add_visits(visits)
        self.patients[name] = patient
        return True
