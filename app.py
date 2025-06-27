from patient import Patient
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
            disease = input("Disease: ")
            priority = int(input("Priority (1-5): "))
            pq.add_patient(Patient(name, age, disease, priority))

        elif choice == '2':
            pq.show_patients()

        elif choice == '3':
            discharged = pq.discharge_patient()
            if discharged:
                print(f"{discharged.name} discharged!")
            else:
                print("No patients.")

        elif choice == '4':
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")

menu()
