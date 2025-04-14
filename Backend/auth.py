import json
import os
from flask import Blueprint, request, jsonify

STUDENT_FILE = os.path.join('Data', 'students.json')
ADMIN_FILE = os.path.join('Data', 'admins.json')
COUNTER_FILE = os.path.join('Data', 'counters.json')

auth_bp = Blueprint('auth_bp', __name__)

def load_json(file_path, default):
    if not os.path.exists(file_path):
        return default
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def generate_matric_number(department, year):
    counters = load_json(COUNTER_FILE, {})

    key = f"{department.lower()}_{year}"
    count = counters.get(key, 0) + 1
    counters[key] = count

    counters["matric_serial"] = counters.get("matric_serial", 0) + 1
    serial = counters["matric_serial"]

    save_json(COUNTER_FILE, counters)

    dept_codes = {
        "accounting": "ACC", "biochemistry": "BCH", "banking and finance": "BFN", "biological science": "BIO",
        "nursing": "BNS", "philosophy": "PHL", "business administration": "BUS", "theology": "THE",
        "computer engineering": "CEG", "pure and applied chemistry": "CHM", "computer science": "CSC",
        "economics": "ECO", "electrical and electronic engineering": "EEG", "english and literary studies": "ENG",
        "entrepreneurship": "ENT", "physics": "PHY", "guidance and counseling": "GAC",
        "history and international relations": "HIS", "law": "LAW", "medicine and surgery": "MED",
        "medical laboratory science": "MLS", "mass communication": "MAC", "applied microbiology": "MCB",
        "marketing": "MKT", "peace and conflict studies": "PCS", "pharmacy": "PHM",
        "political science and diplomacy": "POL", "public administration": "PAD", "software engineering": "SEN"
    }

    code = dept_codes.get(department.lower(), "GEN")
    matric = f"AOC/{code}/{str(year)[-2:]}/{serial:04d}"
    return matric

def generate_staff_id():
    counters = load_json(COUNTER_FILE, {})
    count = counters.get("staff", 0) + 1
    counters["staff"] = count
    save_json(COUNTER_FILE, counters)
    return f"ADM{str(count).zfill(4)}"

def verify_student_login(matric, password):
    students = load_json(STUDENT_FILE, [])
    for student in students:
        if student.get("matric") == matric and student.get("password") == password:
            return student
    return None

def verify_admin_login(email, password):
    admins = load_json(ADMIN_FILE, [])
    for admin in admins:
        if admin.get("email") == email and admin.get("password") == password:
            return admin
    return None

@auth_bp.route('/login/student', methods=['POST'])
def api_student_login():
    data = request.get_json()
    student = verify_student_login(data.get("matric"), data.get("password"))
    if student:
        return jsonify(student)
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route('/login/admin', methods=['POST'])
def api_admin_login():
    data = request.get_json()
    admin = verify_admin_login(data.get("email"), data.get("password"))
    if admin:
        return jsonify(admin)
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route('/id/matric', methods=['POST'])
def api_generate_matric():
    data = request.get_json()
    matric = generate_matric_number(data.get("department"), data.get("year"))
    return jsonify({"matric": matric})

@auth_bp.route('/id/staff', methods=['GET'])
def api_generate_staff():
    staff_id = generate_staff_id()
    return jsonify({"staff_id": staff_id})
