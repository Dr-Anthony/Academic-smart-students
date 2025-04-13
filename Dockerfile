FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && \
    pip install flask

EXPOSE 5000

CMD ["python", "Backend/index.py"]
