import json
import os

STUDENT_FILE = os.path.join('Data', 'students.json')

def load_students():
    if not os.path.exists(STUDENT_FILE):
        return []
    with open(STUDENT_FILE, 'r') as f:
        return json.load(f)

def save_students(data):
    with open(STUDENT_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def get_profile(matric_no):
    students = load_students()
    for student in students:
        if student.get("matric") == matric_no:
            return student
    return None

def update_profile(matric_no, updates):
    students = load_students()
    for i, student in enumerate(students):
        if student.get("matric") == matric_no:
            students[i].update(updates)
            save_students(students)
            return True
    return False

def check_duplicate_fullname(fullname, dob):
    students = load_students()
    for student in students:
        if student.get("fullname") == fullname and student.get("dob") == dob:
            return True
    return False
