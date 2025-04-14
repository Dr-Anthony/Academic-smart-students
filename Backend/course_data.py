import json
import os
from flask import Blueprint, request, jsonify

COURSE_FILE = os.path.join('Data', 'courses.json')

course_bp = Blueprint('course_bp', __name__)

def load_courses():
    if not os.path.exists(COURSE_FILE):
        return {}
    with open(COURSE_FILE, 'r') as file:
        return json.load(file)

def save_courses(data):
    with open(COURSE_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def get_courses(department, level, semester):
    key = f"{department}_{level}_{semester}".lower()
    data = load_courses()
    return data.get(key, [])

def add_course(department, level, semester, course):
    key = f"{department}_{level}_{semester}".lower()
    data = load_courses()

    if key not in data:
        data[key] = []

    data[key].append(course)
    save_courses(data)

def overwrite_courses(department, level, semester, course_list):
    key = f"{department}_{level}_{semester}".lower()
    data = load_courses()
    data[key] = course_list
    save_courses(data)

# API routes

@course_bp.route('/add', methods=['POST'])
def api_add_course():
    data = request.get_json()
    department = data.get('department')
    level = data.get('level')
    semester = data.get('semester')
    course = data.get('course')

    if not department or not level or not semester or not course:
        return jsonify({'error': 'Missing required fields'}), 400

    add_course(department, level, semester, course)
    return jsonify({'message': 'Course added successfully'}), 201

@course_bp.route('/', methods=['GET'])
def api_get_courses():
    department = request.args.get('department')
    level = request.args.get('level')
    semester = request.args.get('semester')

    if not department or not level or not semester:
        return jsonify({'error': 'Missing required query parameters'}), 400

    courses = get_courses(department, level, semester)
    return jsonify(courses)
