function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function isValidPhone(phone) {
  return /^[0-9]{10,15}$/.test(phone);
}

function validateForm() {
  const email = document.getElementById("email")?.value.trim();
  const phone = document.getElementById("phone")?.value.trim();

  if (!isValidEmail(email) || !isValidPhone(phone)) {
    alert("Please enter a valid email and phone number.");
    return false;  // stops form submission
  }

  return true; // proceed with form submission
}
