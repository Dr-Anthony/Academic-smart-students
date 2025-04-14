#  BACKEND FILES
# ------------------
# 8. wsgi.py (Deployment entry point)

from Backend.index import app
from app import app

app.run(debug=True)

# This file is used for production servers like Gunicorn or uWSGI
# Run using: gunicorn wsgi:app
