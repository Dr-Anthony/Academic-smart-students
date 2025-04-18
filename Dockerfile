FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY . .

COPY Requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r Requirements.txt
    
EXPOSE 5000

# Run using gunicorn + your production-ready wsgi.py
CMD ["gunicorn", "Backend.Py.wsgi:app", "--bind", "0.0.0.0:5000"]
