"""
medical_staff.py - Contains MedicalStaff parent class and Nurse, Doctor child-classes

Cole, Mia: s8248723
Matta, Ishi: s8239982
Singh, Lovedeep: s8208559
"""

from abc import ABC, abstractmethod

class MedicalStaff(ABC):
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id
        self.hours_worked = 0

    # return the type of the sub_class i.e "regular" or "vip"
    @abstractmethod
    def get_type(self):
        pass

    # increment hours
    def add_hours(self, hours_worked):
        self.hours_worked += hours_worked


class Nurse(MedicalStaff):
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id)
        self.patients_attended_today = 0

    def __str__(self):
        return f"({self.name}, {self.staff_id}, {self.patients_attended_today})"

    def get_type(self):
        return "nurse"

    # record patient attended by the nurse
    def record_patient_attendance(self, value=1):
        self.patients_attended_today += value


class Doctor(MedicalStaff):
    def __init__(self, name, staff_id, shift_budget):
        super().__init__(name, staff_id)
        self.shift_budget = shift_budget

    def __str__(self):
        return f"({self.name}, {self.staff_id}, {self.shift_budget})"

    def get_type(self):
        return "doctor"
