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
RUN apt-get update && apt-get install -y \
    portaudio19-dev \            # Core audio interface for PyAudio
    libasound2-dev \             # ALSA sound support for Linux
    libportaudio2 \              # Runtime lib for PortAudio
    libportaudiocpp0 \           # C++ wrapper for PortAudio
    ffmpeg \                     # Needed for Whisper and audio conversion
    libav-tools \                # Legacy ffmpeg tools (sometimes needed)
    build-essential \            # Compilers + make (required for pyaudio build)
    espeak \                     # TTS engine used by pyttsx3 (Linux-compatible)
    && rm -rf /var/lib/apt/lists/*  # Clean up cache to reduce image size

# Copy your entire project into the container
COPY . .

# Upgrade pip and install all Python dependencies from your Requirements.txt
RUN pip install --upgrade pip && \
    pip install -r Requirements.txt

# Open port 5000 for web traffic
EXPOSE 5000

# Start the Flask app using Gunicorn (production-grade WSGI server)
CMD ["gunicorn", "Backend.Py.wsgi:app", "--bind", "0.0.0.0:5000"]
