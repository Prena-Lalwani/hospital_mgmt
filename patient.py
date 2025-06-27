ILLNESS_PRIORITY = {
    "Heart Attack": 1,
    "Stroke": 2,
    "Fracture": 3,
    "Fever": 4,
    "Cold/Cough": 5
}

class Patient:
    def __init__(self, name, age, illness):
        self.name = name
        self.age = age
        self.illness = illness
        self.priority = ILLNESS_PRIORITY[illness]

    def __str__(self):
        return f"{self.name} | Age: {self.age} | Illness: {self.illness} | Priority: {self.priority}"
