"""
patient.py - Contains Patient parent class and RegularPatient, VIPPatient child-classes

Cole, Mia: s8248723
Matta, Ishi: s8239982
Singh, Lovedeep: s8208559
"""

from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, name, patient_id, contact_details):
        self.name = name
        self.patient_id = patient_id
        self.contact_details = contact_details
        self.visits = 1

    # return the type of the sub_class i.e "regular" or "vip"
    @abstractmethod
    def get_type(self):
        pass

    # increment visits by either 1 or the provided amount
    def add_visits(self, visit_count=1):
        self.visits += visit_count


class RegularPatient(Patient):
    def __init__(self, name, patient_id, contact_details):
        super().__init__(name, patient_id, contact_details)

    def __str__(self):
        return f"({self.name}, {self.patient_id}, {self.contact_details})"

    def get_type(self):
        return "regular"


class VIPPatient(Patient):
    def __init__(self, name, patient_id, contact_details, priority_rank):
        super().__init__(name, patient_id, contact_details)
        self.priority_rank = priority_rank

    def __str__(self):
        return f"({self.name}, {self.patient_id}, {self.contact_details}, {self.priority_rank})"

    def get_type(self):
        return "vip"
