class Patient:
    def __init__(self, name, age, disease, priority):
        self.name = name
        self.age = age
        self.disease = disease
        self.priority = priority  # 1 (high) to 5 (low)

    def __str__(self):
        return f"{self.name} | Age: {self.age} | Issue: {self.disease} | Priority: {self.priority}"
