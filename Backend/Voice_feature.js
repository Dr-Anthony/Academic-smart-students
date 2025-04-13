// Function to send text to the server for speaking via the Flask backend
async function speak(text) {
  await fetch("http://127.0.0.1:5000/api/voice/speak", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  });
}

// Function to listen for voice commands using the Flask backend
async function listen() {
  const res = await fetch("http://127.0.0.1:5000/api/voice/listen");
  const data = await res.json();
  return data.result;
}

// Function to activate voice commands and provide guidance throughout the site
async function activateVoiceCommands() {
  // Speak an introductory message when the page loads
  await speak("Welcome. I will guide you through the site. Please say a command.");

  // Infinite loop to continuously listen for commands
  while (true) {
    const command = await listen(); // Always listen for new commands

    const page = window.location.pathname.split("/").pop();

    // Provide context based on the current page
    if (page === "dashboard.html") {
      await speak("You are on the dashboard. Say 'course' to go to your course registration, 'result' to view your results, 'profile' to view your profile, or 'log out' to log out.");
    }

    if (page === "course_registration.html") {
      await speak("You are on the course registration page. Say 'register' to register for courses.");
    }

    if (page === "profile.html") {
      await speak("You are on your profile page. Say 'edit' to update your profile or 'view' to check your profile.");
    }

    if (page === "results.html") {
      await speak("You are on the results page. Say 'print' to print your results.");
    }

    // Navigate based on commands
    if (command.includes("course")) {
      window.location.href = "course_registration.html";
      await speak("Navigating to course registration.");
    }
    else if (command.includes("result")) {
      window.location.href = "results.html";
      await speak("Navigating to your results.");
    }
    else if (command.includes("profile")) {
      window.location.href = "profile.html";
      await speak("Navigating to your profile.");
    }
    else if (command.includes("log out")) {
      localStorage.clear();
      await speak("Logging out now.");
      window.location.href = "login.html";
    }
    else if (command.includes("sign up") && page === "login.html") {
      window.location.href = "signup.html";
      await speak("Navigating to sign-up page.");
    }
    else if (command.includes("register") && page === "signup.html") {
      document.querySelector("button[type=submit]").click();
      await speak("Submitting your registration.");
    }
    else if (command.includes("print") && page === "results.html") {
      window.print();
      await speak("Printing your results.");
    }
    else {
      await speak("Sorry, I didn't understand that. Please try again.");
    }
  }
}

// Start voice commands as soon as the page loads
window.addEventListener("DOMContentLoaded", () => {
  setTimeout(() => {
    if (!window.voiceDisabled) activateVoiceCommands(); // Enable voice commands
  }, 1000);
});
