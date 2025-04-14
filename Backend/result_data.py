import json
import os
from flask import Blueprint, request, jsonify

RESULT_FILE = os.path.join('Data', 'results.json')

result_bp = Blueprint('result_bp', __name__)

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

# API routes

@result_bp.route('/<matric_no>/<semester>/<session>', methods=['GET'])
def api_get_student_result(matric_no, semester, session):
    result = get_student_result(matric_no, semester, session)
    if result:
        return jsonify(result)
    return jsonify({'error': 'Result not found'}), 404

@result_bp.route('/<matric_no>/<semester>/<session>', methods=['POST'])
def api_save_student_result(matric_no, semester, session):
    data = request.get_json()
    result_object = data.get('result_object')
    if not result_object:
        return jsonify({'error': 'Missing result object'}), 400
    save_student_result(matric_no, semester, session, result_object)
    return jsonify({'message': 'Result saved successfully'}), 201

@result_bp.route('/<matric_no>/<semester>/<session>', methods=['DELETE'])
def api_delete_student_result(matric_no, semester, session):
    success = delete_student_result(matric_no, semester, session)
    if success:
        return jsonify({'message': 'Result deleted successfully'}), 200
    return jsonify({'error': 'Result not found'}), 404
