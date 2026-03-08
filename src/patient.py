class Patient:
    def __init__(self, name, patient_id, contact_details):
        self.name = name
        self.patient_id = patient_id
        self.contact_details = contact_details
        self.visits = 1

    def get_type(self):
        pass

    def add_visits(self, visit_count=0):
        self.visits += visit_count


class RegularPatient(Patient):
    def __init__(self, name, patient_id, contact_details):
        super().__init__(name, patient_id, contact_details)

    def get_type(self):
        return "regular"


class VIPPatient(Patient):
    def __init__(self, name, patient_id, contact_details, priority_rank):
        super().__init__(name, patient_id, contact_details)
        self.priority_rank = priority_rank

    def get_type(self):
        return "vip"
