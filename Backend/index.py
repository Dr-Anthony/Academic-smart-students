from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os

# === Import Blueprints ===
from .auth import auth_bp
from .student_data import student_bp
from .result_data import result_bp
from .notice_data import notice_bp
from .course_data import course_bp
from .profile_manager import profile_bp

# === App Initialization ===
base_dir = os.path.abspath(os.path.dirname(__file__))
template_path = os.path.join(base_dir, '..', 'templates')
app = Flask(__name__, template_folder=template_path)
app.config['UPLOAD_FOLDER'] = 'uploads'

# === Ensure Upload Folder Exists ===
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# === Register Blueprints ===
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(student_bp, url_prefix='/api/student')
app.register_blueprint(result_bp, url_prefix='/api/result')
app.register_blueprint(notice_bp, url_prefix='/api/notice')
app.register_blueprint(course_bp, url_prefix='/api/course')
app.register_blueprint(profile_bp, url_prefix='/api/profile')

# ========================= Static Routes =========================
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/Backend/<path:filename>')
def serve_js(filename):
    return send_from_directory('Backend', filename)

# ========================= Page Routes =========================
# === Admin Pages ===
@app.route("/admin_login")
def admin_login():
    return render_template("admin/admin_login.html")

@app.route("/admin_signup")
def admin_signup():
    return render_template("admin/admin_signup.html")

@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template("admin/admin_dashboard.html")

@app.route("/add_notice")
def add_notice():
    return render_template("admin/add_notice.html")

@app.route("/manage_course_registration")
def manage_course_registration():
    return render_template("admin/manage_course_registration.html")

@app.route("/manage_results")
def manage_results():
    return render_template("admin/manage_results.html")

@app.route("/edit_students")
def edit_students():
    return render_template("admin/edit_students.html")

@app.route("/search")
def search_page():
    return render_template("admin/search.html")

@app.route("/student_details")
def student_details():
    return render_template("admin/student_details.html")

@app.route("/reset_password")
def reset_password():
    return render_template("admin/reset_password.html")

@app.route("/admin_forgot")
def admin_forgot():
    return render_template("admin/admin_forgot.html")

# === Student Pages ===
@app.route("/")
@app.route("/index")
def landing():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("user/signup.html")

@app.route("/login")
def login():
    return render_template("user/login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("user/dashboard.html")

@app.route("/profile")
def profile():
    return render_template("user/profile.html")

@app.route("/profile_update")
def profile_update():
    return render_template("user/profile_update.html")

@app.route("/course_registration")
def course_registration():
    return render_template("user/course_registration.html")

@app.route("/results")
def results():
    return render_template("user/results.html")

@app.route("/Department_preview")
def department_preview():
    return render_template("Department_preview.html")

@app.route("/base")
def base():
    return render_template("base.html")