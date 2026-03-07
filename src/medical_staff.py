from abc import ABC, abstractmethod
import printer

class MedicalStaff(ABC):
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id
        self.hours_worked = 0

    @abstractmethod
    def get_type(self):
        pass

    def add_hours(self, hours_worked):
        self.hours_worked += hours_worked

class Nurse(MedicalStaff):
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id)
        self.patients_attended_today = 0

    def get_type(self):
        return "nurse"

class Doctor(MedicalStaff):
    def __init__(self, name, staff_id, shift_budget):
        super().__init__(name, staff_id)
        self.patients_attended_today = 0
        self.shift_budget = shift_budget

    def get_type(self):
        return "doctor"
