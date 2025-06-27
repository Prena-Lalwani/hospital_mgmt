from patient import Patient, ILLNESS_PRIORITY
from queue_manager import PatientQueue

pq = PatientQueue()
pq.load_from_file()

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

            print("Select illness:")
            illnesses = list(ILLNESS_PRIORITY.keys())
            for i, illness in enumerate(illnesses, start=1):
                print(f"{i}. {illness}")
            illness_choice = int(input("Choice (1-5): "))
            disease = illnesses[illness_choice - 1]
            priority = ILLNESS_PRIORITY[disease]

            pq.add_patient(Patient(name, age, disease, priority))

        elif choice == '2':
            pq.show_patients()

        elif choice == '3':
            discharged = pq.discharge_patient()
            if discharged:
                print(f"{discharged.name} has been discharged.")
            else:
                print("No patients to discharge.")

        elif choice == '4':
            pq.save_to_file()
            print("✅ Data saved. Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")

menu()
