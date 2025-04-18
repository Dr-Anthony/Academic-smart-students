import json
import os
from flask import Blueprint, request, jsonify

STUDENT_FILE = os.path.join('Data', 'students.json')

profile_bp = Blueprint('profile_bp', __name__)

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
    # If not found, create new student with this matric
    updates["matric"] = matric_no
    students.append(updates)
    save_students(students)
    return True


def check_duplicate_fullname(fullname, dob):
    students = load_students()
    for student in students:
        if student.get("fullname") == fullname and student.get("dob") == dob:
            return True
    return False

# API routes

@profile_bp.route('/<matric_no>', methods=['GET'])
def api_get_profile(matric_no):
    profile = get_profile(matric_no)
    if profile:
        return jsonify(profile)
    return jsonify({'error': 'Profile not found'}), 404

@profile_bp.route('/<matric_no>', methods=['PUT'])
def api_update_profile(matric_no):
    updated_data = request.get_json()
    success = update_profile(matric_no, updated_data)
    if success:
        return jsonify({'message': 'Profile updated successfully'})
    return jsonify({'error': 'Profile not found'}), 404

@profile_bp.route('/check-duplicate', methods=['POST'])
def api_check_duplicate_fullname():
    data = request.get_json()
    if check_duplicate_fullname(data.get("fullname"), data.get("dob")):
        return jsonify({'duplicate': True})
    return jsonify({'duplicate': False})
