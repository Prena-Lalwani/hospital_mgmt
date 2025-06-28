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
                    writer.writerow([p.name, p.age, p.disease, p.priority])
        except Exception as e:
            print(f"❌ Failed to save file: {e}")


    def search_by_name(self, name):
        matches = [p for p in self.queue if p.name.lower() == name.lower()]
        if matches:
            print(f"\n🔍 Found {len(matches)} match(es):")
            for p in matches:
                print(p)
        else:
            print("❌ No patient found with that name.")

    def load_from_file(self, filename="patients.csv"):
        try:
            with open(filename, mode="r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 4:
                        name, age, disease, priority = row
                        self.add_patient(Patient(name, int(age), disease, int(priority)))
            print("✅ Patient data loaded from file.")
        except FileNotFoundError:
            print("No saved data found. Starting fresh.")
        except Exception as e:
            print(f"❌ Failed to load file: {e}")

