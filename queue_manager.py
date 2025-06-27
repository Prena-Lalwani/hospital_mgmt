import csv
from patient import Patient, ILLNESS_PRIORITY

class PatientQueue:
    def __init__(self):
        self.queue = []

    def add_patient(self, patient):
        self.queue.append(patient)
        self.queue.sort(key=lambda p: p.priority)

    def discharge_patient(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def show_patients(self):
        if not self.queue:
            print("No patients in the queue.")
        for i, p in enumerate(self.queue):
            print(f"{i+1}. {p}")

    def save_to_file(self, filename="patients.csv"):
        try:
            with open(filename, mode="w", newline="") as f:
                writer = csv.writer(f)
                for p in self.queue:
                    writer.writerow([p.name, p.age, p.disease])
        except Exception as e:
            print(f"❌ Failed to save file: {e}")

    def load_from_file(self, filename="patients.csv"):
        try:
            with open(filename, mode="r") as f:
                reader = csv.reader(f)
                for row in reader:
                    name, age, disease = row
                    priority = ILLNESS_PRIORITY.get(disease, 5)
                    self.add_patient(Patient(name, int(age), disease, priority))
        except FileNotFoundError:
            print("No saved data found. Starting fresh.")
        except Exception as e:
            print(f"❌ Failed to load file: {e}")
