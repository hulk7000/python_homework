students = {
    "Alice": {"math": 90, "english": 80},
    "Bob": {"math": 70, "english": 95},
    "Charlie": {"math": 60, "english": 85},
}

best_score = -1
best_student = ""
best_subject = ""

for student, subjects in students.items():
    for subject, score in subjects.items():
        if score > best_score:
            best_score = score
            best_student = student
            best_subject = subject

print(f"Best score: {best_score} by {best_student} in {best_subject}")