import csv
import heapq
import os
from patient import Patient, ILLNESS_PRIORITY


class PatientQueue:
    def __init__(self):
        self.queue = []

    def add_patient(self, patient):
        heapq.heappush(self.queue, (patient.priority, patient))
        print(f"✅ Added to queue: {patient.name}, priority {patient.priority}")

    def discharge_patient(self):
        if self.queue:
            return heapq.heappop(self.queue)[1]  # return only the Patient object
        return None

    def show_patients(self):
        if not self.queue:
            print("No patients in the queue.")
        else:
            print("\n👥 Current Patients (by priority):")
            for i, (_, patient) in enumerate(sorted(self.queue)):
                print(f"{i+1}. {patient}")

    def save_to_file(self, filename="patients.csv"):
        try:
            with open(filename, mode="w", newline="") as f:
                writer = csv.writer(f)
                for _, p in self.queue:
                    writer.writerow([p.name, p.age, p.disease, p.priority])
            print(f"💾 File saved at: {os.path.abspath(filename)}")
        except Exception as e:
            print(f"❌ Failed to save file: {e}")

    def search_by_name(self, name):
        matches = [p for _, p in self.queue if p.name.lower() == name.lower()]
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
                        patient = Patient(name, int(age), disease, int(priority))
                        self.add_patient(patient)
            print("✅ Patient data loaded from file.")
        except FileNotFoundError:
            print("No saved data found. Starting fresh.")
        except Exception as e:
            print(f"❌ Failed to load file: {e}")
