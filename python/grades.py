student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


def grade_students(scores):
    # Scores 91 - 100: Grade = "Outstanding"
    # Scores 81 - 90: Grade = "Exceeds Expectations"
    # Scores 71 - 80: Grade = "Acceptable"
    # Scores 70 or lower: Grade = "Fail"
    grades = {}
    for name in scores:
        if scores[name] >= 91:
            grades[name] = "Outstanding"
        elif scores[name] >= 81 and scores[name] <= 90:
            grades[name] = "Exceeds Expectations"
        elif scores[name] >= 71 and scores[name] <= 80:
            grades[name] = "Acceptable"
        else:
            grades[name] = "Fail"

    return grades


print(grade_students(student_scores))
