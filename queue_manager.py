from patient import Patient

class PatientQueue:
    def __init__(self):
        self.queue = []

    def add_patient(self, patient):
        self.queue.append(patient)
        self.queue.sort(key=lambda p: p.priority)  # auto-sorted

    def discharge_patient(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def show_patients(self):
        if not self.queue:
            print("🟡 No patients in queue.")
            return

        print("\n📋 Current Patient Queue:")
        for i, p in enumerate(self.queue):
            print(f"{i+1}. {p}")
