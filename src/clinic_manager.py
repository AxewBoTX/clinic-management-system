import pickle
from medical_staff import Nurse, Doctor
from slugify import slugify
from patient import RegularPatient, VIPPatient


class ClinicManager:
    def __init__(self):
        self.staff = {}
        self.patients = {}

    def save_data(self, file_name="clinic_data.pkl"):
        data = {"staff": self.staff, "patients": self.patients}
        with open(file_name, "wb") as file:
            pickle.dump(data, file)

    def load_data(self, file_name="clinic_data.pkl"):
        try:
            with open(file_name, "rb") as file:
                data = pickle.load(file)
                self.staff = data.get("staff", {})
                self.patients = data.get("patients", {})
        except FileNotFoundError:
            self.staff = {}
            self.patients = {}

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

    def add_regular_patient(self, patient_id, name, contact_details):
        for curr_patient in self.patients.values():
            if curr_patient.patient_id == patient_id:
                return curr_patient

        patient = RegularPatient(name, patient_id, contact_details)
        self.patients[patient_id] = patient
        return None

    def add_vip_patient(self, patient_id, name, contact_details, priority_rank):
        for curr_patient in self.patients.values():
            if curr_patient.patient_id == patient_id:
                return curr_patient

        patient = VIPPatient(name, patient_id, contact_details, priority_rank)
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

    def record_patient_attendance(self, staff_id, patient_id):
        if staff_id in self.staff:
            staff = self.staff[staff_id]
            if isinstance(staff, Nurse):
                if patient_id in self.patients:
                    patient = self.patients[patient_id]
                    staff.record_patient_attendance(1)
                    patient.add_visits(1)
                    return True
                else:
                    False
            else:
                return False
        else:
            return False

    def generate_daily_report(self) -> dict:
        output = {}

        output["total_staff"] = len(self.staff)

        nurse_count = 0
        patients_attended_today = 0
        top_nurse = None
        for curr_staff in self.staff.values():
            if isinstance(curr_staff, Nurse):
                nurse_count += 1
                patients_attended_today += curr_staff.patients_attended_today
            if top_nurse is None:
                top_nurse = curr_staff
            else:
                if curr_staff.patients_attended_today > top_nurse.patients_attended_today:
                    top_nurse = curr_staff
        output["nurses"] = nurse_count
        output["patients_attended"] = patients_attended_today
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
