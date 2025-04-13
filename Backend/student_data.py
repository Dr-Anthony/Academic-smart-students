import json
import os

DATA_FILE = os.path.join('Data', 'students.json')

def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_students(students):
    with open(DATA_FILE, 'w') as file:
        json.dump(students, file, indent=4)

def add_student(student):
    students = load_students()
    students.append(student)
    save_students(students)

def get_student_by_matric(matric_no):
    students = load_students()
    for student in students:
        if student.get('matric') == matric_no:
            return student
    return None

def update_student(matric_no, updated_data):
    students = load_students()
    for i, student in enumerate(students):
        if student.get('matric') == matric_no:
            students[i].update(updated_data)
            save_students(students)
            return True
    return False
