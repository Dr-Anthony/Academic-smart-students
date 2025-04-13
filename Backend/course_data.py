import json
import os

COURSE_FILE = os.path.join('Data', 'courses.json')

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
