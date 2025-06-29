# 🏥 Hospital Management System (CLI App)

This is a simple **Command-Line Interface (CLI)** based Hospital Management System developed in Python using **OOP**, **DSA**, and **CSV file handling**. It manages patients based on the **severity of their illness** using a **priority queue** implemented via `heapq`.

---

## 📌 Features

- Add a new patient (priority auto-assigned based on illness)
- View current waiting list (sorted by urgency)
- Discharge the highest-priority patient
- Search patient by name
- Persistent data storage via `patients.csv`
- Loads patient records on startup
- Optionally: Search by illness (if added)

---

## 💻 Technologies Used

- Python 3
- `heapq` (for efficient priority queue)
- `csv` (for file-based data persistence)
- OOP Concepts (`class`, `__lt__`, encapsulation)
- Optional: `rich` for CLI styling (not required)

---

## 🧠 Illness-Based Priority

```text
1 - Heart Attack
2 - Stroke
3 - Fracture
4 - Fever
5 - Cold/Cough

#🗂️ Project Structure
hospital_mgmt/
│
├── app.py              # Main CLI interface
├── patient.py          # Patient class and illness-priority mapping
├── queue_manager.py    # Priority queue logic using heapq
├── patients.csv        # Saved patient data (auto-created)
├── requirements.txt    # (optional) dependencies
└── README.md           # Project overview

#🚀 How to Run
git clone https://github.com/your-username/hospital_mgmt.git
cd hospital_mgmt

#Run the app
python app.py

