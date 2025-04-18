# Website for the Blind - Voice Interactive Student Portal

This project is a web-based portal tailored to assist visually impaired students with:
- Voice-driven navigation
- Audio feedback and result reading
- Accessible course registration and profile management

##  Technologies Used
- **Flask** (Python backend)
- **HTML/CSS/JS** (Frontend)
- **SpeechRecognition & pyttsx3** (Voice engine)
- **Docker** + **Render** (Deployment)

##  Features
- Voice-controlled login and profile update
- Matric number & staff ID auto-generation
- Department-specific dashboards and notices
- GPA & CGPA result management system
- Admin and student portals

##  Setup Instructions
1. Clone the repo
2. Create virtual environment: `python -m venv venv`
3. Activate it:
   - Windows: `venv\Scripts\activate`
   - Unix/macOS: `source venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r Requirements.txt
   ```
5. Run the app:
   ```bash
   python Backend/index.py
   ```

##  Docker
Build and run using:
```bash
docker-compose up --build
```

---
> Project originally developed by **Dr. Anthony Chibuikem Okoye** for visually inclusive education initiatives.
