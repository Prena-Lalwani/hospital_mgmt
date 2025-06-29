ILLNESS_PRIORITY = {
    "Heart Attack": 1,
    "Stroke": 2,
    "Fracture": 3,
    "Fever": 4,
    "Cold/Cough": 5
}

class Patient:
    def __init__(self, name, age, disease, priority):
        self.name = name
        self.age = age
        self.disease = disease
        self.priority = priority

    def __str__(self):
        return f"{self.name} | Age: {self.age} | Issue: {self.disease} | Priority: {self.priority}"
    
    def __lt__(self, other):
        # Just compare names to break ties when priority is the same
        return self.name < other.name
    
