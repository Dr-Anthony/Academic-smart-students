from Backend.index import app
from flask import jsonify, send_from_directory
import datetime, os, logging

# Setup logging to file + console
log_dir = "log"
os.makedirs(log_dir, exist_ok=True)

log_filename = f"{log_dir}/app_{datetime.datetime.now().strftime('%Y-%m-%d')}.log"

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logging.getLogger().addHandler(logging.StreamHandler())

# Configuration for different environments
app.config['ENV'] = os.getenv('FLASK_ENV', 'production')
app.config['DEBUG'] = app.config['ENV'] == 'development'

# Routes
@app.route("/")
def welcome():
    logging.info("Homepage accessed.")
    return """
    <html>
    <head>
        <title>Voice Portal</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 10%; }
            a { text-decoration: none; color: #007bff; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>Voice Interactive Portal</h1>
        <p>The platform is operational.</p>
        <a href='/status'>Check API Status</a>
    </body>
    </html>
    """

@app.route("/status")
def status():
    logging.info("Status endpoint accessed.")
    return jsonify({
        "status": "running",
        "timestamp": datetime.datetime.now().isoformat(),
        "developer": "Tony Okoye",
        "environment": app.config['ENV']
    })

@app.route("/Backend/<path:filename>")
def serve_backend_files(filename):
    logging.info(f"Serving Backend file: {filename}")
    backend_dir = os.path.join(os.getcwd(), 'Backend')
    return send_from_directory(backend_dir, filename)