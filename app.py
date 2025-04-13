from Backend.index import app
from flask import jsonify, send_from_directory
import datetime, os, logging

#  Setup logging to file + console
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

#  Routes
@app.route("/")
def welcome():
    logging.info("Homepage accessed.")
    return """
    <html><head><title>Voice Portal</title></head>
    <body style='font-family: Arial; text-align: center; margin-top: 10%'>
    <h1> Voice Interactive Portal</h1>
    <p>Platform is running.</p>
    <a href='/status'>Check API Status</a>
    </body></html>
    """

@app.route("/status")
def status():
    logging.info("Status checked.")
    return jsonify({
        "status": "running",
        "timestamp": datetime.datetime.now().isoformat(),
        "developer": "Tony Okoye"
    })

@app.route("/static/<path:filename>")
def serve_static(filename):
    logging.info(f"Serving static file: {filename}")
    return send_from_directory(os.path.join(os.getcwd(), 'static'), filename)

#  Auto-run 
app.run(debug=True)


