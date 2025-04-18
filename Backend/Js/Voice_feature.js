window.onload = function () {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = "en-US";
  recognition.interimResults = false;
  recognition.continuous = true;

  setTimeout(() => recognition.start(), 1000);

  recognition.onresult = async function (event) {
    const command = event.results[event.results.length - 1][0].transcript.trim().toLowerCase();
    console.log("🧠 You said:", command);

    try {
      const response = await fetch("/listen", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ command })
      });

      const result = await response.json();
      const reply = result.response;

      if (reply) {
        const utterance = new SpeechSynthesisUtterance(reply);
        utterance.lang = 'en-US';
        speechSynthesis.speak(utterance);
        console.log("🤖 Assistant says:", reply);

        // Click button
        if (reply.includes("click")) {
          const match = reply.match(/click (the )?(.*?)( button)?/i);
          if (match) {
            const label = match[2].trim().toLowerCase();
            const buttons = document.querySelectorAll("button, a, input[type=submit]");
            buttons.forEach(btn => {
              if (btn.innerText.trim().toLowerCase().includes(label)) {
                btn.click();
              }
            });
          }
        }

        // Type into input
        if (reply.includes("type") || reply.includes("enter")) {
          const inputMatch = reply.match(/(?:type|enter) '(.*?)' (?:in|into|to) (.*?)$/i);
          if (inputMatch) {
            const text = inputMatch[1];
            const field = inputMatch[2].toLowerCase();
            const inputs = document.querySelectorAll("input, textarea");
            inputs.forEach(input => {
              if (input.name?.toLowerCase().includes(field) || input.placeholder?.toLowerCase().includes(field)) {
                input.value = text;
              }
            });
          }
        }

        // Read screen
        if (reply.includes("read the screen") || reply.includes("what is on this page")) {
          const content = document.body.innerText.slice(0, 800);
          const screenRead = new SpeechSynthesisUtterance(content);
          screenRead.lang = 'en-US';
          speechSynthesis.speak(screenRead);
        }

        // Open dropdowns
        if (reply.includes("open dropdown")) {
          const dropdowns = document.querySelectorAll("select");
          dropdowns.forEach(dropdown => dropdown.focus());
        }

        // Form submission
        if (reply.includes("submit form") || reply.includes("validate form")) {
          const form = document.querySelector("form");
          if (form) form.requestSubmit();
        }

        // Open modal
        if (reply.includes("open modal")) {
          const modals = document.querySelectorAll(".modal, .popup");
          modals.forEach(modal => modal.style.display = 'block');
        }

        // Tab toggle
        if (reply.includes("switch tab to") || reply.includes("open tab")) {
          const tabMatch = reply.match(/(?:switch tab to|open tab) (.+)/i);
          if (tabMatch) {
            const tabLabel = tabMatch[1].trim().toLowerCase();
            const tabs = document.querySelectorAll('[role="tab"], .tab');
            tabs.forEach(tab => {
              if (tab.innerText.trim().toLowerCase().includes(tabLabel)) {
                tab.click();
              }
            });
          }
        }

        // File upload focus
        if (reply.includes("upload file") || reply.includes("select file")) {
          const inputs = document.querySelectorAll('input[type="file"]');
          if (inputs.length > 0) inputs[0].click();
        }

        // Search on page
        if (reply.includes("search for")) {
          const match = reply.match(/search for (.+)/i);
          if (match) {
            const keyword = match[1].trim().toLowerCase();
            const allText = document.body.innerText.toLowerCase();
            const found = allText.includes(keyword);
            const message = found ? `Yes, I found "${keyword}" on this page.` : `Sorry, I couldn't find "${keyword}".`;
            speechSynthesis.speak(new SpeechSynthesisUtterance(message));
          }
        }
      }

      if (result.redirect) {
        setTimeout(() => {
          window.location.href = result.redirect;
        }, 2000);
      }
    } catch (error) {
      console.error("🛑 Voice assistant error:", error);
    }
  };

  recognition.onerror = function (e) {
    console.error("🎤 Speech error:", e);
    recognition.stop();
    setTimeout(() => recognition.start(), 2000);
  };

  recognition.onend = function () {
    setTimeout(() => recognition.start(), 1000);
  };
};