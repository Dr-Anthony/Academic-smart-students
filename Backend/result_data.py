import json
import os

RESULT_FILE = os.path.join('Data', 'results.json')

def load_results():
    if not os.path.exists(RESULT_FILE):
        return {}
    with open(RESULT_FILE, 'r') as file:
        return json.load(file)

def save_results(data):
    with open(RESULT_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def save_student_result(matric_no, semester, session, result_object):
    key = f"results_{matric_no}_{semester}_{session}".lower()
    data = load_results()
    data[key] = result_object
    save_results(data)

def get_student_result(matric_no, semester, session):
    key = f"results_{matric_no}_{semester}_{session}".lower()
    data = load_results()
    return data.get(key)

def delete_student_result(matric_no, semester, session):
    key = f"results_{matric_no}_{semester}_{session}".lower()
    data = load_results()
    if key in data:
        del data[key]
        save_results(data)
        return True
    return False
