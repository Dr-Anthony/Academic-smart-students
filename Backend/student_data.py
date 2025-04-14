import json
import os
from flask import Blueprint, request, jsonify

DATA_FILE = os.path.join('Data', 'students.json')
student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/register', methods=['POST'])
def api_register_student():
    data = request.get_json()
    add_student(data)
    return jsonify({'message': 'Student registered successfully'}), 200

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
    # If not found, add as new
    students.append(updated_data)
    save_students(students)
    return True

@student_bp.route('/add', methods=['POST'])
def api_add_student():
    data = request.get_json()
    add_student(data)
    return jsonify({'message': 'Student added successfully'})

@student_bp.route('/<matric_no>', methods=['GET'])
def api_get_student(matric_no):
    student = get_student_by_matric(matric_no)
    if student:
        return jsonify(student)
    return jsonify({'error': 'Student not found'}), 404

@student_bp.route('/<matric_no>', methods=['PUT'])
def api_update_student(matric_no):
    updated_data = request.get_json()
    success = update_student(matric_no, updated_data)
    if success:
        return jsonify({'message': 'Student updated successfully'})
    return jsonify({'error': 'Student not found'}), 404
