#!/bin/bash

# Activate virtual environment if it exists
if [ -d "venv" ]; then
  source venv/bin/activate
fi

# Set Flask environment variables
export FLASK_APP=Backend/Py/wsgi.py
export FLASK_ENV=development

# Try to run Flask app, fallback to direct python if flask is not installed
if command -v flask &> /dev/null; then
  echo "🚀 Running with Flask..."
  flask run --host=0.0.0.0 --port=5000
else
  echo "⚠️ Flask not installed, using python fallback..."
  python -m flask run --host=0.0.0.0 --port=5000
fi
