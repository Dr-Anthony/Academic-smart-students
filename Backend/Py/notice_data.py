import json
import os
from flask import Blueprint, request, jsonify

NOTICE_FILE = os.path.join('Data', 'notices.json')

notice_bp = Blueprint('notice_bp', __name__)

def load_notices():
    if not os.path.exists(NOTICE_FILE):
        return []
    with open(NOTICE_FILE, 'r') as file:
        return json.load(file)

def save_notices(data):
    with open(NOTICE_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_notice(title, body, department="all", attachment=None):
    notices = load_notices()
    new_notice = {
        "title": title,
        "body": body,
        "department": department.lower(),
        "attachment": attachment
    }
    notices.insert(0, new_notice)  # newest first
    save_notices(notices)

def get_notices_for_department(department):
    notices = load_notices()
    department = department.lower()
    return [
        notice for notice in notices
        if notice.get("department") == "all" or notice.get("department") == department
    ]

# API routes

@notice_bp.route('/add', methods=['POST'])
def api_add_notice():
    data = request.get_json()
    add_notice(data.get("title"), data.get("body"), data.get("department", "all"), data.get("attachment"))
    return jsonify({'message': 'Notice added successfully'}), 201

@notice_bp.route('/<department>', methods=['GET'])
def api_get_notices_for_department(department):
    notices = get_notices_for_department(department)
    if notices:
        return jsonify(notices)
    return jsonify({'error': 'No notices found for this department'}), 404
