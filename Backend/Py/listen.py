from flask import Blueprint, request, jsonify
import os, threading, speech_recognition as sr, openai, pyttsx3
from dotenv import load_dotenv
import traceback

listen_bp = Blueprint('listen', __name__)

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

engine = pyttsx3.init()
engine.setProperty('rate', 160)
voice_id = next((v.id for v in engine.getProperty('voices') if 'english' in v.name.lower()), engine.getProperty('voices')[0].id)
engine.setProperty('voice', voice_id)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

@listen_bp.route('/listen', methods=['POST'])
def listen_route():
    data = request.get_json()
    command = data.get("command", "").strip()

    if not command:
        return jsonify({"error": "No command"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": (
                    "You are a smart JARVIS-like assistant on a website. You can control the webpage using JavaScript, "
                    "help users fill out forms, open modals, read content, click buttons, and redirect them. "
                    "Always return clear responses. If a user says to go to a page, mention 'Redirecting to /pagename'. "
                    "If they say to type, click, open modal, etc., describe the action in simple terms so the frontend can follow it."
                )},
                {"role": "user", "content": command}
            ]
        )
        reply = response.choices[0].message["content"]

        redirect = None
        if "redirecting to /" in reply.lower():
            redirect = "/" + reply.lower().split("redirecting to /")[1].split()[0]

        speak(reply)
        return jsonify({"response": reply, "redirect": redirect})

    except Exception as e:
        print(" GPT Error:", e)
        traceback.print_exc()  # This prints full error details
        return jsonify({"response": "Something went wrong with my brain"}), 500
