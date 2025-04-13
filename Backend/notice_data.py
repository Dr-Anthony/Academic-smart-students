import json
import os

NOTICE_FILE = os.path.join('Data', 'notices.json')

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
