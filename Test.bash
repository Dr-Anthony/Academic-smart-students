#!/bin/bash

# Activate virtual environment if it exists
if [ -d "venv" ]; then
  source venv/bin/activate
fi

# Set Flask environment variables
export FLASK_APP=Backend/index.py
export FLASK_ENV=development

# Try to run Flask app, fallback to direct python if flask is not installed
if command -v flask &> /dev/null; then
  flask run
else
  echo "Flask not installed, using python fallback..."
  python Backend/index.py
fi
