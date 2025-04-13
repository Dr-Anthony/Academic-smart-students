function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }
  
  function isValidPhone(phone) {
    return /^[0-9]{10,15}$/.test(phone);
  }
  if (!isValidEmail(email) || !isValidPhone(phone)) {
    alert("Invalid email or phone format.");
    return;
  }
    