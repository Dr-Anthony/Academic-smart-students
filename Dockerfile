# Use a slim Python 3.11 base image for reduced size
FROM python:3.11-slim

# Disable .pyc bytecode files and enable real-time logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system-level libraries required for:
# - Audio input/output (PyAudio, speech recognition)
# - Offline text-to-speech (pyttsx3, espeak)
# - Audio processing (ffmpeg for Whisper or OpenAI API fallback)
# - Build tools for compiling C-based Python packages (like pyaudio)
# Install audio and build dependencies
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    libasound2-dev \
    libportaudio2 \
    libportaudiocpp0 \
    ffmpeg \
    build-essential \
    espeak-ng \
    && rm -rf /var/lib/apt/lists/*


# Copy your entire project into the container
COPY . .

# Upgrade pip and install all Python dependencies from your Requirements.txt
RUN pip install --upgrade pip && \
    pip install -r Requirements.txt

# Open port 5000 for web traffic
EXPOSE 5000

# Start the Flask app using Gunicorn (production-grade WSGI server)
CMD ["gunicorn", "Backend.Py.wsgi:app", "--bind", "0.0.0.0:5000"]
