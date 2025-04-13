// ../../Backend/duplicate_checker.js

function isDuplicateSignup(email, phone) {
    const existing = JSON.parse(localStorage.getItem("students")) || [];
  
    return existing.some(student =>
      student.email.toLowerCase() === email.toLowerCase() ||
      student.phone === phone
    );
  }
  
  function saveStudentData(data) {
    const students = JSON.parse(localStorage.getItem("students")) || [];
    students.push(data);
    localStorage.setItem("students", JSON.stringify(students));
  }
  