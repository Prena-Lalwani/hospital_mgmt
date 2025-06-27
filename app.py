from patient import Patient, ILLNESS_PRIORITY
from queue_manager import PatientQueue

pq = PatientQueue()

def menu():
    while True:
        print("\n🏥 Hospital Management System")
        print("1. Add Patient")
        print("2. View Waiting List")
        print("3. Discharge Patient")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Name: ")
            age = int(input("Age: "))

            # 🧠 Show illness options
            print("\nSelect Illness:")
            illnesses = list(ILLNESS_PRIORITY.keys())
            for idx, illness in enumerate(illnesses, 1):
                print(f"{idx}. {illness}")
            
            illness_choice = int(input("Enter illness number: "))
            illness = illnesses[illness_choice - 1]

            patient = Patient(name, age, illness)
            pq.add_patient(patient)
            print(f"✅ {patient.name} added successfully!")

        elif choice == '2':
            pq.show_patients()

        elif choice == '3':
            discharged = pq.discharge_patient()
            if discharged:
                print(f"✅ {discharged.name} has been discharged.")
            else:
                print("⚠️ No patients to discharge.")

        elif choice == '4':
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

menu()
