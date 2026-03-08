from medical_staff import Nurse, Doctor
from slugify import slugify
from patient import RegularPatient, VIPPatient


class ClinicManager:
    def __init__(self, clinic_name="My Clinic"):
        self.clinic_name = clinic_name
        self.staff = {}
        self.patients = {}

    def save_data():
        pass

    def load_data():
        pass

    def add_nurse(self, staff_id, name, hours_worked=0):
        for curr_staff in self.staff.values():
            if curr_staff.staff_id == staff_id:
                return curr_staff

        nurse = Nurse(name, staff_id)
        nurse.add_hours(hours_worked)
        self.staff[nurse.staff_id] = nurse
        return None

    def add_doctor(self, staff_id, name, shift_budget, hours_worked=0):
        for curr_staff in self.staff.values():
            if curr_staff.staff_id == staff_id:
                return curr_staff

        doctor = Doctor(name, staff_id, shift_budget)
        doctor.add_hours(hours_worked)
        self.staff[doctor.staff_id] = doctor
        return None

    def add_regular_patient(self, patient_id, name, contact_details, visits):
        for curr_patient in self.patients.values():
            if curr_patient.patient_id == patient_id:
                return curr_patient

        patient = RegularPatient(name, patient_id, contact_details)
        patient.add_visits(visits)
        self.patients[patient_id] = patient
        return None

    def add_vip_patient(self, patient_id, name, contact_details, visits, priority_rank):
        for curr_patient in self.patients.values():
            if curr_patient.patient_id == patient_id:
                return curr_patient

        patient = VIPPatient(name, patient_id, contact_details, priority_rank)
        patient.add_visits(visits)
        self.patients[patient_id] = patient
        return None

    def search(self, search_input):
        search_input = slugify(search_input)
        search_list = list(self.staff.values())
        search_list.extend(list(self.patients.values()))
        search_results = []

        for item in search_list:
            if search_input in slugify(item.name):
                search_results.append(item)

        return search_results

    def record_patient_attendance(self, staff_id, patient_num):
        if staff_id in self.staff:
            item = self.staff[staff_id]
            if isinstance(item, Nurse):
                item.record_patient_attendance(patient_num)
                return True
            else:
                False
        else:
            return False
