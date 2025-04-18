# speak.py — Pro TTS: Speaks Only When Prompted
import pyttsx3
from flask import Blueprint, request, jsonify
import threading
import time
import random

speak_bp = Blueprint('speak', __name__)
_last_spoken = None
_last_time = 0
_cooldown_seconds = 15

voice_variants = {
    "listening": [
        "Yes, I'm listening.",
        "Go ahead, I'm all ears.",
        "Listening now.",
        "Speak, please."
    ],
    "didnt_understand": [
        "Sorry, I didn’t get that.",
        "Please repeat that more clearly.",
        "I couldn't understand you."
    ],
    "command_unknown": [
        "That command is not recognized.",
        "Hmm, I don't know how to do that.",
        "Try saying something different."
    ]
}

def speak_text(text=None, category=None):
    global _last_spoken, _last_time
    current_time = time.time()
    if category in voice_variants:
        text = random.choice(voice_variants[category])
    if not text or (text == _last_spoken and current_time - _last_time < _cooldown_seconds):
        return

    def _speak():
        try:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            voice_id = next((v.id for v in voices if 'nigeria' in v.name.lower() or 'english' in v.name.lower()), voices[0].id)
            engine.setProperty('voice', voice_id)
            engine.setProperty('rate', 150)
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"[TTS Error] {e}")

    _last_spoken = text
    _last_time = current_time
    threading.Thread(target=_speak, daemon=True).start()

@speak_bp.route('/speak', methods=['POST'])
def speak_route():
    data = request.get_json()
    speak_text(data.get('text'), data.get('category'))
    return jsonify({'status': 'ok'})
